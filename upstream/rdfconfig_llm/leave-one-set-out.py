# -*- coding: utf-8 -*-
"""
Cross-validation fine-tuning script with:
- Multi-DB support (uniprot, rhea, bgee, uniprot_and_bgee)
- One-vs-All scheme:
    * For each main_id, we create one fold:
      test_main_ids = [that main_id], train = all others
- Multiple OpenAI API keys (OPENAI_API_KEY, OPENAI_API_KEY2, ...)
- Handling of:
    * "maximum of 5 active requests" limit for fine-tuning jobs
    * Daily / quota limits by switching API keys
- Resume capability:
    * Per-DB, per-fold results are saved and reused if the script is re-run
- Fine-tuning jobs:
    * Up to 3 folds are processed in parallel -> at most 3 active FT jobs

このスクリプトは、demo_finetuning_cv_parallell_fix.ipynb をベースに、
1 vs All (main_idごとに test=1, train=残り) に対応したものです。
"""

import os
import re
import json
import time
import random
import csv
import threading
from datetime import datetime
from typing import Any, Dict, List, Tuple

from concurrent.futures import ThreadPoolExecutor, as_completed

from openai import OpenAI
from functions.SPARQL_executer import execute_query
from functions.results_evaluater import evaluate_jaccard

from dotenv import load_dotenv
load_dotenv()

# =========================================================
# 設定
# =========================================================

# 対象とする DB
DB_LIST = [ "uniprot", "bgee", "uniprot_and_bgee", "rhea"] 

# 1 vs All の fold 順序を決める乱数シード（fold順をランダムにしたい場合用）
RANDOM_SEED = 42

# 出力ディレクトリ
OUTPUT_DIR = "output"
CV_RUNS_DIR = os.path.join(OUTPUT_DIR, "cv_leave-one-set-out_runs")
DATASET_DIR = "dataset"

# FT ジョブの最大並列数（≦ 5 にしておく）
MAX_PARALLEL_FT_JOBS = 3


# =========================================================
# OpenAI API キーのローテーター（スレッドセーフ）
# =========================================================

import time
from datetime import datetime, timezone, timedelta
from typing import List, Tuple
from openai import OpenAI
import threading

class APIKeyRotator:
    """
    OPENAI_API_KEY, OPENAI_API_KEY2, ... を順番に使い回すヘルパー。
    - daily limit / quota エラーが出たキーは exhausted にして今後使わない
    - get_client() で「使える client」を返す
    - 全キー exhausted（=日次リミット到達）なら、次の 0:00 UTC まで sleep してから
      exhausted フラグをリセットして再開する
    """

    def __init__(self) -> None:
        self.clients: List[OpenAI] = []
        self.names: List[str] = []   # ログ用のキー名（環境変数名）
        self.exhausted: List[bool] = []

        i = 1
        while True:
            if i == 1:
                env_name = "OPENAI_API_KEY"
            else:
                env_name = f"OPENAI_API_KEY{i}"
            key = os.getenv(env_name)
            if not key:
                break

            client = OpenAI(api_key=key)

            self.clients.append(client)
            self.names.append(env_name)
            self.exhausted.append(False)
            print(f"[KEY ROTATOR] loaded {env_name}")
            i += 1

        if not self.clients:
            raise RuntimeError(
                "No API key found. Please set OPENAI_API_KEY (and optionally OPENAI_API_KEY2, ...)."
            )

        self._idx = 0  # round-robin 開始位置
        self._lock = threading.Lock()

    def _seconds_until_next_utc_midnight(self) -> float:
        """次の 0:00 UTC までの秒数を計算"""
        now_utc = datetime.now(timezone.utc)
        tomorrow = now_utc.date() + timedelta(days=1)
        reset_time_utc = datetime.combine(
            tomorrow, datetime.min.time(), tzinfo=timezone.utc
        )  # tomorrow 00:00 UTC
        diff = (reset_time_utc - now_utc).total_seconds()
        return max(diff, 60.0)  # 念のため最低1分

    def get_client(self) -> Tuple[int, OpenAI, str]:
        """
        まだ exhausted になっていない client を1つ返す。
        すべて exhausted なら、次の 0:00 UTC まで sleep して
        exhausted フラグをリセットしてから再トライする。
        戻り値: (index, client, env_name)
        """
        while True:
            with self._lock:
                n = len(self.clients)
                for _ in range(n):
                    idx = self._idx
                    self._idx = (self._idx + 1) % n
                    if not self.exhausted[idx]:
                        return idx, self.clients[idx], self.names[idx]

                # ここに来たということは「全キー exhausted」
                sleep_seconds = self._seconds_until_next_utc_midnight()
                jst_reset_hour = 9  # 0:00 UTC = 9:00 JST
                print(
                    f"[KEY ROTATOR] All API keys exhausted by daily limit. "
                    f"Sleeping {int(sleep_seconds)} seconds until next 00:00 UTC (09:00 JST)."
                )

            # ロックの外で sleep
            time.sleep(sleep_seconds + 5)  # ちょっと余裕見る

            # sleep から戻ってきたら exhausted を全部リセットして再開
            with self._lock:
                self.exhausted = [False] * len(self.exhausted)
                print(
                    "[KEY ROTATOR] Daily limit reset assumed. "
                    "Cleared exhausted flags and will resume using API keys."
                )
            # while の先頭に戻って再度キーを選ぶ

    def mark_exhausted(self, idx: int, reason: str = "") -> None:
        """このキーは今日の quota を使い切ったとみなして以降使わない。"""
        with self._lock:
            self.exhausted[idx] = True
        print(f"[KEY ROTATOR] Mark {self.names[idx]} as exhausted. reason={reason}")

# =========================================================
# OpenAI のエラー判定 & FT ジョブ作成ヘルパー
# =========================================================

def is_daily_limit_error(msg: str) -> bool:
    """
    エラーメッセージから「日次リミット / quota 系」っぽいものを判定。
    実際のメッセージを見て、必要に応じて条件を調整してください。
    """
    lower = msg.lower()
    return (
        ("daily" in lower and "limit" in lower)
        or ("quota" in lower and "exceeded" in lower)
        or ("usage limit" in lower and "exhausted" in lower)
    )


def create_ft_job_with_limit_handling(
    client: OpenAI,
    training_file_id: str,
    model: str,
    n_epochs: int = 2,
    max_retries: int = 60,
    wait_on_limit_sec: int = 60,
):
    """
    fine-tuning.jobs.create を叩くときに、
    - 「maximum of 5 active requests」や short-term rate limit は待ってリトライ
    - 「日次リミット / quota」っぽいエラーは呼び出し元に投げる
    """
    for attempt in range(1, max_retries + 1):
        try:
            time.sleep(3)  # API 連打防止
            job = client.fine_tuning.jobs.create(
                training_file=training_file_id,
                model=model,
                hyperparameters={"n_epochs": n_epochs},
            )
            print(f"[FT] job created (attempt {attempt}): {job.id}")
            return job

        except Exception as e:  # noqa: BLE001
            msg = str(e)

            # ---- 日次リミット / quota 系はここで判定して「即 raise」 ----
            if is_daily_limit_error(msg):
                print("[FT ERROR] Seems daily/quota limit reached:")
                print(msg)
                # この例外はそのまま上に投げる（外側でキー切り替えする）
                raise

            # ---- それ以外の 429 / active job limit っぽいものは待ってリトライ ----
            if (
                "maximum of 5 active requests" in msg
                or "rate_limit_exceeded" in msg
                or "429" in msg
            ):
                print(
                    f"[FT WARNING] hit active-job / short-term rate limit "
                    f"(attempt {attempt}/{max_retries}). wait {wait_on_limit_sec} sec...\n"
                    f"  {msg}"
                )
                time.sleep(wait_on_limit_sec)
                continue

            # 明らかに別種のエラーはそのまま上げる
            raise

    raise RuntimeError(
        f"Failed to create fine-tuning job after {max_retries} retries "
        f"(still hitting active-job / short-term rate limit)."
    )


def wait_for_job_completion(
    client: OpenAI,
    job_id: str,
    fold_idx: int,
    poll_interval: int = 60,
):
    """
    fine_tuning.jobs.retrieve で status を監視し、
    succeeded / failed / cancelled になるまで待つ。
    """
    while True:
        time.sleep(3)  # API を叩く前に少し待つ（rate limit 対策）
        job = client.fine_tuning.jobs.retrieve(job_id)
        print(f"[fold {fold_idx + 1}] status: {job.status}")

        if job.status in ("succeeded", "failed", "cancelled"):
            break

        time.sleep(poll_interval)

    if job.status != "succeeded":
        raise RuntimeError(f"fine-tuning failed on fold {fold_idx + 1}: {job.status}")

    return job


def load_extracted_data_for_db(
    db: str,
) -> List[Dict[str, Any]]:
    """
    questions/json_format/{db}.json から質問データを読み込む。
    """
    json_path = os.path.join("questions", "json_format", f"{db}.json")
    with open(json_path, "r") as f:
        questions = json.load(f)

    extracted_data: List[Dict[str, Any]] = []
    for question in questions:
        item = {
            "id": question.get("id", ""),
            "question": question.get("user_question") or question.get("question", ""),
            "variables": question.get("variables", []),
            "params": question.get("param") or question.get("params", []),
            "output": question.get("sparql") or question.get("output", ""),
            "share_url": question.get("share_url", ""),
        }
        extracted_data.append(item)

    print(f"[load] db={db}, num_questions={len(extracted_data)}")
    return extracted_data


# =========================================================
# CV 用ユーティリティ
# =========================================================

def extract_main_id(id_str: str) -> int:
    """
    "ID12-3-1" のような ID 文字列から 12 の部分だけを取り出して int にする
    """
    head = id_str.split("-")[0]  # "ID12"
    num = re.sub(r"\D", "", head)  # "12"
    return int(num)


def make_train_test_data(
    all_items: List[Dict[str, Any]],
    test_main_ids: List[int],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    main_id のリスト test_main_ids をテスト用にして、
    それ以外を学習用に分ける。
    1 vs All では test_main_ids は常に1要素の想定。
    """
    test_main_ids_set = set(test_main_ids)

    test_data: List[Dict[str, Any]] = []
    train_data: List[Dict[str, Any]] = []

    for d in all_items:
        mid = extract_main_id(d["id"])
        if mid in test_main_ids_set:
            test_data.append(d)
        else:
            train_data.append(d)

    # id で重複しているものをテストデータ側から落とす
    seen = set()
    dedup_test: List[Dict[str, Any]] = []
    for d in test_data:
        if d["id"] in seen:
            continue
        dedup_test.append(d)
        seen.add(d["id"])

    return train_data, dedup_test


def make_training_jsonl(
    train_data: List[Dict[str, Any]],
    db: str,
    fold_idx: int,
    system_prompt: str,
) -> str:
    """
    fine-tuning 用の JSONL を fold ごとに作成する
    """
    os.makedirs(DATASET_DIR, exist_ok=True)
    out_path = os.path.join(DATASET_DIR, f"train_data_cv_fold{fold_idx + 1}_{db}.jsonl")

    with open(out_path, "w") as f:
        for data in train_data:
            # "PREFIX ..." 以降を抜き出して answer にする
            if data.get("output"):
                output = data["output"]
                prefix_idx = output.find("PREFIX")
                answer = output[prefix_idx:] if prefix_idx != -1 else output
            else:
                answer = ""

            message = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": data["question"]},
                    {"role": "assistant", "content": answer},
                ]
            }
            f.write(json.dumps(message, ensure_ascii=False) + "\n")

    return out_path


def process_items(new_items: List[Dict[str, Any]], db: str) -> List[Dict[str, Any]]:
    """
    test 用の質問リストを作る。
    """
    processed_list: List[Dict[str, Any]] = []

    for new_item in new_items:
        new_dict = {
            "user_question": new_item["question"],
            "database": db,
            "variables": new_item.get("variables", []),
            "param": new_item.get("params", []),
            "id": new_item["id"],
            "sparql": new_item.get("output", ""),
        }
        processed_list.append(new_dict)

    return processed_list


def normalize_score_dict(score_dict: Dict[str, Any]) -> Tuple[Dict[str, Any], float]:
    """
    evaluate_jaccard の出力を JSON 保存しやすい形にして、
    ついでに質問ごとの平均 Jaccard を計算する
    """
    normalized: Dict[str, Any] = {}
    per_question_scores: List[float] = []

    for key, value in score_dict.items():
        if isinstance(value, dict) and "jaccard_score" in value:
            jaccard_value = float(value["jaccard_score"])
            normalized[key] = {"jaccard_score": jaccard_value}
            per_question_scores.append(jaccard_value)
        else:
            try:
                normalized[key] = float(value)
            except Exception:  # noqa: BLE001
                normalized[key] = value

    mean_val = (
        sum(per_question_scores) / len(per_question_scores)
        if per_question_scores
        else 0.0
    )
    return normalized, mean_val


def save_cv_results(
    run_id: str,
    db: str,
    system_prompt: str,
    fold_outputs: List[Dict[str, Any]],
    fold_scores: List[float],
    cv_mean: float,
) -> Tuple[str, str]:
    """
    CV の結果を JSON + CSV で保存
    """
    os.makedirs(CV_RUNS_DIR, exist_ok=True)

    # JSON で全体サマリ
    json_path = os.path.join(CV_RUNS_DIR, f"cv_run_{db}_{run_id}.json")
    summary = {
        "db": db,
        "run_id": run_id,
        "system_prompt": system_prompt,
        "per_fold_mean_jaccard": fold_scores,
        "cv_mean_jaccard": cv_mean,
        "folds": fold_outputs,
    }
    with open(json_path, "w") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    # CSV で fold × id ごとの jaccard_score
    csv_path = os.path.join(CV_RUNS_DIR, f"cv_scores_{db}_{run_id}.csv")
    rows: List[Dict[str, Any]] = []
    for fold in fold_outputs:
        fold_idx = fold.get("fold_index")
        for qid, metrics in fold["score"].items():
            if isinstance(metrics, dict) and "jaccard_score" in metrics:
                rows.append(
                    {
                        "fold": fold_idx,
                        "id": qid,
                        "jaccard_score": metrics["jaccard_score"],
                    }
                )

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["fold", "id", "jaccard_score"])
        writer.writeheader()
        writer.writerows(rows)

    print("Saved CV artifacts:", json_path, csv_path)
    return json_path, csv_path


# =========================================================
# CV 状態の保存 / 復元
# =========================================================

def load_cv_state(state_path: str) -> Dict[str, Any]:
    """途中経過(state)をJSONから読み込む"""
    if not os.path.exists(state_path):
        return {}
    with open(state_path, "r") as f:
        return json.load(f)


def save_cv_state(state_path: str, state: Dict[str, Any]) -> None:
    """途中経過(state)をJSONに保存する"""
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    with open(state_path, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


# =========================================================
# 1 fold 分の処理（APIキーのローテーション＋FT＋評価）
# =========================================================

def run_one_fold(
    fold_idx: int,
    test_main_ids: List[int],
    system_prompt: str,
    endpoint: str,
    db: str,
    extracted_data: List[Dict[str, Any]],
    key_rotator: APIKeyRotator,
) -> Dict[str, Any]:
    """
    1 fold 分の train → fine-tuning → test → スコア算出までを実行。
    ここでは 1 vs All の前提で test_main_ids は1要素の想定。
    日次リミットに当たったキーは次のキーに切り替えて再試行する。
    """

    while True:
        key_idx, client, key_name = key_rotator.get_client()
        print(f"[fold {fold_idx + 1}] use client from {key_name}")

        try:
            print(f"===== Fold {fold_idx + 1} (db={db}) =====")
            print(f"[fold {fold_idx + 1}] test_main_ids: {sorted(test_main_ids)}")

            # --- データ分割 (1 vs All) ---
            test_ids_for_log = list(test_main_ids)
            train_data, test_source_data = make_train_test_data(
                extracted_data, test_main_ids
            )
            print(
                f"[fold {fold_idx + 1}] train: {len(train_data)}, test: {len(test_source_data)}"
            )

            # --- fine-tuning 用 JSONL 作成 & アップロード ---
            train_jsonl_path = make_training_jsonl(
                train_data, db=db, fold_idx=fold_idx, system_prompt=system_prompt
            )

            with open(train_jsonl_path, "rb") as f:
                time.sleep(3)  # files.create の前に軽く wait
                uploaded = client.files.create(file=f, purpose="fine-tune")
            training_file_id = uploaded.id
            print(f"[fold {fold_idx + 1}] training_file: {training_file_id}")

            # --- fine-tuning ジョブ作成（5 active job / rate limit 対応付き） ---
            job = create_ft_job_with_limit_handling(
                client=client,
                training_file_id=training_file_id,
                model="gpt-4o-mini-2024-07-18",
                n_epochs=2,
            )
            print(f"[fold {fold_idx + 1}] job id: {job.id}")

            # --- 学習完了までポーリング ---
            job = wait_for_job_completion(
                client=client,
                job_id=job.id,
                fold_idx=fold_idx,
                poll_interval=60,
            )
            ft_model = job.fine_tuned_model
            print(f"[fold {fold_idx + 1}] fine-tuned model: {ft_model}")

            # --- テスト質問の作成 ---
            test_questions = process_items(test_source_data, db=db)

            # --- fine-tuned モデルで SPARQL 生成 ---
            for q in test_questions:
                time.sleep(2)  # chat.completions.create の前に軽く wait
                completion = client.chat.completions.create(
                    model=ft_model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": q["user_question"]},
                    ],
                )
                q["llm_sparql"] = completion.choices[0].message.content

            # --- 生成した SPARQL を実行して results を付与 ---
            query_results: List[Tuple[Any, str]] = []

            def _run_query(question: Dict[str, Any]) -> Tuple[Any, str]:
                # エンドポイントへの負荷を抑えたいならここに sleep を入れる
                time.sleep(0.1)
                result, _ = execute_query(
                    question, endpoint, "llm_sparql", 10000, ""
                )
                return result, question["id"]

            # テスト質問内でのクエリ実行も並列化
            with ThreadPoolExecutor(max_workers=8) as ex:
                futures = [ex.submit(_run_query, q) for q in test_questions]
                for fut in as_completed(futures):
                    result, qid = fut.result()
                    query_results.append((result, qid))
                    # 結果数のログ（result が list/tuple の場合のみ）
                    if isinstance(result, (list, tuple)) and len(result) > 0:
                        try:
                            length = len(result[0])
                        except Exception:  # noqa: BLE001
                            length = 0
                    else:
                        length = 0
                    print(qid, length)

            # results を test_questions に紐づけ
            for (result, question_id) in query_results:
                for question in test_questions:
                    if question["id"] == question_id:
                        # evaluate_jaccard が unhashable type: 'dict' を出さないよう、
                        # エラーオブジェクト(dict)の場合は空リストに置き換える
                        if isinstance(result, dict):
                            question["results"] = []
                        else:
                            question["results"] = result

            # --- 正解側（gold）の results を用意 ---
            save_path_with_results = (
                f"data/questions/easy_question_augmented_with_results_{db}_baseline_FT.json"
            )
            with open(save_path_with_results, "r") as f:
                all_gold_questions = json.load(f)

            gold_ids = {d["id"] for d in test_questions}
            gold_questions = [q for q in all_gold_questions if q["id"] in gold_ids]

            # --- Jaccard スコア計算 ---
            score = evaluate_jaccard(gold_questions, test_questions)
            normalized_score, mean_jaccard = normalize_score_dict(score)

            print(f"[fold {fold_idx + 1}] mean Jaccard: {mean_jaccard:.4f}")

            return {
                "fold_index": fold_idx + 1,
                "test_main_ids": test_ids_for_log,
                "training_file_id": training_file_id,
                "fine_tune_job_id": job.id,
                "fine_tuned_model": ft_model,
                "mean_jaccard": mean_jaccard,
                "score": normalized_score,
                "test_questions": test_questions,
                "job_status": job.status,
                "api_key_name": key_name,
            }

        except Exception as e:  # noqa: BLE001
            msg = str(e)
            # 日次リミット / quota 系は API キーを切り替えて再試行
            if is_daily_limit_error(msg):
                print(
                    f"[fold {fold_idx + 1}] daily/quota limit on {key_name}, "
                    "mark key exhausted and try another key."
                )
                key_rotator.mark_exhausted(key_idx, reason=msg)
                # while ループの先頭に戻って別キーで再挑戦
                continue

            # それ以外の例外はそのまま投げる
            raise


# =========================================================
# 1 DB 分の 1-vs-All CV 実行（途中から再開可 & 最大3並列）
# =========================================================

def run_cv_for_db(
    db: str,
    extracted_data: List[Dict[str, Any]],
    endpoint: str,
    key_rotator: APIKeyRotator,
) -> Dict[str, Any]:
    """
    指定した db について 1-vs-All CV を実行し、結果を保存してサマリを返す。
    途中で止まっても、fold（=main_idごと）の状態を JSON に保存しておくことで再開可能。
    FT ジョブは fold 単位で最大3並列。
    """
    print("=" * 80)
    print(f"[CV] start db={db}, num_questions={len(extracted_data)}")

    # --- main_id の一覧を作成 ---
    all_main_ids = sorted({extract_main_id(d["id"]) for d in extracted_data})
    n = len(all_main_ids)
    if n == 0:
        print(f"[CV] db={db} has no data. skip.")
        return {}

    print(f"[CV] db={db}, num_main_ids={n}")

    # 順序をランダムにしたい場合：
    # rand = random.Random(RANDOM_SEED)
    # rand.shuffle(all_main_ids)

    # 1 vs All: 各 main_id ごとに fold を1つ作る
    fold_id_lists: List[List[int]] = [[mid] for mid in all_main_ids]

    system_prompt = (
        "Create a SPARQL query to retrieve values from the database for the user question"
    )

    state_path = os.path.join(CV_RUNS_DIR, f"cv_state_{db}.json")
    cv_state = load_cv_state(state_path)
    state_lock = threading.Lock()

    fold_outputs: List[Dict[str, Any]] = []
    remaining_folds: List[Tuple[int, List[int]]] = []

    # すでに終わっている fold は fold_outputs に入れてスキップ対象から外す
    for fold_idx, test_ids in enumerate(fold_id_lists):
        fold_name = f"fold{fold_idx + 1}"
        print("-" * 60)
        print(
            f"[CV] db={db} {fold_name} "
            f"(fold_index={fold_idx + 1}/{len(fold_id_lists)}, main_id={test_ids[0]})"
        )

        if fold_name in cv_state:
            saved = cv_state[fold_name]
            if saved.get("job_status") == "succeeded":
                print(f"[CV] {fold_name} already finished -> skip")
                fold_outputs.append(saved)
                continue

        # まだ終わっていない fold は実行対象
        remaining_folds.append((fold_idx, test_ids))

    # 実行すべき fold がなければそのまま集計
    if remaining_folds:
        print(
            f"[CV] db={db} will run {len(remaining_folds)} 1-vs-All folds in parallel "
            f"(max_workers={min(MAX_PARALLEL_FT_JOBS, len(remaining_folds))})"
        )

        def task(fold_idx: int, test_ids: List[int]) -> None:
            # それぞれの fold を実行し、終わったら state を更新
            time.sleep(5)  # 軽く待って rate limit 緩和
            fold_result = run_one_fold(
                fold_idx=fold_idx,
                test_main_ids=test_ids,
                system_prompt=system_prompt,
                endpoint=endpoint,
                db=db,
                extracted_data=extracted_data,
                key_rotator=key_rotator,
            )
            fold_name = f"fold{fold_idx + 1}"
            with state_lock:
                cv_state[fold_name] = fold_result
                save_cv_state(state_path, cv_state)
                fold_outputs.append(fold_result)

            print(
                f"[CV] db={db} {fold_name} finished - "
                f"job_id={fold_result['fine_tune_job_id']}, "
                f"mean Jaccard={fold_result['mean_jaccard']:.4f}, "
                f"key={fold_result['api_key_name']}"
            )

        # 最大3並列で fold を処理
        max_workers = min(MAX_PARALLEL_FT_JOBS, len(remaining_folds))
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futures = [
                ex.submit(task, fold_idx, test_ids)
                for (fold_idx, test_ids) in remaining_folds
            ]
            # エラーを検出しておく
            for fut in as_completed(futures):
                fut.result()  # 例外があればここで raise

    # fold_outputs は既存 + 今回の結果が混ざっているので fold_index 順に並べ直す
    fold_outputs_sorted = sorted(fold_outputs, key=lambda fo: fo["fold_index"])

    # --- fold ごとのスコアと全体平均 ---
    fold_scores = [fo["mean_jaccard"] for fo in fold_outputs_sorted]
    cv_mean = sum(fold_scores) / len(fold_scores)

    print(f"========== 1-vs-All CV result (db={db}, folds={len(fold_outputs_sorted)}) ==========")
    print("Per-fold mean Jaccard:", fold_scores)
    print("1-vs-All average Jaccard:", cv_mean)

    # --- fold ごとの fine-tuned モデル名を保存 ---
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fine_tuned_models = {
        f"fold{fo['fold_index']}": fo["fine_tuned_model"]
        for fo in fold_outputs_sorted
    }
    ft_models_path = os.path.join(OUTPUT_DIR, f"fine_tuned_models_cv_{db}.json")
    with open(ft_models_path, "w") as f:
        json.dump(fine_tuned_models, f, ensure_ascii=False, indent=2)

    print("Saved fine-tuned models per fold:", fine_tuned_models)
    print("Saved to:", ft_models_path)

    # --- CV 実験全体の記録を JSON/CSV で保存 ---
    run_id = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    cv_json_path, cv_csv_path = save_cv_results(
        run_id, db, system_prompt, fold_outputs_sorted, fold_scores, cv_mean
    )

    return {
        "db": db,
        "run_id": run_id,
        "fold_scores": fold_scores,
        "cv_mean": cv_mean,
        "cv_state_path": state_path,
        "ft_models_path": ft_models_path,
        "cv_json_path": cv_json_path,
        "cv_csv_path": cv_csv_path,
    }


# =========================================================
# メイン処理：全 DB まとめて実行 ＆ サマリ保存
# =========================================================

def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(CV_RUNS_DIR, exist_ok=True)

    # OpenAI API キーのローテーター
    key_rotator = APIKeyRotator()

    all_db_summary: Dict[str, Any] = {}
    overall_start = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

    for db in DB_LIST:
        # ENDPOINT_{DB} を環境変数から取得
        endpoint_env = f"ENDPOINT_{db.upper()}"
        endpoint = os.environ.get(endpoint_env)
        if not endpoint:
            print(f"[WARN] {endpoint_env} is not set. Skip db={db}.")
            continue

        try:
            extracted_data = load_extracted_data_for_db(db)
        except Exception as e:  # noqa: BLE001
            print(f"[ERROR] failed to load data for db={db}: {e}")
            continue

        if not extracted_data:
            print(f"[WARN] db={db} has no data. skip.")
            continue

        try:
            summary = run_cv_for_db(
                db=db,
                extracted_data=extracted_data,
                endpoint=endpoint,
                key_rotator=key_rotator,
            )
        except Exception as e:  # noqa: BLE001
            print(f"[ERROR] CV failed for db={db}: {e}")
            continue

        all_db_summary[db] = summary

    # すべての DB のサマリをまとめて保存
    all_summary_path = os.path.join(
        CV_RUNS_DIR, f"all_db_summary_{overall_start}.json"
    )
    with open(all_summary_path, "w") as f:
        json.dump(all_db_summary, f, ensure_ascii=False, indent=2)

    print("All DB summary saved to:", all_summary_path)


if __name__ == "__main__":
    main()

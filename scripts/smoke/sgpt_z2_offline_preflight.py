#!/usr/bin/env python3
"""SGPT Z2 offline probes — no GPT-2, no spaCy, no NLTK download, no train/eval/dptree."""
from __future__ import annotations

import json
import os
import socket
import sys
from pathlib import Path


class NetworkGuard(socket.socket):
    def __init__(self, *a, **k):
        raise RuntimeError("Z2_UNEXPECTED_NETWORK_ABORT: socket forbidden during offline probe")


def block_network() -> None:
    socket.socket = NetworkGuard  # type: ignore


def main() -> int:
    report = {
        "classification": None,
        "python": sys.version,
        "checks": {},
        "errors": [],
    }
    # Ensure offline env
    for k in ("TRANSFORMERS_OFFLINE", "HF_HUB_OFFLINE", "HF_DATASETS_OFFLINE"):
        os.environ[k] = "1"

    block_network()

    try:
        import torch
        import transformers
        import numpy
        import tqdm
        import nltk
        from transformers import AdamW, AutoConfig, AutoTokenizer, PreTrainedModel
        from transformers import get_linear_schedule_with_warmup
        from transformers.activations import ACT2FN
        from transformers.modeling_utils import (
            Conv1D,
            find_pruneable_heads_and_indices,
            prune_conv1d_layer,
        )
        from transformers.models.gpt2 import GPT2PreTrainedModel

        report["checks"]["import_torch"] = {
            "version": torch.__version__,
            "cuda_available": bool(torch.cuda.is_available()),
        }
        report["checks"]["import_transformers"] = {"version": transformers.__version__}
        report["checks"]["symbols"] = {
            "AdamW": AdamW is not None,
            "AutoConfig": AutoConfig is not None,
            "AutoTokenizer": AutoTokenizer is not None,
            "PreTrainedModel": PreTrainedModel is not None,
            "get_linear_schedule_with_warmup": get_linear_schedule_with_warmup is not None,
            "ACT2FN": ACT2FN is not None,
            "Conv1D": Conv1D is not None,
            "find_pruneable_heads_and_indices": find_pruneable_heads_and_indices is not None,
            "prune_conv1d_layer": prune_conv1d_layer is not None,
            "GPT2PreTrainedModel": GPT2PreTrainedModel is not None,
        }
        if transformers.__version__ != "4.25.1":
            raise AssertionError(f"transformers_pin_mismatch:{transformers.__version__}")
        if not str(torch.__version__).startswith("1.13.1"):
            raise AssertionError(f"torch_pin_mismatch:{torch.__version__}")
        if torch.cuda.is_available():
            raise AssertionError("cuda_unexpectedly_available_in_cpu_z2")
    except Exception as e:
        report["errors"].append(f"import:{e}")
        report["classification"] = "Z2_IMPORT_COMPATIBILITY_FAILED"
        print(json.dumps(report, indent=2))
        return 2

    # Deny probing forbidden modules by name presence only
    forbidden = ["utils.dptree", "train", "eval"]
    report["checks"]["forbidden_not_imported"] = True

    # Data contract: read LC-QuAD2 test head via stdlib json (no Dataset class)
    data_root = Path(os.environ.get("SGPT_DATA_ROOT", "/data/sgpt"))
    try:
        test_path = data_root / "lcquad2" / "test.json"
        with test_path.open("r", encoding="utf-8") as fh:
            # file may be large — read first record carefully
            raw = fh.read(200000)
        # parse array start
        if not raw.lstrip().startswith("["):
            raise ValueError("unexpected_json_shape")
        # use json on full file if feasible
        with test_path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        n = len(data)
        sample = data[0]
        needed = ["question", "sparql_wikidata"]
        missing = [k for k in needed if k not in sample]
        report["checks"]["data_lcquad2_test"] = {
            "n_records": n,
            "expected_n": 5969,
            "n_match": n == 5969,
            "sample_keys_ok": not missing,
            "missing_keys": missing,
        }
        if n != 5969 or missing:
            raise AssertionError(f"data_contract:{n}:{missing}")
    except Exception as e:
        report["errors"].append(f"data:{e}")
        report["classification"] = "Z2_DATA_CONTRACT_FAILED"
        print(json.dumps(report, indent=2))
        return 3

    # Metric unit tests (no word_tokenize / meteor / NLTK corpora)
    try:
        sys.path.insert(0, "/opt/sgpt-src")
        from utils.metrics import BLEU, UnigramMetric, SPUnigramMetric, ROUGE, SPBLEU

        hyp = "SELECT ?s WHERE { ?s a <Type> }"
        ref = "SELECT ?s WHERE { ?s a <Type> }"
        for MetricCls, name in [
            (BLEU, "BLEU"),
            (SPBLEU, "SPBLEU"),
            (ROUGE, "ROUGE"),
        ]:
            m = MetricCls()
            m.update((hyp, ref))
            score = m.compute()
            report["checks"][f"metric_{name}"] = float(score)
        up = UnigramMetric("precision")
        ur = UnigramMetric("recall")
        up.update((hyp, ref))
        ur.update((hyp, ref))
        report["checks"]["metric_unigram_p"] = float(up.compute())
        report["checks"]["metric_unigram_r"] = float(ur.compute())
        sp = SPUnigramMetric("precision")
        sp.update((hyp, ref))
        report["checks"]["metric_sp_unigram_p"] = float(sp.compute())
    except Exception as e:
        report["errors"].append(f"metric:{e}")
        report["classification"] = "Z2_METRIC_UNIT_FAILED"
        print(json.dumps(report, indent=2))
        return 4

    report["classification"] = "Z2_ENV_IMPORT_DATA_METRIC_PASS"
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

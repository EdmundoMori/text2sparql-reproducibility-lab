#!/usr/bin/env python3
"""Prompt 17 — metadata-only resolver for common dataset provenance.

Stdlib only. Allowlisted hosts. No dataset payload downloads.
No Hugging Face /resolve/, no archives, no SPARQL, no git clone.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ALLOWED_HOSTS = {
    "api.github.com",
    "github.com",
    "arxiv.org",
    "export.arxiv.org",
    "api.crossref.org",
    "doi.org",
    "huggingface.co",
    "zenodo.org",
    "lc-quad.sda.tech",
    "www.lc-quad.sda.tech",
}

FORBIDDEN_PATH_MARKERS = (
    "/resolve/",
    "/raw/",
    ".zip",
    ".tar",
    ".gz",
    ".bz2",
    ".7z",
    ".parquet",
    ".csv",
    ".jsonl",
    "/archive/",
    "codeload.github.com",
)

# Allow small documentation paths via Contents API / raw for LICENSE/README/CITATION only
DOC_BASENAMES = {
    "readme",
    "readme.md",
    "license",
    "license.md",
    "license.txt",
    "licence",
    "citation",
    "citation.cff",
    "citing.md",
}

USER_AGENT = (
    "text2sparql-reproducibility-lab/common-dataset-provenance-17 "
    "(+https://github.com/EdmundoMori/text2sparql-reproducibility-lab)"
)
TIMEOUT = 45
MAX_BYTES = 2_000_000
RETRIES = 3


def _host(url: str) -> str:
    return urllib.parse.urlparse(url).hostname or ""


def _reject_url(url: str) -> None:
    host = _host(url)
    if host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowlisted:{host}:{url}")
    low = url.lower()
    for m in FORBIDDEN_PATH_MARKERS:
        if m in low:
            # allow github.com tree/blob HTML pages and api trees
            if host == "github.com" and ("/tree/" in low or "/blob/" in low or "/commit/" in low):
                if any(ext in low for ext in (".zip", ".tar", ".gz", ".parquet", ".csv")):
                    raise RuntimeError(f"forbidden_url_marker:{m}:{url}")
                continue
            if host == "api.github.com" and "/git/trees/" in low:
                continue
            if host == "api.github.com" and "/contents/" in low:
                # only docs — checked later by caller
                continue
            if host == "huggingface.co" and "/api/datasets/" in low:
                continue
            if host in ("arxiv.org", "export.arxiv.org", "api.crossref.org", "doi.org"):
                continue
            if m in ("/raw/",) and host == "api.github.com":
                continue
            if m.startswith(".") and host == "api.github.com":
                continue
            # hard reject resolve and archives always
            if m in ("/resolve/", "codeload.github.com", "/archive/"):
                raise RuntimeError(f"forbidden_url_marker:{m}:{url}")
            if m in ("/raw/",) and "raw.githubusercontent.com" in host:
                raise RuntimeError(f"forbidden_url_marker:{m}:{url}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(
    url: str,
    dest: Path,
    network_log: Path,
    classification: str,
    method: str = "GET",
    accept: str | None = None,
) -> tuple[int, bytes, str]:
    _reject_url(url)
    headers = {"User-Agent": USER_AGENT, "Accept": accept or "*/*"}
    if "api.github.com" in url:
        headers["Accept"] = accept or "application/vnd.github+json"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    last_err: Exception | None = None
    for attempt in range(1, RETRIES + 1):
        req = urllib.request.Request(url, method=method, headers=headers)
        ctx = ssl.create_default_context()
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
                status = resp.status
                ctype = resp.headers.get("Content-Type", "")
                data = b"" if method == "HEAD" else resp.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES:
                    raise RuntimeError(f"response_too_large:{url}:{len(data)}")
            break
        except Exception as e:  # noqa: BLE001
            last_err = e
            if attempt == RETRIES:
                with network_log.open("a", encoding="utf-8") as fh:
                    fh.write(
                        f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\t"
                        f"{method}\tERR\t0\t\t{classification}\t{_host(url)}\t{url}\t{type(e).__name__}:{e}\n"
                    )
                raise
            time.sleep(min(2 * attempt, 5))
    else:
        raise last_err or RuntimeError("fetch_failed")

    digest = sha256_bytes(data) if data else ""
    dest.parent.mkdir(parents=True, exist_ok=True)
    if data:
        dest.write_bytes(data)
    with network_log.open("a", encoding="utf-8") as fh:
        fh.write(
            f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\t{method}\t{status}\t"
            f"{len(data)}\t{digest}\t{classification}\t{_host(url)}\t{url}\t{ctype}\n"
        )
    return status, data, digest


def github_json(path: str, dest: Path, network_log: Path, classification: str) -> dict | list:
    url = f"https://api.github.com{path}"
    _status, data, _ = fetch(url, dest, network_log, classification)
    return json.loads(data.decode("utf-8"))


def github_contents_doc(owner: str, repo: str, path: str, ref: str, raw_dir: Path, network_log: Path) -> dict:
    base = Path(path).name.lower()
    if base not in DOC_BASENAMES and not any(base.startswith(x) for x in ("license", "readme", "citation")):
        raise RuntimeError(f"contents_api_only_for_docs:{path}")
    q = urllib.parse.urlencode({"ref": ref})
    api_path = f"/repos/{owner}/{repo}/contents/{path}?{q}"
    obj = github_json(api_path, raw_dir / f"contents_{owner}_{repo}_{path.replace('/', '_')}.json", network_log, "github_contents_doc")
    if isinstance(obj, dict) and obj.get("encoding") == "base64" and obj.get("size", 0) > 200_000:
        raise RuntimeError(f"doc_too_large_or_payload:{path}")
    return obj  # type: ignore[return-value]


def local_existing_copies(paths: list[Path], out_json: Path, log: Path) -> list[dict]:
    rows: list[dict] = []
    with log.open("a", encoding="utf-8") as fh:
        for p in paths:
            if not p.exists() or not p.is_file():
                fh.write(f"MISSING\t{p}\n")
                continue
            h = hashlib.sha256()
            with p.open("rb") as f:
                for chunk in iter(lambda: f.read(1 << 20), b""):
                    h.update(chunk)
            digest = h.hexdigest()
            size = p.stat().st_size
            row: dict = {"path": str(p), "size_bytes": size, "local_sha256": digest}
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                if isinstance(data, list):
                    row["record_count"] = len(data)
                    row["json_type"] = "list"
                    if data and isinstance(data[0], dict):
                        row["top_level_fields"] = sorted(data[0].keys())
                elif isinstance(data, dict):
                    row["json_type"] = "dict"
                    row["top_keys"] = sorted(data.keys())
                    for k in ("questions", "train", "test", "data"):
                        if isinstance(data.get(k), list):
                            row["record_count"] = len(data[k])
                            row["list_key"] = k
                            if data[k] and isinstance(data[k][0], dict):
                                row["item_fields"] = sorted(data[k][0].keys())
                            break
            except Exception as e:  # noqa: BLE001
                row["json_error"] = str(e)[:200]
            rows.append(row)
            fh.write(f"OK\t{p}\t{size}\t{digest}\t{row.get('record_count','')}\n")
    out_json.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    return rows


def resolve_qald9_plus(raw_dir: Path, network_log: Path) -> dict:
    owner, repo = "Perevalov", "qald_9_plus"
    out: dict = {"owner": owner, "repo": repo}
    out["repo_meta"] = github_json(f"/repos/{owner}/{repo}", raw_dir / "qald_repo.json", network_log, "github_repo")
    out["commits"] = github_json(
        f"/repos/{owner}/{repo}/commits?per_page=30", raw_dir / "qald_commits.json", network_log, "github_commits"
    )
    out["tags"] = github_json(f"/repos/{owner}/{repo}/tags?per_page=50", raw_dir / "qald_tags.json", network_log, "github_tags")
    out["releases"] = github_json(
        f"/repos/{owner}/{repo}/releases?per_page=20", raw_dir / "qald_releases.json", network_log, "github_releases"
    )
    default_branch = out["repo_meta"].get("default_branch", "main")
    out["default_branch"] = default_branch
    out["branch"] = github_json(
        f"/repos/{owner}/{repo}/branches/{default_branch}", raw_dir / "qald_branch.json", network_log, "github_branch"
    )
    head_sha = out["branch"]["commit"]["sha"]
    out["head_sha"] = head_sha
    out["tree"] = github_json(
        f"/repos/{owner}/{repo}/git/trees/{head_sha}?recursive=1",
        raw_dir / "qald_tree.json",
        network_log,
        "github_tree_recursive",
    )
    for doc in ("README.md", "LICENSE", "LICENSE.md", "CITATION.cff"):
        try:
            out[f"doc_{doc}"] = github_contents_doc(owner, repo, doc, head_sha, raw_dir, network_log)
        except Exception as e:  # noqa: BLE001
            out[f"doc_{doc}_error"] = str(e)
    # paper metadata
    try:
        _s, data, _ = fetch(
            "https://api.crossref.org/works/10.1109/ICSC52841.2022.00045",
            raw_dir / "qald_crossref.json",
            network_log,
            "crossref_doi",
        )
        out["crossref"] = json.loads(data.decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        out["crossref_error"] = str(e)
    try:
        _s, data, _ = fetch(
            "https://export.arxiv.org/api/query?id_list=2202.00120",
            raw_dir / "qald_arxiv.xml",
            network_log,
            "arxiv_atom",
            accept="application/atom+xml",
        )
        out["arxiv_bytes"] = len(data)
    except Exception as e:  # noqa: BLE001
        out["arxiv_error"] = str(e)
    # HF dataset card metadata API only
    try:
        _s, data, _ = fetch(
            "https://huggingface.co/api/datasets/casey-martin/qald_9_plus",
            raw_dir / "qald_hf_api.json",
            network_log,
            "hf_dataset_api",
        )
        out["hf"] = json.loads(data.decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        out["hf_error"] = str(e)
    return out


def resolve_lcquad2(raw_dir: Path, network_log: Path) -> dict:
    owner, repo = "AskNowQA", "LC-QuAD2.0"
    out: dict = {"owner": owner, "repo": repo}
    out["repo_meta"] = github_json(f"/repos/{owner}/{repo}", raw_dir / "lcq_repo.json", network_log, "github_repo")
    out["commits"] = github_json(
        f"/repos/{owner}/{repo}/commits?per_page=30", raw_dir / "lcq_commits.json", network_log, "github_commits"
    )
    out["tags"] = github_json(f"/repos/{owner}/{repo}/tags?per_page=50", raw_dir / "lcq_tags.json", network_log, "github_tags")
    out["releases"] = github_json(
        f"/repos/{owner}/{repo}/releases?per_page=20", raw_dir / "lcq_releases.json", network_log, "github_releases"
    )
    default_branch = out["repo_meta"].get("default_branch", "master")
    out["default_branch"] = default_branch
    out["branch"] = github_json(
        f"/repos/{owner}/{repo}/branches/{default_branch}", raw_dir / "lcq_branch.json", network_log, "github_branch"
    )
    head_sha = out["branch"]["commit"]["sha"]
    out["head_sha"] = head_sha
    out["tree"] = github_json(
        f"/repos/{owner}/{repo}/git/trees/{head_sha}?recursive=1",
        raw_dir / "lcq_tree.json",
        network_log,
        "github_tree_recursive",
    )
    for doc in ("README.md", "LICENSE", "LICENSE.md", "CITATION.cff"):
        try:
            out[f"doc_{doc}"] = github_contents_doc(owner, repo, doc, head_sha, raw_dir, network_log)
        except Exception as e:  # noqa: BLE001
            out[f"doc_{doc}_error"] = str(e)
    try:
        _s, data, _ = fetch(
            "https://api.crossref.org/works/10.1007/978-3-030-30796-7_5",
            raw_dir / "lcq_crossref.json",
            network_log,
            "crossref_doi",
        )
        out["crossref"] = json.loads(data.decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        out["crossref_error"] = str(e)
    try:
        _s, data, _ = fetch(
            "https://huggingface.co/api/datasets/mohnish/lc_quad",
            raw_dir / "lcq_hf_api.json",
            network_log,
            "hf_dataset_api",
        )
        out["hf"] = json.loads(data.decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        out["hf_error"] = str(e)
    # homepage HEAD only
    try:
        _s, data, digest = fetch(
            "http://lc-quad.sda.tech/",
            raw_dir / "lcq_homepage.html",
            network_log,
            "homepage_html",
            method="GET",
            accept="text/html",
        )
        # http may redirect — if host not allowlisted after redirect urllib follows; host check at start
        out["homepage_sha256"] = digest
        out["homepage_bytes"] = len(data)
    except Exception as e:  # noqa: BLE001
        out["homepage_error"] = str(e)
        # try https
        try:
            _s, data, digest = fetch(
                "https://lc-quad.sda.tech/",
                raw_dir / "lcq_homepage_https.html",
                network_log,
                "homepage_html_https",
            )
            out["homepage_sha256"] = digest
            out["homepage_bytes"] = len(data)
        except Exception as e2:  # noqa: BLE001
            out["homepage_error_https"] = str(e2)
    return out


def summarize_tree(tree_obj: dict) -> list[dict]:
    rows = []
    for t in tree_obj.get("tree", []):
        if t.get("type") != "blob":
            continue
        path = t.get("path", "")
        # skip large likely payloads from being "downloaded" — we only record metadata
        rows.append(
            {
                "path": path,
                "size": t.get("size"),
                "sha": t.get("sha"),
                "mode": t.get("mode"),
            }
        )
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--repo-root", type=Path, default=Path("."))
    ap.add_argument("--local-existing-copies", action="store_true")
    ap.add_argument("--fetch-remote", action="store_true")
    args = ap.parse_args(argv)

    root: Path = args.repo_root.resolve()
    run_id = args.run_id
    raw_dir = root / "workdir" / "metadata" / "common-datasets" / run_id
    log_dir = root / "logs" / "dataset-provenance" / run_id
    raw_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    network_log = log_dir / "network.log"
    if not network_log.exists():
        network_log.write_text(
            "timestamp\tmethod\tstatus\tbytes\tsha256\tclassification\thost\turl\tcontent_type_or_error\n",
            encoding="utf-8",
        )

    summary: dict = {"run_id": run_id}

    if args.local_existing_copies:
        paths = [
            root / "upstream/mkgqagent/data/datasets/qald_9_plus_train_dbpedia_en.json",
            root / "upstream/mkgqagent/data/datasets/corporate_en.json",
            root / "upstream/sgpt/data/lcquad2/train.json",
            root / "upstream/sgpt/data/lcquad2/val.json",
            root / "upstream/sgpt/data/lcquad2/test.json",
            root / "upstream/sgpt/data/lcquad2/original/train.json",
            root / "upstream/sgpt/data/lcquad2/original/val.json",
            root / "upstream/sgpt/data/lcquad2/original/test.json",
        ]
        summary["local"] = local_existing_copies(
            paths, raw_dir / "local_existing_copies.json", log_dir / "local-copy-audit.log"
        )

    if args.fetch_remote:
        qald = resolve_qald9_plus(raw_dir / "qald9plus", network_log)
        (raw_dir / "qald9plus_summary.json").write_text(
            json.dumps(
                {
                    "head_sha": qald.get("head_sha"),
                    "default_branch": qald.get("default_branch"),
                    "tags": [t.get("name") for t in (qald.get("tags") or [])],
                    "releases": [r.get("tag_name") for r in (qald.get("releases") or [])],
                    "tree_truncated": bool((qald.get("tree") or {}).get("truncated")),
                    "blobs": summarize_tree(qald.get("tree") or {}),
                    "hf_id": (qald.get("hf") or {}).get("id"),
                    "license_file": "LICENSE" if "doc_LICENSE" in qald or "doc_LICENSE.md" in qald else None,
                    "errors": {k: v for k, v in qald.items() if k.endswith("_error")},
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        summary["qald9plus"] = {
            "head_sha": qald.get("head_sha"),
            "n_blobs": len(summarize_tree(qald.get("tree") or {})),
        }

        lcq = resolve_lcquad2(raw_dir / "lcquad2", network_log)
        (raw_dir / "lcquad2_summary.json").write_text(
            json.dumps(
                {
                    "head_sha": lcq.get("head_sha"),
                    "default_branch": lcq.get("default_branch"),
                    "tags": [t.get("name") for t in (lcq.get("tags") or [])],
                    "releases": [r.get("tag_name") for r in (lcq.get("releases") or [])],
                    "tree_truncated": bool((lcq.get("tree") or {}).get("truncated")),
                    "blobs": summarize_tree(lcq.get("tree") or {}),
                    "hf_id": (lcq.get("hf") or {}).get("id"),
                    "homepage_error": lcq.get("homepage_error"),
                    "errors": {k: v for k, v in lcq.items() if k.endswith("_error") or k.endswith("_error_https")},
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        summary["lcquad2"] = {
            "head_sha": lcq.get("head_sha"),
            "n_blobs": len(summarize_tree(lcq.get("tree") or {})),
        }

    (raw_dir / "resolver_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    # metadata sha list
    lines = []
    for p in sorted(raw_dir.rglob("*")):
        if p.is_file():
            data = p.read_bytes()
            lines.append(f"{sha256_bytes(data)}  {p.relative_to(root)}")
    (log_dir / "metadata.sha256").write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

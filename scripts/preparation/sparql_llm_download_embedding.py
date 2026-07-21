#!/usr/bin/env python3
"""Controlled download of exact FastEmbed model intfloat/multilingual-e5-large.

Abort if:
- model id is not exact
- FastEmbed resolves a different model name
- provenance cannot be determined
- post-download inventory is empty
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

REQUIRED_MODEL = "intfloat/multilingual-e5-large"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inventory(cache_dir: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not cache_dir.exists():
        return rows
    for p in sorted(cache_dir.rglob("*")):
        if p.is_file():
            rows.append(
                {
                    "path": str(p.relative_to(cache_dir)),
                    "size_bytes": p.stat().st_size,
                    "sha256": sha256_file(p),
                }
            )
    return rows


def main() -> int:
    cache_dir = Path(os.environ["EMBEDDING_CACHE_DIR"])
    out = Path(os.environ.get("DOWNLOAD_OUTPUT", "/data/output/embedding-download.json"))
    out.parent.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    model = os.environ.get("EMBEDDING_MODEL", REQUIRED_MODEL)
    if model != REQUIRED_MODEL:
        err = {"ok": False, "error": f"REFUSED_NON_EXACT_MODEL:{model}"}
        out.write_text(json.dumps(err, indent=2) + "\n")
        print(json.dumps(err), file=sys.stderr)
        return 2

    from fastembed import TextEmbedding
    import fastembed

    supported = TextEmbedding.list_supported_models()
    meta = None
    for m in supported:
        name = m.get("model") if isinstance(m, dict) else str(m)
        if name == REQUIRED_MODEL:
            meta = m
            break
    if meta is None:
        err = {"ok": False, "error": "PROVENANCE_NOT_FOUND_IN_FASTEMBED_SUPPORTED_MODELS"}
        out.write_text(json.dumps(err, indent=2) + "\n")
        print(json.dumps(err), file=sys.stderr)
        return 3

    sources = meta.get("sources") if isinstance(meta, dict) else None
    if not sources:
        err = {"ok": False, "error": "PROVENANCE_SOURCES_MISSING", "meta": meta}
        out.write_text(json.dumps(err, indent=2) + "\n")
        print(json.dumps(err), file=sys.stderr)
        return 3

    os.environ["FASTEMBED_CACHE_PATH"] = str(cache_dir)
    # Allow download only in this script (caller provides network)
    os.environ.pop("HF_HUB_OFFLINE", None)
    os.environ.pop("TRANSFORMERS_OFFLINE", None)

    report: dict[str, Any] = {
        "ok": False,
        "requested_model": REQUIRED_MODEL,
        "resolved_model": meta.get("model"),
        "fastembed_version": getattr(fastembed, "__version__", "unknown"),
        "provenance": {
            "sources": sources,
            "model_file": meta.get("model_file"),
            "additional_files": meta.get("additional_files"),
            "dim": meta.get("dim"),
            "size_in_GB": meta.get("size_in_GB"),
            "license": meta.get("license"),
            "description": meta.get("description"),
        },
        "cache_dir": str(cache_dir),
        "files_before": inventory(cache_dir),
        "download_started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    if report["resolved_model"] != REQUIRED_MODEL:
        report["error"] = "RESOLVED_MODEL_MISMATCH"
        out.write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps({"ok": False, "error": report["error"]}), file=sys.stderr)
        return 2

    t0 = time.time()
    try:
        emb = TextEmbedding(REQUIRED_MODEL, cache_dir=str(cache_dir))
        # Force materialization with a tiny encode (still same model)
        _ = list(emb.embed(["lab provenance ping"]))
    except TypeError:
        emb = TextEmbedding(REQUIRED_MODEL)
        _ = list(emb.embed(["lab provenance ping"]))
    except Exception as e:
        report["error"] = f"DOWNLOAD_OR_LOAD_FAILED:{e}"
        report["elapsed_seconds"] = time.time() - t0
        out.write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps({"ok": False, "error": report["error"]}), file=sys.stderr)
        return 1

    report["elapsed_seconds"] = time.time() - t0
    report["download_finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    report["files_after"] = inventory(cache_dir)
    report["total_size_bytes"] = sum(f["size_bytes"] for f in report["files_after"])
    report["ok"] = len(report["files_after"]) > 0 and report["total_size_bytes"] > 0
    if not report["ok"]:
        report["error"] = "EMPTY_CACHE_AFTER_DOWNLOAD"
        out.write_text(json.dumps(report, indent=2) + "\n")
        return 1

    out.write_text(json.dumps(report, indent=2) + "\n")
    print(
        json.dumps(
            {
                "ok": True,
                "files": len(report["files_after"]),
                "total_size_bytes": report["total_size_bytes"],
                "hf": sources.get("hf") if isinstance(sources, dict) else None,
                "url": sources.get("url") if isinstance(sources, dict) else None,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

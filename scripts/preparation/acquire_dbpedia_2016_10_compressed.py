#!/usr/bin/env python3
"""Controlled compressed-only acquisition of DBpedia 2016-10 endpoint-equivalent package.

Constraints (Prompt 24B / human authorization):
- Exactly the 114 manifest files
- Exact allowlist paths/hosts only
- Sequential downloads; max 2 retries per file
- Size + published MD5 (112/114) + local SHA-256 (114/114)
- No decompress / RDF / Docker / Virtuoso / SPARQL
- Abort on redirect to non-allowlisted host, size/MD5 mismatch, byte cap
"""

from __future__ import annotations

import argparse
import hashlib
import json
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import yaml

EXPECTED_FILE_COUNT = 114
EXPECTED_BYTES = 6925795437
EXPECTED_BYTE_CAP = 6995053391
EXPECTED_MANIFEST_CONTENT_HASH = (
    "2dcbc4df0b4af368d797a36525d607dae809317310c8c35d70066c5275c454c7"
)
EXPECTED_MANIFEST_FILE_SHA256 = (
    "3993dde79ece90062bc1303d9e0de3b0016ec6572ab1c1fc6491f9d1cff0bc6c"
)
EXPECTED_ALLOWLIST_FILE_SHA256 = (
    "3a773f39b41f26f3ce1e077053c58c37c8f7fd6486f78303688b2ec9197067eb"
)
EXPECTED_ALLOWLIST_CONTENT_SHA256 = (
    "c51993149add578a71f6904a7ca575a8e60f8872b7845f45f32cb22dface167c"
)
EXPECTED_VALIDATION_SHA256 = (
    "7690437868942ff1cae8eae6af60bf28b94ed82f9fecc5f8941e683b070bc15b"
)
PAYLOAD_HOST = "downloads.dbpedia.org"
NO_MD5 = {
    "instance_types_lhd_dbo_en.ttl.bz2",
    "instance_types_lhd_ext_en.ttl.bz2",
}
MAX_RETRIES = 2  # attempts after first failure => up to 3 tries total; auth: 2 retries
CHUNK = 1024 * 1024


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(CHUNK)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        while True:
            b = f.read(CHUNK)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text())


class RedirectHostError(RuntimeError):
    pass


class StrictHTTPSRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, allowed_hosts: set[str]):
        super().__init__()
        self.allowed_hosts = allowed_hosts

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[override]
        host = urlsplit(newurl).hostname
        if host not in self.allowed_hosts:
            raise RedirectHostError(f"redirect to non-allowlisted host: {host} -> {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def log_line(path: Path, msg: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(msg.rstrip() + "\n")


def fail(result: dict, out_json: Path, network_log: Path, msg: str, status: str = "FAIL") -> int:
    result["final_status"] = status
    result["errors"].append(msg)
    result["ended_at_unix"] = time.time()
    out_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    log_line(network_log, f"ABORT_OR_FAIL status={status} msg={msg}")
    print(msg, file=sys.stderr)
    return 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, default=Path("."))
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--authorization-id", required=True)
    ap.add_argument("--out-json", type=Path, required=True)
    ap.add_argument("--network-log", type=Path, required=True)
    ap.add_argument("--dest", type=Path, required=True)
    args = ap.parse_args()

    root = args.repo_root.resolve()
    run_id = args.run_id
    auth_id = args.authorization_id
    dest: Path = args.dest
    dest.mkdir(parents=True, exist_ok=True)

    manifest_path = root / "configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_ENDPOINT_FILE_MANIFEST.yaml"
    allow_path = root / "configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_GRAPH_NETWORK_ALLOWLIST.yaml"
    validation_path = root / "logs/dbpedia-acquisition-consistency/20260722T134313Z/package-static-validation.json"

    result: dict[str, Any] = {
        "validation_version": "dbpedia-2016-10-acquisition-v1",
        "run_id": run_id,
        "authorization_id": auth_id,
        "prompt": "Prompt_24B",
        "started_at_unix": time.time(),
        "files": [],
        "errors": [],
        "warnings": [],
        "checks": [],
        "network_bytes_received": 0,
        "external_monetary_cost_usd": 0.0,
        "decompress_attempted": False,
        "rdf_parsed": False,
        "docker_pull": False,
        "virtuoso": False,
        "sparql": False,
        "final_status": "IN_PROGRESS",
    }

    # Preflight hashes
    mf_hash = sha256_file(manifest_path)
    al_hash = sha256_file(allow_path)
    val_hash = sha256_file(validation_path)
    for name, got, exp in [
        ("manifest_file_sha256", mf_hash, EXPECTED_MANIFEST_FILE_SHA256),
        ("allowlist_file_sha256", al_hash, EXPECTED_ALLOWLIST_FILE_SHA256),
        ("validation_report_sha256", val_hash, EXPECTED_VALIDATION_SHA256),
    ]:
        result["checks"].append({"check": name, "pass": got == exp, "detail": got})
        if got != exp:
            return fail(result, args.out_json, args.network_log, f"{name} mismatch: {got} != {exp}", "ABORT")

    allow = load_yaml(allow_path)
    payload_paths = set(allow.get("allowed_payload_exact_paths") or [])
    payload_hosts = set(allow.get("allowed_payload_hosts") or [])
    if payload_hosts != {PAYLOAD_HOST}:
        return fail(result, args.out_json, args.network_log, f"payload hosts mismatch: {payload_hosts}", "ABORT")
    if len(payload_paths) != EXPECTED_FILE_COUNT:
        return fail(result, args.out_json, args.network_log, f"payload path count {len(payload_paths)}", "ABORT")

    stored = allow.get("allowlist_content_sha256")
    if stored != EXPECTED_ALLOWLIST_CONTENT_SHA256:
        return fail(
            result,
            args.out_json,
            args.network_log,
            f"allowlist_content_sha256 mismatch: {stored}",
            "ABORT",
        )
    result["checks"].append(
        {"check": "allowlist_content_sha256", "pass": True, "detail": stored}
    )

    val = json.loads(validation_path.read_text())
    if val.get("final_status") != "STATIC_CONSISTENCY_PASS":
        return fail(result, args.out_json, args.network_log, "static validation not PASS", "ABORT")
    if val.get("manifest_content_hash") != EXPECTED_MANIFEST_CONTENT_HASH:
        return fail(result, args.out_json, args.network_log, "manifest content hash mismatch", "ABORT")

    manifest = load_yaml(manifest_path)
    files = manifest.get("files") or []
    if len(files) != EXPECTED_FILE_COUNT:
        return fail(result, args.out_json, args.network_log, f"manifest files {len(files)}", "ABORT")

    expected_urls = []
    for f in files:
        url = f["source_url"]
        parts = urlsplit(url)
        if parts.scheme != "https" or parts.hostname != PAYLOAD_HOST:
            return fail(result, args.out_json, args.network_log, f"bad url {url}", "ABORT")
        if parts.path not in payload_paths:
            return fail(result, args.out_json, args.network_log, f"path not in allowlist: {parts.path}", "ABORT")
        if parts.path.startswith("//") or "//" in parts.path:
            return fail(result, args.out_json, args.network_log, f"noncanonical path {parts.path}", "ABORT")
        expected_urls.append(url)

    if len(set(expected_urls)) != EXPECTED_FILE_COUNT:
        return fail(result, args.out_json, args.network_log, "duplicate urls", "ABORT")

    # Disk check: need compressed total + margin
    free = None
    try:
        import shutil
        free = shutil.disk_usage(dest).free
    except Exception as e:  # noqa: BLE001
        result["warnings"].append(f"disk_usage_failed:{e}")
    if free is not None and free < EXPECTED_BYTES + (512 * 1024 * 1024):
        return fail(result, args.out_json, args.network_log, f"insufficient disk free={free}", "ABORT")

    handler = StrictHTTPSRedirectHandler({PAYLOAD_HOST})
    # Default SSL context
    ctx = ssl.create_default_context()
    opener = urllib.request.build_opener(handler, urllib.request.HTTPSHandler(context=ctx))

    total_received = 0
    log_line(args.network_log, f"BEGIN run_id={run_id} auth={auth_id} files={EXPECTED_FILE_COUNT}")

    for idx, fmeta in enumerate(files, 1):
        file_id = fmeta["file_id"]
        url = fmeta["source_url"]
        parts = urlsplit(url)
        path = parts.path
        name = Path(path).name
        expected_size = int(fmeta["remote_size_bytes"])
        pub_md5 = fmeta.get("published_checksum")
        algo = fmeta.get("published_checksum_algorithm")
        rel_subdir = Path(fmeta["path"]).parent  # e.g. core-i18n/en
        out_dir = dest / rel_subdir
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / name
        tmp_path = out_path.with_suffix(out_path.suffix + ".partial")

        entry: dict[str, Any] = {
            "file_id": file_id,
            "source_url": url,
            "path": fmeta["path"],
            "expected_size": expected_size,
            "local_path": str(out_path.relative_to(root)) if out_path.is_relative_to(root) else str(out_path),
            "attempts": 0,
            "status": "PENDING",
        }

        # Skip re-download if already valid
        if out_path.exists() and out_path.stat().st_size == expected_size:
            local_sha = sha256_file(out_path)
            ok_md5 = True
            local_md5 = None
            if name not in NO_MD5 and pub_md5 and algo == "md5":
                local_md5 = md5_file(out_path)
                ok_md5 = local_md5 == pub_md5
            if ok_md5:
                entry.update(
                    {
                        "attempts": 0,
                        "status": "REUSED_VALID",
                        "actual_size": expected_size,
                        "local_sha256": local_sha,
                        "local_md5": local_md5,
                        "md5_ok": ok_md5 if name not in NO_MD5 else None,
                        "size_ok": True,
                    }
                )
                total_received += expected_size
                result["files"].append(entry)
                log_line(args.network_log, f"REUSE {idx}/{EXPECTED_FILE_COUNT} {file_id} size={expected_size}")
                args.out_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
                continue

        success = False
        last_err = ""
        for attempt in range(1, MAX_RETRIES + 2):  # 1 initial + 2 retries
            entry["attempts"] = attempt
            try:
                if tmp_path.exists():
                    tmp_path.unlink()
                req = urllib.request.Request(
                    url,
                    method="GET",
                    headers={"User-Agent": "text2sparql-reproducibility-lab/24B-zero-cost"},
                )
                t0 = time.time()
                with opener.open(req, timeout=600) as resp:
                    final_url = resp.geturl()
                    final_host = urlsplit(final_url).hostname
                    if final_host != PAYLOAD_HOST:
                        raise RedirectHostError(f"final host {final_host}")
                    final_path = urlsplit(final_url).path
                    if final_path != path:
                        # allow only exact path (no silent alias)
                        raise RuntimeError(f"final path mismatch {final_path} != {path}")
                    h_sha = hashlib.sha256()
                    h_md5 = hashlib.md5()
                    got = 0
                    with tmp_path.open("wb") as out:
                        while True:
                            chunk = resp.read(CHUNK)
                            if not chunk:
                                break
                            out.write(chunk)
                            h_sha.update(chunk)
                            h_md5.update(chunk)
                            got += len(chunk)
                            if total_received + got > EXPECTED_BYTE_CAP:
                                raise RuntimeError("byte cap exceeded during download")
                elapsed = time.time() - t0
                if got != expected_size:
                    raise RuntimeError(f"size mismatch got={got} expected={expected_size}")
                local_sha = h_sha.hexdigest()
                local_md5 = h_md5.hexdigest()
                md5_ok = True
                if name not in NO_MD5:
                    if not pub_md5 or algo != "md5":
                        raise RuntimeError("missing published md5 for non-LHD file")
                    if local_md5 != pub_md5:
                        raise RuntimeError(f"md5 mismatch got={local_md5} expected={pub_md5}")
                else:
                    md5_ok = None  # type: ignore[assignment]
                tmp_path.replace(out_path)
                total_received += got
                entry.update(
                    {
                        "status": "DOWNLOADED_VALID",
                        "actual_size": got,
                        "local_sha256": local_sha,
                        "local_md5": local_md5 if name not in NO_MD5 else local_md5,
                        "md5_ok": True if name not in NO_MD5 else None,
                        "size_ok": True,
                        "elapsed_sec": round(elapsed, 3),
                        "published_md5": pub_md5,
                    }
                )
                success = True
                log_line(
                    args.network_log,
                    f"OK {idx}/{EXPECTED_FILE_COUNT} attempt={attempt} {file_id} bytes={got} sha256={local_sha[:12]} elapsed={elapsed:.1f}s",
                )
                break
            except RedirectHostError as e:
                last_err = str(e)
                log_line(args.network_log, f"REDIRECT_FAIL {file_id} {e}")
                if tmp_path.exists():
                    tmp_path.unlink(missing_ok=True)
                entry["status"] = "FAIL"
                entry["error"] = last_err
                result["files"].append(entry)
                return fail(result, args.out_json, args.network_log, f"redirect/host fail {file_id}: {e}", "FAIL")
            except Exception as e:  # noqa: BLE001
                last_err = str(e)
                log_line(args.network_log, f"RETRYABLE {idx}/{EXPECTED_FILE_COUNT} attempt={attempt} {file_id} err={e}")
                if tmp_path.exists():
                    tmp_path.unlink(missing_ok=True)
                if attempt >= MAX_RETRIES + 1:
                    break
                time.sleep(min(2 ** attempt, 30))

        if not success:
            entry["status"] = "FAIL"
            entry["error"] = last_err
            result["files"].append(entry)
            return fail(result, args.out_json, args.network_log, f"download failed {file_id}: {last_err}", "FAIL")

        result["files"].append(entry)
        result["network_bytes_received"] = total_received
        # checkpoint progress
        args.out_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    # Final aggregates
    if len(result["files"]) != EXPECTED_FILE_COUNT:
        return fail(result, args.out_json, args.network_log, f"file result count {len(result['files'])}", "FAIL")
    if total_received != EXPECTED_BYTES:
        return fail(
            result,
            args.out_json,
            args.network_log,
            f"total bytes {total_received} != {EXPECTED_BYTES}",
            "FAIL",
        )
    if total_received > EXPECTED_BYTE_CAP:
        return fail(result, args.out_json, args.network_log, "cap exceeded", "FAIL")

    # Ensure no extra files beyond manifest under dest leaf dirs? soft check: only count manifest paths
    missing = []
    for fmeta in files:
        p = dest / fmeta["path"]
        if not p.exists():
            missing.append(fmeta["path"])
    if missing:
        return fail(result, args.out_json, args.network_log, f"missing files: {missing[:5]}", "FAIL")

    result["network_bytes_received"] = total_received
    result["expected_bytes"] = EXPECTED_BYTES
    result["byte_cap"] = EXPECTED_BYTE_CAP
    result["file_count"] = EXPECTED_FILE_COUNT
    result["md5_verified_count"] = sum(1 for e in result["files"] if e.get("md5_ok") is True)
    result["sha256_count"] = sum(1 for e in result["files"] if e.get("local_sha256"))
    result["no_md5_files"] = sorted(NO_MD5)
    result["destination"] = str(dest)
    result["ended_at_unix"] = time.time()
    result["final_status"] = "ACQUISITION_PASS"
    result["checks"].append({"check": "total_bytes", "pass": True, "detail": str(total_received)})
    result["checks"].append({"check": "file_count", "pass": True, "detail": "114"})
    result["checks"].append({"check": "md5_112", "pass": result["md5_verified_count"] == 112, "detail": str(result["md5_verified_count"])})
    result["checks"].append({"check": "sha256_114", "pass": result["sha256_count"] == 114, "detail": str(result["sha256_count"])})
    args.out_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    log_line(args.network_log, f"PASS total_bytes={total_received} files=114 cost_usd=0.00")
    print("ACQUISITION_PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

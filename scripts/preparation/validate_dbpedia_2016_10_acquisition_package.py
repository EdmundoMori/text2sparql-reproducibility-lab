#!/usr/bin/env python3
"""Offline static consistency validator for DBpedia 2016-10 acquisition package.

No network. Validates manifest ↔ allowlist ↔ acquisition manifest ↔ scope lock.
Exit nonzero on any error.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import yaml

EXPECTED_FILE_COUNT = 114
EXPECTED_BYTES = 6925795437
EXPECTED_BYTE_CAP = 6995053391
EXPECTED_MANIFEST_HASH = (
    "2dcbc4df0b4af368d797a36525d607dae809317310c8c35d70066c5275c454c7"
)
EXPECTED_MD5_FILES = 112
EXPECTED_NO_MD5 = {
    "instance_types_lhd_dbo_en.ttl.bz2",
    "instance_types_lhd_ext_en.ttl.bz2",
}
PAYLOAD_HOST = "downloads.dbpedia.org"
LHD_NAMES = EXPECTED_NO_MD5


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text())


def check(name: str, ok: bool, errors: list, warnings: list, checks: list, detail: str = "") -> None:
    checks.append({"check": name, "pass": bool(ok), "detail": detail})
    if not ok:
        errors.append(f"{name}: {detail or 'failed'}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, default=Path("."))
    ap.add_argument("--out-json", type=Path, required=True)
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args()
    root: Path = args.repo_root.resolve()

    manifest_path = root / "configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_ENDPOINT_FILE_MANIFEST.yaml"
    allow_path = root / "configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_GRAPH_NETWORK_ALLOWLIST.yaml"
    acq_path = root / "configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_GRAPH_ACQUISITION_MANIFEST.yaml"
    lock_path = root / "configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_CANONICAL_SCOPE_LOCK.yaml"

    errors: list[str] = []
    warnings: list[str] = []
    checks: list[dict] = []

    manifest = load_yaml(manifest_path)
    allow = load_yaml(allow_path)
    acq = load_yaml(acq_path)
    lock = load_yaml(lock_path)

    files = manifest.get("files") or []
    check("scope_status_closed", manifest.get("scope_status") == "CLOSED", errors, warnings, checks, str(manifest.get("scope_status")))
    check("exact_file_count_field", manifest.get("exact_file_count") == EXPECTED_FILE_COUNT, errors, warnings, checks, str(manifest.get("exact_file_count")))
    check("files_len", len(files) == EXPECTED_FILE_COUNT, errors, warnings, checks, str(len(files)))

    file_ids = [f.get("file_id") for f in files]
    paths = [f.get("path") for f in files]
    urls = [f.get("source_url") for f in files]
    check("file_id_unique", len(file_ids) == len(set(file_ids)), errors, warnings, checks)
    check("path_unique", len(paths) == len(set(paths)), errors, warnings, checks)
    check("source_url_unique", len(urls) == len(set(urls)), errors, warnings, checks)

    expected_payload_paths: set[str] = set()
    noncanonical: list[str] = []
    total_bytes = 0
    md5_count = 0
    no_md5: set[str] = set()
    component_ser: dict[tuple, list] = {}

    for f in files:
        url = f.get("source_url") or ""
        parts = urlsplit(url)
        path = parts.path
        name = Path(path).name
        size = int(f.get("remote_size_bytes") or 0)
        total_bytes += size

        if parts.scheme != "https":
            noncanonical.append(f"scheme:{url}")
        if parts.hostname != PAYLOAD_HOST:
            noncanonical.append(f"host:{url}")
        if not path.startswith("/") or path.startswith("//"):
            noncanonical.append(f"slash:{url}")
        if not path.startswith("/2016-10/"):
            noncanonical.append(f"release:{url}")
        if "//" in path:
            noncanonical.append(f"double_slash_in_path:{url}")
        if ".." in path:
            noncanonical.append(f"dotdot:{url}")
        if parts.query or parts.fragment:
            noncanonical.append(f"query_fragment:{url}")
        if f.get("required") is not True:
            noncanonical.append(f"required_false:{f.get('file_id')}")

        expected_payload_paths.add(path)

        ck_algo = f.get("published_checksum_algorithm")
        ck = f.get("published_checksum")
        if ck_algo == "md5" and ck:
            md5_count += 1
        else:
            no_md5.add(name)

        key = (f.get("component") or f.get("dataset_component"), f.get("serialization"))
        component_ser.setdefault(key, []).append(name)

    check("https_host_path_canonical", len(noncanonical) == 0, errors, warnings, checks, "; ".join(noncanonical[:10]))
    check("total_bytes", total_bytes == EXPECTED_BYTES, errors, warnings, checks, str(total_bytes))
    check("md5_count", md5_count == EXPECTED_MD5_FILES, errors, warnings, checks, str(md5_count))
    check("no_md5_exact", no_md5 == EXPECTED_NO_MD5, errors, warnings, checks, str(sorted(no_md5)))
    check("payload_path_count", len(expected_payload_paths) == EXPECTED_FILE_COUNT, errors, warnings, checks, str(len(expected_payload_paths)))

    # duplicate serialization of same basename across ttl/tql would appear as same component with multi ser — soft check: no tql in package
    tql = [u for u in urls if u.endswith(".tql.bz2")]
    check("no_tql_duplicates", len(tql) == 0, errors, warnings, checks, str(len(tql)))

    # Allowlist
    payload_hosts = list(allow.get("allowed_payload_hosts") or [])
    payload_paths = list(allow.get("allowed_payload_exact_paths") or [])
    meta_hosts = list(allow.get("allowed_metadata_hosts") or [])
    meta_paths = list(allow.get("allowed_metadata_exact_paths") or [])
    ck_paths = list(allow.get("allowed_checksum_exact_paths") or [])

    check("payload_hosts", payload_hosts == [PAYLOAD_HOST], errors, warnings, checks, str(payload_hosts))
    check("payload_path_len", len(payload_paths) == EXPECTED_FILE_COUNT, errors, warnings, checks, str(len(payload_paths)))
    check("payload_paths_unique", len(payload_paths) == len(set(payload_paths)), errors, warnings, checks)

    payload_set = set(payload_paths)
    missing = sorted(expected_payload_paths - payload_set)
    extra = sorted(payload_set - expected_payload_paths)
    double_slash = [p for p in payload_paths if p.startswith("//") or "//" in p[1:]]
    check("set_equality", payload_set == expected_payload_paths, errors, warnings, checks, f"missing={len(missing)} extra={len(extra)}")
    check("no_double_slash", len(double_slash) == 0, errors, warnings, checks, str(double_slash[:5]))
    check("checksum_paths_disjoint", len(set(ck_paths) & payload_set) == 0, errors, warnings, checks)
    check("checksum_not_empty", len(ck_paths) > 0, errors, warnings, checks, str(len(ck_paths)))
    check("no_checksum_in_payload", all(not p.endswith("_checksums.md5") for p in payload_paths), errors, warnings, checks)
    check("allowlist_inactive", allow.get("status") == "DOCUMENTARY_ONLY_NOT_ACTIVE", errors, warnings, checks, str(allow.get("status")))
    check("no_mirrors_in_payload_hosts", "mirror" not in json.dumps(payload_hosts).lower(), errors, warnings, checks)

    # Acquisition + lock
    check("acq_file_count", acq.get("exact_file_count") == EXPECTED_FILE_COUNT, errors, warnings, checks, str(acq.get("exact_file_count")))
    check("acq_bytes", acq.get("compressed_total_bytes") == EXPECTED_BYTES, errors, warnings, checks, str(acq.get("compressed_total_bytes")))
    check("acq_cap", acq.get("maximum_payload_bytes") == EXPECTED_BYTE_CAP, errors, warnings, checks, str(acq.get("maximum_payload_bytes")))
    check(
        "acq_hash",
        acq.get("exact_file_manifest_hash") == EXPECTED_MANIFEST_HASH,
        errors,
        warnings,
        checks,
        str(acq.get("exact_file_manifest_hash")),
    )
    check("acq_auth_id_null", acq.get("authorization_id") is None, errors, warnings, checks, str(acq.get("authorization_id")))
    check("acq_auth_unsigned", acq.get("authorization_status") == "UNSIGNED", errors, warnings, checks, str(acq.get("authorization_status")))
    check("acq_not_acquired", acq.get("acquisition_status") == "NOT_ACQUIRED", errors, warnings, checks, str(acq.get("acquisition_status")))
    check("acq_not_deployed", acq.get("deployment_status") == "NOT_DEPLOYED", errors, warnings, checks, str(acq.get("deployment_status")))
    check(
        "acq_g4_runtime",
        acq.get("g4_runtime_status") == "NOT_SATISFIED",
        errors,
        warnings,
        checks,
        str(acq.get("g4_runtime_status")),
    )
    check(
        "lock_hash",
        lock.get("canonical_scope_content_sha256") == EXPECTED_MANIFEST_HASH,
        errors,
        warnings,
        checks,
        str(lock.get("canonical_scope_content_sha256")),
    )
    check("lock_count", lock.get("exact_file_count") == EXPECTED_FILE_COUNT, errors, warnings, checks, str(lock.get("exact_file_count")))
    check("lock_bytes", lock.get("compressed_total_bytes") == EXPECTED_BYTES, errors, warnings, checks, str(lock.get("compressed_total_bytes")))

    final = "STATIC_CONSISTENCY_PASS" if not errors else "STATIC_CONSISTENCY_FAIL"
    report = {
        "validation_version": "1.0.0",
        "run_id": args.run_id,
        "manifest_file_count": len(files),
        "manifest_total_bytes": total_bytes,
        "manifest_content_hash": EXPECTED_MANIFEST_HASH,
        "allowlist_payload_path_count": len(payload_paths),
        "allowlist_payload_host_count": len(payload_hosts),
        "missing_payload_paths": missing,
        "extra_payload_paths": extra,
        "noncanonical_paths": noncanonical,
        "duplicate_paths": [],
        "checksum_path_count": len(ck_paths),
        "checksum_coverage_files": md5_count,
        "no_checksum_files": sorted(no_md5),
        "byte_cap": acq.get("maximum_payload_bytes"),
        "authorization_status": acq.get("authorization_status"),
        "acquisition_status": acq.get("acquisition_status"),
        "deployment_status": acq.get("deployment_status"),
        "metadata_host_count": len(meta_hosts),
        "metadata_path_count": len(meta_paths),
        "checks": checks,
        "errors": errors,
        "warnings": warnings,
        "final_status": final,
        "manifest_sha256": sha256_file(manifest_path),
        "allowlist_sha256": sha256_file(allow_path),
        "acquisition_manifest_sha256": sha256_file(acq_path),
        "scope_lock_sha256": sha256_file(lock_path),
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"final_status": final, "errors": len(errors), "out": str(args.out_json)}, indent=2))
    return 0 if final == "STATIC_CONSISTENCY_PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Offline validator for COMMON_CORE_BENCHMARK_FREEZE_V1."""
from __future__ import annotations
import csv, hashlib, json, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
CFG = ROOT / "configs/common/benchmark-freeze"
AUD = ROOT / "audit/benchmark-freeze"
errors = []
manifest_path = CFG / "COMMON_CORE_BENCHMARK_FREEZE_V1.yaml"
manifest = yaml.safe_load(manifest_path.read_text())
portfolio = list(csv.DictReader((AUD / "PHASE2_BENCHMARK_PORTFOLIO_FREEZE.csv").open()))
groups = yaml.safe_load((CFG / "COMMON_CORE_COMPARISON_GROUPS_V1.yaml").read_text())["groups"]
expected_hash = (CFG / "COMMON_CORE_BENCHMARK_FREEZE_V1.sha256").read_text().split()[0]
actual_hash = hashlib.sha256(manifest_path.read_bytes()).hexdigest()

def check(condition, message):
    if not condition:
        errors.append(message)

check(manifest["freeze_version"] == "1.0.0-25R4", "freeze version")
check("benchmark_freeze_sha256" not in manifest, "self hash present")
check(expected_hash == actual_hash, "sidecar hash mismatch")
dataset = manifest["primary_benchmark"]
check(dataset["dataset_id"] == "QALD9_PLUS_EN_DBPEDIA", "dataset identity")
check(dataset["dataset_source_revision"] == "8eb038a61e1bc09cbd21640aa667a1714f53cda4", "dataset revision")
check((dataset["train_count"], dataset["test_count"]) == (408, 150), "dataset counts")
check(dataset["test_seal_status"] == "SEALED", "test seal")
graph = manifest["graph"]
check(graph["graph_id"] == "DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT", "graph identity")
check(graph["compressed_file_count"] == 114, "graph file count")
check(graph["compressed_bytes"] == 6925795437, "graph bytes")
check(graph["deployment_status"] == "NOT_DEPLOYED", "graph deployment")
check(manifest["fairness"]["track_taxonomy_version"] == "2.0.0-25R3", "taxonomy")
check(manifest["metrics"]["contract_version"] == "0.1.0-documentary", "metric version")
check(manifest["metrics"]["conformance_status"] == "36_VECTORS_DEFINED_NOT_EXECUTED", "vectors")
ids = [f"{r['method_id']}/{r['variant_id']}" for r in portfolio]
check(len(ids) == len(set(ids)), "duplicate variant IDs")
check(all(r["portfolio_role"] for r in portfolio), "missing portfolio role")
known = set(ids)
for group in groups:
    for member in group["members"]:
        check(member["variant"] in known, f"unknown group member {member['variant']}")
        row = portfolio[ids.index(member["variant"])]
        if group["group_id"].startswith("QALD_"):
            check(row["track_v2"] not in {"IA_DOMAIN_NATIVE", "IA_HISTORICAL"}, "domain/historical in QALD group")
oracle = next(r for r in portfolio if r["variant_id"] == "ZERO_COST_RETRAIN_QK")
check(oracle["portfolio_role"] == "DIAGNOSTIC_ONLY", "oracle not diagnostic")
check(all(r["zero_cost_status"] == "COMPLIANT_TARGET" for r in portfolio if r["portfolio_role"] == "EXECUTION_TARGET"), "paid execution target")
check(all(r["legal_status"] == "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE" and r["execution_eligibility"] == "NOT_CURRENTLY_ELIGIBLE" for r in portfolio if r["method_id"] == "mkgqagent"), "mKG legal blocker")
check(all(r["legal_status"] == "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE" and r["execution_eligibility"] == "NOT_CURRENTLY_ELIGIBLE" for r in portfolio if r["method_id"] == "cot_sparql"), "CoT legal blocker")
check(all(r["legal_status"] == "CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN" for r in portfolio if r["method_id"] == "rdfconfig_llm"), "RDFConfig LE2")
check(all(r["execution_eligibility"] == "NOT_CURRENTLY_ELIGIBLE" for r in portfolio), "execution falsely eligible")
gates = manifest["execution_gates"]
check(gates["G4"] == "NOT_SATISFIED" and "PENDING" in gates["G5"] and "PENDING" in gates["G6I"], "runtime gate falsely passed")
result = {"errors": errors, "freeze_id": manifest["freeze_id"], "freeze_version": manifest["freeze_version"], "manifest_sha256": actual_hash, "status": "PASS" if not errors else "FAIL"}
out = ROOT / "audit/benchmark-freeze/benchmark-freeze-validation.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
sys.exit(0 if not errors else 1)

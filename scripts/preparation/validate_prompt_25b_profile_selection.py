#!/usr/bin/env python3
"""Offline validator for Prompt 25B documentary profile selection."""
from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
RUN = "20261012T150501Z"
FREEZE_SHA = "f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c"
GATE = "LOCAL_WSL_HOST_ADJUSTED_PROFILE_SELECTED_D1_PACKAGE_READY_FOR_HUMAN_AUTHORIZATION"
NEXT = "HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION"
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_yaml(path: str) -> dict:
    return yaml.safe_load(read(path))


freeze_raw = read("configs/common/benchmark-freeze/COMMON_CORE_BENCHMARK_FREEZE_V1.yaml")
check(hashlib.sha256(freeze_raw.encode()).hexdigest() == FREEZE_SHA, "benchmark freeze hash changed")
freeze = yaml.safe_load(freeze_raw)
check(freeze["primary_benchmark"]["test_seal_status"] == "SEALED", "QALD test seal not preserved")
check(freeze["graph"]["deployment_status"] == "NOT_DEPLOYED", "freeze graph deployment changed")

plan = read("PLAN_SYNC.md")
for value in (
    "52b74bceb15bbf8f149e6a94d2be9e2aee5803a5",
    "7e0bdb20be7e05601dc22072964ff0ea22b7a3c7",
    "f271997477c8505c1d223b91d7630d09135d3cd3",
):
    check(value in plan, f"25R4 reconciliation missing {value}")
check("publication metadata commit: `SELF` (second and final Prompt 25R4 commit)" not in plan, "25R4 SELF not reconciled")

form = read("docs/protocols/common/benchmark-freeze/20261012T143717Z/HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION_V2.md")
check(form.count("- [x] `LOCAL_WSL_HOST_ADJUSTED`") == 1, "selected profile checkbox invalid")
check(form.count("- [x]") == 1, "more than one profile selected")
for value in ("SIGNED_SELECTION_ONLY", "APPROVED_PROFILE_SELECTION", "EDMUNDO MORI ORRILLO", "15.19 GiB"):
    check(value in form, f"human form missing {value}")

matrix_path = ROOT / "audit/deployment-profile-selection/LOCAL_WSL_HOST_HEADROOM_ANALYSIS.csv"
with matrix_path.open(newline="", encoding="utf-8") as stream:
    allocations = list(csv.DictReader(stream))
check([row["proposed_wsl_gib"] for row in allocations] == ["8", "10", "11", "12", "13", "14"], "allocation candidates")
selected = next((row for row in allocations if row["proposed_wsl_gib"] == "12"), {})
check(selected.get("remaining_host_gib") == "3.19", "12 GiB host headroom")
check(selected.get("virtuoso_capacity_class") == "MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK", "12 GiB classification")
fourteen = next((row for row in allocations if row["proposed_wsl_gib"] == "14"), {})
check(fourteen.get("recommendation") == "REJECT_HOST_STARVATION_RISK", "14 GiB incorrectly recommended")

config = read("configs/common/graph/dbpedia2016-10/profile-selection/PROPOSED_WSL_CONFIG.ini")
check("DOCUMENTARY TEMPLATE ONLY" in config and "memory=12GB" in config and "swap=8GB" in config, "proposed WSL template")

manifest = load_yaml("configs/common/graph/dbpedia2016-10/deployment/DBPEDIA_2016_10_DEPLOYMENT_MANIFEST.yaml")
expected_manifest = {
    "selected_resource_profile": "LOCAL_WSL_HOST_ADJUSTED",
    "resource_selection_status": "HUMAN_SELECTED",
    "human_verified_host_ram_gib": 15.19,
    "selection_authorization_scope": "PROFILE_ONLY",
    "resource_configuration_status": "NOT_CONFIGURED",
    "d1_package_status": "READY_FOR_HUMAN_AUTHORIZATION",
    "d1_authorization_status": "READY_UNSIGNED",
    "deployment_status": "NOT_DEPLOYED",
    "g4_runtime_status": "NOT_SATISFIED",
}
for key, value in expected_manifest.items():
    check(manifest.get(key) == value, f"deployment manifest {key}")

runtime = load_yaml("configs/common/graph/dbpedia2016-10/deployment/DBPEDIA_2016_10_VIRTUOSO_RUNTIME_PIN.yaml")
check(runtime["status"] == "PINNED_METADATA_ONLY", "runtime pin status")
check("VERIFY_BEFORE_LOAD" in runtime["license"] and "NOASSERTION" in runtime["license"], "runtime license blocker")

registry = load_yaml("METHOD_REGISTRY.yaml")
check(registry["schema_version"] == "0.31", "registry schema")
check(registry["phase"] == "phase2_local_wsl_host_adjusted_selected_d1_authorization_pending", "registry phase")
check(registry["selected_deployment_profile"] == "LOCAL_WSL_HOST_ADJUSTED", "registry profile")
check(registry["resource_configuration_status"] == "NOT_CONFIGURED", "registry resource status")
check(registry["benchmark_execution_status"] == "NOT_CURRENTLY_ELIGIBLE", "benchmark eligibility changed")

gate_path = f"docs/protocols/common/graph/dbpedia2016-10/profile-selection/{RUN}/LOCAL_WSL_HOST_ADJUSTED_PROFILE_SELECTION_GATE.md"
gate = read(gate_path)
check(gate.count(f"**`{GATE}`**") == 1, "primary gate count")
check(gate.count(f"Exactly one next action: `{NEXT}`") == 1, "gate next action count")

next_doc = read("audit/NEXT_AFTER_LOCAL_WSL_HOST_ADJUSTED_SELECTION_DECISION.md")
check(next_doc.count(f"Exactly one next action: `{NEXT}`") == 1, "next-decision action count")
check("RESERVED_NOT_AUTHORIZED" in next_doc, "D1 execution prompt status")

report = read("audit/PHASE2_DBPEDIA_LOCAL_WSL_HOST_ADJUSTED_SELECTION_AND_D1_PREPARATION_REPORT.md")
check(sum(line.startswith("## ") for line in report.splitlines()) == 30, "report section count")

roadmap_path = ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv"
with roadmap_path.open(newline="", encoding="utf-8") as stream:
    roadmap = list(csv.DictReader(stream))
check(any(row["vehicle"] == "Prompt_25B" and row["status"] == "COMPLETE" for row in roadmap), "roadmap 25B")
check(any(row["action"] == NEXT and row["status"] == "NEXT_HUMAN_GATE_REQUIRED" for row in roadmap), "roadmap next")

index_rows = []
for line in read("docs/plan-sync/ARTIFACT_INDEX.md").splitlines():
    if line.startswith("| ") and not line.startswith("| ID") and not line.startswith("|---"):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 3:
            index_rows.append((cells[0], cells[2].strip("`")))
check(len({row[0] for row in index_rows}) == len(index_rows), "duplicate artifact ID")
check(len({row[1] for row in index_rows}) == len(index_rows), "duplicate artifact path")

changed = subprocess.check_output(["git", "diff", "--name-only"], cwd=ROOT, text=True).splitlines()
for forbidden in (".wslconfig", "workdir/graphs/", "upstream/", "adapters/"):
    check(not any(forbidden in path for path in changed), f"forbidden changed path: {forbidden}")

log_dir = ROOT / f"logs/deployment-profile-selection/{RUN}"
status = "PASS" if not errors else "FAIL"
(log_dir / "schema-validation.log").write_text(
    f"{status}\nfreeze_yaml_parse=true\ndeployment_manifest_yaml_parse=true\nmethod_registry_yaml_parse=true\n",
    encoding="utf-8",
)
(log_dir / "validation.log").write_text(
    "\n".join(
        [
            status,
            f"errors={json.dumps(errors, sort_keys=True)}",
            "NO_CONFIG_CHANGES=true",
            "NO_WSL_RESTART=true",
            "NO_SWAP_CHANGE=true",
            "NO_DECOMPRESSION=true",
            "NO_DOCKER_PULL=true",
            "NO_CONTAINER_CREATION=true",
            "NO_VIRTUOSO=true",
            "NO_SPARQL=true",
            "NO_MODEL_EXECUTION=true",
            "NO_TRAINING=true",
            "NO_ADAPTER_IMPLEMENTATION=true",
            "NO_BENCHMARK=true",
            "DBPEDIA_NOT_DEPLOYED=true",
            "G4_NOT_SATISFIED=true",
            "G5_PENDING=true",
            "G6I_PENDING=true",
            "TEST_SEALED=true",
            "EXTERNAL_MONETARY_COST_USD=0.00",
        ]
    )
    + "\n",
    encoding="utf-8",
)
print(json.dumps({"run_id": RUN, "status": status, "errors": errors}, sort_keys=True))
sys.exit(0 if not errors else 1)

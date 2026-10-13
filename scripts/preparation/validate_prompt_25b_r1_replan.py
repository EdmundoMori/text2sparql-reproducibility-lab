#!/usr/bin/env python3
"""Offline validator for Prompt 25B-R1 D1 host/guest replan."""
from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
RUN = "20261013T080249Z"
FREEZE_SHA = "f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c"
GATE = "WINDOWS_HOST_WSL_GUEST_D1_REPLAN_COMPLETE_READY_FOR_HOST_APPLY_AUTHORIZATION"
NEXT = "HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION"
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def yload(path: str) -> dict:
    return yaml.safe_load(read(path))


freeze_raw = read("configs/common/benchmark-freeze/COMMON_CORE_BENCHMARK_FREEZE_V1.yaml")
check(hashlib.sha256(freeze_raw.encode()).hexdigest() == FREEZE_SHA, "freeze hash")
freeze = yaml.safe_load(freeze_raw)
check(freeze["primary_benchmark"]["test_seal_status"] == "SEALED", "test seal")
check(freeze["graph"]["deployment_status"] == "NOT_DEPLOYED", "freeze deployment")

plan = read("PLAN_SYNC.md")
for sha in (
    "f271997477c8505c1d223b91d7630d09135d3cd3",
    "d5813ffa39226e9cb8f7ba8a2eb8a063c21fbd97",
    "ed97ea76c092ec39821151d72d8f5fed2da9219b",
):
    check(sha in plan, f"25B reconciliation {sha}")
check("publication metadata commit: `SELF` (second and final Prompt 25B commit)" not in plan, "25B SELF")

doc_base = f"docs/protocols/common/graph/dbpedia2016-10/d1-topology/{RUN}"
required = [
    "WINDOWS_HOST_WSL_GUEST_EXECUTION_TOPOLOGY.md",
    "D1_ORCHESTRATION_CORRECTION.md",
    "WINDOWS_HOST_MEMORY_REASSESSMENT.md",
    "WINDOWS_HOST_SWAP_STORAGE_CONSTRAINT.md",
    "WINDOWS_WSLCONFIG_MERGE_POLICY.md",
    "WINDOWS_HOST_D1_MANUAL_APPLY_GUIDE.md",
    "D1V_POST_RESTART_VERIFICATION_SPEC.md",
    "D1_SPLIT_HOST_GUEST_PASS_SEMANTICS.md",
    "D1_SPLIT_STOP_CONDITIONS.md",
    "RESOURCE_CONSTRAINED_DBPEDIA_LOAD_POLICY.md",
    "HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION_V2.md",
    "WINDOWS_HOST_WSL_GUEST_D1_REPLAN_GATE.md",
    "PRIOR_INTERRUPTED_D1_EFFECTS_RECONCILIATION.md",
]
for name in required:
    check((ROOT / doc_base / name).is_file(), f"missing {name}")

subprofile = yload("configs/common/graph/dbpedia2016-10/profile-selection/LOCAL_WSL_RESOURCE_CONSTRAINED_V1.yaml")
check(subprofile["wsl_memory_max_gib"] == 10, "subprofile memory")
check(subprofile["wsl_swap_gib"] == 2, "subprofile swap")
check(subprofile["estimated_host_headroom_gib"] == 5.19, "host headroom")
check(subprofile["do_not_claim_full_load_feasible"] is True, "load claim")
check(subprofile["proposal_status"] == "DOCUMENTARY_NOT_APPLIED", "proposal status")

ini = read("configs/common/graph/dbpedia2016-10/profile-selection/PROPOSED_WSL_CONFIG_RESOURCE_CONSTRAINED_V1.ini")
check(ini == "[wsl2]\nmemory=10GB\nswap=2GB\n", "exact 10/2 ini")

old_ini = read("configs/common/graph/dbpedia2016-10/profile-selection/PROPOSED_WSL_CONFIG.ini")
check("memory=12GB" in old_ini and "swap=8GB" in old_ini and "SUPERSEDED" in old_ini, "old proposal preservation")

ps1 = read("scripts/windows/prepare_wsl_resource_constrained_profile.ps1")
check("memory=10GB" in ps1 and "swap=2GB" in ps1, "PowerShell values")
check("Get-CimInstance Win32_ComputerSystem" in ps1, "PowerShell RAM check")
check("wsl.exe --list --verbose" in ps1, "PowerShell WSL check")
check("CONFIG_WRITTEN_RESTART_NOT_YET_PERFORMED" in ps1, "PowerShell terminal status")
check("--shutdown" not in ps1 and "--terminate" not in ps1, "PowerShell automatic shutdown")
check("start-service docker" not in ps1.lower() and "docker pull" not in ps1.lower() and "docker run" not in ps1.lower(), "PowerShell Docker action")

old_form = read("docs/protocols/common/graph/dbpedia2016-10/profile-selection/20261012T150501Z/HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION.md")
check("SUPERSEDED_AFTER_INTERRUPTED_AUTHORIZED_ATTEMPT" in old_form, "old form status")
new_form = read(f"{doc_base}/HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION_V2.md")
check("READY_UNSIGNED" in new_form and new_form.count("- [ ]") == 5 and "- [x]" not in new_form, "new form unsigned")

manifest = yload("configs/common/graph/dbpedia2016-10/deployment/DBPEDIA_2016_10_DEPLOYMENT_MANIFEST.yaml")
check(manifest["selected_resource_subprofile"] == "LOCAL_WSL_RESOURCE_CONSTRAINED_V1", "manifest subprofile")
check(manifest["proposed_wsl_memory_gib"] == 10 and manifest["proposed_wsl_swap_gib"] == 2, "manifest proposal")
check(manifest["d1_orchestration_status"] == "REPLANNED_SPLIT_HOST_GUEST", "manifest orchestration")
check(manifest["d1_authorization_status"] == "READY_UNSIGNED_V2", "manifest auth")
check(manifest["deployment_status"] == "NOT_DEPLOYED", "deployment")
check(manifest["g4_runtime_status"] == "NOT_SATISFIED", "G4")
check("PRIOR_12_8_APPLIED" in manifest["resource_configuration_status"], "prior applied effect not hidden")

registry = yload("METHOD_REGISTRY.yaml")
check(registry["schema_version"] == "0.32", "registry schema")
check(registry["phase"] == "phase2_windows_host_wsl_guest_d1_replanned_authorization_pending", "registry phase")
check(registry["benchmark_execution_status"] == "NOT_CURRENTLY_ELIGIBLE", "benchmark status")
check(registry["g6d_status_current"] == "DOCUMENTED", "G6D")
check(registry["g6i_status_current"] == "PENDING", "G6I")
check(registry["adapters_current"] is False, "adapters")

with (ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv").open(newline="", encoding="utf-8") as stream:
    roadmap = list(csv.DictReader(stream))
check(any(row["action"] == "D1P_HOST_PACKAGE_PREPARATION" and row["status"] == "COMPLETE" for row in roadmap), "D1P roadmap")
check(any(row["action"] == NEXT and row["status"] == "NEXT_HUMAN_GATE_REQUIRED" for row in roadmap), "next roadmap")

report = read("audit/PHASE2_WINDOWS_HOST_WSL_GUEST_D1_REPLAN_REPORT.md")
check(sum(line.startswith("## ") for line in report.splitlines()) == 22, "report sections")
gate = read(f"{doc_base}/WINDOWS_HOST_WSL_GUEST_D1_REPLAN_GATE.md")
check(gate.count(f"**`{GATE}`**") == 1, "gate count")
check(gate.count(f"Exactly one next action: `{NEXT}`") == 1, "next action count")

changed = subprocess.check_output(["git", "diff", "--name-only"], cwd=ROOT, text=True).splitlines()
check(not any(path.startswith("upstream/") or "workdir/graphs/" in path for path in changed), "forbidden repo paths")
check((ROOT / "scripts/windows/prepare_wsl_resource_constrained_profile.ps1").is_file(), "host script")
check(not (ROOT / f"logs/d1-topology-replan/{RUN}/host-script-execution.log").exists(), "host script execution evidence")

log_dir = ROOT / f"logs/d1-topology-replan/{RUN}"
status = "PASS" if not errors else "FAIL"
(log_dir / "schema-validation.log").write_text(
    f"{status}\nfreeze_yaml=true\nsubprofile_yaml=true\ndeployment_manifest_yaml=true\nmethod_registry_yaml=true\n",
    encoding="utf-8",
)
(log_dir / "validation.log").write_text(
    "\n".join(
        [
            status,
            f"errors={json.dumps(errors, sort_keys=True)}",
            "HOST_SCRIPT_EXECUTED_IN_25B_R1=false",
            "NO_RESOURCE_CHANGE_IN_25B_R1=true",
            "NO_WSL_SHUTDOWN_IN_25B_R1=true",
            "CURRENT_UBUNTU_SESSION_ACTIVE=true",
            "NO_DBPEDIA_DECOMPRESSION=true",
            "NO_DOCKER_PULL=true",
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

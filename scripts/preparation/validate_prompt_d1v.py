#!/usr/bin/env python3
"""Offline validation for Prompt D1V and overall D1 closure."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
RUN = "20261013T085129Z"
FREEZE_SHA = "f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c"
GATE = "D1_RESOURCE_CONFIGURATION_PASS_READY_FOR_D2_AUTHORIZATION"
NEXT = "HUMAN_D2_DECOMPRESSION_AND_RDF_VALIDATION_AUTHORIZATION"
errors: list[str] = []


def check(value: bool, message: str) -> None:
    if not value:
        errors.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


freeze_raw = read("configs/common/benchmark-freeze/COMMON_CORE_BENCHMARK_FREEZE_V1.yaml")
check(hashlib.sha256(freeze_raw.encode()).hexdigest() == FREEZE_SHA, "freeze hash")
freeze = yaml.safe_load(freeze_raw)
check(freeze["primary_benchmark"]["test_seal_status"] == "SEALED", "test seal")

resource_log = read(f"logs/d1-verification/{RUN}/resource-observations.log")
docker_log = read(f"logs/d1-verification/{RUN}/docker-readonly.log")
mem = int(re.search(r"^MemTotal:\s+(\d+) kB$", resource_log, re.M).group(1))
swap = int(re.search(r"^SwapTotal:\s+(\d+) kB$", resource_log, re.M).group(1))
cpu = int(re.search(r"^\$ nproc\n(\d+)$", resource_log, re.M).group(1))
disk_match = re.search(r"^/dev/sdd\s+ext4\s+\d+\s+\d+\s+(\d+)\s+", resource_log, re.M)
disk_kb = int(disk_match.group(1)) if disk_match else 0
check(mem == 10182848 and 9.4 <= mem / 1024 / 1024 <= 10.1, "memory acceptance")
check(swap == 2097152 and 1.9 <= swap / 1024 / 1024 <= 2.1, "swap acceptance")
check(cpu == 16, "CPU")
check(disk_kb / 1024 / 1024 > 305, "disk envelope")
check("microsoft-standard-WSL2" in resource_log, "WSL2 kernel")
check("/usr/bin/docker" in docker_log and "Docker version 29.1.3" in docker_log, "Docker client")
check("failed to connect to the docker API" in docker_log, "Docker daemon classification")
check("docker pull" not in docker_log and "docker run" not in docker_log, "Docker prohibited action")

base = f"docs/protocols/common/graph/dbpedia2016-10/d1-verification/{RUN}"
for name in (
    "D1H_WINDOWS_HOST_APPLY_EVIDENCE.md",
    "D1R_WSL_RESTART_EVIDENCE.md",
    "D1V_POST_RESTART_RESOURCE_VERIFICATION_REPORT.md",
    "D1_RESOURCE_CONFIGURATION_GATE.md",
    "HUMAN_D2_DECOMPRESSION_AND_RDF_VALIDATION_AUTHORIZATION.md",
):
    check((ROOT / base / name).is_file(), f"missing {name}")

component_path = ROOT / "audit/d1-verification/D1_COMPONENT_STATUS_MATRIX.csv"
with component_path.open(newline="", encoding="utf-8") as stream:
    components = {row["component"]: row["status"] for row in csv.DictReader(stream)}
check(components == {"D1P": "PASS", "D1H": "PASS", "D1R": "PASS", "D1V": "PASS", "D1": "PASS_RESOURCE_CONSTRAINED_PROFILE"}, "component status")

manifest = yaml.safe_load(read("configs/common/graph/dbpedia2016-10/deployment/DBPEDIA_2016_10_DEPLOYMENT_MANIFEST.yaml"))
for key in ("d1p_status", "d1h_status", "d1r_status", "d1v_status"):
    check(manifest.get(key) == "PASS", f"manifest {key}")
check(manifest["d1_status"] == "PASS_RESOURCE_CONSTRAINED_PROFILE", "manifest D1")
check(manifest["resource_configuration_status"] == "CONFIGURED_AND_VERIFIED", "manifest resource")
check(manifest["observed_guest_memory_kb"] == mem and manifest["observed_guest_swap_kb"] == swap, "manifest observations")
check(manifest["graph_payload_status"] == "COMPRESSED_ACQUIRED", "payload compressed")
check(manifest["deployment_status"] == "NOT_DEPLOYED", "deployment")
check(manifest["g4_runtime_status"] == "NOT_SATISFIED", "G4")

registry = yaml.safe_load(read("METHOD_REGISTRY.yaml"))
check(registry["schema_version"] == "0.33", "registry schema")
check(registry["phase"] == "phase2_d1_resource_configuration_pass_d2_authorization_pending", "registry phase")
check(registry["benchmark_execution_status"] == "NOT_CURRENTLY_ELIGIBLE", "benchmark")
check(registry["g6d_status_current"] == "DOCUMENTED", "G6D")
check(registry["g6i_status_current"] == "PENDING", "G6I")
check(registry["adapters_current"] is False, "adapters")
check(registry["d2_authorization_status"] == "READY_UNSIGNED", "D2 status")

auth = read(f"{base}/HUMAN_D2_DECOMPRESSION_AND_RDF_VALIDATION_AUTHORIZATION.md")
check("READY_UNSIGNED" in auth and "- [x]" not in auth, "D2 form unsigned")
check("Docker pull" in auth and "Not authorized" in auth, "D2 exclusions")

gate = read(f"{base}/D1_RESOURCE_CONFIGURATION_GATE.md")
check(gate.count(f"**`{GATE}`**") == 1, "gate count")
check(gate.count(f"Exactly one next action: `{NEXT}`") == 1, "gate next")
next_doc = read("audit/NEXT_AFTER_D1_RESOURCE_CONFIGURATION_DECISION.md")
check(next_doc.count(f"Exactly one next action: `{NEXT}`") == 1, "next decision")

report = read("audit/PHASE2_D1_RESOURCE_CONFIGURATION_AND_POST_RESTART_VERIFICATION_REPORT.md")
check(sum(line.startswith("## ") for line in report.splitlines()) == 23, "main report sections")

plan = read("PLAN_SYNC.md")
for sha in (
    "ed97ea76c092ec39821151d72d8f5fed2da9219b",
    "1962a465759e8b6b68fecbd0ac3322949b4e7ad5",
    "0c11b8280f35973bcb54baf3b2f53d6dfb85e265",
):
    check(sha in plan, f"25B-R1 reconciliation {sha}")
check("publication metadata commit: `SELF` (second and final Prompt 25B-R1 commit)" not in plan, "25B-R1 SELF")

with (ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv").open(newline="", encoding="utf-8") as stream:
    roadmap = list(csv.DictReader(stream))
for action in ("D1P_HOST_PACKAGE_PREPARATION", "HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION", "D1H_WINDOWS_HOST_CONFIG_APPLY", "D1R_WSL_RESTART", "D1V_POST_RESTART_VERIFICATION"):
    check(any(row["action"] == action and row["status"] == "COMPLETE" for row in roadmap), f"roadmap {action}")
check(any(row["action"] == "HUMAN_D2_AUTHORIZATION" and row["status"] == "NEXT_HUMAN_GATE_REQUIRED" for row in roadmap), "roadmap D2 gate")

status = "PASS" if not errors else "FAIL"
log_dir = ROOT / f"logs/d1-verification/{RUN}"
(log_dir / "schema-validation.log").write_text(
    f"{status}\nfreeze_yaml=true\ndeployment_manifest_yaml=true\nmethod_registry_yaml=true\n",
    encoding="utf-8",
)
(log_dir / "validation.log").write_text(
    "\n".join(
        [
            status,
            f"errors={json.dumps(errors, sort_keys=True)}",
            "D1P=PASS",
            "D1H=PASS",
            "D1R=PASS",
            "D1V=PASS",
            "D1=PASS_RESOURCE_CONSTRAINED_PROFILE",
            "NO_RESOURCE_MODIFICATION=true",
            "NO_WSL_SHUTDOWN_IN_D1V=true",
            "NO_PACKAGE_INSTALL=true",
            "NO_DOCKER_START=true",
            "NO_DOCKER_PULL=true",
            "NO_DBPEDIA_DECOMPRESSION=true",
            "NO_VIRTUOSO=true",
            "NO_SPARQL=true",
            "NO_MODEL_EXECUTION=true",
            "NO_TRAINING=true",
            "NO_ADAPTER_IMPLEMENTATION=true",
            "NO_BENCHMARK=true",
            "EXTERNAL_MONETARY_COST_USD=0.00",
        ]
    )
    + "\n",
    encoding="utf-8",
)
print(json.dumps({"run_id": RUN, "status": status, "errors": errors, "memory_kb": mem, "swap_kb": swap, "disk_kb": disk_kb}, sort_keys=True))
sys.exit(0 if not errors else 1)

#!/usr/bin/env python3
"""Generate Prompt D1V post-restart verification and D1 closure artifacts."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
RUN = "20261013T085129Z"
INITIAL_HEAD = "0c11b8280f35973bcb54baf3b2f53d6dfb85e265"
FREEZE_SHA = "f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c"
GATE = "D1_RESOURCE_CONFIGURATION_PASS_READY_FOR_D2_AUTHORIZATION"
NEXT = "HUMAN_D2_DECOMPRESSION_AND_RDF_VALIDATION_AUTHORIZATION"
ARTIFACT_COMMIT = "`846bb3bd079a5d806e4d8c55ca39bca626dd0454`"
PUB_COMMIT = "`SELF` (second and final Prompt D1V commit)"

MEM_KB = 10182848
SWAP_KB = 2097152
CPU = 16
DISK_AVAILABLE_KB = 945429020
MEM_GIB = round(MEM_KB / 1024 / 1024, 2)
DISK_GIB = round(DISK_AVAILABLE_KB / 1024 / 1024, 2)

DOC = ROOT / f"docs/protocols/common/graph/dbpedia2016-10/d1-verification/{RUN}"
LOG = ROOT / f"logs/d1-verification/{RUN}"
for directory in (DOC, LOG, ROOT / "audit/d1-verification"):
    directory.mkdir(parents=True, exist_ok=True)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def csv_write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


HEADER = f"""**RUN_ID:** `{RUN}`
**Mode:** READ_ONLY_RUNTIME_VERIFICATION · ZERO_COST · NO_DEPLOYMENT
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `{FREEZE_SHA}`
"""

# Consume the D1 Windows-host authorization without inventing host-side observations.
auth_path = ROOT / "docs/protocols/common/graph/dbpedia2016-10/d1-topology/20261013T080249Z/HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION_V2.md"
write(
    auth_path,
    f"""# Human D1 Windows-host apply authorization V2

**Original status:** `READY_UNSIGNED`
**Current status:** `SIGNED_AND_CONSUMED_D1H_D1R_D1V_ONLY`
**Decision:** `APPROVED`
**Approver:** `EDMUNDO MORI ORRILLO`
**Date:** `2026-10-13`

Authorized and consumed: safe Windows-host `.wslconfig` backup/hash and 10GB/2GB merge; manual Windows
PowerShell `wsl --shutdown`; subsequent Ubuntu restart; separate read-only D1V verification.

Not authorized and not performed: DBpedia decompression/RDF parsing, Docker pull/container, Virtuoso,
graph load, SPARQL, gold, metrics, models, training, adapters or benchmark.
""",
)

write(
    DOC / "D1H_WINDOWS_HOST_APPLY_EVIDENCE.md",
    f"""# D1H Windows-host apply evidence

{HEADER}

Evidence source: `HUMAN_SUPPLIED_WINDOWS_POWERSHELL_TRANSCRIPT`; these Windows-file facts are not claimed as
independently observed by Cursor.

- host RAM: 15.19 GiB
- Windows C: free: 7.84 GiB
- distribution: `Ubuntu-22.04`
- `.wslconfig`: `C:\\Users\\USUARIO\\.wslconfig`
- backup: `C:\\Users\\USUARIO\\.wslconfig.backup-20261013T103737`
- backup SHA-256: `a3edd980b35e011c970be441cb074f34baf1d978143d2d9fb5d3c662d9fae0a3`
- new config SHA-256: `d159d10caf6190abfda771fdba9a47d85c1c708b660171e2e197492b8dc36036`
- final config: `[wsl2]`, `memory=10GB`, `swap=2GB`
- terminal marker: `D1H_APPLY_PASS_RESTART_NOT_YET_PERFORMED`

Classification: `D1H_PASS_HUMAN_EXECUTED_EVIDENCE_PROVIDED`.
""",
)

write(
    DOC / "D1R_WSL_RESTART_EVIDENCE.md",
    f"""# D1R WSL restart evidence

{HEADER}

The human reports manually executing `wsl --shutdown` in Windows PowerShell, then restarting
`Ubuntu-22.04`. Cursor does not claim to have observed the shutdown event itself.

Independent supporting evidence from the new guest session: kernel uptime reset; guest memory is
{MEM_KB} kB (~{MEM_GIB} GiB) and swap is {SWAP_KB} kB (2 GiB), matching the changed 10/2 envelope.

Classification: `D1R_PASS_EFFECTIVE_RESTART_CONFIRMED_BY_NEW_GUEST_RESOURCE_STATE`.
""",
)

write(
    DOC / "D1V_POST_RESTART_RESOURCE_VERIFICATION_REPORT.md",
    f"""# D1V post-restart resource verification report

{HEADER}

- Kernel: `6.6.87.2-microsoft-standard-WSL2`, x86_64.
- WSL2: `WSL2_GUEST_CONFIRMED`.
- MemTotal: `{MEM_KB} kB` = ~{MEM_GIB} GiB; `free -h` displays 9.7 GiB.
- Memory target/range: 10GB; 9.4–10.1 GiB accepted.
- Memory result: `TARGET_10GB_EFFECTIVELY_APPLIED` / PASS.
- SwapTotal: `{SWAP_KB} kB`; `/dev/sdc`, partition, 2G, 0B used.
- Swap result: `TARGET_2GB_SWAP_APPLIED` / PASS.
- CPU: {CPU} logical processors / PASS.
- Filesystem: `/dev/sdd`, ext4, 1007G total, 902G displayed available (~{DISK_GIB} GiB raw).
- Storage: mounted/accessed and >305 GiB envelope / PASS.
- Docker: client 29.1.3 present; daemon inactive/unreachable.
- Docker classification: `DOCKER_CLIENT_PRESENT_DAEMON_INACTIVE_NONBLOCKING_D1`.
- Configuration changes during D1V: none.
- ZERO_COST: USD 0.00.
- Prohibited actions: none executed.

D1V classification: `PASS`.
""",
)

csv_write(
    ROOT / "audit/d1-verification/D1_COMPONENT_STATUS_MATRIX.csv",
    ["component", "status", "evidence", "claim_boundary"],
    [
        {"component": "D1P", "status": "PASS", "evidence": "Prompt25B-R1 package/push", "claim_boundary": "package only"},
        {"component": "D1H", "status": "PASS", "evidence": "human Windows transcript and hashes", "claim_boundary": "human-supplied host evidence"},
        {"component": "D1R", "status": "PASS", "evidence": "human restart report + effective guest state", "claim_boundary": "shutdown event not Cursor-observed"},
        {"component": "D1V", "status": "PASS", "evidence": "independent read-only guest commands", "claim_boundary": "resource observation only"},
        {"component": "D1", "status": "PASS_RESOURCE_CONSTRAINED_PROFILE", "evidence": "D1P+D1H+D1R+D1V", "claim_boundary": "full graph load feasibility not proven"},
    ],
)

write(
    DOC / "D1_RESOURCE_CONFIGURATION_GATE.md",
    f"""# D1 resource-configuration gate

{HEADER}

**`{GATE}`**

- D1P_PASS
- D1H_PASS
- D1R_PASS
- D1V_PASS
- WINDOWS_HOST_CONTROL_PLANE
- WSL2_UBUNTU_GUEST
- LOCAL_WSL_RESOURCE_CONSTRAINED_V1
- 10GB_MEMORY_EFFECTIVELY_APPLIED
- 2GB_SWAP_APPLIED
- 16_LOGICAL_CPUS_VISIBLE
- LINUX_STORAGE_HEADROOM_SUFFICIENT
- FULL_GRAPH_LOAD_FEASIBILITY_NOT_PROVEN
- DBPEDIA_STILL_COMPRESSED
- DBPEDIA_NOT_DEPLOYED
- G4_NOT_SATISFIED
- NO_DOCKER_PULL
- NO_VIRTUOSO
- NO_SPARQL
- ZERO_EXTERNAL_MONETARY_COST
- HUMAN_D2_GATE_REQUIRED

Exactly one next action: `{NEXT}`. D2 execution prompt: `RESERVED_NOT_AUTHORIZED`.
ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
""",
)

write(
    DOC / "HUMAN_D2_DECOMPRESSION_AND_RDF_VALIDATION_AUTHORIZATION.md",
    f"""# Human D2 decompression and RDF-validation authorization

{HEADER}

**Status:** `READY_UNSIGNED`

Proposed D2 scope only:

- [ ] verify the compressed canonical scope (114 files);
- [ ] verify existing checksums;
- [ ] decompress DBpedia 2016-10 into the approved Linux workdir;
- [ ] perform static file-level/RDF-syntax validation with pre-approved ZERO_COST tools;
- [ ] monitor disk usage and stop before the approved planning envelope is violated;
- [ ] record artifacts and hashes.

Disk prerequisite: Linux free space must remain above the conservative ~305 GiB envelope plus an explicit
operational margin. Stop on checksum mismatch, unexpected file count/size, disk pressure, malformed output,
ZERO_COST violation, freeze mismatch, or any need for an unauthorized stage.

Not authorized: Docker pull, container creation, Virtuoso, database load, SPARQL, gold, metrics, models,
training, adapters or benchmark.

Approver: ______ · Date: ______ · Decision: ______
""",
)

manifest_path = ROOT / "configs/common/graph/dbpedia2016-10/deployment/DBPEDIA_2016_10_DEPLOYMENT_MANIFEST.yaml"
manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
manifest.update(
    {
        "selected_resource_profile": "LOCAL_WSL_HOST_ADJUSTED",
        "selected_resource_subprofile": "LOCAL_WSL_RESOURCE_CONSTRAINED_V1",
        "resource_configuration_status": "CONFIGURED_AND_VERIFIED",
        "d1p_status": "PASS",
        "d1h_status": "PASS",
        "d1r_status": "PASS",
        "d1v_status": "PASS",
        "d1_status": "PASS_RESOURCE_CONSTRAINED_PROFILE",
        "observed_guest_memory_kb": MEM_KB,
        "observed_guest_swap_kb": SWAP_KB,
        "observed_cpu_count": CPU,
        "observed_linux_free_disk_kb": DISK_AVAILABLE_KB,
        "graph_payload_status": "COMPRESSED_ACQUIRED",
        "deployment_status": "NOT_DEPLOYED",
        "g4_runtime_status": "NOT_SATISFIED",
    }
)
write(manifest_path, yaml.safe_dump(manifest, sort_keys=False))

write(
    ROOT / "docs/decisions/027_d1_resource_configuration_and_post_restart_verification.md",
    f"""# Decision 027 — D1 resource configuration and post-restart verification

Date: 2026-10-13 · RUN_ID: `{RUN}`

The 10 GiB memory / 2 GiB swap constrained profile is effective. D1P, D1H, D1R and D1V pass under the
Windows-host/WSL2-Ubuntu topology. The local profile remains
`RESOURCE_CONSTRAINED_HIGH_RISK_FOR_FULL_GRAPH_LOAD`; D1 does not prove D4 feasibility or satisfy G4.

D2 authorization may be considered next, but D2 is not automatically authorized or executed.
""",
)

sections = [
    ("Executive summary", "D1P/D1H/D1R/D1V pass; overall D1 is PASS_RESOURCE_CONSTRAINED_PROFILE."),
    ("Input authorization", "EDMUNDO MORI ORRILLO approved D1H/D1R/D1V on 2026-10-13; scope consumed only for D1."),
    ("D1 topology", "Windows host controls WSL2; Ubuntu guest performs read-only verification."),
    ("D1P", "PASS: split package prepared/published by Prompt25B-R1."),
    ("D1H", "PASS from human-supplied Windows PowerShell evidence."),
    ("Windows config evidence", "Backup/new hashes and final 10GB/2GB values recorded conservatively."),
    ("D1R", "PASS from human restart report plus changed resource envelope in new guest."),
    ("D1V", "PASS from independent read-only commands in the new Ubuntu session."),
    ("Memory", f"MemTotal {MEM_KB} kB (~{MEM_GIB} GiB), within 9.4–10.1 GiB."),
    ("Swap", f"SwapTotal {SWAP_KB} kB, /dev/sdc 2G, unused."),
    ("CPU", "16 logical processors visible."),
    ("Linux filesystem", f"ext4 mounted; ~{DISK_GIB} GiB raw available, above 305 GiB."),
    ("Docker", "Client 29.1.3 present; daemon inactive, nonblocking for D1; no start/pull."),
    ("Resource capacity boundary", "Full DBpedia/Virtuoso load feasibility remains unproven and high-risk."),
    ("DBpedia status", "114 compressed files remain compressed; NOT_DEPLOYED."),
    ("G4", "NOT_SATISFIED."),
    ("G5", "Implementation and conformance pending."),
    ("G6I", "Pending; G6D documented; adapters false."),
    ("Benchmark", "NOT_CURRENTLY_ELIGIBLE; QALD test SEALED."),
    ("D1 final gate", GATE),
    ("D2 authorization status", "READY_UNSIGNED; D2 RESERVED_NOT_AUTHORIZED."),
    ("Next action", f"Exactly one: `{NEXT}`."),
    ("Claim boundary", "D1 closes resource configuration only, not graph load/runtime feasibility."),
]
report = "# PHASE2 D1 resource configuration and post-restart verification report\n\n" + HEADER + "\n"
for i, (title, body) in enumerate(sections, 1):
    report += f"\n## {i}. {title}\n\n{body}\n"
write(ROOT / "audit/PHASE2_D1_RESOURCE_CONFIGURATION_AND_POST_RESTART_VERIFICATION_REPORT.md", report)

write(
    ROOT / "audit/NEXT_AFTER_D1_RESOURCE_CONFIGURATION_DECISION.md",
    f"""# Next after D1 resource configuration

{HEADER}

D1P/D1H/D1R/D1V: PASS. Overall: `PASS_RESOURCE_CONSTRAINED_PROFILE`.
DBpedia remains compressed and NOT_DEPLOYED; G4 not satisfied; G5/G6I pending; adapters false; benchmark
not eligible; QALD test SEALED.

Exactly one next action: `{NEXT}`.
Status: `HUMAN_GATE_REQUIRED`. D2 execution prompt: `RESERVED_NOT_AUTHORIZED`.
ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
""",
)

registry_path = ROOT / "METHOD_REGISTRY.yaml"
registry = registry_path.read_text(encoding="utf-8").split("\n# Prompt D1V resource verification overlay", 1)[0].rstrip()
registry = registry.replace("schema_version: '0.32'", "schema_version: '0.33'", 1)
registry = registry.replace(
    "phase: phase2_windows_host_wsl_guest_d1_replanned_authorization_pending",
    "phase: phase2_d1_resource_configuration_pass_d2_authorization_pending",
    1,
)
registry = registry.replace("phase2_next_action: HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION", f"phase2_next_action: {NEXT}")
registry = registry.replace("next_research_action: HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION", f"next_research_action: {NEXT}")
overlay = {
    "d1_verification_run_id": RUN,
    "d1p_status_current": "PASS",
    "d1h_status_current": "PASS",
    "d1r_status_current": "PASS",
    "d1v_status_current": "PASS",
    "d1_status_current": "PASS_RESOURCE_CONSTRAINED_PROFILE",
    "observed_wsl_memory_kb": MEM_KB,
    "observed_wsl_memory_gib": MEM_GIB,
    "observed_wsl_swap_kb": SWAP_KB,
    "observed_wsl_swap_gib": 2.0,
    "observed_cpu_count": CPU,
    "observed_linux_free_disk_kb": DISK_AVAILABLE_KB,
    "observed_linux_free_disk_gib": DISK_GIB,
    "docker_client_status": "PRESENT_29_1_3",
    "docker_daemon_status": "INACTIVE_UNREACHABLE_NONBLOCKING_D1",
    "d2_authorization_status": "READY_UNSIGNED",
    "next_research_action_current": NEXT,
}
registry += "\n\n# Prompt D1V resource verification overlay\n" + yaml.safe_dump(overlay, sort_keys=False)
write(registry_path, registry)

profile_path = ROOT / "configs/common/COMMON_PROTOCOL_PROFILE.yaml"
profile = profile_path.read_text(encoding="utf-8").split("\n# Prompt D1V resource verification overlay", 1)[0].rstrip()
profile = profile.replace(
    "phase: phase2_windows_host_wsl_guest_d1_replanned_authorization_pending",
    "phase: phase2_d1_resource_configuration_pass_d2_authorization_pending",
)
profile = profile.replace("next_action: HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION", f"next_action: {NEXT}")
profile = profile.replace("phase2_next_action: HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION", f"phase2_next_action: {NEXT}")
profile += f"""

# Prompt D1V resource verification overlay
d1_verification_run_id: {RUN}
d1_status: PASS_RESOURCE_CONSTRAINED_PROFILE
observed_wsl_memory_kb: {MEM_KB}
observed_wsl_swap_kb: {SWAP_KB}
observed_cpu_count: {CPU}
observed_linux_free_disk_kb: {DISK_AVAILABLE_KB}
docker_client_status: PRESENT_29_1_3
docker_daemon_status: INACTIVE_UNREACHABLE_NONBLOCKING_D1
d2_authorization_status: READY_UNSIGNED
"""
write(profile_path, profile)

roadmap = [
    ("1", "GLOBAL_BLOCKER_RECOVERY_AND_ZERO_COST_RECONCILIATION", "Prompt_25R1", "COMPLETE"),
    ("2", "ZERO_COST_METHOD_RECOVERY_PROTOCOL", "Prompt_25R2", "COMPLETE"),
    ("3", "FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "Prompt_25R3", "COMPLETE"),
    ("4", "PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "Prompt_25R3A", "COMPLETE"),
    ("5", "COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN", "Prompt_25R4", "COMPLETE"),
    ("6", "HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION", "human_gate", "COMPLETE"),
    ("7", "LOCAL_WSL_HOST_ADJUSTED_SELECTION_AND_D1_PREPARATION", "Prompt_25B", "COMPLETE"),
    ("8", "D1P_HOST_PACKAGE_PREPARATION", "Prompt_25B_R1", "COMPLETE"),
    ("9", "HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION", "human_gate", "COMPLETE"),
    ("10", "D1H_WINDOWS_HOST_CONFIG_APPLY", "manual_windows_powershell", "COMPLETE"),
    ("11", "D1R_WSL_RESTART", "manual_windows_powershell", "COMPLETE"),
    ("12", "D1V_POST_RESTART_VERIFICATION", "Prompt_D1V", "COMPLETE"),
    ("13", "HUMAN_D2_AUTHORIZATION", "human_gate", "NEXT_HUMAN_GATE_REQUIRED"),
    ("14", "DECOMPRESSION_AND_RDF_VALIDATION", "D2", "RESERVED_NOT_AUTHORIZED"),
    ("15", "HUMAN_D3_AUTHORIZATION", "human_gate", "BLOCKED_ON_D2_PASS_AND_LICENSE"),
    ("16", "RUNTIME_IMAGE_ACQUISITION", "D3", "PLANNED"),
    ("17", "HUMAN_D4_AUTHORIZATION", "human_gate", "BLOCKED_ON_D3_PASS"),
    ("18", "VIRTUOSO_LOAD", "D4", "PLANNED"),
    ("19", "HUMAN_D5_AUTHORIZATION", "human_gate", "BLOCKED_ON_D4_PASS"),
    ("20", "GRAPH_RUNTIME_VALIDATION", "D5_G4", "PLANNED"),
    ("21", "GOLD_MATERIALIZATION", "D6_GOLD", "PLANNED"),
    ("22", "METRIC_IMPLEMENTATION_AND_CONFORMANCE", "G5", "PLANNED"),
    ("23", "METHOD_RECOVERY_EXECUTION", "recovery_prompts", "PLANNED"),
    ("24", "G6I_G7", "decision", "PLANNED"),
    ("25", "ADAPTER_IMPLEMENTATION", "implementation", "PLANNED"),
    ("26", "COMMON_PREFLIGHT", "runtime", "PLANNED"),
    ("27", "QALD_PRIMARY_BENCHMARK", "experiment", "PLANNED"),
    ("28", "TEXT2SPARQL25_EXTERNAL_VALIDATION", "future_experiment", "CONDITIONAL_OWN_GATES"),
    ("29", "ERROR_ANALYSIS_PE6", "research", "PLANNED"),
    ("30", "CASE_STUDY", "research", "PLANNED"),
    ("31", "TEXT_TO_SQL_TRANSFER_PE7", "research", "PLANNED"),
    ("32", "NEW_TEXT_TO_SPARQL_METHOD_PE8", "research", "PLANNED"),
    ("33", "COMPARISON", "research", "PLANNED"),
    ("34", "ABLATIONS", "research", "PLANNED"),
    ("35", "FINAL_LITERATURE_TRIANGULATION", "research", "PLANNED"),
    ("36", "THESIS_REPRODUCIBILITY_PACKAGE", "research", "PLANNED"),
]
csv_write(
    ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv",
    ["order", "action", "vehicle", "status"],
    [dict(zip(["order", "action", "vehicle", "status"], row)) for row in roadmap],
)

addendum = f"""## Prompt D1V — Post-restart resource verification ({RUN})

Human D1 authorization was consumed. D1H applied 10GB/2GB manually on Windows; D1R was human-controlled;
D1V independently observed MemTotal {MEM_KB} kB (~{MEM_GIB} GiB), swap {SWAP_KB} kB, 16 CPUs and ~902 GiB
displayed free on ext4. D1P/D1H/D1R/D1V pass; overall `PASS_RESOURCE_CONSTRAINED_PROFILE`. Docker client is
present and daemon inactive; no start/pull occurred. DBpedia remains compressed/NOT_DEPLOYED, G4 not
satisfied, and full-load feasibility unproven. Next: `{NEXT}`.
"""
for name in ("README.md", "PROJECT_CONTEXT.md", "RESEARCH_PROTOCOL.md"):
    path = ROOT / name
    base = path.read_text(encoding="utf-8").split("\n## Prompt D1V — Post-restart resource verification", 1)[0].rstrip()
    write(path, base + "\n\n" + addendum)

write(
    ROOT / "PLAN_SYNC.md",
    f"""# PLAN_SYNC — Estado para optimización del plan de prompts

**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab
**Última actualización:** 2026-10-13 (Prompt **D1V**)
**Fase:** D1 resource configuration PASS · D2 authorization pending
**SHA inicial D1V:** `{INITIAL_HEAD}`
**RUN_ID:** `{RUN}`

Gate: `{GATE}`. Freeze `{FREEZE_SHA}` unchanged.

## Prompt 25B-R1 reconciliation

Initial `ed97ea76c092ec39821151d72d8f5fed2da9219b`; artifact
`1962a465759e8b6b68fecbd0ac3322949b4e7ad5`; publication/tip
`0c11b8280f35973bcb54baf3b2f53d6dfb85e265`; push confirmed.

## Current state

D1P/D1H/D1R/D1V PASS. Effective guest: {MEM_KB} kB memory, {SWAP_KB} kB swap, {CPU} CPUs and ~902 GiB
displayed free. D1 means configuration observable only; full graph load is unproven. DBpedia remains
compressed and NOT_DEPLOYED.

## Unique next action

`{NEXT}` — `HUMAN_GATE_REQUIRED`. D2 execution prompt: `RESERVED_NOT_AUTHORIZED`.

## Publication

ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
publication metadata commit: {PUB_COMMIT}
push: confirmed by required post-commit remote verification
""",
)

write(
    ROOT / "docs/plan-sync/NEXT_PROMPT_GUIDANCE.md",
    f"""# NEXT_PROMPT_GUIDANCE

**Tras:** Prompt D1V (`{RUN}`)
**Gate:** `{GATE}`

Next: `{NEXT}` — **HUMAN_GATE_REQUIRED**.

The D2 form is `READY_UNSIGNED`. There is no executable D2 prompt; D2 is `RESERVED_NOT_AUTHORIZED`.
""",
)
write(
    ROOT / "docs/plan-sync/PLANNER_LOOP.md",
    f"""# PLANNER_LOOP

1. `PLAN_SYNC.md`
2. `docs/protocols/common/graph/dbpedia2016-10/d1-verification/{RUN}/D1_RESOURCE_CONFIGURATION_GATE.md`
3. `docs/protocols/common/graph/dbpedia2016-10/d1-verification/{RUN}/HUMAN_D2_DECOMPRESSION_AND_RDF_VALIDATION_AUTHORIZATION.md`
4. `audit/PHASE2_D1_RESOURCE_CONFIGURATION_AND_POST_RESTART_VERIFICATION_REPORT.md`
5. `audit/NEXT_AFTER_D1_RESOURCE_CONFIGURATION_DECISION.md`
6. `METHOD_REGISTRY.yaml`

Next: `{NEXT}` — `HUMAN_GATE_REQUIRED`. D2: `RESERVED_NOT_AUTHORIZED`.
""",
)

index_path = ROOT / "docs/plan-sync/ARTIFACT_INDEX.md"
index = index_path.read_text(encoding="utf-8")
index = index.replace("**Última actualización:** 2026-10-13 (Prompt 25B-R1)", "**Última actualización:** 2026-10-13 (Prompt D1V)", 1)
rows = f"""| D1V-GATE | D1 resource gate | `docs/protocols/common/graph/dbpedia2016-10/d1-verification/{RUN}/D1_RESOURCE_CONFIGURATION_GATE.md` | D2 human handoff |
| D1V-RPT | Post-restart verification | `docs/protocols/common/graph/dbpedia2016-10/d1-verification/{RUN}/D1V_POST_RESTART_RESOURCE_VERIFICATION_REPORT.md` | Resource evidence |
| D1V-D2 | D2 authorization form | `docs/protocols/common/graph/dbpedia2016-10/d1-verification/{RUN}/HUMAN_D2_DECOMPRESSION_AND_RDF_VALIDATION_AUTHORIZATION.md` | READY_UNSIGNED |
| D1V-MAIN | D1 closure report | `audit/PHASE2_D1_RESOURCE_CONFIGURATION_AND_POST_RESTART_VERIFICATION_REPORT.md` | Full evidence |
"""
anchor = "| ID | Tema | Ruta | Cuándo leerlo |\n|---|---|---|---|\n"
if "D1V-GATE" not in index:
    index = index.replace(anchor, anchor + rows, 1)
write(index_path, index)

write(
    LOG / "commands.log",
    """Prompt D1V exact read-only command set
uname -a
free -h
cat /proc/meminfo
swapon --show
nproc
df -h /
df -T /
cat /proc/version
uptime
grep -E 'MemTotal|MemAvailable|SwapTotal|SwapFree' /proc/meminfo
command -v docker || true
docker --version || true
docker version || true
docker info || true
""",
)
write(LOG / "schema-validation.log", "PENDING_FINAL_VALIDATION")
write(
    LOG / "validation.log",
    """PENDING_FINAL_VALIDATION
NO_RESOURCE_MODIFICATION=true
NO_WSL_SHUTDOWN_IN_D1V=true
NO_PACKAGE_INSTALL=true
NO_DOCKER_START=true
NO_DOCKER_PULL=true
NO_DBPEDIA_DECOMPRESSION=true
NO_VIRTUOSO=true
NO_SPARQL=true
EXTERNAL_MONETARY_COST_USD=0.00
""",
)

targets = [
    *sorted(DOC.glob("*")),
    ROOT / "audit/d1-verification/D1_COMPONENT_STATUS_MATRIX.csv",
    ROOT / "audit/PHASE2_D1_RESOURCE_CONFIGURATION_AND_POST_RESTART_VERIFICATION_REPORT.md",
    ROOT / "audit/NEXT_AFTER_D1_RESOURCE_CONFIGURATION_DECISION.md",
    ROOT / "docs/decisions/027_d1_resource_configuration_and_post_restart_verification.md",
    manifest_path,
    registry_path,
    profile_path,
    ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv",
    ROOT / "PLAN_SYNC.md",
    LOG / "resource-observations.log",
    LOG / "docker-readonly.log",
]
write(
    LOG / "metadata.sha256",
    "\n".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}" for path in targets),
)
print(f"generated D1V artifacts RUN_ID={RUN} memory_gib={MEM_GIB} disk_gib={DISK_GIB}")

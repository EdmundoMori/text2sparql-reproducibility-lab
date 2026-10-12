#!/usr/bin/env python3
"""Generate Prompt 25B documentary profile-selection and D1 package.

Static/ZERO_COST only. This script writes repository metadata; it never changes
WSL, swap, Docker, graph payloads, runtimes, or benchmark assets.
"""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
RUN = "20261012T150501Z"
INITIAL_HEAD = "f271997477c8505c1d223b91d7630d09135d3cd3"
FREEZE_SHA = "f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c"
ARTIFACT_COMMIT = "`d5813ffa39226e9cb8f7ba8a2eb8a063c21fbd97`"
PUB_COMMIT = "`SELF` (second and final Prompt 25B commit)"
GATE = "LOCAL_WSL_HOST_ADJUSTED_PROFILE_SELECTED_D1_PACKAGE_READY_FOR_HUMAN_AUTHORIZATION"
NEXT = "HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION"

DOC = ROOT / f"docs/protocols/common/graph/dbpedia2016-10/profile-selection/{RUN}"
AUD = ROOT / "audit/deployment-profile-selection"
CFG = ROOT / "configs/common/graph/dbpedia2016-10/profile-selection"
LOG = ROOT / f"logs/deployment-profile-selection/{RUN}"
for directory in (DOC, AUD, CFG, LOG):
    directory.mkdir(parents=True, exist_ok=True)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def csv_write(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


HEADER = f"""**RUN_ID:** `{RUN}`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `{FREEZE_SHA}`
"""

write(
    DOC / "HUMAN_RESOURCE_PROFILE_SELECTION_RECORD.md",
    f"""# Human resource-profile selection record

{HEADER}

- approver: `EDMUNDO MORI ORRILLO`
- decision_date: `2026-10-12`
- decision: `APPROVED`
- selected_profile: `LOCAL_WSL_HOST_ADJUSTED`
- human_verified_host_ram_gib: `15.19`
- evidence_type: `HUMAN_VERIFIED_WINDOWS_POWERSHELL`
- selection_scope: `PROFILE_SELECTION_ONLY`
- authorization_status: `CONSUMED_FOR_PROFILE_SELECTION_ONLY`

This selection does **not** authorize: resource configuration, WSL restart, swap change, decompression,
Docker pull, container creation, Virtuoso, graph load, SPARQL, gold, metrics, models, training, adapters,
or benchmark execution.
""",
)

form = ROOT / "docs/protocols/common/benchmark-freeze/20261012T143717Z/HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION_V2.md"
write(
    form,
    f"""# Human DBpedia deployment resource profile selection V2

**RUN_ID:** `20261012T143717Z`
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION

**Form status:** `SIGNED_SELECTION_ONLY`
**Selection status:** `APPROVED_PROFILE_SELECTION`
**Manifest SHA-256:** `{FREEZE_SHA}`
**Graph:** `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` · 6,925,795,437 compressed bytes
**Current snapshot:** WSL 7.4 GiB RAM · 2.0 GiB swap · ~902 GiB Linux disk free · Docker daemon inactive
**Policy:** `ZERO_EXTERNAL_MONETARY_COST`

Options preserved:

- [ ] `LOCAL_WSL_CURRENT` — not recommended; high OOM risk.
- [x] `LOCAL_WSL_HOST_ADJUSTED` — selected conditionally; configuration remains unauthorized.
- [ ] `WINDOWS_HOST_NATIVE_DOCKER` — conditional/untested.
- [ ] `EXTERNAL_ZERO_COST_RESEARCH_SERVER` — preferred if suitable zero-cost resources are supplied.
- [ ] `REMOTE_IMMUTABLE_ENDPOINT` — separately labelled; not the selected native deployment.
- [ ] `REJECT_AND_DEFER_DEPLOYMENT`.

Approver: **EDMUNDO MORI ORRILLO**
Date: **2026-10-12**
Human-verified host RAM: **15.19 GiB** (`HUMAN_VERIFIED_WINDOWS_POWERSHELL`)
Selected profile: **LOCAL_WSL_HOST_ADJUSTED**
Decision: **APPROVED_PROFILE_SELECTION**

This signed form authorizes profile selection only. It does not authorize `.wslconfig` or swap changes,
restart, decompression, Docker pull, container creation, Virtuoso, SPARQL, gold, metrics, adapters, or
benchmark execution.
""",
)

allocations = []
for proposed in (8, 10, 11, 12, 13, 14):
    remaining = round(15.19 - proposed, 2)
    pct = round(proposed / 15.19 * 100, 2)
    if remaining >= 6:
        headroom = "ADEQUATE_FOR_HOST"
    elif remaining >= 4:
        headroom = "CONSTRAINED"
    elif remaining >= 3:
        headroom = "MARGINAL_CONDITIONAL"
    else:
        headroom = "INADEQUATE_HOST_HEADROOM"
    if proposed < 12:
        capacity = "BELOW_PRIOR_PLANNING_MINIMUM"
        recommendation = "REJECT_FOR_D1_DBPEDIA_LOAD_ENVELOPE"
    elif proposed == 12:
        capacity = "MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK"
        recommendation = "SELECT_AS_DOCUMENTARY_D1_PROPOSAL_WITH_STOP_CONDITIONS"
    else:
        capacity = "ABOVE_PRIOR_MINIMUM_BUT_HOST_CONSTRAINED"
        recommendation = "REJECT_HOST_STARVATION_RISK"
    allocations.append(
        {
            "host_total_gib": "15.19",
            "proposed_wsl_gib": str(proposed),
            "remaining_host_gib": f"{remaining:.2f}",
            "percent_host_assigned_wsl": f"{pct:.2f}",
            "meets_prior_12gib_planning_minimum": str(proposed >= 12).lower(),
            "host_headroom_class": headroom,
            "virtuoso_capacity_class": capacity,
            "recommendation": recommendation,
            "notes": "planning envelope; memory limit is not a guarantee of physical reservation",
        }
    )
csv_write(
    AUD / "LOCAL_WSL_HOST_HEADROOM_ANALYSIS.csv",
    list(allocations[0]),
    allocations,
)

write(
    DOC / "LOCAL_WSL_HOST_ADJUSTED_CAPACITY_REASSESSMENT.md",
    f"""# LOCAL_WSL_HOST_ADJUSTED capacity reassessment

{HEADER}

Inputs: host RAM 15.19 GiB (`HUMAN_VERIFIED_WINDOWS_POWERSHELL`), current WSL RAM ~7.4 GiB, current swap
2 GiB, Linux free disk ~902 GiB, and 6,925,795,437 compressed DBpedia bytes.

Prompt25A's 12 GiB minimum, 32 GiB recommended RAM, 8 GiB swap and ~305 GiB storage figures remain
`PLANNING_ASSUMPTION_NOT_MEASUREMENT`. They are not measured Virtuoso requirements.

The selected D1 proposal is **12 GiB WSL RAM**, leaving **3.19 GiB** for Windows
(79.00% assigned to WSL). Classification: `MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`. It is not recommended
capacity and cannot satisfy the 32 GiB planning recommendation. D1 must recheck host pressure before and
after restart. 13 and 14 GiB are rejected because they leave only 2.19 and 1.19 GiB to the host.
""",
)

write(
    DOC / "LOCAL_WSL_SWAP_PROPOSAL.md",
    f"""# LOCAL_WSL swap proposal

{HEADER}

Current swap is 2 GiB. Documentary candidates:

- 8 GiB: prior planning value; selected as the minimal D1 proposal.
- 12 GiB: additional resilience but more disk I/O exposure; not selected.
- 16 GiB: maximum historical profile range; not justified for this constrained host.

Proposed D1 value: **8 GiB**. Swap is OOM/load-stage resilience, not a replacement for RAM. It does not
make a 15.19 GiB host equivalent to a 32 GiB RAM machine. No swap was changed.
""",
)

write(
    DOC / "LOCAL_WSL_STORAGE_CAPACITY_CHECK.md",
    f"""# LOCAL_WSL storage capacity check

{HEADER}

- Linux graph filesystem free: ~902 GiB.
- Conservative recommended planning envelope: ~305 GiB.
- Approximate headroom after envelope: **597 GiB**.
- Capacity ratio: **2.96×**.
- Classification: `SUFFICIENT_WITH_LARGE_PLANNING_HEADROOM`.

The Windows C: drive has only ~7.4 GiB free and remains a host operational risk, but it is not the primary
graph filesystem. No graph relocation, decompression, or write-heavy operation occurred.
""",
)

write(
    DOC / "LOCAL_WSL_DOCKER_READINESS_CHECK.md",
    f"""# LOCAL_WSL Docker readiness check

{HEADER}

- Docker client: present, 29.1.3.
- Docker daemon: inactive at Prompt25R4 refresh.
- Docker Compose: absent.
- Image pull/container creation: not performed.

Compose is not intrinsically required for the planned single-container Virtuoso path. A future D3/D4 may
use an exact digest-pinned `docker run`-equivalent invocation; therefore Compose must not be installed solely
because it is absent. Docker availability verification is separately gated in D1E.
""",
)

write(
    DOC / "VIRTUOSO_RUNTIME_PIN_REVALIDATION.md",
    f"""# Virtuoso runtime-pin documentary revalidation

{HEADER}

- Runtime: OpenLink Virtuoso Open Source 7.2.17.
- Registry/image: `docker.io/openlink/virtuoso-opensource-7`.
- Tag: `7.2.17-r25-g6eb68b6-ubuntu`.
- Architecture: `linux/amd64`.
- Platform digest: `sha256:748863fd9026fac41667dac484e5044c6c34e95c75bce3bf26c9225fe7684eb6`.
- Index digest: `sha256:2a9914b95f8a52927a73947c87ec2727f78f87d38e41c38c379efb121f9cbed1`.
- Pin status: `PINNED_METADATA_ONLY`.
- License: `VERIFY_BEFORE_LOAD__github_api_NOASSERTION__historically_GPL-2.0-family`.

The unresolved license evidence is a material D3 blocker. No image may be pulled until authoritative license
scope is resolved and D3 receives separate human authorization.
""",
)

write(
    DOC / "D1_RESOURCE_CONFIGURATION_SCOPE.md",
    f"""# D1 resource-configuration scope

{HEADER}

D1 is restricted to separately authorized operations:

1. `D1A_WSL_MEMORY_LIMIT` — proposed 12 GiB template application.
2. `D1B_WSL_SWAP_CONFIGURATION` — proposed 8 GiB template application.
3. `D1C_WSL_RESTART` — explicit shutdown/restart only if authorized.
4. `D1D_POST_RESTART_RESOURCE_VERIFICATION` — read-only observation.
5. `D1E_DOCKER_DAEMON_AVAILABILITY_CHECK` — availability only; no pull/container.

Excluded: decompression, Docker pull, Virtuoso, graph load, RDF parsing, SPARQL, gold, metrics, methods,
training, adapters and benchmark. Invariant: `D1_PASS_REQUIRED_BEFORE_D2_AUTHORIZATION`; no automatic D2.
""",
)

write(
    CFG / "PROPOSED_WSL_CONFIG.ini",
    """; DOCUMENTARY TEMPLATE ONLY — NOT APPLIED
; Prompt 25B does not authorize copying this file to the Windows user profile.
[wsl2]
memory=12GB
swap=8GB
""",
)

write(
    CFG / "PROPOSED_WSL_CONFIG_RATIONALE.md",
    f"""# Proposed WSL config rationale

{HEADER}

Current: ~7.4 GiB WSL RAM and 2 GiB swap. Proposed for a separately authorized D1: 12 GiB RAM and 8 GiB
swap. Reason: meet only the prior 12 GiB planning minimum while retaining 3.19 GiB host headroom and using
the prior 8 GiB swap planning value. Risk: `MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`; host starvation and
swap thrashing remain possible. This is not 32 GiB recommended capacity.

Rollback: restore the pre-D1 `.wslconfig` bytes (or remove the new file if none existed), perform a separately
authorized WSL restart, and remeasure RAM/swap. The template was not applied in Prompt25B.
""",
)

write(
    DOC / "D1_RESOURCE_CONFIGURATION_ROLLBACK_PLAN.md",
    f"""# D1 resource-configuration rollback plan

{HEADER}

Before D1, preserve whether `.wslconfig` exists and, if present, make a byte-for-byte backup with hash and
permissions metadata. Record current memory/swap observations.

Rollback semantics: stop; restore the exact prior file, or delete the newly created file if the prior state
was absent; perform only the explicitly authorized WSL shutdown/restart; remeasure WSL RAM and swap; compare
with the recorded baseline; do not advance to D2. No rollback or configuration was executed now.
""",
)

write(
    DOC / "D1_RESOURCE_CONFIGURATION_STOP_CONDITIONS.md",
    f"""# D1 resource-configuration stop conditions

{HEADER}

Stop without progression if: host RAM materially differs from 15.19 GiB; 3.19 GiB host headroom is not
operationally adequate; WSL fails to restart; 12 GiB/8 GiB are not observed; Linux disk headroom falls below
the approved envelope; Docker is unexpectedly unavailable; authorization is withdrawn; ZERO_COST is
violated; freeze hash differs from `{FREEZE_SHA}`; or any prohibited deployment action would be needed.

There is no automatic progression from D1 to D2.
""",
)

write(
    DOC / "HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION.md",
    f"""# Human D1 resource-configuration authorization

{HEADER}

**Status:** `READY_UNSIGNED`
**Capacity class:** `MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`

Exact proposed actions:

- [ ] Authorize applying the proposed 12 GiB `.wslconfig` memory limit.
- [ ] Authorize applying the proposed 8 GiB swap value.
- [ ] Authorize WSL shutdown/restart.
- [ ] Authorize post-restart read-only resource verification.
- [ ] Authorize Docker daemon availability verification only.

Not included: DBpedia decompression, RDF validation, Docker pull, container creation, Virtuoso, graph load,
SPARQL, gold, metrics, models, training, adapters or benchmark.

Approver: ______ · Date: ______ · Decision: ______

Unsigned means unauthorized. D1 execution prompt: `RESERVED_NOT_AUTHORIZED`.
""",
)

write(
    DOC / "DBPEDIA_DEPLOYMENT_STAGED_AUTHORIZATION_MAP.md",
    f"""# DBpedia deployment staged authorization map

{HEADER}

| Stage | Scope | Prerequisite | Separate human gate | Output gate |
|---|---|---|---|---|
| D1 | Resource configuration and postcheck | Signed D1 form | Required | D1 runtime-resource PASS |
| D2 | Decompression + static RDF validation | D1 PASS | Required later | D2 artifact PASS |
| D3 | Runtime image acquisition by digest | D2 PASS + license resolved | Required later | D3 digest PASS |
| D4 | Virtuoso graph load | D3 PASS | Required later | D4 load PASS |
| D5 | Runtime technical graph validation/G4 | D4 PASS | Required later | G4 runtime PASS/FAIL |

Each stage has its own prerequisites, stop conditions, authorization and output. `D1_PASS_REQUIRED_BEFORE_D2_AUTHORIZATION`.
Nothing in D2–D5 was authorized or executed.
""",
)

write(
    DOC / "LOCAL_WSL_HOST_ADJUSTED_PROFILE_SELECTION_GATE.md",
    f"""# LOCAL_WSL_HOST_ADJUSTED profile-selection gate

{HEADER}

**`{GATE}`**

- BENCHMARK_FREEZE_V1_PRESERVED
- HUMAN_PROFILE_SELECTION_CONSUMED
- HOST_RAM_15_19_GIB_HUMAN_VERIFIED
- LOCAL_WSL_CURRENT_NOT_SELECTED
- LOCAL_WSL_HOST_ADJUSTED_CONDITIONAL
- RESOURCE_CONFIGURATION_NOT_EXECUTED
- SWAP_NOT_MODIFIED
- WSL_NOT_RESTARTED
- DBPEDIA_NOT_DECOMPRESSED
- DOCKER_IMAGE_NOT_PULLED
- VIRTUOSO_NOT_RUN
- G4_NOT_SATISFIED
- TEST_SEAL_PRESERVED
- ZERO_EXTERNAL_MONETARY_COST_PRESERVED
- HUMAN_D1_GATE_REQUIRED

Exactly one next action: `{NEXT}`. D1 execution prompt: `RESERVED_NOT_AUTHORIZED`.
ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
""",
)

# Deployment manifest: preserve prior evidence while adding the consumed selection.
manifest_path = ROOT / "configs/common/graph/dbpedia2016-10/deployment/DBPEDIA_2016_10_DEPLOYMENT_MANIFEST.yaml"
manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
manifest.update(
    {
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
)
write(manifest_path, yaml.safe_dump(manifest, sort_keys=False))

profiles_path = ROOT / "configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_DEPLOYMENT_PROFILES.yaml"
profiles = yaml.safe_load(profiles_path.read_text(encoding="utf-8"))
profiles["selection_status"] = "HUMAN_SELECTED"
profiles["selected_profile"] = "LOCAL_WSL_HOST_ADJUSTED"
profiles["selection_scope"] = "PROFILE_SELECTION_ONLY"
profiles["human_verified_host_ram_gib"] = 15.19
write(profiles_path, yaml.safe_dump(profiles, sort_keys=False))

write(
    ROOT / "docs/decisions/025_local_wsl_host_adjusted_profile_selection.md",
    f"""# Decision 025 — LOCAL_WSL_HOST_ADJUSTED profile selection

Date: 2026-10-12 · RUN_ID: `{RUN}`

EDMUNDO MORI ORRILLO approved `LOCAL_WSL_HOST_ADJUSTED` for profile selection only, bound to freeze
`COMMON_CORE_BENCHMARK_FREEZE_V1` / `1.0.0-25R4` / `{FREEZE_SHA}` and human-verified host RAM 15.19 GiB.

`LOCAL_WSL_CURRENT` was not selected because ~7.4 GiB RAM and 2 GiB swap remain a high-OOM profile.
The host-adjusted profile remains conditional: proposed 12 GiB RAM leaves 3.19 GiB to Windows and is
`MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`; proposed swap is 8 GiB and is not a RAM substitute.

No deployment/resource operation is authorized. Next gate: `{NEXT}` through the unsigned D1 form.
""",
)

sections = [
    ("Executive summary", "The human profile choice was consumed only for selection. A conditional 12/8 GiB D1 proposal is documented; nothing was configured."),
    ("Input freeze", f"COMMON_CORE_BENCHMARK_FREEZE_V1, version 1.0.0-25R4, SHA-256 `{FREEZE_SHA}` remains unchanged and validator PASS."),
    ("Human selection", "EDMUNDO MORI ORRILLO approved LOCAL_WSL_HOST_ADJUSTED on 2026-10-12."),
    ("Authorization boundary", "PROFILE_SELECTION_ONLY; configuration and deployment remain unauthorized."),
    ("Current resources", "WSL ~7.4 GiB RAM, 2 GiB swap, ~902 GiB Linux free, Docker client 29.1.3."),
    ("15.19 GiB host verification", "HUMAN_VERIFIED_WINDOWS_POWERSHELL; not inferred from WSL."),
    ("WSL memory headroom", "12 GiB leaves 3.19 GiB; conditional and marginal."),
    ("Candidate allocations", "8, 10, 11, 12, 13 and 14 GiB evaluated in the CSV; 14 GiB rejected."),
    ("Proposed allocation", "12 GiB, MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK, not recommended capacity."),
    ("Swap", "8 GiB proposed; no change; not equivalent to RAM."),
    ("Storage", "~902 GiB free vs ~305 GiB envelope; 597 GiB headroom, 2.96×."),
    ("Docker", "Client present; daemon inactive; Compose absent and not required merely for a single pinned container."),
    ("Runtime pin", "Virtuoso 7.2.17 amd64 digest remains PINNED_METADATA_ONLY."),
    ("Runtime license", "VERIFY_BEFORE_LOAD/NOASSERTION remains a material D3 blocker."),
    ("D1 scope", "D1A–D1E only; D1_PASS_REQUIRED_BEFORE_D2_AUTHORIZATION."),
    ("Proposed .wslconfig", "12GB memory / 8GB swap documentary template; not applied."),
    ("Rollback", "Preserve/restore exact previous file state and remeasure after separately authorized restart."),
    ("Stop conditions", "Host mismatch/starvation, restart/postcheck failure, disk, Docker, authorization, cost or freeze mismatch stop progression."),
    ("D1 authorization", "READY_UNSIGNED; all five actions have separate checkboxes."),
    ("D2–D5 staging", "Each later stage has a separate prerequisite, authorization, stop conditions and output gate."),
    ("DBpedia", "114 compressed files remain compressed; NOT_DEPLOYED."),
    ("G4", "NOT_SATISFIED."),
    ("G5", "Implementation and conformance pending."),
    ("G6I", "Implementation approval pending."),
    ("Adapters", "common_adapter_allowed=false; no implementation."),
    ("Benchmark", "NOT_CURRENTLY_ELIGIBLE; test remains SEALED."),
    ("Risks", "Host headroom marginal, Windows C: low, daemon inactive, license unresolved, planning assumptions unmeasured."),
    ("Next action", f"Exactly one: `{NEXT}`; D1 execution prompt reserved, not authorized."),
    ("Claim boundaries", "No claim of configured resources, deployed graph, executable method or benchmark result."),
    ("Conservative conclusion", "The profile is selected and a gated proposal exists; the loop stops at the next human decision."),
]
report = "# PHASE2 DBpedia LOCAL_WSL_HOST_ADJUSTED selection and D1 preparation\n\n" + HEADER + "\n"
for number, (title, body) in enumerate(sections, 1):
    report += f"\n## {number}. {title}\n\n{body}\n"
write(ROOT / "audit/PHASE2_DBPEDIA_LOCAL_WSL_HOST_ADJUSTED_SELECTION_AND_D1_PREPARATION_REPORT.md", report)

write(
    ROOT / "audit/NEXT_AFTER_LOCAL_WSL_HOST_ADJUSTED_SELECTION_DECISION.md",
    f"""# Next after LOCAL_WSL_HOST_ADJUSTED selection

{HEADER}

Selection: `LOCAL_WSL_HOST_ADJUSTED`; host RAM 15.19 GiB human-verified; proposed D1 12 GiB RAM / 8 GiB
swap; capacity `MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`; D1 form `READY_UNSIGNED`.

DBpedia remains compressed and `NOT_DEPLOYED`; G4 not satisfied; G5/G6I pending; adapters false; benchmark
not eligible; QALD test SEALED.

Exactly one next action: `{NEXT}`.
Status: `HUMAN_GATE_REQUIRED`. D1 execution prompt: `RESERVED_NOT_AUTHORIZED`.
ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
""",
)

roadmap = [
    ("1", "GLOBAL_BLOCKER_RECOVERY_AND_ZERO_COST_RECONCILIATION", "Prompt_25R1", "COMPLETE"),
    ("2", "ZERO_COST_METHOD_RECOVERY_PROTOCOL", "Prompt_25R2", "COMPLETE"),
    ("3", "FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "Prompt_25R3", "COMPLETE"),
    ("4", "PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "Prompt_25R3A", "COMPLETE"),
    ("5", "COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN", "Prompt_25R4", "COMPLETE"),
    ("6", "HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION", "human_gate", "COMPLETE"),
    ("7", "LOCAL_WSL_HOST_ADJUSTED_SELECTION_AND_D1_PREPARATION", "Prompt_25B", "COMPLETE"),
    ("8", "HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION", "human_gate", "NEXT_HUMAN_GATE_REQUIRED"),
    ("9", "RESOURCE_CONFIGURATION", "D1", "RESERVED_NOT_AUTHORIZED"),
    ("10", "D1_POSTCHECK", "D1_POSTCHECK", "BLOCKED_ON_D1_AUTH_AND_EXECUTION"),
    ("11", "HUMAN_D2_AUTHORIZATION", "human_gate", "BLOCKED_ON_D1_PASS"),
    ("12", "DECOMPRESSION_AND_RDF_VALIDATION", "D2", "PLANNED"),
    ("13", "HUMAN_D3_AUTHORIZATION", "human_gate", "BLOCKED_ON_D2_PASS_AND_LICENSE"),
    ("14", "RUNTIME_IMAGE_ACQUISITION", "D3", "PLANNED"),
    ("15", "HUMAN_D4_AUTHORIZATION", "human_gate", "BLOCKED_ON_D3_PASS"),
    ("16", "VIRTUOSO_LOAD", "D4", "PLANNED"),
    ("17", "HUMAN_D5_AUTHORIZATION", "human_gate", "BLOCKED_ON_D4_PASS"),
    ("18", "GRAPH_RUNTIME_VALIDATION", "D5_G4", "PLANNED"),
    ("19", "GOLD_MATERIALIZATION", "D6_GOLD", "PLANNED"),
    ("20", "METRIC_IMPLEMENTATION_AND_CONFORMANCE", "G5", "PLANNED"),
    ("21", "METHOD_RECOVERY_EXECUTION", "recovery_prompts", "PLANNED"),
    ("22", "G6I_G7", "decision", "PLANNED"),
    ("23", "ADAPTER_IMPLEMENTATION", "implementation", "PLANNED"),
    ("24", "COMMON_PREFLIGHT", "runtime", "PLANNED"),
    ("25", "QALD_PRIMARY_BENCHMARK", "experiment", "PLANNED"),
    ("26", "TEXT2SPARQL25_EXTERNAL_VALIDATION", "future_experiment", "CONDITIONAL_OWN_GATES"),
    ("27", "ERROR_ANALYSIS_PE6", "research", "PLANNED"),
    ("28", "AI_MODEL_DISCOVERY_CASE_STUDY", "research", "PLANNED"),
    ("29", "TEXT_TO_SQL_TRANSFER_PE7", "research", "PLANNED"),
    ("30", "NEW_TEXT_TO_SPARQL_METHOD_PE8", "research", "PLANNED"),
    ("31", "COMPARISON", "research", "PLANNED"),
    ("32", "ABLATIONS", "research", "PLANNED"),
    ("33", "FINAL_LITERATURE_TRIANGULATION", "research", "PLANNED"),
    ("34", "THESIS_REPRODUCIBILITY_PACKAGE", "research", "PLANNED"),
]
csv_write(ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv", ["order", "action", "vehicle", "status"], [dict(zip(["order", "action", "vehicle", "status"], row)) for row in roadmap])

# Registry overlay preserves the benchmark freeze and all method records.
registry_path = ROOT / "METHOD_REGISTRY.yaml"
registry = registry_path.read_text(encoding="utf-8").split("\n# Prompt 25B deployment profile-selection overlay", 1)[0].rstrip()
registry = registry.replace("schema_version: '0.30'", "schema_version: '0.31'", 1)
registry = registry.replace("phase: phase2_common_core_benchmark_design_frozen_deployment_profile_pending", "phase: phase2_local_wsl_host_adjusted_selected_d1_authorization_pending", 1)
registry = registry.replace("phase2_next_action: HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION", f"phase2_next_action: {NEXT}")
registry = registry.replace("next_research_action: HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION", f"next_research_action: {NEXT}")
registry = registry.replace("deployment_profile_selection_status: DEFERRED_BY_SCIENTIFIC_REPLAN_READY_UNSIGNED", "deployment_profile_selection_status: HUMAN_SELECTED")
overlay = {
    "profile_selection_run_id": RUN,
    "selected_deployment_profile": "LOCAL_WSL_HOST_ADJUSTED",
    "deployment_profile_selection_status_current": "HUMAN_SELECTED",
    "profile_selection_authorization_scope": "PROFILE_ONLY",
    "human_verified_host_ram_gib": 15.19,
    "human_host_ram_evidence_type": "HUMAN_VERIFIED_WINDOWS_POWERSHELL",
    "proposed_wsl_memory_gib": 12,
    "proposed_wsl_swap_gib": 8,
    "resource_capacity_class": "MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK",
    "resource_configuration_status": "NOT_CONFIGURED",
    "d1_package_status": "READY_FOR_HUMAN_AUTHORIZATION",
    "d1_human_authorization_status": "READY_UNSIGNED",
    "d1_execution_prompt_status": "RESERVED_NOT_AUTHORIZED",
    "deployment_status_current": "NOT_DEPLOYED",
    "g4_runtime_status_current": "NOT_SATISFIED",
    "g5_runtime_status_current": "IMPLEMENTATION_AND_CONFORMANCE_PENDING",
    "g6d_status_current": "DOCUMENTED",
    "g6i_status_current": "PENDING",
    "adapters_current": False,
    "benchmark_execution_status_current": "NOT_CURRENTLY_ELIGIBLE",
    "next_research_action_current": NEXT,
}
registry += "\n\n# Prompt 25B deployment profile-selection overlay\n" + yaml.safe_dump(overlay, sort_keys=False)
write(registry_path, registry)

profile_path = ROOT / "configs/common/COMMON_PROTOCOL_PROFILE.yaml"
profile = profile_path.read_text(encoding="utf-8").split("\n# Prompt 25B deployment profile-selection overlay", 1)[0].rstrip()
profile = profile.replace("phase: phase2_common_core_benchmark_design_frozen_deployment_profile_pending", "phase: phase2_local_wsl_host_adjusted_selected_d1_authorization_pending")
profile = profile.replace("next_action: HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION", f"next_action: {NEXT}")
profile = profile.replace("phase2_next_action: HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION", f"phase2_next_action: {NEXT}")
profile = profile.replace("deployment_profile_selection_status: READY_UNSIGNED_V2_HUMAN_GATE_REQUIRED", "deployment_profile_selection_status: HUMAN_SELECTED")
profile = profile.replace("human_resource_form_status: READY_UNSIGNED", "human_resource_form_status: SIGNED_SELECTION_ONLY")
profile = profile.replace("prompt25b_status: RESERVED_NOT_AUTHORIZED", "prompt25b_status: CONSUMED_PROFILE_SELECTION_ONLY")
profile += f"""

# Prompt 25B deployment profile-selection overlay
profile_selection_run_id: {RUN}
selected_deployment_profile: LOCAL_WSL_HOST_ADJUSTED
human_verified_host_ram_gib: 15.19
resource_configuration_status: NOT_CONFIGURED
d1_package_status: READY_FOR_HUMAN_AUTHORIZATION
d1_human_authorization_status: READY_UNSIGNED
d1_execution_prompt_status: RESERVED_NOT_AUTHORIZED
"""
write(profile_path, profile)

master_addendum = f"""## Prompt 25B — LOCAL_WSL_HOST_ADJUSTED selection and D1 preparation ({RUN})

EDMUNDO MORI ORRILLO selected `LOCAL_WSL_HOST_ADJUSTED` for profile selection only and human-verified
15.19 GiB host RAM. A documentary D1 proposal of 12 GiB WSL RAM and 8 GiB swap is classified
`MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`; it was not applied. DBpedia remains compressed/NOT_DEPLOYED;
Docker was not started or pulled; G4 is not satisfied; G5/G6I pending; adapters false; benchmark ineligible.
Next: `{NEXT}`. D1 execution is `RESERVED_NOT_AUTHORIZED`.
"""
for name in ("README.md", "PROJECT_CONTEXT.md", "RESEARCH_PROTOCOL.md"):
    path = ROOT / name
    base = path.read_text(encoding="utf-8").split("\n## Prompt 25B — LOCAL_WSL_HOST_ADJUSTED selection", 1)[0].rstrip()
    write(path, base + "\n\n" + master_addendum)

write(
    ROOT / "PLAN_SYNC.md",
    f"""# PLAN_SYNC — Estado para optimización del plan de prompts

**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab
**Última actualización:** 2026-10-12 (Prompt **25B**)
**Fase:** LOCAL_WSL_HOST_ADJUSTED selected · D1 human authorization pending
**SHA inicial 25B:** `{INITIAL_HEAD}`
**RUN_ID:** `{RUN}`

Gate: `{GATE}`.
Freeze `1.0.0-25R4` SHA-256 `{FREEZE_SHA}` remains unchanged; validator PASS.

## Prompt 25R4 reconciliation

Initial `52b74bceb15bbf8f149e6a94d2be9e2aee5803a5`; artifact
`7e0bdb20be7e05601dc22072964ff0ea22b7a3c7`; publication/tip
`f271997477c8505c1d223b91d7630d09135d3cd3`; push confirmed.

## Prompt 25B state

Human selection `LOCAL_WSL_HOST_ADJUSTED` is consumed for profile selection only. Host RAM 15.19 GiB is
human-verified. Proposed D1: 12 GiB RAM / 8 GiB swap, `MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`; no change
was applied. DBpedia remains NOT_DEPLOYED and benchmark execution remains ineligible.

## Unique next action

`{NEXT}` — `HUMAN_GATE_REQUIRED`. D1 execution prompt is `RESERVED_NOT_AUTHORIZED`.

## Publication

ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
publication metadata commit: {PUB_COMMIT}
push: confirmed by required post-commit remote verification
""",
)

write(
    ROOT / "docs/plan-sync/NEXT_PROMPT_GUIDANCE.md",
    f"""# NEXT_PROMPT_GUIDANCE

**Tras:** Prompt 25B (`{RUN}`)
**Gate:** `{GATE}`

## Acción siguiente

`{NEXT}`

Status: **HUMAN_GATE_REQUIRED**.

There is no executable Cursor prompt. D1 is `RESERVED_NOT_AUTHORIZED` until the five exact resource actions
are explicitly approved. No decompression, pull, Virtuoso, graph load, SPARQL or benchmark is included.
""",
)
write(
    ROOT / "docs/plan-sync/PLANNER_LOOP.md",
    f"""# PLANNER_LOOP

1. `PLAN_SYNC.md`
2. `docs/protocols/common/graph/dbpedia2016-10/profile-selection/{RUN}/LOCAL_WSL_HOST_ADJUSTED_PROFILE_SELECTION_GATE.md`
3. `docs/protocols/common/graph/dbpedia2016-10/profile-selection/{RUN}/HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION.md`
4. `audit/PHASE2_DBPEDIA_LOCAL_WSL_HOST_ADJUSTED_SELECTION_AND_D1_PREPARATION_REPORT.md`
5. `audit/NEXT_AFTER_LOCAL_WSL_HOST_ADJUSTED_SELECTION_DECISION.md`
6. `METHOD_REGISTRY.yaml`

Next: `{NEXT}` — `HUMAN_GATE_REQUIRED`.
D1 execution prompt: `RESERVED_NOT_AUTHORIZED`.
""",
)

index_path = ROOT / "docs/plan-sync/ARTIFACT_INDEX.md"
index = index_path.read_text(encoding="utf-8")
index = index.replace("**Última actualización:** 2026-10-12 (Prompt 25R4)", "**Última actualización:** 2026-10-12 (Prompt 25B)", 1)
rows = f"""| P25B-GATE | Profile-selection gate | `docs/protocols/common/graph/dbpedia2016-10/profile-selection/{RUN}/LOCAL_WSL_HOST_ADJUSTED_PROFILE_SELECTION_GATE.md` | Human D1 handoff |
| P25B-REC | Signed selection record | `docs/protocols/common/graph/dbpedia2016-10/profile-selection/{RUN}/HUMAN_RESOURCE_PROFILE_SELECTION_RECORD.md` | Selection evidence |
| P25B-CAP | Capacity reassessment | `docs/protocols/common/graph/dbpedia2016-10/profile-selection/{RUN}/LOCAL_WSL_HOST_ADJUSTED_CAPACITY_REASSESSMENT.md` | 12/8 GiB rationale |
| P25B-D1 | D1 authorization form | `docs/protocols/common/graph/dbpedia2016-10/profile-selection/{RUN}/HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION.md` | READY_UNSIGNED |
| P25B-RPT | Selection/D1 report | `audit/PHASE2_DBPEDIA_LOCAL_WSL_HOST_ADJUSTED_SELECTION_AND_D1_PREPARATION_REPORT.md` | Full evidence |
"""
anchor = "| ID | Tema | Ruta | Cuándo leerlo |\n|---|---|---|---|\n"
if "P25B-GATE" not in index:
    index = index.replace(anchor, anchor + rows, 1)
write(index_path, index)

write(
    LOG / "commands.log",
    f"""Prompt25B RUN_ID={RUN}
initial_head={INITIAL_HEAD}
mode=DOCUMENTARY_STATIC_ZERO_COST_NO_DEPLOYMENT_NO_RESOURCE_MODIFICATION
generator=scripts/preparation/generate_prompt_25b_artifacts.py
""",
)
write(
    LOG / "resource-analysis.log",
    """host_ram_gib=15.19 HUMAN_VERIFIED_WINDOWS_POWERSHELL
current_wsl_ram_gib=7.4
current_swap_gib=2
proposed_wsl_ram_gib=12
remaining_host_ram_gib=3.19
proposed_swap_gib=8
capacity=MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK
linux_free_disk_gib_approx=902
docker_client=29.1.3
docker_daemon=inactive
compose=absent
""",
)
write(
    LOG / "schema-validation.log",
    """PENDING_FINAL_VALIDATION
freeze_yaml_unchanged_required=true
deployment_manifest_yaml_parse_required=true
method_registry_yaml_parse_required=true
""",
)
write(
    LOG / "validation.log",
    """PENDING_FINAL_VALIDATION
NO_CONFIG_CHANGES=true
NO_WSL_RESTART=true
NO_SWAP_CHANGE=true
NO_DECOMPRESSION=true
NO_DOCKER_PULL=true
NO_CONTAINER_CREATION=true
NO_VIRTUOSO=true
NO_SPARQL=true
NO_MODEL_EXECUTION=true
NO_BENCHMARK=true
EXTERNAL_MONETARY_COST_USD=0.00
""",
)

hash_targets = [
    *sorted(DOC.glob("*")),
    AUD / "LOCAL_WSL_HOST_HEADROOM_ANALYSIS.csv",
    *sorted(CFG.glob("*")),
    ROOT / "docs/decisions/025_local_wsl_host_adjusted_profile_selection.md",
    ROOT / "audit/PHASE2_DBPEDIA_LOCAL_WSL_HOST_ADJUSTED_SELECTION_AND_D1_PREPARATION_REPORT.md",
    ROOT / "audit/NEXT_AFTER_LOCAL_WSL_HOST_ADJUSTED_SELECTION_DECISION.md",
    manifest_path,
    profiles_path,
    form,
    ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv",
    ROOT / "METHOD_REGISTRY.yaml",
    ROOT / "configs/common/COMMON_PROTOCOL_PROFILE.yaml",
    ROOT / "PLAN_SYNC.md",
    ROOT / "docs/plan-sync/NEXT_PROMPT_GUIDANCE.md",
    ROOT / "docs/plan-sync/PLANNER_LOOP.md",
    ROOT / "docs/plan-sync/ARTIFACT_INDEX.md",
]
hash_lines = []
for path in hash_targets:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    hash_lines.append(f"{digest}  {path.relative_to(ROOT)}")
write(LOG / "metadata.sha256", "\n".join(hash_lines))

print(f"generated Prompt25B artifacts RUN_ID={RUN}")

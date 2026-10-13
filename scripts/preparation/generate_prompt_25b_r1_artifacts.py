#!/usr/bin/env python3
"""Generate Prompt 25B-R1 host/guest D1 replan artifacts.

Documentary only: never writes Windows files, changes resources, or invokes WSL
lifecycle operations. The prior interrupted attempt is reconciled explicitly.
"""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
RUN = "20261013T080249Z"
INITIAL_HEAD = "ed97ea76c092ec39821151d72d8f5fed2da9219b"
FREEZE_SHA = "f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c"
GATE = "WINDOWS_HOST_WSL_GUEST_D1_REPLAN_COMPLETE_READY_FOR_HOST_APPLY_AUTHORIZATION"
NEXT = "HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION"
ARTIFACT_COMMIT = "*(post-commit)*"
PUB_COMMIT = "*(post-commit tip; max 2 commits)*"

DOC = ROOT / f"docs/protocols/common/graph/dbpedia2016-10/d1-topology/{RUN}"
CFG = ROOT / "configs/common/graph/dbpedia2016-10/profile-selection"
LOG = ROOT / f"logs/d1-topology-replan/{RUN}"
for directory in (DOC, CFG, LOG, ROOT / "scripts/windows"):
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
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `{FREEZE_SHA}`
"""

write(
    DOC / "WINDOWS_HOST_WSL_GUEST_EXECUTION_TOPOLOGY.md",
    f"""# Windows-host / WSL2-Ubuntu-guest execution topology

{HEADER}

Physical/control host: **Windows**. Linux environment: **Ubuntu guest under WSL2**. Cursor execution depends
on that active Ubuntu guest and cannot survive its termination.

Windows owns `.wslconfig`, host RAM, WSL VM lifecycle, shutdown/restart and the host-side swap VHD.
Ubuntu owns the Linux graph workdir, acquired DBpedia payload, and future authorized Docker/Virtuoso/SPARQL
runtime work.

Invariant: `WSL_GUEST_MUST_NOT_TERMINATE_ITSELF_FROM_CURSOR`.
""",
)

write(
    DOC / "D1_ORCHESTRATION_CORRECTION.md",
    f"""# D1 orchestration correction

{HEADER}

Old orchestration — Cursor/WSL applies configuration, calls shutdown, remains connected and verifies — is
`SUPERSEDED_TOPOLOGY_INCOMPATIBLE`. The observed Cursor disconnection is
`D1_ORCHESTRATION_TOPOLOGY_INCOMPATIBILITY`, not a resource-capacity failure and not a D1 PASS.

Revised orchestration:

- `D1P`: Cursor/WSL prepares and publishes the package.
- `D1H`: user applies host configuration manually in Windows PowerShell.
- `D1R`: user closes WSL-dependent applications and manually shuts down WSL from Windows.
- `D1V`: a new Ubuntu/Cursor session performs read-only verification.

No single Cursor session spans D1H/D1R. The prior interrupted attempt is reconciled separately because
read-only evidence now shows that 12/8 was applied before disconnection; that effect is not accepted as D1
completion and is superseded by the 10/2 host-controlled plan.
""",
)

write(
    DOC / "PRIOR_INTERRUPTED_D1_EFFECTS_RECONCILIATION.md",
    f"""# Prior interrupted D1 effects reconciliation

{HEADER}

Evidence from the authorization turn, before this Prompt25B-R1:

- `%UserProfile%\\.wslconfig` was created with 12GB/8GB; SHA-256
  `a3edd980b35e011c970be441cb074f34baf1d978143d2d9fb5d3c662d9fae0a3`.
- the guest restarted and currently reports 12,541,169,664 bytes (~11.68 GiB) RAM and 8,589,934,592 bytes
  (8 GiB) swap;
- Cursor's active WSL connection was interrupted before the authorization turn could complete;
- no decompression, pull, container, Virtuoso, SPARQL, method or benchmark action occurred.

Classification: `PRIOR_AUTHORIZED_ATTEMPT_APPLIED_12_8_BUT_NOT_ACCEPTED_AS_D1_PASS`.
This is not `D1_EXECUTION_FAILURE`. Prompt25B-R1 performs no host write or restart. The current 12/8 state
must be changed only by a future, separately authorized Windows-host application of the 10/2 proposal.
""",
)

write(
    DOC / "WINDOWS_HOST_MEMORY_REASSESSMENT.md",
    f"""# Windows-host memory reassessment

{HEADER}

Host RAM is 15.19 GiB (`HUMAN_VERIFIED_WINDOWS_POWERSHELL`). Planning for worst-case WSL approach to its
maximum:

- 10 GiB WSL maximum leaves 5.19 GiB theoretical host headroom.
- 12 GiB WSL maximum leaves 3.19 GiB theoretical host headroom.

Windows must retain capacity for kernel/services, desktop, Cursor, browser, cache, WSL management and
recovery. The revised first local ZERO_COST envelope is 10 GiB, classified
`LOCAL_WSL_RESOURCE_CONSTRAINED_ZERO_COST`, `RESOURCE_CONSTRAINED`,
`HOST_STABILITY_PRIORITIZED`, and `BELOW_PRIOR_12GIB_PLANNING_ASSUMPTION`.

The historical 12 GiB value is `PLANNING_ASSUMPTION_NOT_MEASUREMENT`. Ten GiB is not claimed sufficient for
the final DBpedia load; it is only a conservative envelope for progressive testing.
""",
)

write(
    DOC / "WINDOWS_HOST_SWAP_STORAGE_CONSTRAINT.md",
    f"""# Windows-host swap storage constraint

{HEADER}

Current observed WSL swap before the interrupted attempt was 2 GiB; the old proposal was 8 GiB. Prompt25R4
reported only ~7.4 GiB free on Windows C:. WSL swap storage is host-side Windows storage: ~902 GiB free on
Linux ext4 does not provide C: capacity.

Revised proposal: preserve **2 GiB** (`PRESERVE_CURRENT_OBSERVED_SWAP`) when the future Windows-host script
is authorized. Swap expansion requires a separate decision. An alternate Windows `swapFile` path may only
be considered after an adequately sized Windows volume is verified; no other drive is inferred.
""",
)

subprofile = {
    "parent_profile": "LOCAL_WSL_HOST_ADJUSTED",
    "execution_topology": "WINDOWS_HOST_CONTROLLED_WSL2_UBUNTU_GUEST",
    "resource_subprofile": "LOCAL_WSL_RESOURCE_CONSTRAINED_V1",
    "host_ram_gib": 15.19,
    "host_ram_evidence": "HUMAN_VERIFIED_WINDOWS_POWERSHELL",
    "wsl_memory_max_gib": 10,
    "wsl_swap_gib": 2,
    "estimated_host_headroom_gib": 5.19,
    "linux_free_disk_gib": "~902",
    "windows_c_free_gib": "~7.4",
    "capacity_class": "RESOURCE_CONSTRAINED_HIGH_RISK_FOR_FULL_GRAPH_LOAD",
    "cost_policy": "ZERO_EXTERNAL_MONETARY_COST",
    "do_not_claim_full_load_feasible": True,
    "fallback_if_D4_resource_failure": "EXTERNAL_ZERO_COST_RESEARCH_SERVER",
    "proposal_status": "DOCUMENTARY_NOT_APPLIED",
}
write(CFG / "LOCAL_WSL_RESOURCE_CONSTRAINED_V1.yaml", yaml.safe_dump(subprofile, sort_keys=False))
write(CFG / "PROPOSED_WSL_CONFIG_RESOURCE_CONSTRAINED_V1.ini", "[wsl2]\nmemory=10GB\nswap=2GB")

write(
    DOC / "WINDOWS_WSLCONFIG_MERGE_POLICY.md",
    f"""# Windows `.wslconfig` merge policy

{HEADER}

Future D1H must: detect `%UserProfile%\\.wslconfig`; make a byte-for-byte timestamped backup first when it
exists; record its SHA-256; preserve unrelated sections/options; insert or update only `memory=10GB` and
`swap=2GB` under `[wsl2]`; write UTF-8; hash the result; and preserve the rollback path. If absent, create
only the three-line 10/2 template. Blind overwrite is forbidden.
""",
)

powershell = r'''# FUTURE MANUAL EXECUTION FROM WINDOWS POWERSHELL ONLY.
# This script intentionally does not shut down/restart WSL or start Docker.
[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
if ($env:OS -ne "Windows_NT") {
    throw "WINDOWS_HOST_REQUIRED"
}

Write-Host "USERPROFILE=$env:USERPROFILE"
$computer = Get-CimInstance Win32_ComputerSystem
$hostGiB = [math]::Round($computer.TotalPhysicalMemory / 1GB, 2)
Write-Host "HOST_RAM_GIB=$hostGiB"
if ($hostGiB -lt 14.5 -or $hostGiB -gt 16.0) {
    throw "HOST_RAM_MATERIALLY_DIFFERS_FROM_15_19_GIB"
}

$cDrive = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
if ($null -eq $cDrive) {
    throw "WINDOWS_C_DRIVE_QUERY_FAILED"
}
$cFreeGiB = [math]::Round($cDrive.FreeSpace / 1GB, 2)
Write-Host "WINDOWS_C_FREE_GIB=$cFreeGiB"
if ($cFreeGiB -lt 2.0) {
    throw "WINDOWS_C_FREE_SPACE_CRITICAL"
}

$wslRows = & wsl.exe --list --verbose
if ($LASTEXITCODE -ne 0) {
    throw "WSL_LIST_FAILED"
}
$wslRows | ForEach-Object { Write-Host $_ }
$ubuntuWsl2 = @($wslRows | Where-Object {
    ($_ -match "(?i)Ubuntu") -and ($_ -match "\s2\s*$")
})
if ($ubuntuWsl2.Count -lt 1) {
    throw "NO_UBUNTU_LIKE_WSL2_DISTRIBUTION"
}

$path = Join-Path $env:USERPROFILE ".wslconfig"
$timestamp = Get-Date -Format "yyyyMMddTHHmmss"
$backup = $null
if (Test-Path -LiteralPath $path) {
    $backup = "$path.backup-$timestamp"
    Copy-Item -LiteralPath $path -Destination $backup -ErrorAction Stop
    $backupHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $backup).Hash.ToLower()
    Write-Host "BACKUP_PATH=$backup"
    Write-Host "BACKUP_SHA256=$backupHash"
    $lines = [System.Collections.Generic.List[string]](Get-Content -LiteralPath $path)
} else {
    $lines = [System.Collections.Generic.List[string]]::new()
}

$sectionStart = -1
$sectionEnd = $lines.Count
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "^\s*\[wsl2\]\s*$") {
        $sectionStart = $i
        for ($j = $i + 1; $j -lt $lines.Count; $j++) {
            if ($lines[$j] -match "^\s*\[[^\]]+\]\s*$") {
                $sectionEnd = $j
                break
            }
        }
        break
    }
}

if ($sectionStart -lt 0) {
    if ($lines.Count -gt 0 -and $lines[$lines.Count - 1] -ne "") {
        $lines.Add("")
    }
    $lines.Add("[wsl2]")
    $lines.Add("memory=10GB")
    $lines.Add("swap=2GB")
} else {
    for ($i = $sectionEnd - 1; $i -gt $sectionStart; $i--) {
        if ($lines[$i] -match "^\s*(memory|swap)\s*=") {
            $lines.RemoveAt($i)
        }
    }
    $lines.Insert($sectionStart + 1, "swap=2GB")
    $lines.Insert($sectionStart + 1, "memory=10GB")
}

$encoding = New-Object System.Text.UTF8Encoding($false)
$finalText = ($lines -join "`r`n") + "`r`n"
[System.IO.File]::WriteAllText($path, $finalText, $encoding)
$newHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLower()
Write-Host "NEW_SHA256=$newHash"
Write-Host "FINAL_FILE_BEGIN"
Get-Content -LiteralPath $path
Write-Host "FINAL_FILE_END"
Write-Host "CONFIG_WRITTEN_RESTART_NOT_YET_PERFORMED"
'''
write(ROOT / "scripts/windows/prepare_wsl_resource_constrained_profile.ps1", powershell)

write(
    DOC / "WINDOWS_HOST_D1_MANUAL_APPLY_GUIDE.md",
    f"""# Windows-host D1 manual apply guide

{HEADER}

1. **H1:** save and close all work inside WSL.
2. **H2:** from Windows PowerShell run `scripts/windows/prepare_wsl_resource_constrained_profile.ps1`.
3. **H3:** review the resulting `.wslconfig`, backup path and hashes.
4. **H4:** close Cursor WSL windows and terminals.
5. **H5:** only from Windows PowerShell run `wsl --shutdown`. Disconnection is expected; do this only after
   repository changes are committed/pushed and work is saved.
6. **H6:** wait until `wsl --list --running` shows no distribution.
7. **H7:** start Ubuntu manually.
8. **H8:** reopen Cursor and this repository.
9. **H9:** run the separate future D1V verification prompt.

The apply/restart process is not expected to keep Cursor connected.
""",
)

write(
    DOC / "D1V_POST_RESTART_VERIFICATION_SPEC.md",
    f"""# D1V post-restart verification specification

{HEADER}

Future D1V is read-only: `uname -a`, `free -h`, `/proc/meminfo`, `swapon --show`, `nproc`, `df -h`, and
`df -T`. Expected approximate values are near 10 GiB memory and 2 GiB swap, allowing normal reporting
differences. Record actual memory, swap, disk, CPU, host-supplied WSL2 evidence, Docker client and daemon
state. Do not pull images or run Virtuoso.
""",
)

write(
    DOC / "D1_SPLIT_HOST_GUEST_PASS_SEMANTICS.md",
    f"""# D1 split host/guest pass semantics

{HEADER}

D1 passes only when `D1P=PASS`, `D1H=PASS`, `D1R=PASS`, and `D1V=PASS`.

- D1P: package prepared and published.
- D1H: Windows configuration safely applied.
- D1R: human-controlled WSL restart completed.
- D1V: a new Ubuntu session observes intended resources.

No single Cursor session spans D1H/D1R. This prompt can pass D1P only.
""",
)

write(
    DOC / "D1_SPLIT_STOP_CONDITIONS.md",
    f"""# D1 split stop conditions

{HEADER}

Stop if host RAM differs materially; target distro is not WSL2; backup fails; merge is unsafe; Windows C:
becomes critically low; WSL fails to restart; observed memory materially differs from 10 GiB; swap differs
from 2 GiB; filesystem/workdir is unavailable; freeze hash mismatches; ZERO_COST is violated; or deployment
would be required. Do not automatically escalate memory.
""",
)

write(
    DOC / "RESOURCE_CONSTRAINED_DBPEDIA_LOAD_POLICY.md",
    f"""# Resource-constrained DBpedia load policy

{HEADER}

10 GiB RAM / 2 GiB swap does not establish full-load feasibility. D2, D3 and D4 remain progressive,
separately authorized stages. Before D4, create a separate low-memory load configuration with conservative
buffers/parallelism, checkpoints, explicit OOM stop conditions and resumability where supported; do not tune
or execute it now.

If D4 cannot operate within the frozen local envelope, classify `LOCAL_RESOURCE_CAPACITY_BLOCKER` and prefer
`EXTERNAL_ZERO_COST_RESEARCH_SERVER`, never paid cloud/GPU/service.
""",
)

# Preserve historical 12/8 evidence and mark it superseded.
old_ini = ROOT / "configs/common/graph/dbpedia2016-10/profile-selection/PROPOSED_WSL_CONFIG.ini"
write(
    old_ini,
    """; HISTORICAL PROMPT25B PROPOSAL — SUPERSEDED_BY_TOPOLOGY_AND_WINDOWS_STORAGE_EVIDENCE
; Preserved as evidence; do not apply.
[wsl2]
memory=12GB
swap=8GB
""",
)
old_rationale = ROOT / "configs/common/graph/dbpedia2016-10/profile-selection/PROPOSED_WSL_CONFIG_RATIONALE.md"
old_text = old_rationale.read_text(encoding="utf-8").split("\n## Prompt25B-R1 supersession", 1)[0].rstrip()
old_text += """

## Prompt25B-R1 supersession

Status: `SUPERSEDED_BY_TOPOLOGY_AND_WINDOWS_STORAGE_EVIDENCE`. Windows is the primary control plane;
12 GiB leaves only 3.19 GiB theoretical host headroom; 8 GiB swap conflicts with constrained C: capacity;
the values were planning assumptions. Revised documentary proposal: 10 GiB / 2 GiB, not applied.
"""
write(old_rationale, old_text)

old_form = ROOT / "docs/protocols/common/graph/dbpedia2016-10/profile-selection/20261012T150501Z/HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION.md"
write(
    old_form,
    f"""# Human D1 resource-configuration authorization — superseded

**Original RUN_ID:** `20261012T150501Z`
**Status:** `SUPERSEDED_AFTER_INTERRUPTED_AUTHORIZED_ATTEMPT`
**Reason:** `WSL_SELF_SHUTDOWN_ORCHESTRATION_INCOMPATIBLE`

The user authorization was received and the prior attempt applied 12/8 before Cursor disconnected. The
turn did not complete atomically and is not accepted as D1 PASS. This form is superseded by the split
Windows-host/WSL-guest protocol. No further action is authorized by this historical form.

Historical proposal: 12 GiB memory / 8 GiB swap, now
`SUPERSEDED_BY_TOPOLOGY_AND_WINDOWS_STORAGE_EVIDENCE`.
""",
)

write(
    DOC / "HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION_V2.md",
    f"""# Human D1 Windows-host apply authorization V2

{HEADER}

**Status:** `READY_UNSIGNED`

- [ ] Authorize Windows-host `.wslconfig` safe merge: `memory=10GB`, `swap=2GB`.
- [ ] Authorize backup and SHA-256 of an existing `.wslconfig`.
- [ ] Authorize manual `wsl --shutdown` **from Windows PowerShell**, after WSL/Cursor work is saved/closed.
- [ ] Authorize subsequent manual WSL restart.
- [ ] Authorize separate read-only D1V verification.

Not authorized: DBpedia decompression, RDF parsing, Docker pull/container, Virtuoso, graph load, SPARQL,
gold, metrics, models, training, adapters or benchmark.

Approver: ______ · Date: ______ · Decision: ______
""",
)

write(
    ROOT / "docs/decisions/026_windows_host_wsl_guest_d1_orchestration_replan.md",
    f"""# Decision 026 — Windows-host / WSL-guest D1 orchestration replan

Date: 2026-10-13 · RUN_ID: `{RUN}`

Cursor's WSL dependency makes self-shutdown orchestration non-atomic. The interrupted authorized attempt
did apply 12/8, but is not D1 PASS. Old 12/8 is superseded; the new documentary subprofile is 10/2 to retain
5.19 GiB theoretical Windows headroom and avoid expanding host-side swap on a C: drive with ~7.4 GiB free.

D1 is split into D1P/D1H/D1R/D1V. Only D1P is performed here. ZERO_COST and the benchmark freeze remain
unchanged. If future D4 encounters local capacity failure, prefer an external ZERO_COST research server.
""",
)

manifest_path = ROOT / "configs/common/graph/dbpedia2016-10/deployment/DBPEDIA_2016_10_DEPLOYMENT_MANIFEST.yaml"
manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
manifest.update(
    {
        "selected_resource_profile": "LOCAL_WSL_HOST_ADJUSTED",
        "selected_resource_subprofile": "LOCAL_WSL_RESOURCE_CONSTRAINED_V1",
        "execution_topology": "WINDOWS_HOST_CONTROLLED_WSL2_UBUNTU_GUEST",
        "proposed_wsl_memory_gib": 10,
        "proposed_wsl_swap_gib": 2,
        "resource_capacity_class": "RESOURCE_CONSTRAINED_HIGH_RISK_FOR_FULL_GRAPH_LOAD",
        "resource_configuration_status": "PRIOR_12_8_APPLIED_SUPERSEDED_PENDING_AUTHORIZED_10_2_HOST_APPLY",
        "d1_package_status": "D1P_PASS_SPLIT_PROTOCOL",
        "d1_orchestration_status": "REPLANNED_SPLIT_HOST_GUEST",
        "d1_authorization_status": "READY_UNSIGNED_V2",
        "deployment_status": "NOT_DEPLOYED",
        "g4": "NOT_SATISFIED",
        "g4_runtime_status": "NOT_SATISFIED",
    }
)
write(manifest_path, yaml.safe_dump(manifest, sort_keys=False))

sections = [
    ("Problem observed", "Cursor's WSL connection terminated when the guest was shut down."),
    ("Why connection interruption is expected", "Cursor execution depends on the WSL2 Ubuntu guest lifecycle."),
    ("Host/guest topology", "Windows is control plane; Ubuntu/WSL2 is execution plane."),
    ("Prior D1 limitation", "Single-session apply/shutdown/verify is topology-incompatible; prior 12/8 effect is not D1 PASS."),
    ("Memory reassessment", "10 GiB leaves 5.19 GiB theoretical host headroom; 12 GiB leaves 3.19 GiB."),
    ("Swap reassessment", "Revised proposal preserves 2 GiB; swap is not RAM."),
    ("Windows C: constraint", "~7.4 GiB free makes an 8 GiB default swap expansion indefensible."),
    ("10/2 resource profile", "LOCAL_WSL_RESOURCE_CONSTRAINED_V1 is documentary, high-risk for full load, not applied."),
    ("D1P", "Package prepared and published in this prompt."),
    ("D1H", "Future manual Windows-host safe merge, separately authorized."),
    ("D1R", "Future manual Windows PowerShell shutdown after work is closed."),
    ("D1V", "Future new-session read-only Ubuntu verification."),
    ("Windows PowerShell package", "Safe backup/merge/hash script exists and is not executed in 25B-R1."),
    ("Rollback", "Timestamped backup and hashes preserve exact prior config."),
    ("Stop conditions", "Host, WSL2, backup, merge, storage, restart, observed resources, filesystem, freeze and cost."),
    ("Future low-memory Virtuoso strategy", "Separate future conservative tuning before D4; none created/executed now."),
    ("ZERO_COST", "External monetary cost remains USD 0.00."),
    ("DBpedia", "Compressed payload unchanged; NOT_DEPLOYED."),
    ("G4/G5/G6I", "G4 NOT_SATISFIED; G5 and G6I pending; G6D documented; adapters false."),
    ("Benchmark", "NOT_CURRENTLY_ELIGIBLE; QALD test remains SEALED."),
    ("Next human action", f"Exactly one: `{NEXT}`."),
    ("Claim boundary", "D1P only; no claim that 10/2 is applied or full load feasible."),
]
report = "# PHASE2 Windows-host / WSL-guest D1 replan report\n\n" + HEADER + "\n"
for i, (title, body) in enumerate(sections, 1):
    report += f"\n## {i}. {title}\n\n{body}\n"
write(ROOT / "audit/PHASE2_WINDOWS_HOST_WSL_GUEST_D1_REPLAN_REPORT.md", report)

write(
    DOC / "WINDOWS_HOST_WSL_GUEST_D1_REPLAN_GATE.md",
    f"""# Windows-host / WSL-guest D1 replan gate

{HEADER}

**`{GATE}`**

- WINDOWS_PRIMARY_HOST
- WSL2_UBUNTU_GUEST
- CURSOR_WSL_DEPENDENCY_RECOGNIZED
- WSL_SELF_SHUTDOWN_FORBIDDEN_FROM_CURSOR
- D1_SPLIT_HOST_GUEST
- OLD_12G_8G_PROPOSAL_SUPERSEDED
- WSL_10G_PROPOSED
- SWAP_2G_PRESERVED
- WINDOWS_C_STORAGE_CONSTRAINT_RECOGNIZED
- NO_RESOURCE_CHANGE_IN_25B_R1
- NO_WSL_SHUTDOWN_IN_25B_R1
- NO_DBPEDIA_DECOMPRESSION
- NO_DOCKER_PULL
- NO_VIRTUOSO
- NO_SPARQL
- ZERO_EXTERNAL_MONETARY_COST
- HUMAN_GATE_REQUIRED

Exactly one next action: `{NEXT}`.
ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
""",
)

write(
    ROOT / "audit/NEXT_AFTER_WINDOWS_HOST_WSL_GUEST_D1_REPLAN_DECISION.md",
    f"""# Next after Windows-host / WSL-guest D1 replan

{HEADER}

D1P PASS; D1H/D1R/D1V pending. New proposal 10 GiB/2 GiB is documentary and not applied. The prior
interrupted 12/8 effect is superseded and not accepted as D1 PASS. DBpedia remains NOT_DEPLOYED; G4 not
satisfied; G5/G6I pending; adapters false; benchmark ineligible; test SEALED.

Exactly one next action: `{NEXT}`.
Status: `HUMAN_GATE_REQUIRED`. No executable WSL shutdown prompt.
ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
""",
)

# Registry/current state overlay.
registry_path = ROOT / "METHOD_REGISTRY.yaml"
registry = registry_path.read_text(encoding="utf-8").split("\n# Prompt 25B-R1 Windows-host/WSL-guest D1 replan overlay", 1)[0].rstrip()
registry = registry.replace("schema_version: '0.31'", "schema_version: '0.32'", 1)
registry = registry.replace(
    "phase: phase2_local_wsl_host_adjusted_selected_d1_authorization_pending",
    "phase: phase2_windows_host_wsl_guest_d1_replanned_authorization_pending",
    1,
)
registry = registry.replace("phase2_next_action: HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION", f"phase2_next_action: {NEXT}")
registry = registry.replace("next_research_action: HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION", f"next_research_action: {NEXT}")
registry = registry.replace("resource_configuration_status: NOT_CONFIGURED", "resource_configuration_status: PRIOR_12_8_APPLIED_SUPERSEDED_PENDING_AUTHORIZED_10_2_HOST_APPLY")
registry = registry.replace("d1_package_status: READY_FOR_HUMAN_AUTHORIZATION", "d1_package_status: SUPERSEDED_BY_SPLIT_D1P_PACKAGE")
registry = registry.replace("d1_human_authorization_status: READY_UNSIGNED", "d1_human_authorization_status: SUPERSEDED_AFTER_INTERRUPTED_AUTHORIZED_ATTEMPT")
registry = registry.replace("d1_execution_prompt_status: RESERVED_NOT_AUTHORIZED", "d1_execution_prompt_status: SUPERSEDED_TOPOLOGY_INCOMPATIBLE")
overlay = {
    "d1_replan_run_id": RUN,
    "d1_execution_topology": "WINDOWS_HOST_CONTROLLED_WSL2_UBUNTU_GUEST",
    "selected_resource_subprofile": "LOCAL_WSL_RESOURCE_CONSTRAINED_V1",
    "proposed_wsl_memory_gib": 10,
    "proposed_wsl_swap_gib": 2,
    "old_resource_proposal_status": "SUPERSEDED_BY_TOPOLOGY_AND_WINDOWS_STORAGE_EVIDENCE",
    "prior_interrupted_effect_status": "12_8_APPLIED_NOT_ACCEPTED_AS_D1_PASS",
    "d1_split_protocol": ["D1P", "D1H", "D1R", "D1V"],
    "d1p_status": "PASS",
    "d1_v2_authorization_status": "READY_UNSIGNED",
    "resource_configuration_status_current": "PRIOR_12_8_APPLIED_SUPERSEDED_PENDING_AUTHORIZED_10_2_HOST_APPLY",
    "next_research_action_current": NEXT,
}
registry += "\n\n# Prompt 25B-R1 Windows-host/WSL-guest D1 replan overlay\n" + yaml.safe_dump(overlay, sort_keys=False)
write(registry_path, registry)

profile_path = ROOT / "configs/common/COMMON_PROTOCOL_PROFILE.yaml"
profile = profile_path.read_text(encoding="utf-8").split("\n# Prompt 25B-R1 Windows-host/WSL-guest D1 replan overlay", 1)[0].rstrip()
profile = profile.replace(
    "phase: phase2_local_wsl_host_adjusted_selected_d1_authorization_pending",
    "phase: phase2_windows_host_wsl_guest_d1_replanned_authorization_pending",
)
profile = profile.replace("next_action: HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION", f"next_action: {NEXT}")
profile = profile.replace("phase2_next_action: HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION", f"phase2_next_action: {NEXT}")
profile = profile.replace("resource_configuration_status: NOT_CONFIGURED", "resource_configuration_status: PRIOR_12_8_APPLIED_SUPERSEDED_PENDING_AUTHORIZED_10_2_HOST_APPLY")
profile = profile.replace("d1_package_status: READY_FOR_HUMAN_AUTHORIZATION", "d1_package_status: SUPERSEDED_BY_SPLIT_D1P_PACKAGE")
profile = profile.replace("d1_human_authorization_status: READY_UNSIGNED", "d1_human_authorization_status: SUPERSEDED_AFTER_INTERRUPTED_AUTHORIZED_ATTEMPT")
profile = profile.replace("d1_execution_prompt_status: RESERVED_NOT_AUTHORIZED", "d1_execution_prompt_status: SUPERSEDED_TOPOLOGY_INCOMPATIBLE")
profile += f"""

# Prompt 25B-R1 Windows-host/WSL-guest D1 replan overlay
d1_replan_run_id: {RUN}
d1_execution_topology: WINDOWS_HOST_CONTROLLED_WSL2_UBUNTU_GUEST
selected_resource_subprofile: LOCAL_WSL_RESOURCE_CONSTRAINED_V1
proposed_wsl_memory_gib: 10
proposed_wsl_swap_gib: 2
d1p_status: PASS
d1_v2_authorization_status: READY_UNSIGNED
prior_interrupted_effect_status: 12_8_APPLIED_NOT_ACCEPTED_AS_D1_PASS
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
    ("9", "HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION", "human_gate", "NEXT_HUMAN_GATE_REQUIRED"),
    ("10", "D1H_WINDOWS_HOST_CONFIG_APPLY", "manual_windows_powershell", "BLOCKED_ON_HUMAN_AUTH"),
    ("11", "D1R_WSL_RESTART", "manual_windows_powershell", "BLOCKED_ON_D1H_PASS"),
    ("12", "D1V_POST_RESTART_VERIFICATION", "Cursor_prompt", "BLOCKED_ON_D1R"),
    ("13", "HUMAN_D2_AUTHORIZATION", "human_gate", "BLOCKED_ON_D1V_PASS"),
    ("14", "DECOMPRESSION_AND_RDF_VALIDATION", "D2", "PLANNED"),
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

addendum = f"""## Prompt 25B-R1 — Windows-host / WSL-guest D1 replan ({RUN})

Windows is the control plane; Ubuntu/WSL2 is the guest in which Cursor runs. Self-shutdown is forbidden from
Cursor. The interrupted authorized attempt applied 12/8 but is not accepted as D1 PASS; it is superseded by
a documentary 10 GiB/2 GiB constrained proposal. D1 is split into D1P/D1H/D1R/D1V. Only D1P is complete.
No host write, shutdown, restart, deployment or benchmark occurred in 25B-R1. Next:
`{NEXT}`.
"""
for name in ("README.md", "PROJECT_CONTEXT.md", "RESEARCH_PROTOCOL.md"):
    path = ROOT / name
    base = path.read_text(encoding="utf-8").split("\n## Prompt 25B-R1 — Windows-host / WSL-guest D1 replan", 1)[0].rstrip()
    write(path, base + "\n\n" + addendum)

write(
    ROOT / "PLAN_SYNC.md",
    f"""# PLAN_SYNC — Estado para optimización del plan de prompts

**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab
**Última actualización:** 2026-10-13 (Prompt **25B-R1**)
**Fase:** Windows-host/WSL-guest D1 replanned · host authorization pending
**SHA inicial 25B-R1:** `{INITIAL_HEAD}`
**RUN_ID:** `{RUN}`

Gate: `{GATE}`. Freeze `{FREEZE_SHA}` unchanged.

## Prompt 25B reconciliation

Initial `f271997477c8505c1d223b91d7630d09135d3cd3`; artifact
`d5813ffa39226e9cb8f7ba8a2eb8a063c21fbd97`; publication/tip
`ed97ea76c092ec39821151d72d8f5fed2da9219b`; push confirmed.

## Current state

D1P is complete. Old 12/8 is superseded; actual prior effect is recorded but not accepted as D1 PASS.
New 10/2 subprofile is documentary/not applied. D1H/D1R/D1V remain pending. DBpedia is NOT_DEPLOYED.

## Unique next action

`{NEXT}` — `HUMAN_GATE_REQUIRED`. No executable WSL shutdown prompt.

## Publication

ARTIFACT_COMMIT: {ARTIFACT_COMMIT}
publication metadata commit: {PUB_COMMIT}
push: pending
""",
)

write(
    ROOT / "docs/plan-sync/NEXT_PROMPT_GUIDANCE.md",
    f"""# NEXT_PROMPT_GUIDANCE

**Tras:** Prompt 25B-R1 (`{RUN}`)
**Gate:** `{GATE}`

Next: `{NEXT}` — **HUMAN_GATE_REQUIRED**.

No executable WSL shutdown prompt is issued. Future D1H and D1R run manually from Windows only after signed
authorization and committed/pushed work. D1V is a separate Cursor session.
""",
)
write(
    ROOT / "docs/plan-sync/PLANNER_LOOP.md",
    f"""# PLANNER_LOOP

1. `PLAN_SYNC.md`
2. `docs/protocols/common/graph/dbpedia2016-10/d1-topology/{RUN}/WINDOWS_HOST_WSL_GUEST_D1_REPLAN_GATE.md`
3. `docs/protocols/common/graph/dbpedia2016-10/d1-topology/{RUN}/HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION_V2.md`
4. `audit/PHASE2_WINDOWS_HOST_WSL_GUEST_D1_REPLAN_REPORT.md`
5. `audit/NEXT_AFTER_WINDOWS_HOST_WSL_GUEST_D1_REPLAN_DECISION.md`
6. `METHOD_REGISTRY.yaml`

Next: `{NEXT}` — `HUMAN_GATE_REQUIRED`. No WSL self-shutdown.
""",
)

index_path = ROOT / "docs/plan-sync/ARTIFACT_INDEX.md"
index = index_path.read_text(encoding="utf-8")
index = index.replace("**Última actualización:** 2026-10-12 (Prompt 25B)", "**Última actualización:** 2026-10-13 (Prompt 25B-R1)", 1)
rows = f"""| P25BR1-GATE | Host/guest replan gate | `docs/protocols/common/graph/dbpedia2016-10/d1-topology/{RUN}/WINDOWS_HOST_WSL_GUEST_D1_REPLAN_GATE.md` | Host apply handoff |
| P25BR1-TOPO | Execution topology | `docs/protocols/common/graph/dbpedia2016-10/d1-topology/{RUN}/WINDOWS_HOST_WSL_GUEST_EXECUTION_TOPOLOGY.md` | Control-plane boundary |
| P25BR1-PS1 | Future Windows host script | `scripts/windows/prepare_wsl_resource_constrained_profile.ps1` | Manual execution only |
| P25BR1-AUTH | Host apply authorization V2 | `docs/protocols/common/graph/dbpedia2016-10/d1-topology/{RUN}/HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION_V2.md` | READY_UNSIGNED |
| P25BR1-RPT | D1 replan report | `audit/PHASE2_WINDOWS_HOST_WSL_GUEST_D1_REPLAN_REPORT.md` | Full evidence |
"""
anchor = "| ID | Tema | Ruta | Cuándo leerlo |\n|---|---|---|---|\n"
if "P25BR1-GATE" not in index:
    index = index.replace(anchor, anchor + rows, 1)
write(index_path, index)

write(
    LOG / "commands.log",
    f"""RUN_ID={RUN}
initial_head={INITIAL_HEAD}
mode=DOCUMENTARY_STATIC_ZERO_COST_NO_RESOURCE_MODIFICATION_NO_WSL_SHUTDOWN
read_only_reconciliation=git,free,swapon,Windows_.wslconfig_read
host_script_executed=false
""",
)
write(
    LOG / "validation.log",
    """PENDING_FINAL_VALIDATION
NO_RESOURCE_CHANGE_IN_25B_R1=true
NO_WSL_SHUTDOWN_IN_25B_R1=true
NO_DOCKER_PULL=true
NO_VIRTUOSO=true
NO_SPARQL=true
NO_BENCHMARK=true
EXTERNAL_MONETARY_COST_USD=0.00
""",
)
write(LOG / "schema-validation.log", "PENDING_FINAL_VALIDATION")

targets = [
    *sorted(DOC.glob("*")),
    *sorted(CFG.glob("*")),
    ROOT / "scripts/windows/prepare_wsl_resource_constrained_profile.ps1",
    ROOT / "docs/decisions/026_windows_host_wsl_guest_d1_orchestration_replan.md",
    ROOT / "audit/PHASE2_WINDOWS_HOST_WSL_GUEST_D1_REPLAN_REPORT.md",
    ROOT / "audit/NEXT_AFTER_WINDOWS_HOST_WSL_GUEST_D1_REPLAN_DECISION.md",
    manifest_path,
    registry_path,
    profile_path,
    ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv",
    ROOT / "PLAN_SYNC.md",
]
write(
    LOG / "metadata.sha256",
    "\n".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}" for path in targets),
)
print(f"generated Prompt25B-R1 artifacts RUN_ID={RUN}")

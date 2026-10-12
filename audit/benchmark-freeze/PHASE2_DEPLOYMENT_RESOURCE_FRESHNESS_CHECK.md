# Deployment resource freshness check

**RUN_ID:** `20261012T143717Z`
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION


- Previous Prompt25A profile: 2026-07-22 / WSL RAM 7.35 GiB / host RAM 15.19 GiB / swap 2.0 GiB /
  Linux disk free 910.8 GiB / Docker 29.1.3 / Compose absent.
- Current 2026-10-12: WSL RAM 7.4 GiB total, 4.9 GiB available at observation; 2.0 GiB swap, unused;
  `/dev/sdd` 1007 GiB total, ~902 GiB free; 16 logical CPUs; Docker client 29.1.3.
- Docker daemon: not running; Compose: absent. No pull or container action.
- Windows host RAM query and `wsl.exe --status`: unavailable due WSL interop error; historical host figure is
  not promoted to a current measurement.
- C: drive has ~7.4 GiB free, but the acquired graph/workdir is on the Linux filesystem with ~902 GiB free.

`material_change = false` for the existing profile definitions.
`profile_reassessment_required = false`. The host-adjusted option remains conditional on human verification
of current host RAM before selection. No profile was selected and no configuration changed.

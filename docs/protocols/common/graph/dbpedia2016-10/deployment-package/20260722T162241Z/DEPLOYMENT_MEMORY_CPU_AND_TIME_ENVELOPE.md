# Memory, CPU and time envelope

**RUN_ID:** `20260722T162241Z`

## Current

- WSL RAM 7.35 GiB · swap 2.0 GiB · CPU 16 threads.

## Planning (assumptions)

See `audit/PHASE2_DBPEDIA_DEPLOYMENT_MEMORY_TIME_SCENARIOS.csv`.

- Local current: **HIGH OOM risk** for full load.
- Host-adjusted (12–14 GiB WSL + more swap): still **conditional**.
- External ≥32–64 GiB RAM: preferred for safe native load if ZERO_COST server exists.

Load duration: planning range **12–96 hours** (not a promise).
Checkpoint/recovery: additional hours. Tag: `PLANNING_ASSUMPTION_NOT_MEASUREMENT`.

# Windows-host memory reassessment

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


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

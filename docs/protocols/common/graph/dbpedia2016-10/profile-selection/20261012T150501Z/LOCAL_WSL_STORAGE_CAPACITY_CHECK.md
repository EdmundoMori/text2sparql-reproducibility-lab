# LOCAL_WSL storage capacity check

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


- Linux graph filesystem free: ~902 GiB.
- Conservative recommended planning envelope: ~305 GiB.
- Approximate headroom after envelope: **597 GiB**.
- Capacity ratio: **2.96×**.
- Classification: `SUFFICIENT_WITH_LARGE_PLANNING_HEADROOM`.

The Windows C: drive has only ~7.4 GiB free and remains a host operational risk, but it is not the primary
graph filesystem. No graph relocation, decompression, or write-heavy operation occurred.

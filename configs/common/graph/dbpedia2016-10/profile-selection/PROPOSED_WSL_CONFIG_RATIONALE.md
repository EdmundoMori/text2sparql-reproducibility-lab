# Proposed WSL config rationale

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Current: ~7.4 GiB WSL RAM and 2 GiB swap. Proposed for a separately authorized D1: 12 GiB RAM and 8 GiB
swap. Reason: meet only the prior 12 GiB planning minimum while retaining 3.19 GiB host headroom and using
the prior 8 GiB swap planning value. Risk: `MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`; host starvation and
swap thrashing remain possible. This is not 32 GiB recommended capacity.

Rollback: restore the pre-D1 `.wslconfig` bytes (or remove the new file if none existed), perform a separately
authorized WSL restart, and remeasure RAM/swap. The template was not applied in Prompt25B.

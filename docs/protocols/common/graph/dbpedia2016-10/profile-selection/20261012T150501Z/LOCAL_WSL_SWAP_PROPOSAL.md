# LOCAL_WSL swap proposal

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Current swap is 2 GiB. Documentary candidates:

- 8 GiB: prior planning value; selected as the minimal D1 proposal.
- 12 GiB: additional resilience but more disk I/O exposure; not selected.
- 16 GiB: maximum historical profile range; not justified for this constrained host.

Proposed D1 value: **8 GiB**. Swap is OOM/load-stage resilience, not a replacement for RAM. It does not
make a 15.19 GiB host equivalent to a 32 GiB RAM machine. No swap was changed.

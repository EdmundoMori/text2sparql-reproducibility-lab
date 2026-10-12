# D1 resource-configuration scope

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


D1 is restricted to separately authorized operations:

1. `D1A_WSL_MEMORY_LIMIT` — proposed 12 GiB template application.
2. `D1B_WSL_SWAP_CONFIGURATION` — proposed 8 GiB template application.
3. `D1C_WSL_RESTART` — explicit shutdown/restart only if authorized.
4. `D1D_POST_RESTART_RESOURCE_VERIFICATION` — read-only observation.
5. `D1E_DOCKER_DAEMON_AVAILABILITY_CHECK` — availability only; no pull/container.

Excluded: decompression, Docker pull, Virtuoso, graph load, RDF parsing, SPARQL, gold, metrics, methods,
training, adapters and benchmark. Invariant: `D1_PASS_REQUIRED_BEFORE_D2_AUTHORIZATION`; no automatic D2.

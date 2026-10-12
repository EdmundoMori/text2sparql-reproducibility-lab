# D1 resource-configuration stop conditions

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Stop without progression if: host RAM materially differs from 15.19 GiB; 3.19 GiB host headroom is not
operationally adequate; WSL fails to restart; 12 GiB/8 GiB are not observed; Linux disk headroom falls below
the approved envelope; Docker is unexpectedly unavailable; authorization is withdrawn; ZERO_COST is
violated; freeze hash differs from `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`; or any prohibited deployment action would be needed.

There is no automatic progression from D1 to D2.

# Windows `.wslconfig` merge policy

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Future D1H must: detect `%UserProfile%\.wslconfig`; make a byte-for-byte timestamped backup first when it
exists; record its SHA-256; preserve unrelated sections/options; insert or update only `memory=10GB` and
`swap=2GB` under `[wsl2]`; write UTF-8; hash the result; and preserve the rollback path. If absent, create
only the three-line 10/2 template. Blind overwrite is forbidden.

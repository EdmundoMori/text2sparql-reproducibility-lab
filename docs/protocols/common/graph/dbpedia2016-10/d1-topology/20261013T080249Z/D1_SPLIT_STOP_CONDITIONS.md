# D1 split stop conditions

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Stop if host RAM differs materially; target distro is not WSL2; backup fails; merge is unsafe; Windows C:
becomes critically low; WSL fails to restart; observed memory materially differs from 10 GiB; swap differs
from 2 GiB; filesystem/workdir is unavailable; freeze hash mismatches; ZERO_COST is violated; or deployment
would be required. Do not automatically escalate memory.

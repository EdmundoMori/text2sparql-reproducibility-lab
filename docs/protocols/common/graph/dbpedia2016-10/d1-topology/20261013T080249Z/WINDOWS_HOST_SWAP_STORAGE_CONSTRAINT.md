# Windows-host swap storage constraint

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Current observed WSL swap before the interrupted attempt was 2 GiB; the old proposal was 8 GiB. Prompt25R4
reported only ~7.4 GiB free on Windows C:. WSL swap storage is host-side Windows storage: ~902 GiB free on
Linux ext4 does not provide C: capacity.

Revised proposal: preserve **2 GiB** (`PRESERVE_CURRENT_OBSERVED_SWAP`) when the future Windows-host script
is authorized. Swap expansion requires a separate decision. An alternate Windows `swapFile` path may only
be considered after an adequately sized Windows volume is verified; no other drive is inferred.

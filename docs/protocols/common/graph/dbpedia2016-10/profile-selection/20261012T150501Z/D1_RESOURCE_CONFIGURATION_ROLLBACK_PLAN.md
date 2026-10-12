# D1 resource-configuration rollback plan

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Before D1, preserve whether `.wslconfig` exists and, if present, make a byte-for-byte backup with hash and
permissions metadata. Record current memory/swap observations.

Rollback semantics: stop; restore the exact prior file, or delete the newly created file if the prior state
was absent; perform only the explicitly authorized WSL shutdown/restart; remeasure WSL RAM and swap; compare
with the recorded baseline; do not advance to D2. No rollback or configuration was executed now.

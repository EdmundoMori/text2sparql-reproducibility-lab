# D1 split host/guest pass semantics

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


D1 passes only when `D1P=PASS`, `D1H=PASS`, `D1R=PASS`, and `D1V=PASS`.

- D1P: package prepared and published.
- D1H: Windows configuration safely applied.
- D1R: human-controlled WSL restart completed.
- D1V: a new Ubuntu session observes intended resources.

No single Cursor session spans D1H/D1R. This prompt can pass D1P only.

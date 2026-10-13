# D1R WSL restart evidence

**RUN_ID:** `20261013T085129Z`
**Mode:** READ_ONLY_RUNTIME_VERIFICATION · ZERO_COST · NO_DEPLOYMENT
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


The human reports manually executing `wsl --shutdown` in Windows PowerShell, then restarting
`Ubuntu-22.04`. Cursor does not claim to have observed the shutdown event itself.

Independent supporting evidence from the new guest session: kernel uptime reset; guest memory is
10182848 kB (~9.71 GiB) and swap is 2097152 kB (2 GiB), matching the changed 10/2 envelope.

Classification: `D1R_PASS_EFFECTIVE_RESTART_CONFIRMED_BY_NEW_GUEST_RESOURCE_STATE`.

# Windows-host D1 manual apply guide

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


1. **H1:** save and close all work inside WSL.
2. **H2:** from Windows PowerShell run `scripts/windows/prepare_wsl_resource_constrained_profile.ps1`.
3. **H3:** review the resulting `.wslconfig`, backup path and hashes.
4. **H4:** close Cursor WSL windows and terminals.
5. **H5:** only from Windows PowerShell run `wsl --shutdown`. Disconnection is expected; do this only after
   repository changes are committed/pushed and work is saved.
6. **H6:** wait until `wsl --list --running` shows no distribution.
7. **H7:** start Ubuntu manually.
8. **H8:** reopen Cursor and this repository.
9. **H9:** run the separate future D1V verification prompt.

The apply/restart process is not expected to keep Cursor connected.

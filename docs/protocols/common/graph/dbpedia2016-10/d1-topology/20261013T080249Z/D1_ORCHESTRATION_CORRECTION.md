# D1 orchestration correction

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Old orchestration — Cursor/WSL applies configuration, calls shutdown, remains connected and verifies — is
`SUPERSEDED_TOPOLOGY_INCOMPATIBLE`. The observed Cursor disconnection is
`D1_ORCHESTRATION_TOPOLOGY_INCOMPATIBILITY`, not a resource-capacity failure and not a D1 PASS.

Revised orchestration:

- `D1P`: Cursor/WSL prepares and publishes the package.
- `D1H`: user applies host configuration manually in Windows PowerShell.
- `D1R`: user closes WSL-dependent applications and manually shuts down WSL from Windows.
- `D1V`: a new Ubuntu/Cursor session performs read-only verification.

No single Cursor session spans D1H/D1R. The prior interrupted attempt is reconciled separately because
read-only evidence now shows that 12/8 was applied before disconnection; that effect is not accepted as D1
completion and is superseded by the 10/2 host-controlled plan.

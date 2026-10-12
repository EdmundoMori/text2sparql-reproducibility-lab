# Decision 025 — LOCAL_WSL_HOST_ADJUSTED profile selection

Date: 2026-10-12 · RUN_ID: `20261012T150501Z`

EDMUNDO MORI ORRILLO approved `LOCAL_WSL_HOST_ADJUSTED` for profile selection only, bound to freeze
`COMMON_CORE_BENCHMARK_FREEZE_V1` / `1.0.0-25R4` / `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c` and human-verified host RAM 15.19 GiB.

`LOCAL_WSL_CURRENT` was not selected because ~7.4 GiB RAM and 2 GiB swap remain a high-OOM profile.
The host-adjusted profile remains conditional: proposed 12 GiB RAM leaves 3.19 GiB to Windows and is
`MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`; proposed swap is 8 GiB and is not a RAM substitute.

No deployment/resource operation is authorized. Next gate: `HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION` through the unsigned D1 form.

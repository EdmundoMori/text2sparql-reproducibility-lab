# D1V post-restart verification specification

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Future D1V is read-only: `uname -a`, `free -h`, `/proc/meminfo`, `swapon --show`, `nproc`, `df -h`, and
`df -T`. Expected approximate values are near 10 GiB memory and 2 GiB swap, allowing normal reporting
differences. Record actual memory, swap, disk, CPU, host-supplied WSL2 evidence, Docker client and daemon
state. Do not pull images or run Virtuoso.

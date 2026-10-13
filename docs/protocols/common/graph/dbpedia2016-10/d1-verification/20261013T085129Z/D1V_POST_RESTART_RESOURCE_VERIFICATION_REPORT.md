# D1V post-restart resource verification report

**RUN_ID:** `20261013T085129Z`
**Mode:** READ_ONLY_RUNTIME_VERIFICATION · ZERO_COST · NO_DEPLOYMENT
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


- Kernel: `6.6.87.2-microsoft-standard-WSL2`, x86_64.
- WSL2: `WSL2_GUEST_CONFIRMED`.
- MemTotal: `10182848 kB` = ~9.71 GiB; `free -h` displays 9.7 GiB.
- Memory target/range: 10GB; 9.4–10.1 GiB accepted.
- Memory result: `TARGET_10GB_EFFECTIVELY_APPLIED` / PASS.
- SwapTotal: `2097152 kB`; `/dev/sdc`, partition, 2G, 0B used.
- Swap result: `TARGET_2GB_SWAP_APPLIED` / PASS.
- CPU: 16 logical processors / PASS.
- Filesystem: `/dev/sdd`, ext4, 1007G total, 902G displayed available (~901.63 GiB raw).
- Storage: mounted/accessed and >305 GiB envelope / PASS.
- Docker: client 29.1.3 present; daemon inactive/unreachable.
- Docker classification: `DOCKER_CLIENT_PRESENT_DAEMON_INACTIVE_NONBLOCKING_D1`.
- Configuration changes during D1V: none.
- ZERO_COST: USD 0.00.
- Prohibited actions: none executed.

D1V classification: `PASS`.

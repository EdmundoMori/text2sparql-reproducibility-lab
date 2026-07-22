# Current machine deployment profile

**RUN_ID:** `20260722T162241Z` · Tag: `CURRENT_MACHINE_PROFILE_REDETECTED`

| Resource | Value |
|---|---|
| CPU | AMD Ryzen 7 7840HS w/ Radeon 780M Graphics · 16 threads (8 cores) |
| Arch | x86_64 |
| WSL RAM | **7.35 GiB** (available ~6.04 GiB) |
| Host RAM | **15.19 GiB** |
| Swap | **2.0 GiB** |
| Disk free (`/`, ext4) | **910.8 GiB** |
| Docker | 29.1.3 (linux/amd64) |
| Compose | **ABSENT** |
| `.wslconfig` | **ABSENT** |
| open files ulimit | 1048576 |
| max user processes | 30081 |
| payload on disk | 6925795437 bytes (~6.45 GiB) |

## Feasibility class (current, no changes)

`LOCAL_WSL_CURRENT_PROFILE_CONDITIONAL_HIGH_RISK` — disk ample; **RAM insufficient for safe full Virtuoso load** of endpoint-equivalent DBpedia without host adjustment or external server.

No host files modified. No packages installed.

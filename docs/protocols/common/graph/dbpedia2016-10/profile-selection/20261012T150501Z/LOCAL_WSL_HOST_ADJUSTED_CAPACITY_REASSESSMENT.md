# LOCAL_WSL_HOST_ADJUSTED capacity reassessment

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Inputs: host RAM 15.19 GiB (`HUMAN_VERIFIED_WINDOWS_POWERSHELL`), current WSL RAM ~7.4 GiB, current swap
2 GiB, Linux free disk ~902 GiB, and 6,925,795,437 compressed DBpedia bytes.

Prompt25A's 12 GiB minimum, 32 GiB recommended RAM, 8 GiB swap and ~305 GiB storage figures remain
`PLANNING_ASSUMPTION_NOT_MEASUREMENT`. They are not measured Virtuoso requirements.

The selected D1 proposal is **12 GiB WSL RAM**, leaving **3.19 GiB** for Windows
(79.00% assigned to WSL). Classification: `MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK`. It is not recommended
capacity and cannot satisfy the 32 GiB planning recommendation. D1 must recheck host pressure before and
after restart. 13 and 14 GiB are rejected because they leave only 2.19 and 1.19 GiB to the host.

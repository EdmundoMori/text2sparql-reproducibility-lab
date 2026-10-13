# Prior interrupted D1 effects reconciliation

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Evidence from the authorization turn, before this Prompt25B-R1:

- `%UserProfile%\.wslconfig` was created with 12GB/8GB; SHA-256
  `a3edd980b35e011c970be441cb074f34baf1d978143d2d9fb5d3c662d9fae0a3`.
- the guest restarted and currently reports 12,541,169,664 bytes (~11.68 GiB) RAM and 8,589,934,592 bytes
  (8 GiB) swap;
- Cursor's active WSL connection was interrupted before the authorization turn could complete;
- no decompression, pull, container, Virtuoso, SPARQL, method or benchmark action occurred.

Classification: `PRIOR_AUTHORIZED_ATTEMPT_APPLIED_12_8_BUT_NOT_ACCEPTED_AS_D1_PASS`.
This is not `D1_EXECUTION_FAILURE`. Prompt25B-R1 performs no host write or restart. The current 12/8 state
must be changed only by a future, separately authorized Windows-host application of the 10/2 proposal.

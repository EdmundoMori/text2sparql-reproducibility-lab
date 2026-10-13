# Windows-host / WSL2-Ubuntu-guest execution topology

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


Physical/control host: **Windows**. Linux environment: **Ubuntu guest under WSL2**. Cursor execution depends
on that active Ubuntu guest and cannot survive its termination.

Windows owns `.wslconfig`, host RAM, WSL VM lifecycle, shutdown/restart and the host-side swap VHD.
Ubuntu owns the Linux graph workdir, acquired DBpedia payload, and future authorized Docker/Virtuoso/SPARQL
runtime work.

Invariant: `WSL_GUEST_MUST_NOT_TERMINATE_ITSELF_FROM_CURSOR`.

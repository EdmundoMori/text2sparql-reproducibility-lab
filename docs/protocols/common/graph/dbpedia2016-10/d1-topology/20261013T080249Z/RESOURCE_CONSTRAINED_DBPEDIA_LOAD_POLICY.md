# Resource-constrained DBpedia load policy

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


10 GiB RAM / 2 GiB swap does not establish full-load feasibility. D2, D3 and D4 remain progressive,
separately authorized stages. Before D4, create a separate low-memory load configuration with conservative
buffers/parallelism, checkpoints, explicit OOM stop conditions and resumability where supported; do not tune
or execute it now.

If D4 cannot operate within the frozen local envelope, classify `LOCAL_RESOURCE_CAPACITY_BLOCKER` and prefer
`EXTERNAL_ZERO_COST_RESEARCH_SERVER`, never paid cloud/GPU/service.

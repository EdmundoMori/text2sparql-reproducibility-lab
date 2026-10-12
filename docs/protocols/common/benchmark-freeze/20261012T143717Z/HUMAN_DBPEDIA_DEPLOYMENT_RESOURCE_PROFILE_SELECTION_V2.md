# Human DBpedia deployment resource profile selection V2

**RUN_ID:** `20261012T143717Z`
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION

**Form status:** `READY_UNSIGNED`
**Selection status:** `NONE`
**Manifest SHA-256:** `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`
**Graph:** `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` · 6,925,795,437 compressed bytes
**Current snapshot:** WSL 7.4 GiB RAM · 2.0 GiB swap · ~902 GiB Linux disk free · Docker daemon unavailable
**Policy:** `ZERO_EXTERNAL_MONETARY_COST`

Select exactly one:

- [ ] `LOCAL_WSL_CURRENT` — not recommended; high OOM risk.
- [ ] `LOCAL_WSL_HOST_ADJUSTED` — conditional; verify current host RAM, human changes `.wslconfig`/restart.
- [ ] `WINDOWS_HOST_NATIVE_DOCKER` — conditional/untested; verify storage and Docker Desktop resources.
- [ ] `EXTERNAL_ZERO_COST_RESEARCH_SERVER` — preferred if suitable zero-cost resources are supplied.
- [ ] `REMOTE_IMMUTABLE_ENDPOINT` — only with immutable 2016-10-equivalent evidence; separately labelled.
- [ ] `REJECT_AND_DEFER_DEPLOYMENT`.

Approver: ______ · Date: ______ · Selected profile: ______ · Decision: ______ · Confirmation: ______

This form authorizes profile selection only. It does not authorize `.wslconfig`/swap changes, restart,
decompression, Docker pull, container creation, Virtuoso, SPARQL, gold, metrics, adapters or benchmark.

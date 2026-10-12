# Human DBpedia deployment resource profile selection V2

**RUN_ID:** `20261012T143717Z`
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION

**Form status:** `SIGNED_SELECTION_ONLY`
**Selection status:** `APPROVED_PROFILE_SELECTION`
**Manifest SHA-256:** `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`
**Graph:** `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` · 6,925,795,437 compressed bytes
**Current snapshot:** WSL 7.4 GiB RAM · 2.0 GiB swap · ~902 GiB Linux disk free · Docker daemon inactive
**Policy:** `ZERO_EXTERNAL_MONETARY_COST`

Options preserved:

- [ ] `LOCAL_WSL_CURRENT` — not recommended; high OOM risk.
- [x] `LOCAL_WSL_HOST_ADJUSTED` — selected conditionally; configuration remains unauthorized.
- [ ] `WINDOWS_HOST_NATIVE_DOCKER` — conditional/untested.
- [ ] `EXTERNAL_ZERO_COST_RESEARCH_SERVER` — preferred if suitable zero-cost resources are supplied.
- [ ] `REMOTE_IMMUTABLE_ENDPOINT` — separately labelled; not the selected native deployment.
- [ ] `REJECT_AND_DEFER_DEPLOYMENT`.

Approver: **EDMUNDO MORI ORRILLO**
Date: **2026-10-12**
Human-verified host RAM: **15.19 GiB** (`HUMAN_VERIFIED_WINDOWS_POWERSHELL`)
Selected profile: **LOCAL_WSL_HOST_ADJUSTED**
Decision: **APPROVED_PROFILE_SELECTION**

This signed form authorizes profile selection only. It does not authorize `.wslconfig` or swap changes,
restart, decompression, Docker pull, container creation, Virtuoso, SPARQL, gold, metrics, adapters, or
benchmark execution.

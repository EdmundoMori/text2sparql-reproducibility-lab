# Human D1 Windows-host apply authorization V2

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


**Status:** `READY_UNSIGNED`

- [ ] Authorize Windows-host `.wslconfig` safe merge: `memory=10GB`, `swap=2GB`.
- [ ] Authorize backup and SHA-256 of an existing `.wslconfig`.
- [ ] Authorize manual `wsl --shutdown` **from Windows PowerShell**, after WSL/Cursor work is saved/closed.
- [ ] Authorize subsequent manual WSL restart.
- [ ] Authorize separate read-only D1V verification.

Not authorized: DBpedia decompression, RDF parsing, Docker pull/container, Virtuoso, graph load, SPARQL,
gold, metrics, models, training, adapters or benchmark.

Approver: ______ · Date: ______ · Decision: ______

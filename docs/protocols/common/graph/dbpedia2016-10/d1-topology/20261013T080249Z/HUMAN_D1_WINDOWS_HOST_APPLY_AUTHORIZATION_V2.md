# Human D1 Windows-host apply authorization V2

**Original status:** `READY_UNSIGNED`
**Current status:** `SIGNED_AND_CONSUMED_D1H_D1R_D1V_ONLY`
**Decision:** `APPROVED`
**Approver:** `EDMUNDO MORI ORRILLO`
**Date:** `2026-10-13`

Authorized and consumed: safe Windows-host `.wslconfig` backup/hash and 10GB/2GB merge; manual Windows
PowerShell `wsl --shutdown`; subsequent Ubuntu restart; separate read-only D1V verification.

Not authorized and not performed: DBpedia decompression/RDF parsing, Docker pull/container, Virtuoso,
graph load, SPARQL, gold, metrics, models, training, adapters or benchmark.

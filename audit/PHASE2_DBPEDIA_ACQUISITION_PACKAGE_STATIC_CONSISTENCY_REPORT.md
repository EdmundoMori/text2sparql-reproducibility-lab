# PHASE2 — DBpedia acquisition package static consistency

**Prompt:** 23C · **RUN_ID:** `20260722T134313Z` · **Cost:** 0.00 · **Network:** none

## Inconsistencia

Allowlist Prompt 23B usaba paths `//2016-10/...` (114); manifest usaba `/2016-10/...`. Exact match = 0.

## Fix

Regeneración estática del allowlist desde `urlsplit(source_url).path`. Scope científico intacto (114 / 6925795437 / hash `2dcbc4df…`).

## Resultados

| Metric | Before | After |
|---|---:|---:|
| payload paths | 114 (`//`) | 114 (`/`) |
| exact set equality | 0 | 114 |
| double slash | 114 | 0 |
| missing/extra | 114/128 vs expected | 0/0 |

Validator: **STATIC_CONSISTENCY_PASS**  
Allowlist file SHA-256: `3a773f39b41f26f3ce1e077053c58c37c8f7fd6486f78303688b2ec9197067eb`  
Validation report SHA-256: `7690437868942ff1cae8eae6af60bf28b94ed82f9fecc5f8941e683b070bc15b`

## Gate / next

`DBPEDIA_ACQUISITION_PACKAGE_STATIC_CONSISTENCY_VERIFIED_READY_FOR_HUMAN_AUTHORIZATION` → `HUMAN_DBPEDIA_2016_10_GRAPH_ACQUISITION_AUTHORIZATION` (humano). Prompt 24B reserved.

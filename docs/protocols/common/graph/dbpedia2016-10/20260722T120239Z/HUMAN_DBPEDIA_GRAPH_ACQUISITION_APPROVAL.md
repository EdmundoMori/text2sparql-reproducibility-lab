# Human authorization — DBpedia 2016-10 graph acquisition

**RUN_ID:** `20260722T120239Z`  
**Form status:** `NOT_READY_CONDITIONAL`

## Readiness checklist (documentary)

| Criterion | Status |
|---|---|
| Exact file list closed | **NO** — 33 unavailable + ontology pending |
| File count known (available candidate) | YES — 81 |
| Compressed total known (available) | YES — 5023159516 |
| Checksum coverage known | PARTIAL (MD5 core/links; LHD missing; 33 unavailable) |
| License documented | YES (evidence; not advice) |
| Resource assessment completed | YES — `CONDITIONAL_HIGH_RISK` |
| Network allowlist exact | DRAFT documentary |
| Destination defined | YES (workdir path in manifest) |
| Stop conditions defined | YES |

## Blockers

1. Close endpoint-equivalent file scope (Prompt **23B**).  
2. Decide treatment of 33 unavailable `*_en_uris_*` files.  
3. Decide ontology include/exclude.  
4. Separate future authorization for **deployment/load** (download auth ≠ Virtuoso auth).

## Authorization fields (UNSIGNED — do not fill)

- authorization_id: _(blank)_
- approver: _(blank)_
- date: _(blank)_
- decision: _(blank)_
- signature: _(blank)_

**Do not reuse** QALD authorization `AUTH_QALD9PLUS_T6B_20260722T105246Z_EMO_01` (CONSUMED_AFTER_PASS).

Checkboxes intentionally unmarked.

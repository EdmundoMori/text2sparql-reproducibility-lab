# Serialization selection

**RUN_ID:** `20260722T120239Z`

## Candidates

| Form | Role |
|---|---|
| `.ttl.bz2` | Present for core-i18n/en and some links |
| `.tql.bz2` | Present for many en datasets (named graphs); **not** used for endpoint-equivalent core package |
| `.nt.bz2` | Dominant in `links/` |

## Decision

**Selected package serialization policy:**

1. Core + LHD: **exactly `.ttl.bz2`** (matches checksum paths and LHD URLs).
2. Links: **as published** unique files (`.nt.bz2` / `.ttl.bz2`) — not dual-loading ttl+tql.
3. Do **not** also load `.tql.bz2` counterparts for the same basename.

## Inference tag

Historical loader byte format not proven → `ENDPOINT_EQUIVALENT_SERIALIZATION_INFERRED` (ttl for core).  
No claim of byte-identity with original Virtuoso load artifacts.

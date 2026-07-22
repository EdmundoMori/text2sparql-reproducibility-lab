# DBpedia 2016-10 endpoint equivalence

**RUN_ID:** `20260722T120239Z`  
Tags: `HISTORICAL_ENDPOINT_SCOPE_DOCUMENTED` · `ENDPOINT_EQUIVALENT_FILE_SCOPE_CONDITIONAL`

## Official historical load list

From https://www.dbpedia.org/resources/sparql/ (metadata GET, Prompt 23):

- directory `2016-10/links/`
- directory `2016-10/core/`
- file `core-i18n/en/instance_types_lhd_dbo_en.ttl.bz2`
- file `core-i18n/en/instance_types_lhd_ext_en.ttl.bz2`

Current endpoint: **Databus Latest Core** (mutable) — not equivalent.

## Scope classes (do not conflate)

| Class | Meaning |
|---|---|
| RELEASE_SCOPE | Entire 2016-10 tree (core-i18n all languages, NIF, page_links, etc.) — **NOT** required |
| CORE_SCOPE | Files intended under `core/` |
| PUBLIC_ENDPOINT_EQUIVALENT_SCOPE | Documented load set above |

## Resolution of `core/`

Apache listing of `core/*.ttl.bz2` shows ~90-byte entries (symlink-sized). **HEAD returns HTTP 404** for those URLs.  
`core/_checksums.md5` maps entries to `./core-i18n/en/<file>.ttl.bz2`.

**Resolution rule:** treat endpoint-equivalent core payload as the **checksum-listed** `core-i18n/en` Turtle bz2 files.

## Availability (Prompt 23 metadata)

| Set | Count | Compressed bytes (HEAD) |
|---|---:|---:|
| Available core (checksum ∩ en) | 29 | 4584240026 |
| LHD extras (docs; not in core md5) | 2 | 85968575 |
| links/*.bz2 | 50 | 352950915 |
| **Available package total** | **81** | **5023159516** |
| Unavailable (checksum-listed, HEAD 404) | 33 | n/a |

Unavailable are primarily `labels|long_abstracts|short_abstracts_en_uris_*.ttl.bz2`.

## Serialization / graphs

- Core/LHD: **`.ttl.bz2`** selected (no `.tql.bz2` duplicates in package).
- Links: as published (mostly `.nt.bz2`, five `.ttl.bz2`) — unique datasets, not dual serializations of the same file.
- Default/named graphs historically used by Virtuoso: **UNKNOWN** (not stated on sparql resources page).
- Ontology `dbpedia_2016-10.owl` exists (HEAD size 2451743) but **not** in the four-bullet list → excluded pending 23B.

## Virtuoso / limits

Not executed. Historical endpoint limits referenced qualitatively on DBpedia page; not reproduced here.

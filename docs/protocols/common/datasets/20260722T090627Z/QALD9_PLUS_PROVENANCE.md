# QALD9_PLUS_PROVENANCE

**RUN_ID:** `20260722T090627Z` · OFFICIAL_AUTHOR_REPO_VERIFIED · REPOSITORY_COMMIT_PIN_VERIFIED

## Paper

- Título: QALD-9-plus… (ICSC 2022)
- DOI: 10.1109/ICSC52841.2022.00045 · arXiv: 2202.00120
- Evidencia: OFFICIAL_PAPER_VERIFIED (Crossref + arXiv Atom metadata)

## Authors repository

- https://github.com/Perevalov/qald_9_plus
- Pin: `8eb038a61e1bc09cbd21640aa667a1714f53cda4`
- LICENSE file: **CC BY 4.0** (`LICENSE_FILE_VERIFIED`)
- CITATION.cff: type dataset
- Releases/tags: none

## Data tree (metadata only)

| path | size_bytes | git_blob_oid |
|---|---:|---|
| data/qald_9_plus_train_dbpedia.json | 6371289 | cce48cbdf2af… |
| data/qald_9_plus_test_dbpedia.json | 1424744 | 06cc04be82be… |
| data/qald_9_plus_train_wikidata.json | 17241155 | a7325d0b195e… |
| data/qald_9_plus_test_wikidata.json | 8882491 | 357518c78607… |

Payload remoto: **no** adquirido.

## Conteos reportados (README)

| split | en | #questions DBpedia | #questions Wikidata |
|---|---:|---:|---:|
| Train | 408 | 408 | 371 |
| Test | 150 | 150 | 136 |

## Vista lógica: QALD9_PLUS_EN_DBPEDIA

| Campo | Valor |
|---|---|
| source_pin | `8eb038a61e1bc09cbd21640aa667a1714f53cda4` |
| train source | data/qald_9_plus_train_dbpedia.json |
| test source | data/qald_9_plus_test_dbpedia.json |
| language | en (selector sobre representación multilingual del archivo) |
| KG | DBpedia |
| reported counts | train 408 / test 150 (README) |
| test_sealed | true |
| payload_status | DATASET_PAYLOAD_NOT_ACQUIRED |
| question/sparql fields | documentados en paper/README; selectores exactos JSON **pending payload** |

## Graph / endpoint

Endpoints históricos GERBIL enlazados en README — **ENDPOINT_REPORTED_NOT_QUERIED**.  
Versión exacta DBpedia: **GRAPH_VERSION_NOT_SPECIFIED** / snapshot no publicado en el repo.

## Mirror HF

casey-martin/qald_9_plus — COMMUNITY_MIRROR / SECONDARY_REPRESENTATION; license card cc-by-4.0; parquet por idioma — **no** canónico.

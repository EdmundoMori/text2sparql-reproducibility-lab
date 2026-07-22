# LCQUAD2_PROVENANCE

**RUN_ID:** `20260722T090627Z` · OFFICIAL_AUTHOR_REPO_VERIFIED · REPOSITORY_COMMIT_PIN_VERIFIED

## Paper

- LC-QuAD 2.0… (ISWC 2019) · DOI 10.1007/978-3-030-30796-7_5
- OFFICIAL_PAPER_VERIFIED (Crossref)

## Authors repository

- https://github.com/AskNowQA/LC-QuAD2.0
- Pin HEAD: `0a5f8f85b6f863c3b80f0fa02839e25d438af3ae`
- README: "natural language queries with corresponding SPARQL queries for **Wikidata and Dbpedia2018**"
- LICENSE file en tree: **ausente** → LICENSE_SCOPE_UNCLEAR a nivel repo; HF card reporta cc-by-3.0 (**LICENSE_METADATA_REPORTED**, no LICENSE_FILE_VERIFIED del authors repo)
- Tags/releases: none
- Files: `dataset/train.json` (26561843 B), `dataset/test.json` (6578362 B)

## Representaciones

| ID | Clase | Nota |
|---|---|---|
| lcquad2_authors_repo | PRIMARY_SOURCE | pin `0a5f8f85b6f863c3b80f0fa02839e25d438af3ae` |
| lcquad2_hf_builder | SECONDARY_REPRESENTATION | mohnish/lc_quad; incluye data.zip (**no descargado**) |
| lcquad2_homepage | OFFICIAL_PROJECT_HOMEPAGE | lc-quad.sda.tech (metadata HTML si disponible) |
| lcquad2_sgpt_original | METHOD_LOCAL_DERIVATIVE | solo `sparql_wikidata`; splits train/val/test |
| lcquad2_sgpt_processed | METHOD_LOCAL_DERIVATIVE | + POS/dep features |

## Vistas lógicas

### LCQUAD2_DBPEDIA18

- KG label reportado: DBpedia2018 (README) → GRAPH_YEAR_REPORTED; release exacto **GRAPH_VERSION_NOT_SPECIFIED**
- Query field: pendiente de confirmar en payload (`sparql_dbpedia` u homólogo) — **no leído**
- Rol: candidato secundario del protocolo común DBpedia
- Conteos oficiales train/test: metadata size conocida; N registros **no** contados remotamente

### LCQUAD2_WIKIDATA

- Separada; no agregar con DBpedia18
- SGPT local observa train 21497 / val 2389 / test 5969 con campo `sparql_wikidata` — **no** sustituye split oficial authors (sin val oficial en tree)

Si al adquirir payload no se confirma separación de campos: `LCQUAD2_KG_VIEW_UNRESOLVED`.

## Claim

Results/HF/SGPT ≠ ejecución común. Payload authors **no** adquirido.

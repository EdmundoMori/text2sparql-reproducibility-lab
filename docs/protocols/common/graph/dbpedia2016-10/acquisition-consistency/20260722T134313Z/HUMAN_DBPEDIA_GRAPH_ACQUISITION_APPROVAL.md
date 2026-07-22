# Human authorization — DBpedia 2016-10 graph acquisition (Prompt 23C)

**RUN_ID (form package):** `20260722T134313Z`  
**Form status:** `APPROVED_CONSUMED_BY_PROMPT_24B`  
**authorization_id:** `AUTH_DBPEDIA2016_10_ACQ_20260722T134313Z_EMO_01`

## Package identity

| Campo | Valor |
|---|---|
| target graph ID | `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` |
| release | `2016-10` |
| canonical manifest | `configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_ENDPOINT_FILE_MANIFEST.yaml` |
| canonical manifest SHA-256 (file) | `3993dde79ece90062bc1303d9e0de3b0016ec6572ab1c1fc6491f9d1cff0bc6c` |
| canonical_scope_content_sha256 | `2dcbc4df0b4af368d797a36525d607dae809317310c8c35d70066c5275c454c7` |
| allowlist | `configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_GRAPH_NETWORK_ALLOWLIST.yaml` |
| allowlist file SHA-256 | `3a773f39b41f26f3ce1e077053c58c37c8f7fd6486f78303688b2ec9197067eb` |
| allowlist_content_sha256 (payload list) | `c51993149add578a71f6904a7ca575a8e60f8872b7845f45f32cb22dface167c` |
| validation report | `logs/dbpedia-acquisition-consistency/20260722T134313Z/package-static-validation.json` |
| validation report SHA-256 | `7690437868942ff1cae8eae6af60bf28b94ed82f9fecc5f8941e683b070bc15b` |
| exact file count | **114** |
| exact compressed bytes | **6925795437** |
| maximum payload bytes | **6995053391** |
| published MD5 | **112/114** |
| no MD5 | `instance_types_lhd_dbo_en.ttl.bz2`, `instance_types_lhd_ext_en.ttl.bz2` |
| post-download SHA-256 | **obligatorio** |
| destination | `workdir/graphs/dbpedia/2016-10/endpoint-equivalent/compressed/` |
| payload host | `downloads.dbpedia.org` |
| acquisition resources | FEASIBLE_CURRENT_DISK_CONDITIONAL_HUMAN_AUTHORIZATION |
| deployment resources | CONDITIONAL_HIGH_RISK (autorización separada) |

## AUTORIZABLE

- descargar exactamente 114 archivos del manifest
- verificar size/MD5 publicados
- calcular SHA-256 local
- almacenar compressed payload
- registrar logs/manifests

## NO AUTORIZABLE

- descomprimir / parsear RDF
- Virtuoso / Docker pull
- SPARQL / gold / métricas / adapters / benchmark

## Stop conditions

size/MD5 mismatch · URL fuera de allowlist · bytes > cap · archivo extra · redirect no allowlisted · intento de load · coste > 0

## Campos de autorización (cumplimentados)

- approver: EDMUNDO MORI ORRILLO
- date: 2026-07-22
- decision: APPROVED
- authorization_id: AUTH_DBPEDIA2016_10_ACQ_20260722T134313Z_EMO_01
- confirmation: CONFIRMED — single Prompt 24B attempt; consumed after PASS/FAIL/ABORT

## Consumo

- Ejecución autorizada: **Prompt 24B** (único intento)
- execution_run_id: `20260722T135601Z`
- consumption: autorizado al inicio del intento; estado final tras PASS/FAIL/ABORT

No reutilizar auth QALD. Esta autorización no es reutilizable tras el intento.

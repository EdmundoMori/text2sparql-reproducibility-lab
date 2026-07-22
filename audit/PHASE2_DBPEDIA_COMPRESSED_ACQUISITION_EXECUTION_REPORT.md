# PHASE2 — DBpedia 2016-10 compressed acquisition execution report

**Prompt:** 24B · **RUN_ID:** `20260722T135601Z` · **Cost:** 0.00  
**authorization_id:** `AUTH_DBPEDIA2016_10_ACQ_20260722T134313Z_EMO_01` · **CONSUMED_AFTER_PASS**  
**Gate:** `DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_COMPRESSED_ACQUISITION_PASS_VALIDATED`

## Resumen

Adquisición compressed-only de exactamente **114** archivos endpoint-equivalent DBpedia 2016-10.  
Bytes exactos **6925795437**. MD5 publicado verificado en **112/114**. SHA-256 local en **114/114**.  
Dos LHD sin MD5: size + SHA-256. Host único `downloads.dbpedia.org`.  
Payloads solo en `workdir/` (gitignore). Sin descompresión, RDF, Docker, Virtuoso ni SPARQL.

## Totales

| Métrica | Valor |
|---|---|
| files | 114 |
| bytes | 6925795437 |
| byte cap | 6995053391 |
| MD5 OK | 112 |
| SHA-256 | 114 |
| retries used (any file) | 0 (all attempt=1) |
| destination | `workdir/graphs/dbpedia/2016-10/endpoint-equivalent/compressed/` |
| git payloads | excluded |

## Evidencia

- result JSON: `logs/dbpedia-acquisition-execution/20260722T135601Z/acquisition-result.json`
- network log: `logs/dbpedia-acquisition-execution/20260722T135601Z/network.log`
- file matrix: `audit/PHASE2_DBPEDIA_COMPRESSED_ACQUISITION_FILE_MATRIX.csv`
- local manifest: `docs/protocols/common/graph/dbpedia2016-10/acquisition-execution/20260722T135601Z/acquisition_result_manifest.yaml`

## No realizado

descompresión · carga Virtuoso · SPARQL · gold · métricas · adapters · benchmark · common rebase

## Gates de fase

G4 runtime NOT_SATISFIED · G5 pending · G6I pending · adapters false · benchmark NOT_CURRENTLY_ELIGIBLE · QALD test SEALED

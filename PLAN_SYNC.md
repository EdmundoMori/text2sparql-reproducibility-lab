# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **23** — DBpedia graph target / acquisition package)  
**Fase:** 1 **cerrada** · 2 **graph target selected** · file scope **CONDITIONAL** · adquisición **pending auth**  
**SHA inicial 23:** `831f34b8aa488d17200a29ec9d04c76796adbbcf`  
**Graph RUN_ID:** `20260722T120239Z`  

> ZERO_COST. Gate `DBPEDIA_2016_10_NATIVE_GRAPH_TARGET_SELECTED_PACKAGE_CONDITIONAL_FILE_SCOPE`.  
> Primary: `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` (2016-10).  
> Fallback: `COMMON_GRAPH_REBASE`. Current endpoint rejected. Query subgraph rejected.  
> Available package: **81** files / **5023159516** bytes · **33** unavailable blockers.  
> Payload **NOT_ACQUIRED** · deployment **NOT_DEPLOYED** · human form **NOT_READY_CONDITIONAL**.  
> QALD ACQUIRED_VALIDATED · auth CONSUMED · test SEALED · LC-QuAD T6C HOLD.  
> G4 target documented / runtime **no** · G5 runtime **pending** · G6I **pending**. Adapters **false**. Benchmark **no**.  
> Siguiente: **Prompt 23B** (cerrar file scope). Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 23 — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T120239Z` |
| Gate | **DBPEDIA_2016_10_NATIVE_GRAPH_TARGET_SELECTED_PACKAGE_CONDITIONAL_FILE_SCOPE** |
| QALD lineage | `QALD9PLUS_DBPEDIA_LINEAGE_INFERRED_HIGH_CONFIDENCE` |
| Target | `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` / `2016-10` |
| Fallback | `COMMON_GRAPH_REBASE` |
| Serialization | ttl.bz2 core+LHD; links as published |
| Files / bytes | 81 / 5023159516 (available) |
| Checksums | PARTIAL MD5 |
| License | CC BY-SA 3.0 + GFDL evidence |
| Resource class | `CONDITIONAL_HIGH_RISK` |
| Acquisition / deployment | NOT_ACQUIRED / NOT_DEPLOYED |
| Coste | 0.00 · no RDF payload · no SPARQL · no Docker pull |

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_metric_adapter_and_legal_contracts_defined_pending_assets_implementation_and_benchmark (+ graph target preparatory) |
| PE6 | diagnostic_metric_observability_and_legal_boundaries_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

---

## 3. Metadata Prompt 22 (reconciliada)

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `3818db51b9468bc4b7b74b7b783a76c96d102b43` |
| publication metadata commit | `831f34b8aa488d17200a29ec9d04c76796adbbcf` |
| remote tip final post-22 | `831f34b8aa488d17200a29ec9d04c76796adbbcf` |

---

## 4. Siguiente prompt (único)

**Prompt 23B — Cierre documental del file scope endpoint-equivalent DBpedia 2016-10 (resolver 33 unavailable / ontology / core symlink resolution), ZERO_COST, sin descargar grafos ni ejecutar SPARQL.**

Acción: **CLOSE_DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_FILE_SCOPE**. **No ejecutado en 23.**

Reservado después: Prompt 24B adquisición controlada (solo tras scope cerrado + auth humana). Adquisición ≠ despliegue.

---

## 5. Registro Prompt 23

| Campo | Valor |
|---|---|
| commit inicial | `831f34b8aa488d17200a29ec9d04c76796adbbcf` |
| ARTIFACT_COMMIT | e24e36c2cc65692b981e7f1e7990d4bfcce496c7 |
| publication metadata commit | *(post-push tip; max 2 commits)* |
| push | pending |

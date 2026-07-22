# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **17** — dataset version & provenance)  
**Fase:** 1 **cerrada** · 2 **provenance documentada** (métricas/oracle pending)  
**SHA inicial 17:** `ba306d069910e3807bd211cc7416c1e88e637e86`  
**Provenance RUN_ID:** `20260722T090627Z`  
**Protocol RUN_ID (Prompt 16):** `20260722T083201Z`

> ZERO_COST. Gate `DATASET_PROVENANCE_DOCUMENTED_READY_FOR_METRIC_ORACLE_CONTRACT`. Adapters **false**. Benchmark **no**. Payload **no** adquirido. Graph snapshot **pending**. G4 **no** satisfecho. Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 17 — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T090627Z` |
| Gate | **DATASET_PROVENANCE_DOCUMENTED_READY_FOR_METRIC_ORACLE_CONTRACT** |
| Qualifiers | DATASET_PAYLOAD_NOT_ACQUIRED · GRAPH_SNAPSHOT_ACQUISITION_PENDING · LOCAL_SHA256_PENDING_CONTROLLED_ACQUISITION · G4_RUNTIME_PIN_NOT_SATISFIED |
| QALD pin | `8eb038a61e1bc09cbd21640aa667a1714f53cda4` (`CURRENT_SOURCE_SNAPSHOT_NOT_PUBLICATION_RELEASE`) |
| LC-QuAD pin | `0a5f8f85b6f863c3b80f0fa02839e25d438af3ae` (mismo qualifier) |
| Vistas | PRIMARY `QALD9_PLUS_EN_DBPEDIA` · SECONDARY `LCQUAD2_DBPEDIA18` · EXT `LCQUAD2_WIKIDATA` |
| Licencias | QALD LICENSE CC BY 4.0 verified · LC-QuAD authors `LICENSE_SCOPE_UNCLEAR` (HF card reported only) |
| Splits | train/test oficiales; test sellado; `DERIVED_DEV_SPEC_DEFINED_NOT_APPLIED` |
| Hash semantics | commit/tree/blob ≠ SHA-256; published file checksums NOT_PUBLISHED |
| Graph | year reported (LC-QuAD DBpedia2018) / version not specified (QALD); snapshot not published |
| Representaciones | authors · HF · mKGQAgent derivative · SGPT original/processed (no canónicos) |
| Adapters / benchmark | false / NOT_CURRENTLY_ELIGIBLE |
| Coste / ejecución | 0.00 / sin downloads / sin SPARQL |

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_framework_defined_pending_benchmark (+ preparatory provenance evidence) |
| PE6 | diagnostic_metric_framework_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

PE1–PE4 intactos (Fase 1 cerrada).

---

## 3. Metadata Prompt 16 (reconciliada)

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `ee3ae4a20c2243f3f432ef0097ad2bfcd4f46382` |
| publication metadata | `4a51e6a60833a1224651f4dc3c077baba79e4e18` |
| remote tip final post-16 | `ba306d069910e3807bd211cc7416c1e88e637e86` |

No tratar `4a51e6a…` como tip remoto final.

---

## 4. Siguiente prompt (único)

**Prompt 18 — Cierre documental del contrato de métricas, canonicalización de respuestas y SPARQL, oracle/grounding y análisis estadístico del protocolo común, ZERO_COST, sin implementar métricas ni ejecutar consultas.**

Fuente: `audit/NEXT_AFTER_DATASET_PROVENANCE_DECISION.md` (T3). **No ejecutado en 17.**

---

## 5. Registro Prompt 17

| Campo | Valor |
|---|---|
| commit inicial | `ba306d069910e3807bd211cc7416c1e88e637e86` |
| ARTIFACT_COMMIT | `4f642c2718b1a99244958ac31e9eef7d2c74f7cf` |
| publication metadata commit | `34e2d4589f1c19a5e58237399ef364f4a657ed56` |
| remote tip final post-17 | `2043b98d11cced9eb1f55485ec6614b873839f5f` |
| push | done |

# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **16** — common protocol framework)  
**Fase:** 1 **cerrada** · 2 **framework definido** (dataset provenance pending)  
**SHA inicial 16:** `df1ee9758e2b9f4bc78515dfa5f67f3af057d2ed`  
**Protocol RUN_ID:** `20260722T083201Z`

> ZERO_COST. Gate `COMMON_PROTOCOL_FRAMEWORK_DEFINED_READY_FOR_DATASET_PROVENANCE`. Adapters **false**. Benchmark **no**. Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 16 — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T083201Z` |
| Gate | **COMMON_PROTOCOL_FRAMEWORK_DEFINED_READY_FOR_DATASET_PROVENANCE** |
| Tracks IA | IA_Q_ONLY · IA_SCHEMA_COMMON · IA_ORACLE_GROUNDING · IA_FIXED_EXTERNAL_GROUNDING · IA_DOMAIN_NATIVE · IA_HISTORICAL |
| Datasets | PRIMARY QALD9_PLUS_EN_DBPEDIA · SECONDARY LCQUAD2 |
| Pins | DATASET_PIN_PENDING · GRAPH_SNAPSHOT_PENDING · METRIC_DETAIL_PENDING |
| Adapters / benchmark | false / NOT_CURRENTLY_ELIGIBLE |
| Coste / ejecución | 0.00 / ninguna |

Variantes clave: `sgpt_q` (IA_Q_ONLY) ≠ `sgpt_qk` (IA_ORACLE_GROUNDING).

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_framework_defined_pending_benchmark |
| PE6 | diagnostic_metric_framework_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

PE1–PE4 intactos (Fase 1 cerrada).

---

## 3. Metadata Prompt 15 (reconciliada)

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `9ceb112e7e8b157cb1961a24183cfea45abde07b` |
| publication metadata | `019e1771ee3d604e05799677b6477c3943370e7c` |
| remote tip final post-15 | `df1ee9758e2b9f4bc78515dfa5f67f3af057d2ed` |

---

## 4. Siguiente prompt (único)

**Prompt 17 — Cierre documental de versiones, licencias, archivos, splits, hashes y endpoint/graph provenance de QALD-9 Plus y LC-QuAD 2.0, ZERO_COST, sin descargar datasets ni ejecutar consultas.**

Fuente: `audit/NEXT_AFTER_COMMON_PROTOCOL_DECISION.md` (T2). **No ejecutado en 16.**

---

## 5. Registro Prompt 16

| Campo | Valor |
|---|---|
| commit inicial | `df1ee9758e2b9f4bc78515dfa5f67f3af057d2ed` |
| ARTIFACT_COMMIT | _(tras commit de evidencia; sin cadena recursiva)_ |
| push | pending |

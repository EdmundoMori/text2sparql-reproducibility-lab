# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **18** — metric/oracle/statistical contract)  
**Fase:** 1 **cerrada** · 2 **G5 documentary** (adapters contracts pending)  
**SHA inicial 18:** `dd6a01196d72589c1d0c304c959398df002e0aff`  
**Metric RUN_ID:** `20260722T093257Z`  
**metric_contract_version:** `0.1.0-documentary`

> ZERO_COST. Gate `METRIC_ORACLE_CONTRACT_DOCUMENTED_READY_FOR_ADAPTER_CONTRACTS`. Adapters **false**. Benchmark **no**. Implementación métricas **pending**. G4 **no**. G5 runtime **pending**. Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 18 — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T093257Z` |
| Gate | **METRIC_ORACLE_CONTRACT_DOCUMENTED_READY_FOR_ADAPTER_CONTRACTS** |
| Primarias | Answer P/R/F1 (macro) · Execution Exact Accuracy |
| Semantics | SET_OF_ROWS · valid empty≠no output · failures in denom |
| Canon | RDF_TERM_V1 · SPARQL_V1_CONSERVATIVE |
| Oracle / linking | ORACLE_CONTRACT_DEFINED · observable-only linking · sgpt_q≠sgpt_qk |
| Stats | bootstrap_seed 2026072201 · 10000 · Holm · within-track |
| Vectors | 36 · NOT_EXECUTED |
| G4 / G5 | not / documentary yes · runtime pending |
| Coste | 0.00 |

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_and_metric_contract_defined_pending_benchmark |
| PE6 | diagnostic_metric_contract_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

---

## 3. Metadata Prompt 17 (reconciliada)

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `4f642c2718b1a99244958ac31e9eef7d2c74f7cf` |
| publication metadata | `34e2d4589f1c19a5e58237399ef364f4a657ed56` · `2043b98d11cced9eb1f55485ec6614b873839f5f` · `dd6a01196d72589c1d0c304c959398df002e0aff` |
| remote tip final post-17 | `dd6a01196d72589c1d0c304c959398df002e0aff` |

(Corregido: tip real = `dd6a0119…`, no `2043b98d…`.)

---

## 4. Siguiente prompt (único)

**Prompt 19 — Definición documental de contratos de adapters externos por track, variante y método elegible, ZERO_COST, sin implementar adapters ni ejecutar métodos.**

Fuente: `audit/NEXT_AFTER_METRIC_ORACLE_CONTRACT_DECISION.md` (T4). **No ejecutado en 18.**

---

## 5. Registro Prompt 18

| Campo | Valor |
|---|---|
| commit inicial | `dd6a01196d72589c1d0c304c959398df002e0aff` |
| ARTIFACT_COMMIT | *(se registra tras commit)* |
| publication metadata commit | *(siguiente)* |
| push | pending |

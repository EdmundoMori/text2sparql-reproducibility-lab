# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt **14B** — GPT-2 + P2A)  
**Fase:** 1 — native audit; **abierta**  
**SHA inicial 14B:** `ba31ecfd82dff9bf57752305005e43a73a88a657`

> ZERO_COST. P1+P2A **PASS**. Sin forward P2B. Sin train. Auth 14B consumida.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 14B — resumen

| Campo | Valor |
|---|---|
| Execution RUN_ID | `20260721T135432Z` |
| Protocol RUN_ID | `20260721T134213Z` |
| Clasificación | **`Z3_P2A_MODEL_LOAD_PREFLIGHT_PASS`** |
| Gate | **`READY_FOR_Z3_ONE_STEP_TRAINING_AUTHORIZATION`** |
| GPT-2 | revision `607a30d7…` verificada |
| TBX / protobuf | 2.5.1 / 3.20.1 |
| Z3 image | `text2sparql-lab/sgpt-z3-py38:20260721T135432Z` |
| Expected steps | 1 |
| Forward / train | 0 |
| Coste | **0.00** |
| `reproduction_status` | `audit_only` |

Informe: `audit/sgpt/Z3_P2A_ARTIFACT_AND_MODEL_LOAD_REPORT.md`

---

## 3. Siguiente prompt (único)

Tras firma de training approval:

**Prompt 14C — Ejecución SGPT Z3 one-step reduced training smoke, ZERO_COST, sin Table 4.**

---

## 4. PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 5. Registro Prompt 14B

| Campo | Valor |
|---|---|
| commit inicial | `ba31ecfd82dff9bf57752305005e43a73a88a657` |
| ARTIFACT_COMMIT | f63a5dde8d53a6759078a4fe6e8649a371a554ec |
| FINAL_HEAD | f63a5dde8d53a6759078a4fe6e8649a371a554ec |
| push | done |

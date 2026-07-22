# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **15** — gate final Fase 1)  
**Fase:** 1 **cerrada** · 2 **protocol_definition_pending**  
**SHA inicial 15:** `220ecbee3a22287980be2bb4c9757681386fd01f`

> ZERO_COST. Gate `PHASE1_CLOSED_READY_FOR_COMMON_EVALUATION_PROTOCOL_DEFINITION` + `RESIDUAL_METHOD_BLOCKERS_PRESERVED`. Adapters **false**. Sin ejecución. Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 15 — resumen

| Campo | Valor |
|---|---|
| Gate | **`PHASE1_CLOSED_READY_FOR_COMMON_EVALUATION_PROTOCOL_DEFINITION`** |
| Qualifier | `RESIDUAL_METHOD_BLOCKERS_PRESERVED` |
| phase1_status | `closed` |
| phase2_status | `protocol_definition_pending` |
| Adapters | **false** |
| Coste / ejecución | **0.00** / ninguna |

### Seis métodos activos — outcomes

| method | reproduction_status | nac |
|---|---|---|
| sparql_llm | smoke_only | true |
| sgpt | smoke_only | true |
| mkgqagent | blocked | true |
| rdfconfig_llm | blocked | true |
| cot_sparql | blocked | true |
| firesparql | not_reproducible | true |

TeBaQA: `HISTORICAL_ONLY`.

### PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence |
| PE3 | not_started (`no_comparable_original_metric_run_available`) |
| PE4 | substantially_answered_for_current_portfolio |

Residual blockers: LICENSE (varios); COST online; MISSING_CHECKPOINT/TRAINER/RUNNER; HARDWARE; METRIC_AMBIGUITY; GOLD_GROUNDING.

---

## 3. Metadata Prompt 14D (corregida)

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `39bdc72411e692fcb8b1519c45ced775056f2a06` |
| publication metadata | `fa200879407fcc3e9a1735b84fcc2523c7097816` |
| publication metadata | `001511931c6d8f001b1b9db9e524fdbcf4294618` |
| remote tip final post-14D | `220ecbee3a22287980be2bb4c9757681386fd01f` |

**No usar** el SHA erróneo `…e729…` (typo); el artifact real es `…e692…`.

---

## 4. Siguiente prompt (único)

**Prompt 16 — Definición documental del protocolo común de evaluación Text-to-SPARQL por tracks, datasets, métricas y criterios de elegibilidad, ZERO_COST, sin implementar adapters ni ejecutar benchmarks.**

Fuente: `audit/NEXT_PHASE2_PROTOCOL_DECISION.md` (T1). **No ejecutado en 15.**

---

## 5. Registro Prompt 15

| Campo | Valor |
|---|---|
| commit inicial | `220ecbee3a22287980be2bb4c9757681386fd01f` |
| ARTIFACT_COMMIT | `9ceb112e7e8b157cb1961a24183cfea45abde07b` |
| publication metadata commit | `019e1771ee3d604e05799677b6477c3943370e7c` |
| push | done |

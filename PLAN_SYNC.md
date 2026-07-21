# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador) e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt **11C** — política coste cero + re-gate)  
**Fase:** 1 — native audit; **abierta**  
**SHA inicial 11C:** `60590cc000cc18c76c796ca7a4655c07c658ffda`

> Política: **MAX_EXTERNAL_MONETARY_COST_USD = 0.00**. Sin OpenRouter. Sin POST `/chat`.  
> Prompt 12 chat: **CANCELLED_BY_ZERO_COST_POLICY**.  
> Smoke ≠ PE3.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Metadata Prompt 11 (corrección)

| Campo | SHA |
|---|---|
| Prompt 11 **artifact commit** | `ee477c9d1d37b86d03593c141cd90577f7f1ba43` |
| Prompt 11 **final HEAD** | `a2478b721970444401bd7edae313e1e1aa81926e` |

No denominar el artifact commit como HEAD final.

---

## 3. Completado reciente

| # | Acto | Resultado |
|---|---|---|
| 11 | Modelo + cota | propuesta histórica; form **no firmado** |
| Interino | NO-GO económico | superseded por 11C |
| **11C** | Coste cero + re-gate | **`NO_GO_ECONOMIC_ZERO_COST_POLICY`**; **GO_NEXT_ZERO_COST = Z1 SGPT env** |

---

## 4. Prompt 11C — resumen

| Campo | Valor |
|---|---|
| Decisión humana | “elijo coste 0” — EDMUNDO MORI ORRILLO, 2026-07-21 |
| Gate online sparql_llm | **NO_GO_ECONOMIC_ZERO_COST_POLICY** |
| Prompt 12 chat | **cancelled/deferred indefinitely** |
| GO_NEXT_ZERO_COST | **SGPT_ENVIRONMENT_DEFINITION** (`sgpt`) |
| Coste externo | **$0.00** |
| PE2 online | `deferred_by_zero_cost_policy` |
| `reproduction_status` sparql_llm | `smoke_only` |
| `native_audit_complete` | `false` (todos) |
| `common_adapter_allowed` | `false` |

Artefactos: [`ZERO_COST_NATIVE_AUDIT_REGATE.md`](audit/ZERO_COST_NATIVE_AUDIT_REGATE.md) · [`NEXT_ZERO_COST_EXECUTION_DECISION.md`](audit/NEXT_ZERO_COST_EXECUTION_DECISION.md) · [`HUMAN_ZERO_COST_DECISION.md`](docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/HUMAN_ZERO_COST_DECISION.md)

---

## 5. Siguiente prompt (único)

**Prompt 12 — Definición documental de entorno SGPT (ZERO_COST; sin train; sin Table 4)**

No ejecutar en 11C. No chat smoke. No OpenRouter.

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 6. PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence (online deferred_by_zero_cost_policy) |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 7. Changelog

| Fecha | Cambio |
|---|---|
| 2026-07-21 | Prompt 11 artifact `ee477c9d` / HEAD `a2478b72` |
| 2026-07-21 | Prompt 11C ZERO_COST + GO_NEXT_ZERO_COST=SGPT env |

---

## 8. Registro Prompt 11C

| Campo | Valor |
|---|---|
| commit inicial | `60590cc000cc18c76c796ca7a4655c07c658ffda` |
| gate online | `NO_GO_ECONOMIC_ZERO_COST_POLICY` |
| GO_NEXT_ZERO_COST | `Z1` / `sgpt` |
| commit final | `32f597c006d95b5603bf2fc4f5c18f423df28ca8` |
| push | confirmado en origin/main |

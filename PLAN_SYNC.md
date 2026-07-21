# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador) e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt 11 — modelo, cota, gate humano)  
**Fase:** 1 — native audit; **abierta**  
**Commit inicial 11:** `df41c8c5ad7404c491cb0164dbba7be37b40a228`  
**RUN_ID:** `20260721T100618Z`

> Smoke ≠ PE3. Caché/índice en `workdir/` **no** van a Git. MCP público ≠ pin local.  
> Prompt 11: **0** inferencias; **no** POST `/chat`; autorización humana **pendiente**.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Completado reciente

| # | Prompt | Resultado |
|---|---|---|
| 5B | CORE_OFFLINE | `smoke_only` |
| 9 | Protocolo API/SIB | CONDITIONAL_GO → LOCAL_CHAT_API_ONE_QUESTION |
| 10 | Env agent + docs | index blocked (sin caché) |
| 10B | Download e5-large + index + preflight | `ENVIRONMENT_READY_INDEX_READY_PREFLIGHT_PASS` |
| **11** | Modelo + cota + gate humano | **`READY_FOR_HUMAN_APPROVAL`** |

---

## 3. Prompt 11 — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260721T100618Z` |
| Modelo seleccionado | `openrouter/openai/gpt-4o-mini-2024-07-18` |
| Slug OpenRouter | `openai/gpt-4o-mini-2024-07-18` |
| Precios (prompt/completion) | `1.5e-7` / `6e-7` USD/token |
| TWO_CALL_BOUND | ≈ **$0.0581** |
| MAX_OPENROUTER_USD propuesto | **$0.10** |
| Retries cliente | openai `max_retries=2` ⇒ ≤3 HTTP/logical; ≤6 total |
| Pregunta congelada | `How can I retrieve active site annotations in UniProt?` |
| Gate documental | **READY_FOR_HUMAN_APPROVAL** |
| Autorización humana | **PENDING** (`HUMAN_LLM_SMOKE_APPROVAL.md`) |
| Inferencias / POST /chat / SPARQL | **0 / 0 / 0** |
| `reproduction_status` | `smoke_only` |
| `native_audit_complete` | `false` |
| `common_adapter_allowed` | `false` |

Informe: [`audit/sparql_llm/LOCAL_CHAT_API_MODEL_BUDGET_FINAL_GATE_REPORT.md`](audit/sparql_llm/LOCAL_CHAT_API_MODEL_BUDGET_FINAL_GATE_REPORT.md)  
Gate dir: [`docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/`](docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/)

---

## 4. Siguiente paso

1. Investigador completa y responde con el bloque de `HUMAN_LLM_SMOKE_APPROVAL.md`.  
2. Tras firma + clave dedicada con límite $0.10: **Prompt 12 — Ejecución controlada de LOCAL_CHAT_API_ONE_QUESTION**.  
3. No redactar Prompt 12 hasta esa aprobación.

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 5. PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence (modelo/cota listos; smoke no ejecutado) |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 6. Changelog

| Fecha | Cambio |
|---|---|
| 2026-07-21 | Prompt 10 env ready; index blocked |
| 2026-07-21 | Prompt 10B cache+index+preflight pass; next=Prompt 11 |
| 2026-07-21 | Prompt 11 model+budget gate READY_FOR_HUMAN_APPROVAL; next=aprobación humana → Prompt 12 |

---

## 7. Registro Prompt 11

| Campo | Valor |
|---|---|
| commit inicial | `df41c8c5ad7404c491cb0164dbba7be37b40a228` |
| RUN_ID | `20260721T100618Z` |
| gate | `READY_FOR_HUMAN_APPROVAL` |
| commit final | _(se registra tras push)_ |
| push | _(pendiente)_ |

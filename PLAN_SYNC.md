# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador de prompts) y el investigador.  
**Repo GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt 10 — prep entorno agent + docs mínimos; índice bloqueado)  
**Fase lab:** 1 — native audit; **Fase 1 abierta**  
**Commit inicial 10:** `45605d47983961210679fdd8d6b39577eafee1ec`  
**RUN_ID:** `20260721T084637Z`

> Clonar ≠ ejecutar ≠ reproducir. Smoke ≠ PE3. MCP público ≠ pin local. Descarga embeddings ≠ autorizada sin opt-in.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → análisis de errores → transferencia Text-to-SQL → método nuevo → ablaciones.

| Documento | Ruta |
|---|---|
| Protocolo API/SIB | [`docs/protocols/sparql_llm/API_SIB_PROTOCOL.md`](docs/protocols/sparql_llm/API_SIB_PROTOCOL.md) |
| Prep report | [`audit/sparql_llm/LOCAL_CHAT_API_ENV_INDEX_PREP_REPORT.md`](audit/sparql_llm/LOCAL_CHAT_API_ENV_INDEX_PREP_REPORT.md) |
| Presupuesto | [`docs/protocols/sparql_llm/API_BUDGET_AND_SAFETY.md`](docs/protocols/sparql_llm/API_BUDGET_AND_SAFETY.md) |

---

## 2. Bucle

→ [`docs/plan-sync/PLANNER_LOOP.md`](docs/plan-sync/PLANNER_LOOP.md)

---

## 3. Completado

| # | Prompt | Resultado |
|---|---|---|
| 5B | CORE_OFFLINE Docker Py3.11 | `smoke_only` |
| 8 | Gate comparativo | GO_NEXT → protocolo |
| 9 | Protocolo API/SIB | CONDITIONAL_GO → `LOCAL_CHAT_API_ONE_QUESTION` |
| **10** | Prep agent + docs mínimos | **`ENVIRONMENT_READY_INDEX_BLOCKED_PENDING_EMBEDDING_DOWNLOAD_APPROVAL`** |

---

## 4. Prompt 10 — resumen

| Campo | Valor |
|---|---|
| Imagen | `text2sparql-lab/sparql-llm-agent-py311:20260721T084637Z` (`sha256:d51c8d45…`) |
| Base digest | `python@sha256:b18992999…` |
| Entorno | **ready** (`.[agent]`, sparql-llm 0.1.4) |
| Caché e5-large | **absent** — **0 descargas** |
| Documentos | **12** desde `void_uniprot.ttl` (`LAB_MINIMAL_INDEX`) |
| Índice Qdrant | **blocked** (sin caché) |
| Preflight `/chat` | **no ejecutado** |
| LLM calls | **0** |
| Endpoints SPARQL | **0** |
| POST `/chat` | **0** |
| Gate | sigue **CONDITIONAL_GO** (no promovido a GO) |
| `reproduction_status` | `smoke_only` |

Presupuesto actualizado: `MIN_EXPECTED_LLM_CALLS=2`; `MAX_LLM_CALLS=2` PROPOSED con `max_try_fix_sparql=0`; OpenRouter sin `max_tokens` enforceado; firma pendiente.

---

## 5. Siguiente prompt

**Prompt 10B — Descarga controlada y fijación de caché `intfloat/multilingual-e5-large` + construcción del índice mínimo** (requiere autorización explícita del investigador).

No ejecutar 10B sin opt-in. No POST `/chat` todavía.

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 6. PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 7. Índice

→ [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md)

---

## 8. Changelog

| Fecha | Cambio |
|---|---|
| 2026-07-20 | Prompt 9 protocolo API/SIB |
| 2026-07-21 | Prompt 10 env agent ready; docs 12; index blocked; next=10B |

---

## 9. Registro Prompt 10

| Campo | Valor |
|---|---|
| commit inicial | `45605d47983961210679fdd8d6b39577eafee1ec` |
| RUN_ID | `20260721T084637Z` |
| clasificación | `ENVIRONMENT_READY_INDEX_BLOCKED_PENDING_EMBEDDING_DOWNLOAD_APPROVAL` |
| commit final | `e646b557dd3a8432989a364c9dff506e7de776c2` |
| push | confirmado en origin/main |

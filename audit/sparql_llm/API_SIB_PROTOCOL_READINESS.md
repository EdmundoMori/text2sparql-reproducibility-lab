# API_SIB_PROTOCOL_READINESS — sparql_llm

**Fecha:** 2026-07-21 (Prompt 10B)  
**Pinned commit:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**RUN_ID env:** `20260721T084637Z`  
**RUN_ID index/preflight:** `20260721T092249Z`

---

## 1. Veredicto

| Campo | Valor |
|---|---|
| Protocolo API/SIB | **ready** |
| Entorno agent Py3.11 | **ready** |
| Documentos LAB_MINIMAL | **ready** (12) |
| Caché `intfloat/multilingual-e5-large` | **complete_exact_model_cache** |
| Índice mínimo | **INDEX_VERIFIED** |
| Preflight FastAPI | **pass** |
| Gate smoke online | **CONDITIONAL_GO** (presupuesto/modelo) |
| Clasificación 10B | `ENVIRONMENT_READY_INDEX_READY_PREFLIGHT_PASS` |
| `reproduction_status` | `smoke_only` |
| `native_audit_complete` | `false` |
| `common_adapter_allowed` | `false` |

---

## 2. Readiness

| Capacidad | Estado |
|---|---|
| `protocol_definition` | **ready** |
| `agent_environment_py311` | **ready** |
| `minimal_documents` | **ready** |
| `embedding_cache_exact` | **ready** |
| `lab_minimal_index` | **ready** |
| `local_chat_api` preflight | **ready** (startup) |
| `local_chat_api` smoke | **conditional** (clave+presupuesto+modelo) |
| `public_mcp_check` | **external_service_only** |
| TEXT2SPARQL_VIRTUOSO | **blocked** |

---

## 3. Bloqueadores restantes hacia GO de smoke

1. Firma presupuesto OpenRouter (`MAX_OPENROUTER_USD`).  
2. Selección de modelo exacto para 1 pregunta.  
3. `max_tokens` no enforceado en rama OpenRouter.  
4. Aprobación explícita para POST `/chat`.

---

## 4. Next prompt

`Prompt 11 — Cierre de presupuesto, selección de modelo y gate final para LOCAL_CHAT_API_ONE_QUESTION`

---

## 5. Informes

- `audit/sparql_llm/LOCAL_CHAT_API_ENV_INDEX_PREP_REPORT.md` (Prompt 10)  
- `audit/sparql_llm/LOCAL_CHAT_API_EMBEDDING_INDEX_PREFLIGHT_REPORT.md` (Prompt 10B)

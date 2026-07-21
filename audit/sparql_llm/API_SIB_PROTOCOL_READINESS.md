# API_SIB_PROTOCOL_READINESS — sparql_llm

**Fecha:** 2026-07-21 (Prompt 11)  
**Pinned commit:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**RUN_ID env:** `20260721T084637Z`  
**RUN_ID index/preflight:** `20260721T092249Z`  
**RUN_ID model-budget-gate:** `20260721T100618Z`

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
| selected_online_model | `openrouter/openai/gpt-4o-mini-2024-07-18` |
| model_selection_status | **SELECTED** (documental; PROPOSED hasta firma) |
| cost_bound_status | **COMPUTED** (TWO_CALL_BOUND ≈ $0.0581) |
| proposed_openrouter_limit_usd | **0.10** |
| client_retry_status | **INSPECTED** (max_retries=2; ≤6 HTTP attempts) |
| smoke_question_status | **FROZEN** |
| smoke_request_spec_status | **FROZEN** |
| human_llm_approval_status | **PENDING** |
| online_smoke_gate | **READY_FOR_HUMAN_APPROVAL** |
| api_smoke_ready | **conditional** |
| selected_future_online_action | `LOCAL_CHAT_API_ONE_QUESTION` |
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
| `model_budget_gate` | **ready_for_human_approval** |
| `local_chat_api` smoke | **blocked_pending_human_approval_and_key** |
| `public_mcp_check` | **external_service_only** |
| TEXT2SPARQL_VIRTUOSO | **blocked** |

---

## 3. Bloqueadores restantes hacia ejecución del smoke

1. Firma humana de `HUMAN_LLM_SMOKE_APPROVAL.md`.  
2. Clave OpenRouter dedicada con límite duro $0.10 verificada (solo metadata de clave; Prompt 11 no la crea).  
3. Revalidación de metadata/precios inmediatamente antes de Prompt 12.  
4. `max_tokens` sigue sin enforcearse en rama OpenRouter (mitigado por límite de clave).

---

## 4. Next prompt

Tras aprobación firmada + clave limitada:

`Prompt 12 — Ejecución controlada de LOCAL_CHAT_API_ONE_QUESTION`

Prompt 11 **no** ejecuta ni redacta Prompt 12.

---

## 5. Informes

- `audit/sparql_llm/LOCAL_CHAT_API_ENV_INDEX_PREP_REPORT.md` (Prompt 10)  
- `audit/sparql_llm/LOCAL_CHAT_API_EMBEDDING_INDEX_PREFLIGHT_REPORT.md` (Prompt 10B)  
- `audit/sparql_llm/LOCAL_CHAT_API_MODEL_BUDGET_FINAL_GATE_REPORT.md` (Prompt 11)  
- Gate: `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/FINAL_ONLINE_SMOKE_GATE.md`

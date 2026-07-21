# Presupuesto y seguridad API — SPARQL-LLM (futuro smoke)

**Estado:** modelo y cota **PROPOSED** — firma humana **pendiente** (`HUMAN_APPROVAL_PENDING`).  
**Commit pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Acción cubierta:** `LOCAL_CHAT_API_ONE_QUESTION`  
**Actualizado:** Prompt 11 (2026-07-21) — RUN_ID `20260721T100618Z`.  
**Inferencias Prompt 11:** 0.

---

## 1. Principios

1. Mínima red necesaria.  
2. Una sola acción futura seleccionada.  
3. Secretos solo en entorno local gitignored; nunca en git.  
4. No confundir disponibilidad de servicio público con reproducción nativa.  
5. Prompt 9/10/10B/11 **no** gastan presupuesto LLM (cero llamadas OpenRouter de inferencia).

---

## 2. Llamadas LLM por pregunta (`CODE_VERIFIED`)

Con `use_tools=false` (grafo default):

| # | Nodo | Evidencia |
|---|---|---|
| 1 | `extract_user_question` | `agent/nodes/llm_extraction.py` |
| 2 | `call_model` | `agent/nodes/call_model.py` |

**MIN_EXPECTED_LLM_CALLS_PER_QUESTION = 2** (`CODE_VERIFIED`).

### PROPOSED — techo para smoke L0

| Parámetro | Valor PROPOSED | Condiciones |
|---|---|---|
| `MAX_LLM_CALLS` (logical) | **2** | `use_tools=false` ∧ `default_max_try_fix_sparql=0` ∧ `enable_sparql_execution=false` |
| `possible_http_attempts` | **≤ 6** | openai 2.46.0 `max_retries=2` ⇒ ≤3 por invocación lógica |
| `default_max_try_fix_sparql` | **0** | Desviación vs upstream `3` |

**Distinción:** invocaciones lógicas ≠ intentos HTTP. No declarar `HTTP_ATTEMPTS_MAX=2` si hay retries.

---

## 3. Modelo propuesto (Prompt 11)

| Campo | Valor | Etiqueta |
|---|---|---|
| Modelo configuración | `openrouter/openai/gpt-4o-mini-2024-07-18` | PROPOSED / SELECTED documental |
| Slug OpenRouter | `openai/gpt-4o-mini-2024-07-18` | OFFICIAL_METADATA_VERIFIED |
| Snapshot RUN_ID | `20260721T100618Z` | |
| Snapshot timestamp | `2026-07-21T10:08:25Z` | |
| Catalog SHA-256 | `876ea047203ab02b48463bbd74e4578866981fe61bf5d7d9fd0959d2f6395628` | |
| prompt USD/token | `0.00000015` | OFFICIAL_METADATA_VERIFIED |
| completion USD/token | `0.0000006` | OFFICIAL_METADATA_VERIFIED |
| context_length | 128000 | |
| max_completion_tokens | 16384 | |
| TWO_CALL_BOUND | ≈ **$0.0581** | COST_BOUND_DERIVED |
| MAX_OPENROUTER_USD | **0.10** | PROPOSED |
| Estado | **HUMAN_APPROVAL_PENDING** | |

Artefactos: `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/`.

---

## 4. Límites de tokens — **no enforceados** (`CODE_VERIFIED`)

| Hecho | Evidencia |
|---|---|
| Body HTTP `max_tokens` / `temperature` **no** se pasan a `RunnableConfig.configurable` | `agent/main.py` |
| Request `validate_output` **no** mapea a `enable_output_validation` | mismatch de nombres |
| Rama OpenRouter en `load_chat_model` **no** pasa `max_tokens` a `ChatOpenAI` | `agent/utils.py` |

**Consecuencia:** la protección económica primaria es la **clave dedicada con límite duro**, no el body HTTP.

---

## 5. Defaults de retries (cliente resuelto)

| Campo | Valor |
|---|---|
| langchain-openai | 1.3.5 |
| openai | 2.46.0 |
| OpenAI root `max_retries` | **2** |
| ChatOpenAI Field `max_retries` | null (no override en rama OpenRouter) |

Detalle: `RESOLVED_CLIENT_DEFAULTS.md`.

---

## 6. Otros límites PROPOSED

| Parámetro | Valor PROPOSED |
|---|---|
| `MAX_QUESTIONS` | **1** |
| `MAX_LLM_MODELS` | **1** |
| `MAX_RUNS` | **1** |
| `enable_sparql_execution` | **false** |
| `use_tools` | **false** |
| `stream` | **false** |
| `TIMEOUT_CHAT_SECONDS` | **120** |
| Pregunta congelada | `How can I retrieve active site annotations in UniProt?` |

---

## 7. Clave dedicada (requerida; no creada en Prompt 11)

| Campo | Valor |
|---|---|
| Nombre sugerido | `text2sparql-lab-local-chat-smoke-2026-07-21` |
| Límite duro | **$0.10** (= MAX_OPENROUTER_USD propuesto) |
| Reset | sin reset si la UI lo permite |
| Expiración | 24–48 h preferible |
| Reutilizar clave personal | **prohibido** |
| Versionar clave | **prohibido** |
| Tras smoke | revocar/borrar |

---

## 8. Secretos

| Secreto | Almacenamiento | En git |
|---|---|---|
| `OPENROUTER_API_KEY` | local gitignored | nunca |
| Prompt 11 | **ninguna** clave usada | — |

---

## 9. Descarga de embeddings

Autorizada y ejecutada en Prompt 10B (Mori, 2026-07-21). Caché en workdir.

---

## 10. Criterios de aborto (futuro)

1. Superar `MAX_QUESTIONS` o techo lógico de LLM.  
2. SPARQL no intencional.  
3. Benchmark/biodata.  
4. MCP público como nativo.  
5. Gasto > límite de clave.  
6. Descarga embeddings sin autorización.

---

## 11. Registro de aprobación

| Campo | Valor |
|---|---|
| Aprobador | _pendiente_ |
| Fecha aprobación | _pendiente_ |
| `MAX_OPENROUTER_USD` aprobado | _pendiente_ (propuesto 0.10) |
| Modelo exacto aprobado | _pendiente_ (propuesto `openrouter/openai/gpt-4o-mini-2024-07-18`) |
| Descarga embeddings | **sí** (10B) |
| Gate documental Prompt 11 | **READY_FOR_HUMAN_APPROVAL** |
| Notas | Firma: `HUMAN_LLM_SMOKE_APPROVAL.md` — **no firmada** |

**Sin aprobación LLM firmada + clave limitada, el smoke permanece bloqueado.** Este documento **no** firma el presupuesto.

# Presupuesto y seguridad API — SPARQL-LLM (futuro smoke)

**Estado:** valores marcados `PROPOSED` — **requieren aprobación explícita del investigador** antes de cualquier llamada LLM o descarga.  
**Commit pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Acción cubierta:** `LOCAL_CHAT_API_ONE_QUESTION`  
**Actualizado:** Prompt 10 (2026-07-21) — evidencia de grafo LLM; presupuesto **sigue sin firmar**.

---

## 1. Principios

1. Mínima red necesaria.  
2. Una sola acción futura seleccionada.  
3. Secretos solo en entorno local gitignored; nunca en git.  
4. No confundir disponibilidad de servicio público con reproducción nativa.  
5. Prompt 9/10 **no** gastan presupuesto LLM (cero llamadas OpenRouter).

---

## 2. Llamadas LLM por pregunta (`CODE_VERIFIED`)

Con `use_tools=false` (grafo default):

| # | Nodo | Evidencia |
|---|---|---|
| 1 | `extract_user_question` | `agent/nodes/llm_extraction.py` — `load_chat_model(...).with_structured_output(...)` |
| 2 | `call_model` | `agent/nodes/call_model.py` — `load_chat_model(...).invoke(...)` |

**MIN_EXPECTED_LLM_CALLS_PER_QUESTION = 2** (`CODE_VERIFIED`).

Validación/repair puede añadir más llamadas vía `call_model` si `enable_output_validation` permanece True y hay errores ShEx (`CODE_VERIFIED` en `validation.py` + `graph.py`).

### PROPOSED — techo para smoke L0

| Parámetro | Valor PROPOSED | Condiciones |
|---|---|---|
| `MAX_LLM_CALLS` | **2** | Solo si `use_tools=false` **y** `default_max_try_fix_sparql=0` **y** `enable_sparql_execution=false` |
| `default_max_try_fix_sparql` | **0** | Desviación de seguridad vs default upstream `3` |
| Nota | Si `enable_output_validation` sigue en default True, un fallo de validación **no** puede reintentar cuando `max_try_fix_sparql=0` (ruta `max_tries_reached`) | `CODE_VERIFIED` / `INFERENCE` de `route_model_output` |

---

## 3. Límites de tokens — **no enforceados** (`CODE_VERIFIED`)

| Hecho | Evidencia |
|---|---|
| Body HTTP `max_tokens` / `temperature` **no** se pasan a `RunnableConfig.configurable` | `agent/main.py` |
| Request `validate_output` **no** mapea a `Configuration.enable_output_validation` | mismatch de nombres |
| Rama OpenRouter en `load_chat_model` **no** pasa `max_tokens` a `ChatOpenAI` | `agent/utils.py` |
| `Settings.default_max_tokens=512` en Settings mínimo lab | **no** constituye límite efectivo OpenRouter |

**Consecuencia:** `MAX_OUTPUT_TOKENS` **no** está técnicamente enforceado en el commit fijado.  
Este punto permanece como **bloqueador** antes de promover el gate a GO.  
`MAX_OPENROUTER_USD` sigue **TBD — investigador**.

---

## 4. Otros límites PROPOSED (aprobación pendiente)

| Parámetro | Valor PROPOSED | Justificación |
|---|---|---|
| `MAX_QUESTIONS` | **1** | Smoke PE2 mínimo |
| `MAX_LLM_MODELS` | **1** | Un solo modelo |
| `MAX_RUNS` | **1** | Una ejecución etiquetada |
| `enable_sparql_execution` | **false** | Omite `query_sparql` en agent (`CODE_VERIFIED`) |
| `use_tools` | **false** | Grafo default |
| `stream` | **false** | JSON auditable |
| `MAX_ENDPOINTS_IN_SETTINGS` | **1** (UniProt + void local) | Índice mínimo |
| `FORCE_INDEX` / `AUTO_INIT` | **false** | Evitar `init_vectordb` amplio |
| `ALLOW_PUBLIC_MCP_AS_NATIVE` | **false** | Solo availability check |
| `ALLOW_BENCHMARK_SCRIPTS` | **false** en L0 | Separado |
| `MAX_OPENROUTER_USD` | **TBD — investigador** | Sin firma = no smoke |
| `TIMEOUT_CHAT_SECONDS` | **120** (PROPOSED) | Evitar hang |
| `LOG_REDACTION` | obligatorio | Keys / Authorization |

---

## 5. Secretos y manejo

| Secreto | Almacenamiento | Exposición en artefactos |
|---|---|---|
| `OPENROUTER_API_KEY` | `.env` local / secret store | `[REDACTED]` |
| `CHAT_API_KEY` | opcional | `[REDACTED]` |
| `LOGS_API_KEY` | no necesario L0 | n/a |

Prompt 10: **ninguna** clave usada; variables eliminadas del entorno de contenedores.

---

## 6. Descarga de embeddings

- Modelo exacto: `intfloat/multilingual-e5-large`.  
- **Prompt 10B autorizado y ejecutado** (aprobador: EDMUNDO MORI ORRILLO, 2026-07-21).  
- Caché: `complete_exact_model_cache` en workdir (gitignored).  
- Procedencia registrada en `logs/preparation/sparql-llm-embedding-index/20260721T092249Z/embedding-download.json`.

---

## 7. Criterios de aborto de seguridad (futuro)

Abortar inmediatamente si:

1. Se supera `MAX_QUESTIONS` o `MAX_LLM_CALLS`.  
2. Se detecta ejecución SPARQL no intencional.  
3. Se inicia biodata/benchmark completo.  
4. Se usa MCP público como evidencia nativa.  
5. El gasto estimado supera `MAX_OPENROUTER_USD`.  
6. Se intenta descargar embeddings sin autorización.

---

## 8. Registro de aprobación

| Campo | Valor |
|---|---|
| Aprobador | _pendiente_ |
| Fecha aprobación | _pendiente_ |
| `MAX_OPENROUTER_USD` aprobado | _pendiente_ |
| Modelo exacto aprobado | _pendiente_ |
| Descarga embeddings aprobada | **sí** (Prompt 10B; Mori 2026-07-21) |
| Notas | Gate: **CONDITIONAL_GO**; índice+preflight ready; falta firma LLM |

**Sin aprobación LLM, el smoke permanece bloqueado.** Este documento **no** firma el presupuesto OpenRouter.

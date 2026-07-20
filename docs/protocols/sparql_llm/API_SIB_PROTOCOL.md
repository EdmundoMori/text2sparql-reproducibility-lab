# Protocolo API/SIB — SPARQL-LLM (Prompt 9)

**Fecha:** 2026-07-20  
**Tipo:** `protocol_definition` (documental; sin llamadas, sin installs, sin imports ejecutados)  
**method_id:** `sparql_llm`  
**Pinned commit upstream:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Lab HEAD al inicio del Prompt 9:** `3d89a8d61f3fed8eecec8e49f6b79baccf677a76`  
**Etiquetas de evidencia:** `CODE_VERIFIED` | `README_REPORTED` | `EXECUTION_VERIFIED` | `INFERENCE` | `PROPOSED`

---

## 1. Identificación y commits

| Campo | Valor | Evidencia |
|---|---|---|
| Repositorio | `upstream/sparql_llm` (sib-swiss/sparql-llm) | `CODE_VERIFIED` |
| Commit anclado | `3748730e3bd2df2595280b918269fdaadb9fc0c3` | `REPOSITORIES.lock.yaml`; `.git_local` HEAD |
| Licencia | MIT (`LICENSE.txt`) | `LEGAL_VERIFIED` |
| Paquete | `sparql-llm` | `CODE_VERIFIED` `pyproject.toml` |
| Smoke previo | CORE_OFFLINE Docker Py3.11 → `smoke_only` (5B) | `EXECUTION_VERIFIED` |
| Host Py3.10 | `setup_failed` (5A; `typing.Required`) | `EXECUTION_VERIFIED` |

---

## 2. Alcance y no-alcance de este protocolo

**Incluye:** superficies Chat API local (`/chat`), MCP (local y público), contratos request/response observables en código, matrices de configuración/red/side-effects, protocolo documental de benchmarks SIB, candidatos de smoke futuro, presupuesto/seguridad, gate GO/NO-GO.

**Excluye (Prompt 9):** installs; imports ejecutados de upstream; llamadas OpenRouter/OpenAI; llamadas a endpoints SPARQL; Docker nuevo; descarga FastEmbed; init Qdrant; ejecución de benchmarks; Virtuoso/TEXT2SPARQL; adapters; evaluación común; cambio de `reproduction_status`.

---

## 3. Etiquetas de evidencia (obligatorias)

| Etiqueta | Uso |
|---|---|
| `CODE_VERIFIED` | Afirmación leída en el commit anclado |
| `README_REPORTED` | Afirmación del README/upstream docs |
| `EXECUTION_VERIFIED` | Resultado de smoke/lab previo (5A/5B) |
| `INFERENCE` | Conclusión operativa a partir de hechos etiquetados |
| `PROPOSED` | Valor de política/lab que requiere aprobación |

---

## 4. Estado de reproducción (inmutable en Prompt 9)

| Campo | Valor exigido | Evidencia |
|---|---|---|
| `reproduction_status` | `smoke_only` | `METHOD_REGISTRY.yaml` |
| `native_audit_complete` | `false` | registry |
| `common_adapter_allowed` | `false` | registry |
| PE3 / `partially_reproduced` | **no declarar** | `INFERENCE` (stop condition) |

---

## 5. Superficies de ejecución (resumen)

Ocho superficies catalogadas en `EXECUTION_SURFACES.csv`. Las relevantes para el camino nativo condicional son:

1. **LOCAL_CHAT_API** — FastAPI `POST /chat` + LangGraph (`agent/main.py`) — **acción futura seleccionada**.  
2. **LOCAL_MCP_STDIO / LOCAL_MCP_HTTP** — `mcp_server.cli` — nativo pero con side-effects de índice/embeddings.  
3. **PUBLIC_MCP_REMOTE** — `https://chat.expasy.org/mcp` — **no es ejecución nativa**; solo `external_service_availability_check`.  
4. Benchmarks / Compose / UI — documentales o aplazados.

---

## 6. Acción futura seleccionada (única)

**Selected future action:** `LOCAL_CHAT_API_ONE_QUESTION`

**Justificación (`INFERENCE` + `CODE_VERIFIED`):**

- Ejecuta el código anclado vía FastAPI `/chat` + LangGraph (`agent/main.py`).  
- Aporta mejor evidencia PE2 que el MCP público (remoto ≠ commit pin).  
- `enable_sparql_execution` puede fijarse a `false` para reducir red SPARQL (`CODE_VERIFIED` en `validation.py`; biodata usa `False` en `/chat`).

Exactamente **una** acción futura seleccionada; el resto queda catalogado como no seleccionado en `FUTURE_SMOKE_CANDIDATES.csv` y `FUTURE_API_SMOKE_GONOGO.md`.

---

## 7. Gate: CONDITIONAL_GO

**Gate:** `CONDITIONAL_GO` (no `GO`, no `NO_GO`).

Bloqueadores que impiden `GO` inmediato (detalle en §23 y `FUTURE_API_SMOKE_GONOGO.md`):

1. Runtime Python 3.11 (patrón Docker 5B; host 3.10 incompatible).  
2. Ruta o URL Qdrant (`vectordb_url`).  
3. Descarga FastEmbed `intfloat/multilingual-e5-large`.  
4. `init_vectordb` o índice preconstruido.  
5. `OPENROUTER_API_KEY`.  
6. `SETTINGS` mínimo (p. ej. UniProt con `void_file` local).  
7. Aprobación de presupuesto del investigador (`API_BUDGET_AND_SAFETY.md`).

---

## 8. Contrato Chat API (resumen; ver `CHAT_API_CONTRACT.md`)

Fuente: `src/sparql_llm/agent/main.py` (`CODE_VERIFIED`).

| Elemento | Hecho |
|---|---|
| Ruta | `POST /chat` |
| Modelo request | `ChatCompletionRequest`: `messages`, `model`, `max_tokens`, `temperature`, `stream`, `validate_output`, `enable_sparql_execution`, `headers`, `session_id` |
| Auth | Bearer `CHAT_API_KEY` si `settings.chat_api_key` no vacío |
| Configurable pasado a LangGraph | **solo** `model`, `validate_output`, `enable_sparql_execution` |
| `max_tokens` / `temperature` en request | **no** se pasan a `RunnableConfig.configurable` |
| Mensajes | `messages[-10:]` |
| `recursion_limit` | `25` |
| Stream | SSE (`text/event-stream`) vs JSON no-stream |
| MCP mount | `/mcp` streamable HTTP |
| Side-effect import | `mcp = get_mcp_app()` a nivel de módulo |

**Mismatch CODE_VERIFIED:** dataclass `Configuration` usa `enable_output_validation`, no `validate_output`. `from_runnable_config` solo acepta nombres de campo coincidentes → el request `validate_output` queda **ignorado** (campo no matching). Documentado como unused/mismatched.

---

## 9. Contrato MCP (resumen; ver `MCP_CONTRACT.md`)

Fuente: `src/sparql_llm/mcp_server.py` (`CODE_VERIFIED`).

| Elemento | Hecho |
|---|---|
| Nombre FastMCP | `"{org} MCP"` (`settings.app_org`) |
| `streamable_http_path` | `"/"` |
| Flags | `json_response=True`, `stateless_http=True` |
| Tools | `search_sparql_docs`, `get_classes_schema`, `get_resources_info` (opcional), `execute_sparql_query` |
| Resource | `examples://{question}` |
| Execute | validate → `query_sparql` timeout=10 post=True; vacío → `FIX_QUERY_PROMPT`; resultados cap 50 |
| CLI | `--http` streamable-http puerto 8888; stdio por defecto |
| Anomalía CLI | rama `--http` llama `mcp.run()` y luego asigna puerto y vuelve a `run` |

Imports a nivel de módulo desde `index_resources` (embedding, qdrant, metadata). `auto_init` puede llamar `init_vectordb` en `get_mcp_app()`.

---

## 10. Proveedores de modelo (resumen; ver `MODEL_PROVIDER_MATRIX.csv`)

Fuente: `agent/utils.py` `load_chat_model` (`CODE_VERIFIED`).

| Rama | Comportamiento |
|---|---|
| `provider == "openrouter"` | `ChatOpenAI` `base_url=https://openrouter.ai/api/v1`, `OPENROUTER_API_KEY`, `temperature`+`seed` desde `Configuration`; **`max_tokens` NO se pasa** |
| else | `init_chat_model` con `max_tokens`, `temperature`, `seed`, `max_retries=2`, `timeout=None` |

Default Settings: `openrouter/openai/gpt-5.2` (`CODE_VERIFIED` `config.py`).

---

## 11. Settings por defecto (resumen; ver `CONFIGURATION_MATRIX.csv`)

Fuente: `config.py` `Settings` (`CODE_VERIFIED`).

| Clave | Default |
|---|---|
| `vectordb_url` | `data/vectordb` (path local) |
| `embedding_model` | `intfloat/multilingual-e5-large` |
| `sparse_embedding_model` | `Qdrant/bm25` |
| `auto_init` | `True` |
| `force_index` | `False` |
| `default_llm_model` | `openrouter/openai/gpt-5.2` |
| `default_number_of_retrieved_docs` | `10` |
| `default_max_try_fix_sparql` | `3` |
| `default_temperature` | `0.0` |
| `default_max_tokens` | `16384` |
| `default_seed` | `42` |
| `app_public_host` | `chat.expasy.org` |
| UniProt | `void_file: ./tests/void_uniprot.ttl` + endpoint remoto |
| `SETTINGS_FILEPATH` | env → carga JSON `Settings.from_file` |

Muchos endpoints SIB en la lista por defecto (UniProt, Bgee, OMA, HAMAP, SwissLipids, Rhea, Cellosaurus, OrthoDB, METRIN-KG, MetaNetX, SIBiLS).

---

## 12. Configuration runtime y mismatch de nombres

Fuente: `Configuration` + `from_runnable_config` (`CODE_VERIFIED` `config.py`).

Campos relevantes: `enable_entities_resolution`, `enable_output_validation`, `enable_sparql_execution`, `system_prompt`, `model`, `temperature`, `max_tokens`, `seed`, `search_kwargs`, `max_try_fix_sparql`.

Filtro: `_fields = {f.name for f in fields(cls) if f.init}`; solo claves presentes en `_fields` se aplican.

**Consecuencia operativa (`CODE_VERIFIED` + `INFERENCE`):** el flag HTTP `validate_output` **no** controla la validación; el default `enable_output_validation=True` permanece salvo que se pase el nombre correcto en `configurable` (hoy el Chat API no lo hace).

---

## 13. Grafo LangGraph por defecto (`use_tools=False`)

Fuente: `agent/graph.py` (`CODE_VERIFIED`).

Camino default:

`extract_user_question` → `retrieve` → `call_model` → `validate_output` → arista condicional (`route_model_output`) → repair loop hasta `max_try_fix_sparql` o `__end__` / `max_tries_reached`.

Si `settings.use_tools=True`: camino experimental con nodo `tools` / MCP (no es el default).

---

## 14. Validación y ejecución SPARQL en el agent path

Fuente: `agent/nodes/validation.py` (`CODE_VERIFIED`).

1. Gate `enable_output_validation`: si False → return `{}`.  
2. Validación de queries en el mensaje vía `validate_sparql_in_msg`.  
3. Si query válida y `enable_sparql_execution` y `not settings.use_tools` → `query_sparql` (timeout=10, post=False).  
4. **`enable_sparql_execution=false` omite la ejecución SPARQL en el agent path** (`CODE_VERIFIED`).

Recomendación de smoke futuro: `enable_sparql_execution=false` para acotar red (`INFERENCE`; alineado con biodata).

---

## 15. Indexación y side-effects de import

Fuente: `indexing/index_resources.py` (`CODE_VERIFIED`).

| Side-effect | Cuándo |
|---|---|
| `TextEmbedding(...)` | **import-time** → riesgo de descarga del modelo |
| `QdrantClient(path=...)` o `url=...` | **import-time** |
| `EndpointsMetadataManager(..., auto_init)` | módulo; lazy metadata según auto_init |
| Scraping `homepage_url` via httpx | al indexar / cargar descripciones schema.org |
| `get_mcp_app()` / import `agent.main` | chequeo colección + posible `init_vectordb` |

Implicación: arrancar Chat API o MCP **no es offline-puro** si el índice no está preconstruido (`INFERENCE`).

---

## 16. Frontera offline vs online

Ver `OFFLINE_ONLINE_BOUNDARY.md`.

| Capa | Estado lab |
|---|---|
| CORE_OFFLINE (validate/loaders locales) | `smoke_only` EXECUTION_VERIFIED (5B) |
| Índice + embeddings | online o prebuild; no ejecutado en Prompt 9 |
| LLM OpenRouter | online; requiere clave |
| Endpoints SPARQL SIB | online; opcionalmente desactivables en agent path |
| MCP público | servicio externo ≠ pin |

---

## 17. Autenticación y secretos (nombres, no valores)

| Nombre | Rol | Evidencia |
|---|---|---|
| `OPENROUTER_API_KEY` | LLM rama openrouter | `CODE_VERIFIED` `utils.py` |
| `CHAT_API_KEY` / `settings.chat_api_key` | Bearer en `/chat` si seteado | `CODE_VERIFIED` `main.py` |
| `LOGS_API_KEY` | `/logs` | `CODE_VERIFIED` |
| `SETTINGS_FILEPATH` | JSON Settings | `CODE_VERIFIED` `config.py`; `README_REPORTED` |
| `LANGFUSE_*` | tracing opcional | `CODE_VERIFIED` |
| `SENTRY_URL` | errores opcionales | `CODE_VERIFIED` |

**Política:** nunca versionar secretos; ejemplos ficticios con `[REDACTED]` en `CHAT_API_CONTRACT.md`.

---

## 18. Benchmarks SIB (solo protocolo documental)

Ver `SIB_BENCHMARK_PROTOCOL.md`. **No ejecutar** en Prompt 9.

- `tests/benchmark.py`: lista hand-curated `example_queries`; `load_chat_model` y/o httpx; logs en `data/benchmarks`.  
- `tests/benchmark_biodata.py`: UniProt/Bgee/Cellosaurus; KFold 3-fold `random_state=42`; modelos openrouter; POST `localhost:8000/chat` con `validate_output=True`, `enable_sparql_execution=False`; SPARQL se ejecuta aparte; `pytrec_eval` `set_P`/`set_recall`/`set_F`; cache `data/biodata_ref_results_cache.json`; `LIMIT_FOR_DEV=None`.

Tres niveles documentados: L0 smoke 1 pregunta; L1 manual reducido; L2 biodata (aplazado).

---

## 19. Candidatos de smoke futuro (A–F)

Ver `FUTURE_SMOKE_CANDIDATES.csv`. Seleccionado: **D = LOCAL_CHAT_API_ONE_QUESTION** (`CONDITIONAL_GO`).

---

## 20. Presupuesto y seguridad

Ver `API_BUDGET_AND_SAFETY.md`. Valores `PROPOSED` (p. ej. `MAX_QUESTIONS=1`) requieren aprobación del investigador antes de cualquier smoke.

---

## 21. Criterios de éxito y fallo (futuro smoke LOCAL_CHAT_API)

**Éxito mínimo propuesto (`PROPOSED`):**

1. Servidor local arranca sobre código pin `3748730…`.  
2. Una sola pregunta vía `POST /chat` con `enable_sparql_execution=false`.  
3. Respuesta JSON/SSE no vacía; log de pregunta registrado.  
4. Sin ejecución SPARQL en agent path (confirmado por config).  
5. Artefactos de experimento con manifest + deviations.

**Fallo:**

- Import/init descarga o indexación descontrolada sin preaprobación.  
- Más de `MAX_QUESTIONS` llamadas LLM.  
- Uso de MCP público como “nativo”.  
- Declarar PE3 / cambiar `reproduction_status`.

---

## 22. Checklist GO/NO-GO hacia el smoke (sin ejecutarlo)

Ver sección operativa en `FUTURE_API_SMOKE_GONOGO.md`. Resumen:

| Ítem | Estado Prompt 9 |
|---|---|
| Protocolo documental completo | **sí** (este paquete) |
| Runtime Py3.11 listo | pendiente (patrón 5B) |
| Índice mínimo / Qdrant | pendiente |
| FastEmbed disponible o cacheado | pendiente |
| `OPENROUTER_API_KEY` en entorno aislado | pendiente |
| SETTINGS mínimo UniProt void local | pendiente |
| Presupuesto aprobado | pendiente |
| Gate | **CONDITIONAL_GO** |

---

## 23. Bloqueadores CONDITIONAL (detalle)

| # | Bloqueador | Mitigación prevista (Prompt 10+) |
|---|---|---|
| B1 | Python 3.11 runtime | Reutilizar patrón Docker 5B / env Py3.11 |
| B2 | Qdrant path o URL | `data/vectordb` local o servicio |
| B3 | FastEmbed `multilingual-e5-large` | descarga controlada o cache preaprobada |
| B4 | `init_vectordb` o índice prebuilt | init mínimo o artefacto preindexado |
| B5 | `OPENROUTER_API_KEY` | secret local gitignored |
| B6 | SETTINGS endpoints mínimos | UniProt + `./tests/void_uniprot.ttl` |
| B7 | Aprobación presupuesto | firmar `API_BUDGET_AND_SAFETY.md` |

---

## 24. Próximo prompt (título exacto)

`Prompt 10 — Preparación de entorno e índice mínimo para smoke LOCAL_CHAT_API de SPARQL-LLM (sin llamadas LLM)`

Alcance esperado: entorno + índice mínimo **sin** llamadas LLM; no ejecutar aún el smoke de una pregunta salvo que un prompt posterior lo autorice tras gate.

---

## 25. Stop conditions (Prompt 9 y siguientes inmediatos)

- Cualquier llamada real a OpenRouter/OpenAI/SIB/MCP público en Prompt 9.  
- Installs, Docker nuevos no documentados, downloads no aprobados.  
- Modificar `upstream/`.  
- Abrir adapters / evaluación común.  
- Cambiar `reproduction_status`, `native_audit_complete`, `common_adapter_allowed`.  
- Seleccionar una segunda future action en paralelo.  
- Tratar `PUBLIC_MCP_REMOTE` como ejecución nativa.

---

## 26. Inventario de artefactos del protocolo

| # | Path |
|---|---|
| 1 | `docs/protocols/sparql_llm/API_SIB_PROTOCOL.md` (este documento) |
| 2 | `docs/protocols/sparql_llm/EXECUTION_SURFACES.csv` |
| 3 | `docs/protocols/sparql_llm/MCP_CONTRACT.md` |
| 4 | `docs/protocols/sparql_llm/CHAT_API_CONTRACT.md` |
| 5 | `docs/protocols/sparql_llm/MODEL_PROVIDER_MATRIX.csv` |
| 6 | `docs/protocols/sparql_llm/CONFIGURATION_MATRIX.csv` |
| 7 | `docs/protocols/sparql_llm/NETWORK_AND_SIDE_EFFECT_MATRIX.csv` |
| 8 | `docs/protocols/sparql_llm/OFFLINE_ONLINE_BOUNDARY.md` |
| 9 | `docs/protocols/sparql_llm/SIB_BENCHMARK_PROTOCOL.md` |
| 10 | `docs/protocols/sparql_llm/FUTURE_SMOKE_CANDIDATES.csv` |
| 11 | `docs/protocols/sparql_llm/API_BUDGET_AND_SAFETY.md` |
| 12 | `docs/protocols/sparql_llm/FUTURE_API_SMOKE_GONOGO.md` |
| 13 | `audit/sparql_llm/API_SIB_PROTOCOL_READINESS.md` |
| 14 | `logs/sparql-llm-api-sib-protocol/commands.log` |

Cumple los 6 mínimos de `audit/NEXT_EXECUTION_DECISION.md` §10.
`)
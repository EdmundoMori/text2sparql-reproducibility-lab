# Contrato Chat API — SPARQL-LLM

**Commit pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Fuente:** `src/sparql_llm/agent/main.py` (+ `config.py` Configuration)  
**Etiquetas:** `CODE_VERIFIED` salvo donde se indique.  
**Secretos:** ejemplos ficticios; valores `[REDACTED]`.

---

## 1. App FastAPI

| Elemento | Valor |
|---|---|
| Título | `settings.app_name` (default `ExpasyGPT`) |
| Mount MCP | `app.mount("/mcp", mcp.streamable_http_app())` |
| CORS | `allow_origins=["*"]` |
| Lifespan | `mcp.session_manager.run()` |
| UI | `GET /` Jinja2 `webapp/index.html` |
| Feedback | `POST /feedback` |
| Logs admin | `POST /logs` (clave `logs_api_key`) |

**Side-effect de import (`CODE_VERIFIED`):** `mcp = get_mcp_app()` a nivel de módulo → chequeo/auto_init de índice al importar `agent.main`.

---

## 2. `ChatCompletionRequest` (campos)

| Campo | Tipo / default | ¿Se usa en RunnableConfig? | Notas |
|---|---|---|---|
| `messages` | `list[Message]` | inputs (últimos 10) | obligatorio no vacío |
| `model` | default `settings.default_llm_model` | **sí** → `configurable.model` | |
| `max_tokens` | default `16384` | **NO** | no entra en `configurable` |
| `temperature` | default `0.0` | **NO** | no entra en `configurable` |
| `stream` | `False` | controla SSE vs JSON | |
| `validate_output` | `True` | pasado como `validate_output` | **mismatched / ignored** por Configuration |
| `enable_sparql_execution` | `True` | **sí** | nombre coincide |
| `headers` | `{}` | no usado en handler | campo presente, sin uso visible |
| `session_id` | `None` | metadata Langfuse | |

---

## 3. Auth Bearer

Si `settings.chat_api_key` está seteado:

1. Header `Authorization` debe existir y empezar por `Bearer `.  
2. Token tras el espacio debe igualar `settings.chat_api_key`.  
3. En caso contrario: `ValueError` (missing/invalid).

Si `chat_api_key` vacío: no se exige Bearer (`CODE_VERIFIED`).

Ejemplo ficticio (no real):

```http
Authorization: Bearer [REDACTED_CHAT_API_KEY]
```

---

## 4. RunnableConfig construido

```text
configurable = {
  model,
  validate_output,           # nombre HTTP
  enable_sparql_execution,
}
recursion_limit = 25
callbacks = langfuse_handler si LANGFUSE_SECRET_KEY
metadata.langfuse_session_id si session_id
```

**NO se pasan:** `max_tokens`, `temperature`, `seed`, `enable_output_validation`.

Inputs:

```text
messages = [(role, content) for msg in messages[-10:]]
```

---

## 5. Mismatch `validate_output` vs `enable_output_validation` (CODE_VERIFIED)

| Capa | Nombre |
|---|---|
| Request HTTP / ChatCompletionRequest | `validate_output` |
| Dataclass `Configuration` | `enable_output_validation` |
| `from_runnable_config` | solo claves ∈ nombres de campos |

**Conclusión CODE_VERIFIED:** el valor `validate_output` del request **no** se aplica a `Configuration`. La validación queda en el default del dataclass (`True`) salvo otro mecanismo. Documentar como **unused/mismatched field**.

El script biodata envía `"validate_output": True` (`CODE_VERIFIED`); el efecto real sobre el gate de validación es nulo por el mismatch (`INFERENCE` a partir de CODE_VERIFIED).

---

## 6. Streaming vs no-streaming

| `stream` | Respuesta |
|---|---|
| `true` | `StreamingResponse` SSE `text/event-stream`; chunks `data: {json}\n\n`; fin `data: [DONE]` |
| `false` | `graph.ainvoke` → `JSONResponse` con estado convertido |

---

## 7. Ejemplos ficticios de request (NO ejecutar en Prompt 9)

### 7.1 Smoke propuesto (una pregunta, sin SPARQL agent-exec)

```http
POST /chat HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Authorization: Bearer [REDACTED]

{
  "messages": [
    {"role": "user", "content": "What is the HGNC symbol for the P68871 protein?"}
  ],
  "model": "openrouter/openai/gpt-5.2",
  "stream": false,
  "validate_output": true,
  "enable_sparql_execution": false,
  "max_tokens": 16384,
  "temperature": 0.0,
  "session_id": "lab-smoke-fictional-001"
}
```

Notas:

- `enable_sparql_execution: false` → omite `query_sparql` en `validation.py` (`CODE_VERIFIED`).  
- `max_tokens`/`temperature` en el body **no** alteran `Configuration` vía este endpoint (`CODE_VERIFIED`).  
- `validate_output` body **no** mapea a `enable_output_validation` (`CODE_VERIFIED`).

### 7.2 Stream (ficticio)

Igual payload con `"stream": true`; cliente debe consumir SSE.

### 7.3 curl README (referencia; no ejecutar aquí)

README muestra curl a `localhost:8000/chat` con modelo distinto (`README_REPORTED`). Forma alineada con el endpoint; no implica disponibilidad en este lab.

---

## 8. Respuestas esperables (formas, no valores reales)

**No-stream:** objeto JSON serializado del estado LangGraph (mensajes, steps, structured_output posibles) vía `convert_chunk_to_dict`.

**Stream:** secuencia de eventos `messages` / `updates` empaquetados en JSON por línea SSE.

**Errores de contrato:** pregunta vacía → `ValueError("No question provided")`; auth inválida si key configurada.

---

## 9. Dependencia de modelo

`load_chat_model` (`agent/utils.py`):

- Prefijo `openrouter/` → OpenRouter API + `OPENROUTER_API_KEY`; **sin** `max_tokens` en esa rama.  
- Otros proveedores → `init_chat_model` con `max_tokens`, `temperature`, `seed`, `max_retries=2`, `timeout=None`.

Valores efectivos de temperature/max_tokens/seed vienen de `Configuration` (defaults Settings), **no** del body HTTP salvo que se añada cableado futuro.

---

## 10. Relación con biodata (evidencia de uso)

`tests/benchmark_biodata.py` POST a `http://localhost:8000/chat` con:

```json
"validate_output": true,
"enable_sparql_execution": false
```

(`CODE_VERIFIED`). Luego ejecuta SPARQL **fuera** del agent path. Patrón recomendado para smoke PE2 controlado (`INFERENCE`).

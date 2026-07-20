# Contrato MCP — SPARQL-LLM

**Commit pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Fuente primaria:** `src/sparql_llm/mcp_server.py`  
**Etiquetas:** `CODE_VERIFIED` salvo donde se indique.

---

## 1. Rol

El servidor MCP expone herramientas de recuperación documental (ejemplos/esquemas) y ejecución SPARQL para clientes MCP. Puede correr embebido bajo FastAPI (`agent/main.py` monta `/mcp`) o como proceso CLI (`sparql-llm` → `cli`).

**Importante:** el MCP público `https://chat.expasy.org/mcp` (`README_REPORTED`) es un **servicio remoto**; no garantiza el commit pin. Etiqueta operativa: `external_service_availability_check` únicamente — **no** cuenta como ejecución nativa.

---

## 2. Construcción FastMCP (`get_mcp_app`)

| Parámetro | Valor | Evidencia |
|---|---|---|
| `name` | `f"{settings.app_org} MCP"` | `CODE_VERIFIED` |
| `debug` | `True` | `CODE_VERIFIED` |
| `json_response` | `True` | `CODE_VERIFIED` |
| `stateless_http` | `True` | `CODE_VERIFIED` |
| `streamable_http_path` | `"/"` | `CODE_VERIFIED` |
| `dependencies` | `mcp`, `qdrant_client`, `fastembed`, `sparql-llm` | `CODE_VERIFIED` |
| Transport security | si `app_public_host`: DNS rebinding + hosts `localhost:*`, `127.0.0.1:*`, host público | `CODE_VERIFIED` |

---

## 3. Side-effects al construir la app

1. Imports de módulo desde `index_resources`: `embedding_model`, `endpoints_metadata`, `init_vectordb`, `qdrant_client` (`CODE_VERIFIED`).  
2. Chequeo de colección `docs_collection_name` (`expasy` por defecto).  
3. Si `settings.auto_init` y colección ausente/vacía o `force_index` → `init_vectordb()` (`CODE_VERIFIED`).  
4. Errores de init se loguean; el arranque continúa (`CODE_VERIFIED`).

Además, `agent/main.py` ejecuta `mcp = get_mcp_app()` **a nivel de import** → importar `agent.main` dispara el mismo camino (`CODE_VERIFIED`).

---

## 4. Tools

### 4.1 `search_sparql_docs(question, potential_classes, steps)`

- Embeddings sobre `[question, *steps, *potential_classes]`.  
- Query Qdrant: ejemplos SPARQL (`doc_type` = ejemplos) + resto (schemas/info).  
- `limit = settings.default_number_of_retrieved_docs` (default 10).  
- Devuelve prompt `PROMPT_TOOL_SPARQL` con docs formateados.

### 4.2 `get_classes_schema(classes)`

- Embeddings de la lista `classes`.  
- Filtra excluyendo ejemplos SPARQL.  
- Devuelve texto con schemas ShEx relevantes.

### 4.3 `get_resources_info(question)` (si `enable_resources_info_tool=True`, default)

- Solo documentación `doc_type` = “General information”.  
- Descripción: llamar solo si el usuario pregunta por los recursos mismos.

### 4.4 `execute_sparql_query(sparql_query, endpoint_url)`

Pipeline (`CODE_VERIFIED`):

1. `validate_sparql(...)` con `prefixes_map` / `void_dict` de `endpoints_metadata`.  
2. Si hay `fixed_query`, sustituye y notifica.  
3. Si hay `errors`, retorna mensaje de reparación (sin ejecutar).  
4. Si válido: `query_sparql(..., timeout=10, post=True)`.  
5. Sin bindings → mensaje + `FIX_QUERY_PROMPT`.  
6. Con bindings → JSON; si >50 filas, **capea a 50**.  
7. Excepción → error + `FIX_QUERY_PROMPT`.

---

## 5. Resource

`examples://{question}` → delega en `search_sparql_docs(question, [], [])` (`CODE_VERIFIED`).

---

## 6. CLI (`cli`)

| Modo | Comportamiento |
|---|---|
| Default (stdio) | `mcp = get_mcp_app()`; `mcp.run()` |
| `--http` | `mcp.run()` **luego** `mcp.settings.port = args.port` (default **8888**), `log_level=INFO`, `mcp.run(transport="streamable-http")` |

**Anomalía CODE_VERIFIED:** en la rama `--http`, la primera llamada a `mcp.run()` precede a la asignación de puerto y al segundo `run` con transport HTTP. Documentar como comportamiento anómalo del pin; no “arreglar” en Prompt 9.

---

## 7. Despliegue local documentado (README)

| Hecho | Etiqueta |
|---|---|
| `uvx sparql-llm` (stdio) | `README_REPORTED` |
| `SETTINGS_FILEPATH` apunta a JSON de settings | `README_REPORTED` / `CODE_VERIFIED` |
| Público: `https://chat.expasy.org/mcp` | `README_REPORTED` — **external_service_availability_check** |

---

## 8. Relación con la acción futura seleccionada

`LOCAL_CHAT_API_ONE_QUESTION` **no** selecciona MCP como superficie primaria. MCP local permanece candidato nativo no seleccionado; MCP público no es nativo.

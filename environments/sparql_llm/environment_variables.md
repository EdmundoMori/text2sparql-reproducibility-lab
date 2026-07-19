# Variables de entorno — sparql_llm

**Valores:** nunca versionar secretos. Usar `.env` local (gitignored).  
**Fuente:** `Settings` en `upstream/sparql_llm/src/sparql_llm/config.py`, README, compose, `agent/utils.py`, `tests/text2sparql/api.py`.

| Nombre | Scope | Notas |
|---|---|---|
| `SETTINGS_FILEPATH` | MCP / Settings JSON | Path a JSON de endpoints |
| `OPENROUTER_API_KEY` | MCP_OR_AGENT_API | LLM OpenRouter |
| `OPENAI_API_KEY` | MCP_OR_AGENT_API | README_REPORTED; uso vía modelos OpenAI-compatible |
| `CHAT_API_KEY` | FULL_CHAT_STACK | Frontend / anti-abuse |
| `LOGS_API_KEY` | FULL_CHAT_STACK | Logs API |
| `LANGFUSE_HOST` | opcional tracing | |
| `LANGFUSE_PUBLIC_KEY` | opcional | |
| `LANGFUSE_SECRET_KEY` | opcional | gate en agent |
| `VECTORDB_URL` | agent/compose | URL o path Qdrant |
| `AUTO_INIT` | Settings `auto_init` | |
| `USE_TOOLS` | Settings `use_tools` | cambia grafo |
| `DEFAULT_LLM_MODEL` | Settings | override modelo |
| `FORCE_INDEX` | Settings `force_index` | **no** `FORCE_REINDEX` (compose override desalineado) |
| `SENTRY_URL` | opcional | |
| `BENCH_MODEL` | Text2SPARQL API tests | scope D bloqueado localmente |
| `DBPEDIA_URL` | Text2SPARQL tests | bloqueado local |
| `CORPORATE_URL` | Text2SPARQL tests | bloqueado local |

CORE_OFFLINE: ninguna key LLM obligatoria si solo import/validate con archivos locales.

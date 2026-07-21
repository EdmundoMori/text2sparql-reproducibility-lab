# Environment spec — sparql_llm

**Source commit:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Legal:** MIT (`CONFIRMED_LICENSE_FILE`)  
**Package version in code:** `0.1.4` (`src/sparql_llm/__init__.py`) — diverge de `CITATION.cff`/`server.json` `0.1.2`  
**Python requerido (metadata):** `>=3.10` (`pyproject.toml`) — **inconsistente** con `typing.Required` (necesita ≥3.11).  
**Host WSL:** Python 3.10.12 → CORE_OFFLINE en host = `setup_failed` (run 5A).  
**Runtime validado CORE_OFFLINE:** Docker `python:3.11-slim-bookworm` digest `sha256:b18992999…` → `smoke_only` (run 5B `20260720T134943Z`).  
**Runtime agent (Prompt 10):** imagen `text2sparql-lab/sparql-llm-agent-py311:20260721T084637Z` (`Dockerfile.agent-py311`, extra `[agent]`) — entorno **ready**; índice mínimo **bloqueado** (caché e5-large ausente).  
Ver [`container_py311.md`](container_py311.md), [`Dockerfile.core-offline-py311`](Dockerfile.core-offline-py311), [`Dockerfile.agent-py311`](Dockerfile.agent-py311), [`MINIMAL_INDEX_POLICY.md`](MINIMAL_INDEX_POLICY.md), [`minimal_local_chat_settings.json`](minimal_local_chat_settings.json).

Estado: **documentado** + CORE_OFFLINE `smoke_only` + prep agent `ENVIRONMENT_READY_INDEX_BLOCKED_PENDING_EMBEDDING_DOWNLOAD_APPROVAL` (no paper).

### Runs CORE_OFFLINE

| RUN_ID | Runtime | Status | Report |
|---|---|---|---|
| `20260719T112306Z` | host Py3.10 | setup_failed | `audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md` |
| `20260720T134943Z` | Docker Py3.11 | smoke_only | `audit/sparql_llm/CORE_OFFLINE_PY311_SMOKE_REPORT.md` |

### Runs preparación LOCAL_CHAT_API

| RUN_ID | Status | Report |
|---|---|---|
| `20260721T084637Z` | env ready; index blocked (no embedding download) | `audit/sparql_llm/LOCAL_CHAT_API_ENV_INDEX_PREP_REPORT.md` |

Entorno resuelto 5B: `logs/smoke/sparql_llm-core-offline-py311/20260720T134943Z/pip-freeze.txt`.  
Entorno agent 10: `logs/preparation/sparql-llm-local-chat-api/20260721T084637Z/pip-freeze.txt`.

---

## A. CORE_OFFLINE (primer micro-smoke recomendado)

| Incluye | Excluye |
|---|---|
| Loaders ejemplos/VoID/info | LLM / OpenRouter |
| `validate_sparql*` con VoID local (`tests/void_*.ttl`) | Qdrant |
| Import paquete / tests de componentes **sin red** | Docker / Compose |
| deps **base** de `pyproject.toml` (sin extra `agent`) | Indexación completa multi-endpoint |

**Objetivo smoke:** import + validación/loaders locales → etiquetar `smoke_only` solo tras ejecución.  
**No es** reproducción del paper.

## B. MCP_OR_AGENT_API

| Incluye | Notas |
|---|---|
| Extra `agent` (langgraph, fastapi, langchain-openai, …) | LOWER_BOUND en pyproject |
| API OpenRouter / OpenAI-compatible | `OPENROUTER_API_KEY` / afines |
| Embeddings (`intfloat/multilingual-e5-large` default) | Riesgo RAM |
| Qdrant opcional (path local o contenedor) | Compose ausente → `docker run` futuro |
| Una pregunta; **un worker** | No 6 workers del Dockerfile prod |
| Preferir import/MCP stdio vs CLI `--http` | posible bug orden puerto |

**No ejecutar en 4B.**

## C. FULL_CHAT_STACK

API + Qdrant + UI/frontend según `compose.yml` autores.  
**No** es smoke mínimo. Requiere alternativa a Compose o instalar plugin (fuera de 4B).

## D. TEXT2SPARQL_VIRTUOSO — `BLOCKED_ON_LOCAL_HOST`

| Motivo | Evidencia |
|---|---|
| Virtuoso `NumberOfBuffers` ~2.72M (~21 GiB teórico) | `compose.text2sparql.yml` (static audit) |
| RAM WSL ≈7.4 GiB | `MACHINE_PROFILE.md` |
| Dumps DBpedia/Corporate ausentes en worktree | NOT_FOUND en audit |

**No** incluir en futuros comandos locales de este host.

---

## Artefactos

- [`dependency_manifest.yaml`](dependency_manifest.yaml)  
- [`environment_variables.md`](environment_variables.md)  
- [`future_commands.md`](future_commands.md)

## Runs ejecutados (no reemplazan el manifiesto 4B)

| RUN_ID | Resultado | Notas |
|---|---|---|
| `20260719T112306Z` | **setup_failed** | Install 0.1.4 OK; import falla en Python 3.10.12 (`typing.Required`). Informe: `audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md`. Entorno resuelto: `logs/smoke/sparql_llm-core-offline/20260719T112306Z/pip-freeze.txt`. |

**Requisito actualizado:** CORE_OFFLINE necesita **Python ≥3.11** en la práctica (código pin), pese a `requires-python >=3.10` en pyproject.

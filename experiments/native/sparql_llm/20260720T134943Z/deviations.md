# Deviations — sparql_llm CORE_OFFLINE py311 (`20260720T134943Z`)

- **No** se ejecutó el paper / benchmarks / métricas científicas.  
- **No** se usó LLM, OpenRouter/OpenAI, endpoints SPARQL, Qdrant, MCP, agent.  
- **No** se probó Virtuoso / Text2SPARQL challenge.  
- Runtime: **Docker Python 3.11**, no Python del host WSL (3.10).  
- Hallazgo de reproducibilidad conservado: `pyproject.toml` declara `>=3.10` pero el código necesita `typing.Required` (3.11+); el run 5A en 3.10 permanece `setup_failed`.  
- Corrección **solo del harness del lab** (no upstream): guard de red.  
- `--read-only` no viable en smoke (deps escriben en home); aislamiento de red vía `--network none`.  
- Objetivo: CODE_VERIFIED CORE_OFFLINE → etiqueta máxima `smoke_only`.

# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-19  
**Tras:** Prompt 5A → `setup_failed` (Python 3.10 / `typing.Required`)

## Prompt recomendado (prioridad 1)

**Título:** Prompt 5B — Host Python ≥3.11 + reintento sparql_llm CORE_OFFLINE

**Objetivo:** Disponer `python3.11` (o superior) en WSL de forma documentada (sin tocar upstream), recrear venv, reinstalar desde copia pin, ejecutar `scripts/smoke/sparql_llm_core_offline.py`. Si OK → `smoke_only`.

**Alternativa:** si no se puede instalar 3.11, documentar bloqueo permanente CORE_OFFLINE en este host y replanificar (no fingir smoke).

## No proponer aún

- Agent/API/MCP smokes.  
- mkgqagent / rdfconfig.  
- Virtuoso.  
- Patches silenciosos a `upstream/sparql_llm`.

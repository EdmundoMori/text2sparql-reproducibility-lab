# NEXT_PROMPT_GUIDANCE — Qué debe proponer ChatGPT a continuación

**Fecha:** 2026-07-19  
**Estado lab:** WAVE_A static audit + **environment definition (4B)** complete; sin installs.

## Prompt recomendado (prioridad 1)

**Título:** Prompt 5A — sparql_llm CORE_OFFLINE: install + import/validate smoke

**Objetivo:** En venv aislado, instalar deps base del pin `3748730e…` e importar/validar con VoID local. Etiquetar `smoke_only` si OK. **No** reproducción paper. **No** Virtuoso/Compose/API.

**Salidas:** log de comandos, resultado import, actualización METHOD_REGISTRY (`smoke_only` solo si ejecutó), PLAN_SYNC + push.

**Restricciones:** un método; no modificar upstream; no adapters; no WAVE_B/C.

## No proponer aún

- mkgqagent / rdfconfig smokes (legal, Ruby ABSENT, double-agent).  
- Text2SPARQL+Virtuoso.  
- Multi-método.  
- Host Ruby install salvo prompt dedicado de tooling.

## Formato del prompt a Cursor

Incluir: actualizar PLAN_SYNC + ARTIFACT_INDEX + push al cerrar.

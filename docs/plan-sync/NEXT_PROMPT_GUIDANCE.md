# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 11 → modelo `openrouter/openai/gpt-4o-mini-2024-07-18`, cota ≈ $0.0581, límite propuesto $0.10, gate **`READY_FOR_HUMAN_APPROVAL`**

## Acción inmediata (investigador)

Completar y enviar en el chat el bloque de:

`docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/HUMAN_LLM_SMOKE_APPROVAL.md`

Sin esa firma **y** sin clave OpenRouter dedicada con límite duro $0.10, **no** ejecutar Prompt 12.

## Prompt recomendado (prioridad 1) — solo tras aprobación

**Título:** Prompt 12 — Ejecución controlada de LOCAL_CHAT_API_ONE_QUESTION

**Método:** `sparql_llm`  
**Objetivo:** Un único POST `/chat` con la pregunta y el request congelados en Prompt 11, bajo Settings mínimos, `enable_sparql_execution=false`, modelo exacto aprobado, clave dedicada limitada. Registrar evidencia de smoke; conservar `smoke_only`.

**Restricciones:**
- Revalidar metadata OpenRouter antes de gastar.  
- No biodata; no MCP público como nativo; no Virtuoso; no adapters.  
- No afirmar reproducción paper / PE3.  
- Conservar `native_audit_complete=false` / `common_adapter_allowed=false`.

**Condición de éxito:** smoke funcional documentado o aborto seguro con evidencia.

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

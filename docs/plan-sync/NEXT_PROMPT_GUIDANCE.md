# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 10B → caché e5-large + `LAB_MINIMAL_INDEX` + preflight FastAPI **pass**; gate sigue **CONDITIONAL_GO**

## Prompt recomendado (prioridad 1)

**Título:** Prompt 11 — Cierre de presupuesto, selección de modelo y gate final para LOCAL_CHAT_API_ONE_QUESTION

**Método:** `sparql_llm`  
**Objetivo:** Firmar/registrar presupuesto OpenRouter (`MAX_OPENROUTER_USD`), elegir **un** modelo exacto, fijar `MAX_LLM_CALLS=2` con Settings ya preparados (`max_try_fix_sparql=0`, `enable_sparql_execution=false`), documentar límites no enforceados (`max_tokens` OpenRouter), y emitir GO / CONDITIONAL / NO-GO **final** para el smoke de una pregunta. **Sin** ejecutar POST `/chat` en Prompt 11 salvo que el investigador autorice explícitamente la ejecución en el mismo prompt.

**Restricciones:**
- Preferible: solo documental + checklist GO; no LLM si no hay firma.  
- No biodata; no MCP público como nativo; no Virtuoso; no adapters.  
- Conservar `smoke_only` / `native_audit_complete=false` / `common_adapter_allowed=false` hasta evidencia de ejecución.

**Condición de éxito:** decisión formal de gate + presupuesto/modelo registrados (o NO-GO documentado).

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

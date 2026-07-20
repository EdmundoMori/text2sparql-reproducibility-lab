# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-20  
**Tras:** Prompt 9 → protocolo API/SIB SPARQL-LLM; **CONDITIONAL_GO** = `LOCAL_CHAT_API_ONE_QUESTION`

## Prompt recomendado (prioridad 1)

**Título:** Prompt 10 — Preparación de entorno e índice mínimo para smoke LOCAL_CHAT_API de SPARQL-LLM (sin llamadas LLM)

**Método:** `sparql_llm`  
**Objetivo:** Cerrar prerrequisitos del gate CONDITIONAL_GO **sin** invocar OpenRouter/OpenAI, MCP remoto, ni endpoints SPARQL: runtime Py3.11 (patrón Docker 5B), SETTINGS mínimo (UniProt + `void_file` local), política de índice/Qdrant/FastEmbed, checklist de arranque `/chat`, y confirmación de presupuesto propuesto. **Sin llamadas LLM** en Prompt 10.

**Restricciones:**
- Sin `OPENROUTER_API_KEY` en uso real; sin POST `/chat` con modelo; sin MCP público; sin SPARQL vivos.  
- Sin download de embeddings salvo que el investigador autorice explícitamente un paso de cache (preferible documentar/NO-GO hasta aprobación).  
- No cambiar `reproduction_status` (`smoke_only`); `native_audit_complete=false`; `common_adapter_allowed=false`.  
- No Virtuoso; no adapters; no otros métodos.

**Condición de éxito:** entorno/índice mínimo documentado (o bloqueado con evidencia) + checklist GO técnico hacia el smoke D, sin ejecutar el smoke.

**No proponer ahora:** biodata full; train otros métodos; smoke con clave sin índice.

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

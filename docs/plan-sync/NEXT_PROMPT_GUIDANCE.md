# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 10 → entorno agent **ready**; documentos mínimos **ready**; índice **bloqueado** (caché e5-large ausente)

## Prompt recomendado (prioridad 1)

**Título:** Prompt 10B — Descarga controlada y fijación de caché `intfloat/multilingual-e5-large` + construcción del índice mínimo (previa autorización explícita)

**Método:** `sparql_llm`  
**Prerrequisito duro:** autorización **explícita** del investigador para descargar el embedding exacto. Sin ella → NO-GO / no ejecutar.

**Objetivo:** (solo tras aprobación) descargar/fijar caché exacta offline, `build-index` + `verify-index` de `LAB_MINIMAL_INDEX` (≤12 docs ya preparados), opcional preflight FastAPI **sin** POST `/chat` ni OpenRouter.

**Restricciones:**
- No POST `/chat`; no OpenRouter; no MCP público; no SPARQL vivos; no `init_vectordb` completo.  
- No cambiar embedding ni cuantizar.  
- No promover `reproduction_status` ni cerrar Fase 1.  
- Presupuesto LLM sigue sin firmar.

**Condición de éxito:** `INDEX_VERIFIED` + (ideal) preflight pass → entonces Prompt 11 (presupuesto/modelo/gate final).

**Alternativa si no hay autorización de descarga:** documentar bloqueo; no avanzar a smoke.

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

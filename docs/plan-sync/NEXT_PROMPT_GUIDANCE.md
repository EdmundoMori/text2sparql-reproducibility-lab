# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-20  
**Tras:** Prompt 8 → gate comparativo nativo; **GO_NEXT** = protocolo API/SIB `sparql_llm`

## Prompt recomendado (prioridad 1)

**Título:** Prompt 9 — Definición documental del protocolo API/SIB de SPARQL-LLM (sin llamadas de API)

**Método / prerrequisito:** `sparql_llm` — protocolización del camino online/API tras CORE_OFFLINE `smoke_only` (5B).

**Objetivo:** Documentar endpoints/entrypoints (API/MCP), nombres de claves/variables de entorno, formas request/response observables en código/README, límites offline vs online, y criterios de éxito/fallo + checklist GO/NO-GO para un **futuro** smoke API controlado. Etiquetar evidencia (CODE_VERIFIED / README_REPORTED / INFERENCE).

**Restricciones duras:**
- Sin llamadas de API; sin endpoints SPARQL vivos; sin OpenRouter/OpenAI reales.
- Sin pip/conda/Docker/apt/Ruby; sin imports ejecutados de upstream; sin downloads.
- Sin tercer CORE_OFFLINE; sin Virtuoso; sin adapters; sin evaluación común.
- No cambiar `reproduction_status` (`smoke_only`); `native_audit_complete=false`; `common_adapter_allowed=false`.
- No declarar PE3 ni `partially_reproduced`.

**Condición de éxito:** artefacto(s) de protocolo con los 6 mínimos de `audit/NEXT_EXECUTION_DECISION.md` §10; criterios GO/NO-GO hacia smoke API **sin ejecutarlo**.

**No proponer ahora:** smoke API (GO_AFTER_ENVIRONMENT); train SGPT; install CoT; Ruby/RDF-config; run mKGQAgent; recomputar FIRESPARQL; download checkpoints.

## Objetivo de fase (recordatorio)

reproducción nativa → evaluación común → caso de estudio → análisis de errores → transferencia Text-to-SQL → método nuevo → ablaciones.

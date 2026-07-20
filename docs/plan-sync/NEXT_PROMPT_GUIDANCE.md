# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-20  
**Tras:** Prompt 7A → auditoría estática CoT-SPARQL (WAVE_C parcial); `reproduction_status` sigue **audit_only**

## Prompt recomendado (prioridad 1)

**Título:** Prompt 7B — Auditoría estática completa de FIRESPARQL (WAVE_C)

**Objetivo:** Inspeccionar `upstream/firesparql/` (pin en lock) sin install/train: pipeline generación/RAG/one-shot/QLever/métricas, resultados versionados (~598 MiB), deps, blockers legales, factibilidad. Producir `audit/firesparql/*` + completar fila WAVE_C + PLAN_SYNC + push.

**No proponer:** install CoT-SPARQL; descarga CodeLlama/MiniLM/embeddings; llamadas Falcon/Spotlight; train SGPT; smoke API sparql; adapters.

## Objetivo de fase (recordatorio)

reproducción nativa → evaluación común → caso de estudio → análisis de errores → transferencia Text-to-SQL → método nuevo → ablaciones.

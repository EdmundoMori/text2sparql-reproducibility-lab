# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-20  
**Tras:** Prompt 6 → auditoría estática SGPT (WAVE_B) completa; `reproduction_status` sigue **audit_only**

## Prompt recomendado (prioridad 1)

**Título:** Prompt 7 — Auditoría estática WAVE_C (CoT-SPARQL y FIRESPARQL)

**Objetivo:** Inspeccionar `upstream/cot_sparql/` y `upstream/firesparql/` (pins en lock) sin install/train: entrypoints, deps, datos, checkpoints, métricas, blockers legales, factibilidad. Producir audits estáticos + actualizar PLAN_SYNC + push.

**No proponer:** entrenamiento SGPT; descarga GPT-2/spaCy; install PyTorch; smoke API/MCP sparql; adapters; TeBaQA.

## Objetivo de fase (recordatorio)

reproducción nativa → evaluación común → caso de estudio → análisis de errores → transferencia Text-to-SQL → método nuevo → ablaciones.

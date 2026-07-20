# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-20  
**Tras:** Prompt 5B → `smoke_only` (Docker Py3.11 CORE_OFFLINE)

## Prompt recomendado (prioridad 1)

**Título:** Prompt 6 — Auditoría estática SGPT (WAVE_B)

**Objetivo:** Inspeccionar `upstream/sgpt/` (pin en lock) sin install/train: entrypoints, deps, datasets, checkpoints ausentes/presentes, métricas, factibilidad en esta máquina (6 GiB VRAM), gates. Producir `audit/sgpt/STATIC_AUDIT.md` + actualizar PLAN_SYNC + push.

**No proponer:** tercer reintento CORE_OFFLINE; API/MCP sparql inmediato; mkgq/rdfconfig; Virtuoso; adapters.

## Objetivo de fase (recordatorio)

reproducción nativa → evaluación común → caso de estudio → análisis de errores → transferencia Text-to-SQL → método nuevo → ablaciones.

# NEXT_PROMPT_GUIDANCE — Qué debe proponer ChatGPT a continuación

**Fecha:** 2026-07-19  
**Estado lab:** clones WAVE_A/B/C listos; sin installs ni experimentos.

## Prompt recomendado (prioridad 1)

**Título sugerido:** Auditoría estática WAVE_A en árboles clonados

**Objetivo:** Para `sparql_llm`, `mkgqagent` y `rdfconfig_llm` (+ dependencia `rdfconfig_llm_rdf-config` si aplica), inspeccionar `upstream/` **sin instalar ni ejecutar**, y producir fichas reutilizables.

**Salidas esperadas (Cursor debe crear/actualizar):**

- `audit/<method_id>/STATIC_AUDIT.md` — entrypoints, deps, env vars, Docker/Compose, GPU/CPU, riesgos.
- Actualizar `METHOD_REGISTRY.yaml` solo con hechos estáticos (no marcar `reproduced`).
- Actualizar `PLAN_SYNC.md` §3–§6 + esta guía + `ARTIFACT_INDEX.md`.
- Push a GitHub.

**Restricciones obligatorias en el prompt:**

- No `pip install` / Poetry install / Docker build / pull HF.
- No modificar `upstream/`.
- `LICENSE_NOT_CONFIRMED` (mkgqagent): inspección OK; no diseñar adapters.
- Distinguir “documentado en README” vs “verificado en código”.
- Máquina: 7.4 GiB RAM WSL, 6 GiB VRAM, sin Compose plugin.

## Alternativa (prioridad 2, solo si el investigador tiene API keys)

Smoke mínimo WAVE_A etiquetado `smoke_only`, un método a la vez, presupuesto acotado, sin train. No declarar reproducción del paper.

## No proponer aún

- Train FIRESPARQL / CoT-34B / SGPT full train.
- Adaptadores common / evaluación QALD unificada.
- Clonar o ejecutar TeBaQA.
- Declarar `reproduced` / `partially_reproduced`.

## Formato deseado del prompt que ChatGPT entregue al investigador

1. Contexto (1 párrafo).  
2. Objetivo medible.  
3. Pasos numerados para Cursor.  
4. Artefactos de salida (rutas).  
5. Restricciones (lista).  
6. Criterio de “hecho”.  
7. Instrucción final: actualizar `PLAN_SYNC.md` + push.

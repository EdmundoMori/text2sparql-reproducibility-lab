# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 13B — cierre Z1/Z2 + re-gate post-Z2

## Prompt recomendado (único)

**Título:** Prompt 14A — Definición documental del protocolo SGPT Z3 reduced training smoke, ZERO_COST, sin descarga de GPT-2 y sin train.

**Método:** `sgpt`  
**Acción:** PZ1 `GO_NEXT_ZERO_COST`  
**Objetivo:** Documentar protocolo de smoke de entrenamiento reducido (subset, steps, recursos, outputs, stop conditions, matriz de autorización futura). **Sin** descarga GPT-2, **sin** train, **sin** rebuild Z2, **sin** Table 4.

**Restricciones:** ZERO_COST; auth 13A no reutilizable; conservar `audit_only`; `native_audit_complete=false`; `common_adapter_allowed=false`.

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

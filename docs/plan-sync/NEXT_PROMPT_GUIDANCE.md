# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 14A — protocolo Z3 reduced training (documental)

## Prerrequisito humano

Completar y firmar:
`docs/protocols/sgpt/z3/20260721T134213Z/HUMAN_Z3_ARTIFACT_AND_MODEL_PREFLIGHT_APPROVAL.md`

## Prompt recomendado (único) tras aprobación

**Título:** Prompt 14B — Descarga controlada de artefactos GPT-2 y preflight offline de carga SGPT Z3, ZERO_COST, sin train.

**Método:** `sgpt`  
**Objetivo:** P1+P2A (y P2B solo si marcado): descarga GPT-2 fijada + tensorboardX + load preflight offline. **Sin** train. **Sin** Table 4.

**Restricciones:** ZERO_COST; no reutilizar auth 13A; conservar `audit_only`.

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

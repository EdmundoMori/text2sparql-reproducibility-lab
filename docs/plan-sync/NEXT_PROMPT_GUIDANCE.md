# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 14B — GPT-2 download + P2A model-load **PASS**

## Prerrequisito humano

Completar y firmar:
`docs/protocols/sgpt/z3/20260721T134213Z/HUMAN_Z3_ONE_STEP_TRAINING_APPROVAL.md`

## Prompt recomendado (único) tras aprobación

**Título:** Prompt 14C — Ejecución SGPT Z3 one-step reduced training smoke, ZERO_COST, sin Table 4.

**Método:** `sgpt`  
**Objetivo:** Un único paso de optimización con subset canario 1/1/1 bajo límites de recursos del protocolo. **Sin** Table 4. **Sin** P2B separado (forward de train es el del entrypoint).

**Restricciones:** ZERO_COST; auth 14B no reutilizable para re-download; conservar `audit_only`.

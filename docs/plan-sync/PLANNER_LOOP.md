# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-21 (post Prompt 12 SGPT env)

## Ciclo fijo

```text
1. ChatGPT → UN prompt para Cursor
2. Investigador → ejecuta en Cursor
3. Cursor → PLAN_SYNC + artefactos + ARTIFACT_INDEX
4. Cursor → commit + push
5. Investigador → meta-prompt a ChatGPT
6. ChatGPT → relee repo y entrega el siguiente prompt
```

## Fuentes de verdad

1. `PLAN_SYNC.md`  
2. `docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`  
3. `audit/sgpt/ENVIRONMENT_DEFINITION_REPORT.md`  
4. `environments/sgpt/ENVIRONMENT_GATE.md`  
5. `audit/ZERO_COST_POLICY.md`

## Reglas

- ZERO_USD; sin OpenRouter.  
- Prompt 12: sin install/download/train.  
- Siguiente: **12B** pins documentales.  
- Fase 1 abierta.

## Estado

- SGPT env gate: **CONDITIONAL_DEPENDENCY_RESOLUTION**  
- `audit_only`; no Table 4.

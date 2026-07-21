# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-21 (post Prompt 11C)

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
3. `audit/ZERO_COST_NATIVE_AUDIT_REGATE.md`  
4. `audit/NEXT_ZERO_COST_EXECUTION_DECISION.md`  
5. `audit/ZERO_COST_POLICY.md`  
6. `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/HUMAN_ZERO_COST_DECISION.md`  
7. `docs/decisions/004_zero_cost_policy_and_online_smoke_deferral.md`

## Reglas

- Un prompt por turno.  
- **ZERO_USD** activo: no OpenRouter / no POST `/chat` / no paid cloud.  
- `NATIVE_REPRODUCTION_QUEUE.csv` (Prompt 8) es histórico; cola operativa = `ZERO_COST_NATIVE_REPRODUCTION_QUEUE.csv`.  
- No ejecutar la acción GO_NEXT dentro del prompt de gate.

## Estado

- sparql_llm online: **NO_GO_ECONOMIC_ZERO_COST_POLICY**  
- GO_NEXT_ZERO_COST: **SGPT environment definition**  
- Fase 1 abierta; objetivo largo plazo intacto.

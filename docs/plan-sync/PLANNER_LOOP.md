# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-21 (post NO_GO_ECONOMIC + re-gate ZERO_USD)

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
3. `audit/NATIVE_AUDIT_COMPARATIVE_GATE_RERUN_ZERO_USD.md`  
4. `audit/NEXT_EXECUTION_DECISION.md`  
5. `docs/decisions/004_economic_nogo_online_smoke_and_re_gate.md`  
6. `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/ECONOMIC_NO_GO_DECISION.md`

## Reglas

- Un prompt por turno.  
- **ZERO_USD:** no OpenRouter / no POST `/chat` / no modelos de pago.  
- Caché e índice en `workdir/` no se versionan.  
- `common_adapter_allowed: false` hasta native audit.  
- No firmar gasto por el investigador.

## Estado actual

- sparql_llm online: **NO_GO_ECONOMIC**  
- GO_NEXT: **rdfconfig legal/source closure**  
- Fase 1 abierta; objetivo largo plazo intacto.

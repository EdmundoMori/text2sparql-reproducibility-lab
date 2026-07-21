# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-21 (post Prompt 11)

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
3. `audit/sparql_llm/LOCAL_CHAT_API_MODEL_BUDGET_FINAL_GATE_REPORT.md`  
4. `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/FINAL_ONLINE_SMOKE_GATE.md`  
5. `docs/protocols/sparql_llm/API_BUDGET_AND_SAFETY.md`  
6. `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/HUMAN_LLM_SMOKE_APPROVAL.md`

## Reglas

- Un prompt por turno.  
- No POST `/chat` sin firma humana + clave dedicada limitada.  
- Caché e índice en `workdir/` no se versionan.  
- Catálogo OpenRouter completo solo en workdir.  
- `common_adapter_allowed: false` hasta native audit.  
- No firmar por el investigador.

## Estado al cerrar Prompt 11

- Gate: **READY_FOR_HUMAN_APPROVAL**  
- Modelo seleccionado (PROPOSED): `openrouter/openai/gpt-4o-mini-2024-07-18`  
- Inferencias: **0**  
- Siguiente: firma humana → **Prompt 12**  
- Objetivo largo plazo intacto; Fase 1 abierta.

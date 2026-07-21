# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-21 (post Prompt 10B)

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
3. `audit/sparql_llm/LOCAL_CHAT_API_EMBEDDING_INDEX_PREFLIGHT_REPORT.md`  
4. `docs/protocols/sparql_llm/API_BUDGET_AND_SAFETY.md`  
5. `docs/protocols/sparql_llm/FUTURE_API_SMOKE_GONOGO.md`

## Reglas

- Un prompt por turno.  
- No descargar embeddings sin autorización explícita (10B ya autorizada y consumida).  
- No POST `/chat` sin firma de presupuesto/modelo.  
- Caché e índice en `workdir/` no se versionan.  
- `common_adapter_allowed: false` hasta native audit.

## Estado al cerrar Prompt 10B

- `ENVIRONMENT_READY_INDEX_READY_PREFLIGHT_PASS`  
- Siguiente: **Prompt 11** (presupuesto + modelo + gate final)  
- Objetivo largo plazo intacto.

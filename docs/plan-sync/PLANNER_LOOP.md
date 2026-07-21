# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-21 (post Prompt 10 — prep LOCAL_CHAT_API)

## Ciclo fijo

```text
1. ChatGPT → entrega UN prompt listo para Cursor
2. Investigador → pega el prompt en Cursor y lo ejecuta
3. Cursor → actualiza PLAN_SYNC.md + docs específicos + ARTIFACT_INDEX
4. Cursor → commit + push a GitHub
5. Investigador → pega en ChatGPT el meta-prompt de replanificación
6. ChatGPT → relee el repo, valida/ajusta el plan, entrega el siguiente prompt
7. Repetir desde 2 hasta el objetivo de fase
```

## Fuentes de verdad

1. `PLAN_SYNC.md`  
2. `docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`  
3. `docs/plan-sync/ARTIFACT_INDEX.md`  
4. `audit/sparql_llm/LOCAL_CHAT_API_ENV_INDEX_PREP_REPORT.md`  
5. `docs/protocols/sparql_llm/FUTURE_API_SMOKE_GONOGO.md` + `API_BUDGET_AND_SAFETY.md`

## Reglas

- Un solo prompt por turno.  
- Clonar ≠ install ≠ smoke ≠ reproducir.  
- MCP público ≠ ejecución del pin.  
- **No descargar embeddings** sin autorización explícita documentada.  
- `common_adapter_allowed: false` hasta native audit.  
- No promover CONDITIONAL_GO → GO solo por instalar entorno.

## Estado al cerrar Prompt 10

- Clasificación: `ENVIRONMENT_READY_INDEX_BLOCKED_PENDING_EMBEDDING_DOWNLOAD_APPROVAL`.  
- Entorno agent Py3.11 **ready**; 12 docs VoID; caché e5-large **absent**.  
- Siguiente candidato: **Prompt 10B** (descarga controlada + índice) **solo con autorización**.  
- Objetivo largo plazo intacto.

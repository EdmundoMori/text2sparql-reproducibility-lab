# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-21 (post Prompt 12B)

## Ciclo fijo

```text
1. ChatGPT → UN prompt
2. Cursor ejecuta
3. PLAN_SYNC + artefactos
4. commit + push
5. meta-prompt planificador
```

## Fuentes de verdad

1. `PLAN_SYNC.md`  
2. `docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`  
3. `audit/sgpt/PIN_RESOLUTION_REPORT.md`  
4. `environments/sgpt/ENVIRONMENT_GATE.md`  
5. `environments/sgpt/pin-resolution/20260721T113310Z/`

## Estado

- Gate SGPT: **READY_FOR_Z2_DOWNLOAD_AUTHORIZATION**  
- Siguiente: **Prompt 13A** (auth + download + build Z2)  
- ZERO_COST; Fase 1 abierta

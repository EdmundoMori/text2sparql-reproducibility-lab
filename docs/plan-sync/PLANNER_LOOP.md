# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-19

## Ciclo fijo

```text
1. ChatGPT → entrega UN prompt listo para Cursor
2. Investigador → pega el prompt en Cursor y lo ejecuta
3. Cursor → actualiza PLAN_SYNC.md + docs específicos + ARTIFACT_INDEX
4. Cursor → commit + push a GitHub
5. Investigador → pega en ChatGPT el "meta-prompt de replanificación" (abajo / PLAN_SYNC)
6. ChatGPT → relee el repo, valida/ajusta el plan, entrega el siguiente prompt
7. Repetir desde 2 hasta el objetivo de fase
```

## Fuentes de verdad (orden de lectura para ChatGPT)

1. `PLAN_SYNC.md`  
2. `docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`  
3. `docs/plan-sync/ARTIFACT_INDEX.md`  
4. Artefactos citados en §3 de PLAN_SYNC (p. ej. readiness, gaps, environments/)  
5. `METHOD_REGISTRY.yaml`, `MACHINE_PROFILE.md` si el siguiente paso implica runtime

## Reglas del planificador

- Un solo prompt de ejecución por turno (prioridad 1).  
- No reescribir todo el plan salvo bloqueo metodológico.  
- Clonar ≠ install ≠ smoke ≠ reproducir paper.  
- Respetar LICENSE_NOT_CONFIRMED, RAM/Compose/Ruby, y `common_adapter_allowed: false` hasta native audit.  
- Cada prompt a Cursor debe exigir: actualizar PLAN_SYNC + índice + push.

## Estado al cerrar Prompt 4B

- Completado: fundación → 4B (env definition WAVE_A).  
- Siguiente candidato documentado: **Prompt 5A — sparql_llm CORE_OFFLINE**.  
- HEAD de referencia: ver `PLAN_SYNC.md` §9 / GitHub `main`.

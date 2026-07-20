# Bucle de optimización del plan (operativo)

**Última actualización:** 2026-07-20 (post Prompt 9 — protocolo API/SIB SPARQL-LLM)

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

## Fuentes de verdad (orden de lectura para ChatGPT)

1. `PLAN_SYNC.md`  
2. `docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`  
3. `docs/plan-sync/ARTIFACT_INDEX.md`  
4. Artefactos citados en §3 de PLAN_SYNC  
5. `METHOD_REGISTRY.yaml`, `MACHINE_PROFILE.md` si implica runtime  
6. Protocolo online: `docs/protocols/sparql_llm/API_SIB_PROTOCOL.md` + `FUTURE_API_SMOKE_GONOGO.md`

## Reglas del planificador

- Un solo prompt de ejecución por turno (prioridad 1).  
- No reescribir todo el plan salvo bloqueo metodológico.  
- Clonar ≠ install ≠ smoke ≠ reproducir paper.  
- MCP público remoto ≠ ejecución del commit pin (`external_service_availability_check`).  
- Respetar LICENSE_NOT_CONFIRMED, RAM/Compose/Ruby, y `common_adapter_allowed: false` hasta native audit.  
- Cada prompt a Cursor debe exigir: actualizar PLAN_SYNC + índice + push.  
- Tras un smoke exitoso de un método, preferir **auditar el siguiente método** antes de encadenar más smokes del mismo.  
- Tras WAVE_C, el **gate comparativo (Prompt 8)** ya se ejecutó.  
- Tras protocolo API/SIB (Prompt 9), el siguiente paso es **prerrequisitos de índice/entorno** antes de gastar clave.

## Estado al cerrar Prompt 9

- Completado: fundación → Prompt 9 (protocolo API/SIB documental).  
- `sparql_llm` permanece `smoke_only`; gate online **CONDITIONAL_GO** → `LOCAL_CHAT_API_ONE_QUESTION`.  
- Siguiente candidato: **Prompt 10 — Preparación de entorno e índice mínimo para smoke LOCAL_CHAT_API (sin llamadas LLM)**.  
- HEAD: ver `PLAN_SYNC.md` §9 / GitHub `main`.  
- Objetivo largo plazo intacto: reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

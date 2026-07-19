# Plan sync (Cursor ↔ ChatGPT)

1. Cursor ejecuta un prompt del plan.  
2. Actualiza `PLAN_SYNC.md` + docs específicos + push.  
3. ChatGPT relee GitHub y entrega el siguiente prompt.

| Doc | Uso |
|---|---|
| [`../../PLAN_SYNC.md`](../../PLAN_SYNC.md) | Entrada principal |
| [`PLANNER_LOOP.md`](PLANNER_LOOP.md) | Ciclo operativo + reglas |
| [`NEXT_PROMPT_GUIDANCE.md`](NEXT_PROMPT_GUIDANCE.md) | Siguiente paso recomendado |
| [`ARTIFACT_INDEX.md`](ARTIFACT_INDEX.md) | Índice de artefactos |

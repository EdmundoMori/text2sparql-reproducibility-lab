# FAILURE_DENOMINATOR_POLICY

**RUN_ID:** `20260722T083201Z`

## Reglas mínimas

- todos los ELIGIBLE_GLOBAL forman el denominador;
- METHOD_NO_OUTPUT → métricas semánticas = 0;
- METHOD_TIMEOUT → métricas semánticas = 0;
- METHOD_INVALID_QUERY → Syntax=0; Executable=0; Answer=0;
- METHOD_EXECUTION_ERROR → Executable=0; Answer=0;
- METHOD_ABSTENTION → reportar abstención; Answer=0;
- gold/dataset defect → exclusión global (nunca por método);
- outage global endpoint → invalida segmento del run (no imputar automáticamente);
- no denominadores distintos sin mostrarlos explícitamente;
- empty vs empty gold → regla de canonicalización en Prompt 18.

# EVALUABLE_ITEM_POLICY

**RUN_ID:** `20260722T083201Z`

## Estados de ítem

ELIGIBLE_GLOBAL · EXCLUDED_GLOBAL_DATASET_DEFECT · OUT_OF_PREDECLARED_TRACK_SCOPE · METHOD_ABSTENTION · METHOD_TIMEOUT · METHOD_INVALID_QUERY · METHOD_EXECUTION_ERROR · METHOD_NO_OUTPUT · SYSTEM_ENDPOINT_OUTAGE

## Reglas

- conjunto fijado **antes** de ejecutar métodos;
- no usar intersección de outputs exitosos;
- fallo del método **no** elimina el ítem;
- timeout/abstención/query inválida/sin output permanecen en denominador;
- exclusión global requiere evidencia de defecto dataset/gold/snapshot;
- misma exclusión para todos los métodos;
- scope por query form declarado antes del test;
- no exclusiones post-hoc basadas en resultados.

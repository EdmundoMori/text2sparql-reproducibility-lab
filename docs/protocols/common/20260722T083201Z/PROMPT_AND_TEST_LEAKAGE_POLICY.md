# PROMPT_AND_TEST_LEAKAGE_POLICY

**RUN_ID:** `20260722T083201Z`

## Reglas

- prompts congelados antes del test;
- ejemplos solo de train/development;
- IDs de ejemplos registrados;
- ninguna query gold del test en prompts, caches o retrieval corpus;
- ninguna selección basada en resultados del test;
- no cambiar prompts entre métodos tras observar resultados;
- prompts específicos por método permitidos si forman parte del contrato (versionados);
- debugging solo train/dev;
- acceso accidental al test → RUN_INVALID_TEST_LEAKAGE.

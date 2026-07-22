# Z3_ONE_STEP_TRAINING_CONTRACT (P3)

**RUN_ID protocolo:** `20260721T134213Z`  
**Estado:** **EXECUTED** (Prompt 14C)  
**Auth:** `AUTHORIZED_AND_CONSUMED_14C_ATTEMPT2`

## Resultado

| Campo | Valor |
|---|---|
| Attempt 1 | `20260721T183611Z` → `Z3_OTHER_FAILED` |
| Attempt 2 | `20260722T072146Z` → **`Z3_ONE_STEP_REDUCED_TRAINING_PASS`** |
| Imagen | `text2sparql-lab/sgpt-z3-py38:20260721T135432Z` |
| Image ID | `sha256:3363d73b8a36059698eff046f4a18bd5eaebc689c56f3f825ab1e5f39c273c35` |
| Canario | 8714 / 3988 / 6077 |
| expected_optimizer_steps | 1 |
| Claim | `reduced_training_smoke_only` |

## No implica

Table 4 · PE3 · convergencia · calidad · reproducción nativa completa

## Evidencia versionable

`audit/sgpt/Z3_ONE_STEP_REDUCED_TRAINING_REPORT.md`  
`environments/sgpt/builds/20260722T072146Z/`  
Pesos/checkpoints: solo `workdir/` (gitignore).

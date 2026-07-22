# Z3_ONE_STEP_TRAINING_CONTRACT (P3)

**RUN_ID protocolo:** `20260721T134213Z`  
**Estado:** **EXECUTED_AND_CLOSED** (Prompts 14C + 14D)  
**Auth:** attempt1+2 consumidas

## Resultado reconciliado (14D)

| Campo | Valor |
|---|---|
| Attempt 1 raw | `Z3_OTHER_FAILED` (`20260721T183611Z`) |
| Attempt 2 raw | `Z3_OTHER_FAILED` (`20260722T072146Z`) |
| Operativo | `Z3_ONE_STEP_REDUCED_TRAINING_PASS` |
| Qualifier | `PASS_WITH_INDIRECT_OPTIMIZER_STEP_VERIFICATION` |
| Direct optimizer hook att.2 | `NOT_VERIFIED_ATTEMPT2` |
| Claim | `reduced_training_smoke_only` |

## Fórmula pre-run (cumplida en ambos intentos)

```
expected_steps = (len(train_dataloader) // gradient_accumulation_steps) * num_train_epochs = 1
```

## No implica

Table 4 · PE3 · convergencia · calidad · reproducción nativa completa · `partially_reproduced`

## Evidencia

`audit/sgpt/Z3_ONE_STEP_EVIDENCE_RECONCILIATION.md`  
`audit/sgpt/Z3_CLOSURE_REPORT.md`

# Z3_ONE_STEP_TRAINING_CONTRACT (futuro P3)

**RUN_ID:** `20260721T134213Z` · **NOT_EXECUTED** · requiere `HUMAN_Z3_ONE_STEP_TRAINING_APPROVAL`

## Criterios esperados (propuestos)
subset 1/1/1; `per_gpu_train_batch_size=1`; `grad_accum=1`; `--epochs 1`; CPU; seed 42; sin workers; sin fp16/distributed/knowledge/masked; scheduler linear; loss/grad finitos; `optimizer.step` una vez; eval val inherente; eval test; checkpoints/guardado/recarga del código.

## Fórmula (validar pre-run)
```
expected_steps = (len(train_dataloader) // gradient_accumulation_steps) * num_train_epochs
```
Con canario y `per_gpu=1`, `n_gpu=0→factor 1`, **esperado documentado = 1**.  
**No afirmar de antemano** que `global_step` será 1 sin validación pre-run. Divergencia → **NO-GO**.

## Resultados futuros
`Z3_ONE_STEP_REDUCED_TRAINING_PASS` u otros códigos de fallo listados en el prompt  
(**ninguno** = Table 4).

# Z3_ONE_STEP_REDUCED_TRAINING_REPORT — Prompt 14C

**Fecha ejecución:** 2026-07-22  
**RUN_ID:** `20260722T072146Z`  
**Clasificación:** **`Z3_ONE_STEP_REDUCED_TRAINING_PASS`**  
**Coste:** **0.00**  
**Aprobador:** EDMUNDO MORI ORRILLO (`HUMAN_DECISION_VERIFIED`)

## Intentos

| Attempt | RUN_ID | Resultado |
|---|---|---|
| 1 | `20260721T183611Z` | `Z3_OTHER_FAILED` — harness abortó por conteo de `scheduler.step` (init PyTorch + train) |
| 2 | `20260722T072146Z` | **PASS** — entrypoint nativo completó; evidencia en artefactos/logs |

Attempt-1 consumió la primera auth. Attempt-2 usó **reautorización humana** explícita (mensaje del investigador).

## Configuración

LC-QuAD2 QUESTION_ONLY; canary 8714/3988/6077; CPU; `--epochs 1`; batch 1; grad_accum 1; lr 6.25e-5; seed 42; pre-step budget **1**.

## Evidencia de un paso

- Log: una sola `Iteration 1/1`, train loss técnica ≈ 31.3  
- `checkpoint-1` escrito (global_step=1)  
- Eval val (`results 1`) + eval test  
- Guardado final + `training_args.bin` + `params.json`  
- Output ≈ 1.82 GB (< 6 GiB)  
- Sin red; sin downloads; upstream intacto  

**Nota harness:** el contador `Optimizer.step` no enganchó `transformers.AdamW.step` (override). PASS se basa en artefactos/logs nativos, no en ese contador.

## Claim boundary

`reduced_training_smoke_only`  
**No:** Table 4, PE3, convergencia, calidad, reproducción nativa completa, Answer F1.

## Estados

`audit_only`; `native_audit_complete=false`; `common_adapter_allowed=false`; PE3 `not_started`.

## Siguiente

Cierre documental Z3 / re-gate ZERO_COST (sin nuevo train sin auth). Pesos solo en workdir.

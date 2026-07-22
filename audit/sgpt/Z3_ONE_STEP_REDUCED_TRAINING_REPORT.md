# Z3_ONE_STEP_REDUCED_TRAINING_REPORT — Prompt 14C (actualizado 14D)

**Fecha ejecución:** 2026-07-22  
**RUN_ID (attempt 2):** `20260722T072146Z`  
**Coste:** **0.00**  
**Aprobador:** EDMUNDO MORI ORRILLO (`HUMAN_DECISION_VERIFIED`)

## Clasificación (con qualifier)

| Capa | Valor |
|---|---|
| Raw harness attempt 2 | **`Z3_OTHER_FAILED`** |
| Operativa / científica | **`Z3_ONE_STEP_REDUCED_TRAINING_PASS`** |
| Qualifier | **`PASS_WITH_INDIRECT_OPTIMIZER_STEP_VERIFICATION`** |
| Optimizer direct hook | **`NOT_VERIFIED_ATTEMPT2`** |
| Optimizer indirect | **`INDIRECT_CONTROL_FLOW_VERIFIED_HIGH_CONFIDENCE`** |

No usar “PASS” sin el qualifier.

---

## Raw harness versus scientific closure

### Attempt 2 — bruto (`RAW_HARNESS_VERIFIED`)

Fuente: `train-run.log` → `z3_one_step_raw_harness_report.json`

- `classification = Z3_OTHER_FAILED`
- `optimizer_step = 0`
- `backward = 1`
- `scheduler_step_total = 2`
- error: `optimizer_step=0 expected 1`

### Motivo técnico

El launcher parcheó `torch.optim.Optimizer.step`, pero el train nativo usa `transformers.AdamW`, cuyo `step` no fue interceptado. El contador quedó en 0 pese a completar la ruta de train.

### Interpretación post-run (operativa)

Entrypoint nativo completó: Iteration 1/1, loss técnica, backward×1, `checkpoint-1`, eval val/test, guardado final. Control de flujo en `upstream/sgpt/train.py` (líneas 105–120, 137–147) + artefactos ⇒ un optimizer step **indirecto** de alta confianza.

### Limitación

- No hay `OPTIMIZER_STEP_DIRECT_COUNTER_VERIFIED` ni `EXACT_OPTIMIZER_HOOK_PASS` en attempt 2.
- No se compararon pesos pre/post.
- `z3_one_step_report.json` del build fue sobrescrito en 14C con interpretación científica; el bruto se preserva en el log + JSON raw recuperado en 14D.

### Attempt 1

Raw `Z3_OTHER_FAILED` (`20260721T183611Z`): scheduler init contado; sin checkpoint. Auth attempt-1 consumida.

Reconciliación completa: `audit/sgpt/Z3_ONE_STEP_EVIDENCE_RECONCILIATION.md`

---

## Intentos

| Attempt | RUN_ID | Raw | Operativo |
|---|---|---|---|
| 1 | `20260721T183611Z` | `Z3_OTHER_FAILED` | abort harness |
| 2 | `20260722T072146Z` | `Z3_OTHER_FAILED` | PASS + qualifier indirecto |

## Configuración

LC-QuAD2 QUESTION_ONLY; canary 8714/3988/6077; CPU; `--epochs 1`; batch 1; grad_accum 1; lr 6.25e-5; seed 42; pre-step budget **1**.

## Claim boundary

`reduced_training_smoke_only`  
**No:** Table 4, PE3, convergencia, calidad, reproducción nativa completa, Answer F1.

## Estados (post-14D)

`smoke_only`; `native_audit_complete=true` (outcome smoke_only full repro not achieved); `common_adapter_allowed=false`; PE3 `not_started`.

## Siguiente

Prompt 15 (Q11) — gate final Fase 1; **no** nuevo train.

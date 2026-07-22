# Z3_ONE_STEP_EVIDENCE_RECONCILIATION — Prompt 14D

**Fecha:** 2026-07-22  
**Protocol RUN_ID:** `20260721T134213Z`  
**Attempt 2 RUN_ID:** `20260722T072146Z`  
**Coste:** USD **0.00** · sin ejecución en este prompt

## Jerarquía de evidencia (explícita)

1. **RAW_HARNESS_VERIFIED** — stdout/JSON del launcher (`z3_one_step_raw_harness_report.json` / `train-run.log`).
2. **NATIVE_LOG_VERIFIED** — logs del entrypoint nativo `train.py`.
3. **NATIVE_ARTIFACT_VERIFIED** — artefactos en workdir (checkpoint, eval_results, params).
4. **SOURCE_CONTROL_FLOW_VERIFIED** — líneas de `upstream/sgpt/train.py`.
5. **DIRECT_COUNTER_VERIFIED** — hooks del launcher que sí incrementaron.
6. **INDIRECT_CONTROL_FLOW_VERIFIED** / **HIGH_CONFIDENCE_INFERENCE** — conclusión cuando el hook falló.
7. **NOT_DIRECTLY_INSTRUMENTED** — lo que el hook no midió.

Las clasificaciones brutas **no se alteran**.

---

## A. Resultado bruto (attempt 2)

Fuente canónica recuperada del stdout en `train-run.log` →  
`environments/sgpt/builds/20260722T072146Z/z3_one_step_raw_harness_report.json`

| Campo | Valor |
|---|---|
| `classification` | **`Z3_OTHER_FAILED`** |
| `optimizer_step` | **0** |
| `backward` | **1** |
| `scheduler_step_total` | **2** |
| `scheduler_step_after_optimizer` | **0** |
| error | `optimizer_step=0 expected 1` |

Nota: `z3_one_step_report.json` fue sobrescrito en Prompt 14C con la interpretación científica. El bruto permanece en el log y en el JSON recuperado arriba. **No** usar el overwrite como bruto.

---

## B. Causa del hook

### Qué hizo el launcher

`scripts/smoke/sgpt_z3_one_step_train_launcher.py` (también copia en build attempt 2):

- Parchea **`torch.optim.Optimizer.step`** (no la clase concreta HF).
- Parchea `_LRScheduler.step` y `torch.Tensor.backward`.

### Qué usa upstream

`upstream/sgpt/train.py`:

```9:10:upstream/sgpt/train.py
from transformers import (
     AdamW,
```

```59:59:upstream/sgpt/train.py
    optimizer = AdamW(model.parameters(), lr=args.learning_rate, eps=args.adam_epsilon)
```

### Observación

- `backward=1` ⇒ el hook de `Tensor.backward` sí capturó el único backward.
- `optimizer_step=0` ⇒ la llamada real a `optimizer.step()` **no** pasó por el `Optimizer.step` parcheado.
- Interpretación conservadora (`HIGH_CONFIDENCE_INFERENCE`): `transformers.AdamW` define/overridea su propio `step` en la subclase; parchear solo `torch.optim.Optimizer.step` no intercepta ese método.

**Limitación 14D:** no se extrajo el fuente pin `transformers==4.25.1` como texto (prohibido Docker/import). La conclusión se apoya en launcher + import upstream + contadores observados.

**Etiquetas prohibidas para attempt 2:** `OPTIMIZER_STEP_DIRECT_COUNTER_VERIFIED`, `EXACT_OPTIMIZER_HOOK_PASS`.

---

## C. Evidencia de control de flujo (`train.py`)

Con canario 1 ejemplo, `per_gpu_train_batch_size=1`, `gradient_accumulation_steps=1`, `--epochs 1`, CPU:

```105:120:upstream/sgpt/train.py
                loss.backward()
            ...
                optimizer.step()
                if args.scheduler=="linear":
                    scheduler.step()
                ...
                optimizer.zero_grad()
                global_step += 1
```

Checkpoint nombrado con `global_step`:

```137:147:upstream/sgpt/train.py
            checkpoint_prefix = "checkpoint"
            output_dir = os.path.join(args.output_dir, "{}-{}".format(checkpoint_prefix, global_step))
            ...
            model_to_save.save_pretrained(output_dir)
```

Por tanto:

- Un único batch de train ⇒ como máximo un paso en el bloque `(step+1) % grad_accum == 0`.
- `checkpoint-1` solo aparece si `global_step` llegó a **1** tras ese bloque.
- Eval val (desc=`str(global_step)`), guardado final y eval test ocurrieron **después** (logs + `eval_results.txt`).

---

## D. Conclusión conservadora

| Campo | Valor |
|---|---|
| `experiment_operational_classification` | **`Z3_ONE_STEP_REDUCED_TRAINING_PASS`** |
| `verification_qualifier` | **`PASS_WITH_INDIRECT_OPTIMIZER_STEP_VERIFICATION`** |
| `optimizer_step_evidence` | **`INDIRECT_CONTROL_FLOW_VERIFIED_HIGH_CONFIDENCE`** |
| `optimizer_step_direct_hook` | **`NOT_VERIFIED_ATTEMPT2`** |
| raw launcher | permanece **`Z3_OTHER_FAILED`** |

### No se afirma

- interceptor directo de `optimizer.step` en attempt 2;
- comparación de parámetros pre/post;
- calidad, convergencia, Table 4, Answer F1;
- reproducción parcial o completa del artículo;
- PE3 iniciado.

### Attempt 1 (contexto)

Raw `Z3_OTHER_FAILED`: `optimizer_step=1`, `backward=1`, `scheduler_step=2` — abort porque el harness contó el `scheduler.step` de inicialización además del de train. Sin checkpoint/eval. Auth consumida.

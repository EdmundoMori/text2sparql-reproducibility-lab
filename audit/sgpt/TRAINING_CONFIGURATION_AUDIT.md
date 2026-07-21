# Auditoría de configuración de entrenamiento — SGPT

**Fecha:** 2026-07-20  
**Fuentes:** `config/gpt-2-base/params.json`, `train.py`, `README.md`, `utils/args.py`  
**Commit:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` (`PIN`)

---

## Hiperparámetros declarados

| Parámetro | Valor | Evidencia |
|---|---|---|
| `model_name_or_path` | `gpt2` | `CODE_VERIFIED` `params.json` |
| `num_train_epochs` (JSON) | **70** | `CODE_VERIFIED` |
| Epochs README ejemplo | **40** | `README_REPORTED` |
| README “probar” | 10, 20, 30, 40 o 70 | `README_REPORTED` |
| `learning_rate` | **6.25e-5** | `CODE_VERIFIED` `params.json` |
| LR sugerido README | 6e-4 o 6e-5 | `README_REPORTED` |
| `seed` | 42 | `CODE_VERIFIED` |
| `per_gpu_train_batch_size` | 4 | `CODE_VERIFIED` |
| `gradient_accumulation_steps` | 4 | `CODE_VERIFIED` |
| Batch efectivo | **16** | derivado |
| `warmup_steps` | 0 | `CODE_VERIFIED` |
| `fp16` | `""` (vacío) | `CODE_VERIFIED` |
| Scheduler | linear (default HF) | `CODE_VERIFIED` / default |
| `input_max_tokens` / `knowledge_max_tokens` | 50 / 50 | `CODE_VERIFIED` |
| `adam_epsilon` / `max_grad_norm` | 1e-8 / 1 | `CODE_VERIFIED` |

---

## Overrides CLI y bugs

| Tema | Hallazgo | Evidencia |
|---|---|---|
| `--epochs` | Documentado como override si ≠ −1; **`train.py` L267 asigna `params["num_train_epochs"]=fromcommand.epochs` incluso cuando `epochs == -1`** | `CODE_VERIFIED` — **BUG risk** |
| `--device` | CLI **ignorado**: se sobrescribe a `cuda:0` si CUDA disponible | `CODE_VERIFIED` |
| `--knowledge` / `--masked` | controlan variantes Q / Q_K / masked | `CODE_VERIFIED` + `README_REPORTED` |
| `eval_only` | path incompleto (`pass`) | `CODE_VERIFIED` |

---

## Guardado de checkpoints

| Comportamiento | Detalle | Evidencia |
|---|---|---|
| Por época | `checkpoint-{global_step}` | `CODE_VERIFIED` |
| Final | `runs/sgpt/{dataset}/` | `CODE_VERIFIED` / `README_REPORTED` |
| Best-only | `global_eval` asignado pero **nunca comparado** para retención selectiva | `CODE_VERIFIED` — criterio **unclear** |
| Presentes en clon | **ninguno** | `NOT_FOUND` |

---

## Dependencias de red en train

Primera ejecución descarga pesos/tokenizer **`gpt2`** desde Hugging Face → requiere red (`CODE_VERIFIED` / runtime).

Paper usó **2×12 GB** GPU (`PAPER_REPORTED` / contexto lab). Host lab: RTX 4050 **6 GiB** + RAM WSL ~7.4 GiB → factibilidad full native **condicional / not_ready** (ver `DEPENDENCY_AND_RUNTIME_AUDIT.md`, `EXECUTION_READINESS.md`).

---

## Comandos documentados (no ejecutados en esta auditoría)

```bash
# multi-GPU
python -m torch.distributed.launch train.py --dataset lcquad2 --epochs 40
# single GPU
python train.py --dataset lcquad2 --epochs 40
```

(`README_REPORTED` — **no** corridos aquí; restricción auditoría estática.)


---

## Prompt 14A — Z3 protocol definition (añadido)

- RUN_ID: `20260721T134213Z`
- Gate Z3: `READY_FOR_Z3_ARTIFACT_PREFLIGHT_AUTHORIZATION`
- Variante: lcquad2 QUESTION_ONLY CPU canary 1/1/1; expected optimizer steps = 1 (validar pre-run)
- GPT-2: `openai-community/gpt2` @ `607a30d7…` — **NOT_DOWNLOADED**
- tensorboardX==2.5.1 — **NOT_DOWNLOADED**
- Auths: dos formularios UNSIGNED en `docs/protocols/sgpt/z3/20260721T134213Z/`
- Informe: `audit/sgpt/Z3_REDUCED_TRAINING_PROTOCOL_REPORT.md`
- Gate Z2 permanece cerrado: `Z2_ENV_READY_PREFLIGHT_PASS`
- Conservado: `audit_only`; PE3 `not_started`; sin train

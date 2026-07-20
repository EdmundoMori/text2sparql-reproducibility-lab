# CHECKPOINT_AND_TRAINING_ARTIFACT_INVENTORY — firesparql

**Fecha:** 2026-07-20  
**pinned_commit:** `48d6f168e4c1dd3dc467553aef370299911d4e76` (`PIN`)

---

## Checkpoints / pesos

| Artefacto | En git | Ubicación | Licencia | Evidencia |
|---|---|---|---|---|
| Mejor FT 8B 15ep | **no** | HF `Sherry791/Meta-Llama-3-8B-Instruct-ft4sciqa` | MIT en **model card** | `README_REPORTED`; `EXTERNAL_ARTIFACT_REFERENCED` |
| `merge_models/*` (merged LoRA) | **no** | referenciado `codes/run_all_generate.sh` | N/A | `CODE_VERIFIED`; dir `NOT_FOUND` |
| Adapters LoRA crudos | **no** | UNKNOWN (prob. LLaMa-Factory) | UNKNOWN | `NOT_FOUND` |
| Bases Meta-Llama 3 8B / 3.2 3B | **no** | HF (comentarios/result names) | licencia Meta externa | `INFERENCE` / `RESULT_FILE_VERIFIED` naming |

**Importante:** el MIT del checkpoint HF **no** se transfiere al código GitHub (`LICENSE_NOT_CONFIRMED` / `LICENSE ABSENT`).

---

## Artefactos de entrenamiento en este repo

| Item | Estado | Evidencia |
|---|---|---|
| `peft` / `LoraConfig` / `SFTTrainer` / `Trainer` | **NOT_FOUND** | grep estático `.py` |
| `train*.py` de FT | **NOT_FOUND** | find |
| Scripts que **sí** existen | `SciQA-training-transformation.py`, `dblp-training-transformation.py` | solo JSON→`instruction`/`input`/`output` — **no** trainer (`CODE_VERIFIED`) |
| Evidencia training externo | paths `/Users/sherrypan/GitHub/LLaMa-Factory/...` | `one_shot_mapping.py`, notebooks (`CODE_VERIFIED`) |
| Hiperparámetros LoRA (lr, rank, alpha, dropout, batch…) | **UNKNOWN** en este repo | solo epochs=15 “best” (`README_REPORTED` / `PAPER_REPORTED`) |

---

## Datos de FT presentes (`DATA_VERIFIED`)

| Archivo | n | Campos |
|---|---|---|
| `experiment_datasets/sciqa/project_data/sciqa_training_data4ft.json` | 1795 | instruction/input/output |
| `experiment_datasets/dblp/project_data/dblp_training_data4ft.json` | 7000 | instruction/input/output |

sha256: ver `logs/static-audit-firesparql/dataset_inventory_raw.json` y `DATASET_INVENTORY.csv`.

---

## Naming de runs FT en results (`RESULT_FILE_VERIFIED`)

Patrón: `llama3_{8b|3.2_3b}_lora_sft_{3,5,7,10,15,20}epochs_round{1,2,3}` bajo `results/step1_generated_text/ft/` (36 configs × 513 txt).

Esto **demuestra** que los autores ejecutaron inferencia multi-época/multi-round, **no** que el trainer esté en el árbol.

---

## Implicación readiness

- `CHECKPOINT_METADATA_CHECK`: **conditional** (requeriría HF; **no** en esta pasada).  
- `FINE_TUNING_REPRODUCTION`: **not_ready** (trainer ausente; externo LLaMa-Factory).  
- `COMMON_EVALUATION_ADAPTATION`: **legally_blocked** (código sin LICENSE confirmada; adapters).

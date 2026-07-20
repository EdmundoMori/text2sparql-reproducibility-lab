# FINE_TUNING_REPRODUCIBILITY_AUDIT — firesparql

**Fecha:** 2026-07-20  
**Veredicto:** `FINE_TUNING_REPRODUCTION = not_ready`

---

## Qué hay vs qué falta

| Elemento | Estado | Evidencia |
|---|---|---|
| Datos SciQA en formato instruction | presente (1795) | `DATA_VERIFIED` `sciqa_training_data4ft.json` |
| Datos DBLP FT | presente (7000) | `DATA_VERIFIED` |
| Script conversión JSON→FT | presente | `SciQA-training-transformation.py` / `dblp-…` (`CODE_VERIFIED`) |
| Trainer LoRA / SFT en repo | **ausente** | `NOT_FOUND` peft/LoraConfig/SFTTrainer/train*.py |
| Config YAML/JSON de LLaMa-Factory | **ausente** | `NOT_FOUND` |
| `merge_models/` | **ausente** | `NOT_FOUND` |
| Checkpoint HF 15ep | externo | `EXTERNAL_ARTIFACT_REFERENCED` |
| Claim “LoRA 15 epochs best” | paper/README | `PAPER_REPORTED` / `README_REPORTED` |
| lr, rank, alpha, target modules, batch, sched | **UNKNOWN** | no en este árbol |

---

## Evidencia de entrenamiento externo

Paths absolutos a **LLaMa-Factory** en:

- `experiment_datasets/codes/one_shot_mapping.py`  
- notebooks bajo `experiment_datasets/codes/` y `codes/merge_sparql.ipynb`  

(`CODE_VERIFIED`) → el entorno de entrenamiento real estaba en otra máquina/repo.

`run_all_generate.sh` invoca:

```text
python generate_sparql_cuda.py "merge_models/$MODEL" ...
```

sin que `merge_models/` exista en el clon (`CODE_VERIFIED` + `NOT_FOUND`).

---

## Implicaciones

1. **No** se puede afirmar reproducción nativa del fine-tuning solo con este git.  
2. Re-entrenar requeriría reconstruir experimento LLaMa-Factory (fuera de alcance / no documentado aquí) → `domain_specific` + `EXTERNAL`.  
3. Inferencia del “best” modelo podría usar HF (`CHECKPOINT_METADATA_CHECK` / `8B_CHECKPOINT_INFERENCE`) pero: licencia código GitHub `LICENSE_NOT_CONFIRMED`; VRAM 6 GiB bloquea 8B fp16 sin quant ≠ paper.  
4. Transform scripts **no** son el trainer — no confundir preparación de datos con training.

---

## UNKNOWNs intencionales

- Hiperparámetros LoRA exactos.  
- Semilla(s), hardware de train, duración, merge procedure.  
- Si el HF checkpoint es idéntico byte-a-byte a `merge_models/llama3_8b_lora_sft_15epochs` usado en results.

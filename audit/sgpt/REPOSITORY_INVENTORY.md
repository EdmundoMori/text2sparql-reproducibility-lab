# Inventario de repositorio — SGPT (WAVE_B)

**Fecha auditoría:** 2026-07-20  
**Upstream:** `upstream/sgpt/`  
**Pinned commit:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` (`PIN`)  
**Etiquetas:** `PIN` | `CODE_VERIFIED` | `DATA_VERIFIED` | `README_REPORTED` | `NOT_FOUND` | `UNKNOWN`

---

## Identificación

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `sgpt` | lab `METHOD_REGISTRY.yaml` |
| upstream remoto | https://github.com/rashad101/SGPT-SPARQL-query-generation | `REPOSITORIES.lock.yaml` |
| commit pin | `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` | `PIN` |
| licencia | MIT | `PIN` / `upstream/sgpt/LICENSE.md` |
| paper | IEEE Access 2022, DOI 10.1109/ACCESS.2022.3188714 | `PIN` / `README_REPORTED` |

---

## Escala del árbol

| Métrica | Valor | Evidencia |
|---|---|---|
| Archivos (excl. `.git_local`) | **43** | `REPO` |
| Tamaño aproximado | **~218 M**, mayormente `data/` | `REPO` / `audit/CLONING_REPORT.md` |
| Checksums SHA-256 | `logs/static-audit-sgpt/all_file_checksums.sha256` | `DATA_VERIFIED` |
| Inventario datasets | `logs/static-audit-sgpt/dataset_inventory_raw.json` | `DATA_VERIFIED` |

---

## Árbol lógico (código y config)

| Path | Rol | Evidencia |
|---|---|---|
| `train.py` | entrenamiento LM GPT-2 custom | `CODE_VERIFIED` |
| `eval.py` | generación + métricas léxicas | `CODE_VERIFIED` |
| `measure.py` | utilidades de medición / helpers | `CODE_VERIFIED` |
| `scripts/model.py` | arquitectura SGPT (GPT-2 + encoder sintáctico) | `CODE_VERIFIED` |
| `scripts/dataset_lcquad2.py` | dataset LC-QuAD 2.0 + `format_knowledge` / mask | `CODE_VERIFIED` |
| `scripts/dataset_qald9.py` | dataset QALD-9 | `CODE_VERIFIED` |
| `scripts/dataset_vquanda.py` | dataset VQuAnDa | `CODE_VERIFIED` |
| `utils/args.py` | CLI (`--knowledge`, `--masked`, `--epochs`, …) | `CODE_VERIFIED` |
| `utils/metrics.py` | BLEU / F1 / SP-* / METEOR / ROUGE | `CODE_VERIFIED` |
| `utils/data.py`, `dataset_utils.py`, `dptree.py` | carga, features sintácticas | `CODE_VERIFIED` |
| `config/gpt-2-base/params.json` | HPs entrenamiento | `CODE_VERIFIED` |
| `config/gpt-2-base/generation_params.json` | HPs generación | `CODE_VERIFIED` |
| `requirements.txt` | deps Python | `CODE_VERIFIED` |
| `README.md` | install / train / eval | `README_REPORTED` |
| `LICENSE.md` | MIT | `PIN` |

---

## Datos embebidos

| Path | Contenido | Evidencia |
|---|---|---|
| `data/lcquad2/{train,val,test}.json` | splits procesados + POS/dep | `DATA_VERIFIED` |
| `data/lcquad2/original/*` | mismos splits sin features token-level POS/dep IDs | `DATA_VERIFIED` |
| `data/qald9/{train,val,test}.json` + `original/` | DBpedia QALD-9 | `DATA_VERIFIED` |
| `data/vquanda/{train,val,test}.json` + `original/` | DBpedia VQuAnDa | `DATA_VERIFIED` |
| `data/*/pos_mapping.json`, `dep_mapping.json` | vocabularios sintácticos | `DATA_VERIFIED` |

---

## Artefactos de modelo / entrenamiento — ausentes

Búsqueda estática (`REPO` / `NOT_FOUND`):

- `pytorch_model.bin`, `*.safetensors`
- `checkpoint-*`, `runs/`, `outputs/`
- `tokenizer.json`, `merges.txt`, `vocab.json`
- `training_args.bin`, `eval_results.txt`
- logs TensorBoard

**Conclusión:** el clon trae código + datos; **no** trae checkpoints ni resultados de corridas. Ver `CHECKPOINT_AND_RESULTS_INVENTORY.md`.

---

## Git local

El clone lab usa `.git_local/` (no `.git` estándar) para aislamiento; HEAD alineado al pin `1f6964d…` (`PIN`).

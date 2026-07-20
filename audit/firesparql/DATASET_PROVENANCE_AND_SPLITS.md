# DATASET_PROVENANCE_AND_SPLITS — firesparql

**Fecha:** 2026-07-20  
**Inventario tabular:** `DATASET_INVENTORY.csv`  
**Checksums crudos:** `logs/static-audit-firesparql/dataset_inventory_raw.json`

---

## SciQA / ORKG (pipeline principal)

| Artefacto | n / nota | sha256 (prefijo) | Evidencia |
|---|---|---|---|
| `project_data/test_questions.csv` | 513; id/question/query | `14c2ad8c…` | `DATA_VERIFIED` |
| `project_data/train_questions.csv` | 1795 | `ae532eb3…` | `DATA_VERIFIED` |
| `most_similar_questions.csv` | 513 | `9b4150dd…` | `DATA_VERIFIED` |
| `sciqa_training_data4ft.json` | 1795 instruction | `739c183c…` | `DATA_VERIFIED` |
| `orkg-property.json` | 9062 property/label | `220f6d3d…` | `DATA_VERIFIED` |
| `rag_files/orkg-property.json` | copia misma hash | `220f6d3d…` | `DATA_VERIFIED` |
| `handcrafted.csv` | 100 | `e364ffdd…` | `DATA_VERIFIED` |
| `all.json` + train/test/valid questions+answers | dumps oficiales | ver inventory | `DATA_VERIFIED` |

README: test SciQA 513 (`README_REPORTED`) — coincide CSV (`DATA_VERIFIED`).

Procedencia upstream SciQA: notebooks leen paths `QAoverSKGs/SciQA-dataset` y LLaMa-Factory (`EXTERNAL_ARTIFACT_REFERENCED` / historial autores).

---

## DBLP (presente, no pipeline principal)

| Artefacto | n | Evidencia |
|---|---|---|
| `dblp_training_data4ft.json` | 7000 | `DATA_VERIFIED` |
| `test_questions.csv` | 2000 | `DATA_VERIFIED` |
| train/valid/test questions+answers JSON | presentes | `DATA_VERIFIED` |

No hay familia `results/step1/...` DBLP (`RESULT_FILE_VERIFIED` ausencia → `INFERENCE`: DBLP no es el eje del paper table README).

---

## Splits y fugas

- One-shot usa **SPARQL gold de train** como ejemplo → diseño few-shot, no leakage test→train de la query objetivo, pero sí información privilegiada de train (`CODE_VERIFIED`).  
- Overlap IDs train∩test: **no recalculado** en esta pasada (evitar pandas) → `UNKNOWN` formal; conteos independientes 1795/513.

---

## Paths de consumo

Scripts esperan `xueli_data/sciqa/project_data/...` mientras el clon guarda `experiment_datasets/sciqa/project_data/...` (`CODE_VERIFIED` vs layout `DATA_VERIFIED`) → hace falta symlink/copia para smokes futuros.

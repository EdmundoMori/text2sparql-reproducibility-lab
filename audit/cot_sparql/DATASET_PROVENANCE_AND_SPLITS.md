# Procedencia y splits — CoT-SPARQL

**Fecha:** 2026-07-20  
**Etiquetas:** `DATA_VERIFIED` | `PAPER_REPORTED` | `README_REPORTED` | `CODE_VERIFIED` | `NOT_FOUND` | `INFERENCE`

---

## Datasets en el repositorio

| Archivo | n | Split presente | KG (paper/README) | Evidencia |
|---|---|---|---|---|
| `qald_10_train.json` | **412** | train only | Wikidata (QALD-10) | `DATA_VERIFIED` + `PAPER_REPORTED` |
| `train_lcquad2.json` | **21497** | train only | Wikidata | `DATA_VERIFIED` |
| `train_qald.json` | **350** | train only | DBpedia (QALD-9) | `DATA_VERIFIED` |
| `train_vquanda.json` | **3500** | train only | DBpedia | `DATA_VERIFIED` |

**Test / validation:** **NOT_FOUND** en el árbol (`dataset/` solo trains + `gitignore`). El paper reporta experimentos sobre benchmarks con test (`PAPER_REPORTED`); el código publicado **no** incluye scripts ni splits de evaluación (`CODE_VERIFIED` / `NOT_FOUND`).

Checksums SHA-256: `logs/static-audit-cot-sparql/all_file_checksums.sha256` → `DATASET_INVENTORY.csv`.

---

## Uso en el método

| Uso | Fuente | Notas |
|---|---|---|
| Few-shot retrieval Wikidata | parquet desde LC-QuAD2 train (notebook) | gold `new_LabelsEnt` / `newPredLabels` |
| Few-shot retrieval DBpedia | parquet esperado desde QALD-9 train + VQuAnDa train | gold `entities` / `relations`; export notebook incompleto |
| Eval paper (BLEU/F1/…) | **no implementada en repo** | métricas solo `PAPER_REPORTED` |
| `qald_10_train.json` | presente | **no** referenciado por `main.py`/`contextb.py` en path runtime (`CODE_VERIFIED` ausencia de refs) — posible material experimental/`INFERENCE` |

---

## Esquemas observados (`DATA_VERIFIED`)

- **QALD-10:** `{"questions":[…]}` con `id`, `question`, `query`, `answers`.  
- **LC-QuAD2:** lista; campos incl. `question`, `sparql_wikidata`, `new_LabelsEnt`, `newPredLabels`, …  
- **QALD-9 style / VQuAnDa:** `en_ques`, `sparql`, `entities`, `relations`, …

---

## Gaps vs paper

| Tema | Paper | Repo | Etiqueta |
|---|---|---|---|
| Splits test | usados en tablas | ausentes | `PAPER_REPORTED` vs `NOT_FOUND` |
| Predicciones | tablas métricas | ausentes | `NOT_FOUND` |
| Embeddings empaquetados | enlaces README | no en git | `EXTERNAL_ARTIFACT_REFERENCED` |

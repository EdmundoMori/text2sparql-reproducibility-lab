# Procedencia y splits de datasets — SGPT

**Fecha:** 2026-07-20  
**Fuentes de conteo:** `logs/static-audit-sgpt/dataset_inventory_raw.json` (`DATA_VERIFIED`)  
**Checksums:** `logs/static-audit-sgpt/all_file_checksums.sha256` (`DATA_VERIFIED`)  
**Commit:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` (`PIN`)

---

## Conteos procesados (`DATA_VERIFIED`)

| Dataset | Train | Val | Test | KG (campo SPARQL) |
|---|---:|---:|---:|---|
| LC-QuAD 2.0 (`lcquad2`) | 21497 | 2389 | **5969** | Wikidata (`sparql_wikidata`) |
| QALD-9 (`qald9`) | 350 | 58 | 150 | DBpedia (`sparql`) |
| VQuAnDa (`vquanda`) | 3500 | 500 | 1000 | DBpedia (`sparql`) |

Los conteos de `original/` coinciden con los procesados (mismos *n*).

---

## Mismatch paper vs datos locales

| Afirmación | Valor | Evidencia |
|---|---|---|
| Paper Table 2 / notas Table 4 — test LC-QuAD 2.0 | **6046** (citado a menudo) | `PAPER_REPORTED` / `RESULT_EVIDENCE_MATRIX.csv` |
| Split procesado en repo | **5969** | `DATA_VERIFIED` |
| Diferencia | **77** ejemplos | `MISMATCH` |

Cualquier comparación futura Table 4 ↔ eval local debe etiquetar este desfase.

---

## Procesado vs original

| Capa | Contenido | Evidencia |
|---|---|---|
| `data/{ds}/{split}.json` | incluye `question_pos_ids`, `question_dep_ids`, `question_dep_lvl`, `mapping`, etc. | `DATA_VERIFIED` |
| `data/{ds}/original/{split}.json` | mismos ejemplos **sin** features token-level POS/dep IDs | `DATA_VERIFIED` |
| `pos_mapping.json` / `dep_mapping.json` | vocabularios por dataset | `DATA_VERIFIED` |

El path de entrenamiento documentado usa los JSON **procesados** (features sintácticas requeridas por el modelo).

---

## Fuga / reutilización de IDs entre splits

| Dataset | train∩val | train∩test | val∩test | Evidencia |
|---|---:|---:|---:|---|
| lcquad2 (`uid`) | 0 | 0 | 0 | `DATA_VERIFIED` |
| vquanda (`id`) | 0 | 0 | 0 | `DATA_VERIFIED` |
| **qald9 (`id`)** | 0 | **150** | 0 | `DATA_VERIFIED` |

**QALD-9:** los 150 IDs de `test` están contenidos en `train` (train=350 → 200 solo-train + 150 compartidos). Comparación de `en_ques`+`sparql` sobre el solapamiento: **0** pares idénticos (`DATA_VERIFIED`) → no es copia exacta del ejemplo, sino **reutilización de identificadores** con contenido distinto. Riesgo de confusión en análisis por ID; no demuestra contamination textual exacta.

---

## Duplicados exactos (pregunta, SPARQL)

| Dataset / split | `exact_q_sparql_dups` | Evidencia |
|---|---:|---|
| lcquad2 train / val / test | 303 / 6 / 19 | `DATA_VERIFIED` |
| qald9 original train | 3 | `DATA_VERIFIED` |
| qald9 procesado; vquanda todos | 0 | `DATA_VERIFIED` |

Duplicados intra-split no equivalen a leakage entre splits.

---

## Entidades / conocimiento auxiliar

Ver detalle en `ARCHITECTURE_AND_DATA_FLOW.md` y `CONFIGURATION_AND_VARIANTS_MATRIX.csv`:

- LC-QuAD 2.0 + `--knowledge`: QIDs desde `new_LabelsEnt` filtrados por aparición en gold SPARQL (`INFERENCE` + `CODE_VERIFIED`).
- QALD-9 / VQuAnDa + `--knowledge`: lista `entities` sin filtro SPARQL en código (`CODE_VERIFIED`).
- Sin EL/RL en inferencia (`CODE_VERIFIED`).

---

## Citas de integridad

- Inventario crudo: `logs/static-audit-sgpt/dataset_inventory_raw.json`
- SHA-256 por archivo: `logs/static-audit-sgpt/all_file_checksums.sha256`
- Tabla tabular: `audit/sgpt/DATASET_INVENTORY.csv`

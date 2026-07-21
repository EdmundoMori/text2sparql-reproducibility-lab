# DATA_AND_ARTIFACT_CONTRACT — SGPT

**Fuente conteos/checksums:** `audit/sgpt/DATASET_INVENTORY.csv` (`DATA_VERIFIED`)  
**Prohibición:** no modificar datos en `upstream/sgpt/data/`. Escrituras solo en `workdir/` / logs lab.

---

## LC-QuAD2 (Wikidata)

| Split | Path | n | sha256 (prefijo) |
|---|---|---:|---|
| train | `data/lcquad2/train.json` | 21497 | e001876e… |
| val | `data/lcquad2/val.json` | 2389 | c521855f… |
| test | `data/lcquad2/test.json` | **5969** | 0f1b754e… |

Campos: `question`, `sparql_wikidata`, entidades `new_LabelsEnt` / `entities` / `ent_id`; POS/dep en versión no-original.

**Split drift:** test **5969** en repo vs ~**6046** en paper — **reportar**, no “corregir”.

## QALD9 (DBpedia)

| Split | n |
|---|---:|
| train | 350 |
| val | 58 |
| test | 150 |

**Split drift:** QALD9 reutiliza **150 IDs** entre train y test (`DATASET_PROVENANCE_AND_SPLITS.md`) — reportar, no corregir.

spaCy: `dataset_qald9.py` → `en_core_web_sm`.

## VQuAnDa (DBpedia)

| Split | n |
|---|---:|
| train | 3500 |
| val | 500 |
| test | 1000 |

## Escritura permitida (lab)

- `workdir/sgpt/**` (gitignored)  
- `logs/**`, `experiments/native/sgpt/**` futuros  

## Escritura prohibida

- Cualquier path bajo `upstream/sgpt/`

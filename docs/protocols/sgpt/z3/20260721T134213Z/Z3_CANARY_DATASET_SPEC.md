# Z3_CANARY_DATASET_SPEC

**RUN_ID:** `20260721T134213Z`  
**Etiquetas:** `PROPOSED_CANARY`; `RESOURCE_CANARY_NOT_REPRESENTATIVE`; `NOT_FOR_METRIC_COMPARISON`  
**Selección:** `DATA_VERIFIED` (lectura RO de JSON; **sin** ejecutar Dataset)

## Tamaños
| Split | n | uid seleccionado | record_sha256 |
|---|---|---|---|
| train | 1 | `8714` | `9bec27f17bdec58e145a83caa6fb62e962d4299be8504ab9c2c70c4c3b74ab78` |
| val | 1 | `3988` | `472dedd3e90fef308ea160f534ea427ae31a65e3192100fc80e4137660be7f08` |
| test | 1 | `6077` | `04c8d8b13f704aa19b00b468b33aa8e753c1020fc71d57a99a077a124c7a033b` |

**subset_manifest_sha256:** `97f3c8b40c140ed5d88fa3426a5d0800ce9f77f4961f5c33249a3ffd0e77e37e`  
Algoritmo: `sgpt-z3-canary-v1` — detalle en `Z3_CANARY_SELECTION.json`.

## Límites de longitud (protocolo)
- `input_max_tokens=50`, `knowledge_max_tokens=50` (params upstream)
- Filtro estático canario: question ≤200 chars; SPARQL ≤500 chars
- Embeddings POS/DEP/level tamaño **50** (`scripts/model.py`); IDs mapeados deben ser `<50`

## Estructura futura (no creada en 14A)
```
workdir/runs/sgpt-z3/20260721T134213Z/source/data/lcquad2/
  train.json  val.json  test.json
  dep_mapping.json  pos_mapping.json   # copia sin alteración desde upstream
```
**Prohibido** escribir en `upstream/sgpt/data`.

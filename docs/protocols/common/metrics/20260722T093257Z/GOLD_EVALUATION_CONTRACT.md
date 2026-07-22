# GOLD_EVALUATION_CONTRACT

**RUN_ID:** `20260722T093257Z` · `GOLD_CONTRACT_DEFINED` · `GOLD_MATERIALIZATION_PENDING`

## Reglas

- Gold SPARQL y respuestas **no** se exponen al adapter.
- Respuestas gold comunes se materializarán ejecutando gold SPARQL sobre el **mismo** grafo fijado.
- Respuestas históricas del dataset = evidencia separada (no mezclar grafos).
- Gold inválido/incompatible → adjudicación global (no fallo de un método).
- Resultado gold vacío **válido** ≠ defecto.
- Estado actual: `GOLD_MATERIALIZATION_PENDING` · `DATASET_PAYLOAD_NOT_ACQUIRED` · `GRAPH_SNAPSHOT_ACQUISITION_PENDING`.

Schema: `configs/common/GOLD_EVALUATION_RECORD_SCHEMA.json`.

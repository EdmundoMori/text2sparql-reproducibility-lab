# Blocker taxonomy (Prompt 25R1)

**Version:** 1.0.0-25R1 · **RUN_ID:** `20261012T122043Z`

Machine-readable: `configs/common/recovery/BLOCKER_TAXONOMY.yaml`

| Class | Meaning |
|---|---|
| B_LEGAL | licencia/copyright/redistribución |
| B_COST | servicio o compute de pago |
| B_HARDWARE | GPU/RAM/disk/CPU insuficiente |
| B_MODEL | checkpoint/modelo ausente o incompatible |
| B_ARTIFACT | embeddings/index/config/runner/trainer ausente |
| B_RUNTIME | incompatibilidad de entorno |
| B_SERVICE | endpoint/linker/API externo requerido |
| B_DATASET | dataset/split/provenance |
| B_GRAPH | KG/snapshot/endpoint runtime |
| B_EVALUATION | métrica/evaluator |
| B_IMPLEMENTATION | bug/dead code/missing runner |
| B_DOMAIN | dominio/KG distinto |
| B_FAIRNESS | input access incompatible entre tracks |
| B_REPRODUCIBILITY | dependencia mutable |
| B_POLICY | ZERO_COST / lab protocol |

Un blocker puede tener varias clases.

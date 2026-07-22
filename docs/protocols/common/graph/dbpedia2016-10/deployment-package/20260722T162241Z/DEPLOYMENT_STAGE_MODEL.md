# Deployment stage model (D0–D7)

**RUN_ID:** `20260722T162241Z` · Tag: `DEPLOYMENT_STAGES_SEPARATED`

| Stage | Name | Auth | Now |
|---|---|---|---|
| D0 | Resource & runtime package | documentary | **THIS PROMPT** |
| D1 | Resource configuration (`.wslconfig`/swap) | profile selection | pending |
| D2 | Decompression + static RDF validation | execution auth | blocked |
| D3 | Runtime image acquisition (digest pull) + config | execution auth | blocked |
| D4 | Virtuoso load | execution auth | blocked |
| D5 | Graph runtime technical validation | execution auth | blocked |
| D6 | Gold materialization | separate gates | blocked |
| D7 | Common evaluation | adapters+benchmark | blocked |

Each stage has dedicated contracts/gates. Acquisition auth `AUTH_DBPEDIA2016_10_ACQ_20260722T134313Z_EMO_01` is **consumed** and **not reusable**.
See `audit/PHASE2_DBPEDIA_DEPLOYMENT_STAGE_GATE_MATRIX.csv`.

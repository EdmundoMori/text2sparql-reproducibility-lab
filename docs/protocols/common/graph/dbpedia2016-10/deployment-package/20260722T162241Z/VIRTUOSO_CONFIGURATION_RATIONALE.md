# Virtuoso configuration rationale

Template: `configs/common/graph/dbpedia2016-10/deployment/VIRTUOSO_INI_TEMPLATE.ini`

Parameterized until human profile selection:

- `NumberOfBuffers` / `MaxDirtyBuffers` from RAM profile
- `MaxQueryMem`, `MaxQueryExecutionTime`, `ResultSetMaxRows` for eval fairness
- `DirsAllowed` limited to layout paths
- DB/trx/log under `virtuoso/` layout
- Publish ports only on `127.0.0.1`
- Post-load read-only transition in D4/D5 procedures

Tag: `LOADER_CONFIGURATION_DOCUMENTED`. **Not executed.**

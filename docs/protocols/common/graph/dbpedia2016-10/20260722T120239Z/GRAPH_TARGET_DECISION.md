# Graph target decision

**RUN_ID:** `20260722T120239Z`

## Primary

- `primary_graph_target`: **DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT**
- `graph_target_version`: **2016-10**
- `evaluation_label`: **QALD9PLUS_EN_DBPEDIA_NATIVE_GRAPH**
- Tags: `GRAPH_TARGET_NATIVE_SELECTED` · `QALD9_NATIVE_GRAPH_DBPEDIA_2016_10`

## Fallback

- `fallback_graph_target`: **MODERN_IMMUTABLE_DBPEDIA_SNAPSHOT_REBASE**
- `fallback_label`: **COMMON_GRAPH_REBASE**
- Tag: `COMMON_GRAPH_REBASE_FALLBACK_DEFINED`
- Not selected merely for easier deployment.

## Rejected as primary

- Current public DBpedia endpoint → `REMOTE_MUTABLE_ENDPOINT_REJECTED_FOR_REPRODUCIBLE_PRIMARY`
- Query-coverage subgraph → `QUERY_COVERAGE_SUBGRAPH_REJECTED_FOR_PRIMARY`
- Third-party historical endpoint without verifiable snapshot

## Conditional note

File scope **not fully closed** (33 checksum-listed files HTTP 404; `core/` symlinks broken). Target remains scientifically primary; package gate is conditional.

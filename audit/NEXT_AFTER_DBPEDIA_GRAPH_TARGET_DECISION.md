# NEXT AFTER DBpedia graph target decision

| Campo | Valor |
|---|---|
| Prompt | 23 |
| RUN_ID | `20260722T120239Z` |
| Gate | `DBPEDIA_2016_10_NATIVE_GRAPH_TARGET_SELECTED_PACKAGE_CONDITIONAL_FILE_SCOPE` |
| Selected target | `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` |
| Fallback | `MODERN_IMMUTABLE_DBPEDIA_SNAPSHOT_REBASE` / `COMMON_GRAPH_REBASE` |
| File scope | CONDITIONAL (33 unavailable; core/ 404 resolved partially) |
| Serialization | ttl.bz2 core+LHD; links as published |
| File count (available) | 81 |
| Compressed total (available) | 5023159516 |
| Checksum coverage | PARTIAL MD5 |
| License | CC BY-SA 3.0 + GFDL evidence recorded |
| Resource class | `CONDITIONAL_HIGH_RISK` |
| Authorization | UNSIGNED / form `NOT_READY_CONDITIONAL` |
| Acquisition | NOT_ACQUIRED |
| Deployment | NOT_DEPLOYED |
| G4 | TARGET_DOCUMENTED / RUNTIME_NOT_SATISFIED |
| **Siguiente acción única** | **`CLOSE_DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_FILE_SCOPE`** |
| Reserved prompt | **Prompt 23B** — cierre documental del file scope endpoint-equivalent (ZERO_COST, sin descargar) |
| Later reserved | Prompt 24B acquisition (solo tras auth humana y scope cerrado) |
| Prohibited now | RDF download, Docker pull, Virtuoso, SPARQL, gold, metrics, adapters, benchmark, auto-auth |
| Stop | cualquier GET de payload; reuse auth QALD; cost > 0 |

Prompt 22 metadata reconciliada:

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `3818db51b9468bc4b7b74b7b783a76c96d102b43` |
| publication metadata commit / remote tip | `831f34b8aa488d17200a29ec9d04c76796adbbcf` |

## Commits Prompt 23

- ARTIFACT_COMMIT: `e24e36c2cc65692b981e7f1e7990d4bfcce496c7`
- publication metadata commit: `9b0a56273505cb9967d0f505ed3ba216e92287b2`

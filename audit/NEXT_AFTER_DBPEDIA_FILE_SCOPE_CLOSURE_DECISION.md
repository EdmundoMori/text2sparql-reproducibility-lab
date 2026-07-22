# NEXT AFTER DBpedia file-scope closure

| Campo | Valor |
|---|---|
| Prompt | 23B |
| RUN_ID | `20260722T132719Z` |
| Gate | `DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_FILE_SCOPE_CLOSED_PARTIAL_PUBLISHED_CHECKSUMS_READY_FOR_HUMAN_ACQUISITION_AUTHORIZATION` |
| Blockers in | 33 |
| Resolved | 33 |
| Unresolved required | **0** |
| Root-cause | wrong `en/` path for `*_en_uris_<lang>`; canonical `core-i18n/<lang>/` |
| Core alias | broken symlink listing → canonical lang/en paths |
| Ontology | `NOT_DOCUMENTED_AS_ENDPOINT_COMPONENT` |
| Final file count | **114** |
| Final compressed total | **6925795437** |
| Checksum coverage | 98.2456% files / 98.7587% bytes |
| No-checksum files | 2 LHD |
| Acquisition resources | FEASIBLE_CURRENT_DISK_CONDITIONAL_HUMAN_AUTHORIZATION |
| Deployment resources | CONDITIONAL_HIGH_RISK_REQUIRES_SEPARATE_RESOURCE_AND_DEPLOYMENT_GATE |
| Form | `READY_UNSIGNED` |
| Authorization | UNSIGNED / null |
| Acquisition | NOT_ACQUIRED |
| Deployment | NOT_DEPLOYED |
| G4 | TARGET_DOCUMENTED / RUNTIME_NOT_SATISFIED |
| **Siguiente acción** | **`HUMAN_DBPEDIA_2016_10_GRAPH_ACQUISITION_AUTHORIZATION`** |
| Status | HUMAN_GATE_REQUIRED |
| Reserved prompt | Prompt 24B — compressed-only acquisition (after human approval) |
| Prohibited | RDF download now; decompress; Virtuoso; SPARQL; gold; metrics; adapters; benchmark; auto-auth |

## Prompt 23 metadata reconciliada

| Campo | SHA |
|---|---|
| initial HEAD | `831f34b8aa488d17200a29ec9d04c76796adbbcf` |
| ARTIFACT_COMMIT | `e24e36c2cc65692b981e7f1e7990d4bfcce496c7` |
| publication / tip | `9b0a56273505cb9967d0f505ed3ba216e92287b2` |

## Commits Prompt 23B

- ARTIFACT_COMMIT: `5fbbcc47a5a4d28c264ec6c20c4a6212ac870904`

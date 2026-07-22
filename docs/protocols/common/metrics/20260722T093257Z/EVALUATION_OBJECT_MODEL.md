# EVALUATION_OBJECT_MODEL

**RUN_ID:** `20260722T093257Z`

| Objeto | Procedencia | Visible método | Visible evaluador | Hash | Materialización |
|---|---|---|---|---|---|
| NaturalLanguageQuestion | dataset | sí | sí | question_hash | post-payload |
| GoldSPARQL | dataset authors | no | sí | gold_sparql_hash | post-payload |
| PredictedSPARQL | método `final_sparql` | sí (output) | sí | predicted_sparql_hash | post-run |
| GoldExecutionResult | gold×graph fijado | no | sí | gold_result_hash | GOLD_MATERIALIZATION_PENDING |
| PredictedExecutionResult | pred×mismo graph | no (eval) | sí | pred_result_hash | post-run |
| RDFTerm | resultado | n/a | sí | term_hash | canonicalization V1 |
| ResultRow | tabla | n/a | sí | row_hash | canonicalization V1 |
| ResultTable | set of rows | n/a | sí | table_hash | SET_OF_ROWS |
| BooleanResult | ASK | n/a | sí | bool_hash | ASK |
| GraphResult | CONSTRUCT/DESCRIBE | n/a | sí | n/a_v1 | out of scope v1 |
| GoldGroundingManifest | evaluator from gold | no | sí | oracle_manifest_hash | pending |
| PredictedGroundingManifest | linker output | si observable | sí | pred_ground_hash | if OBSERVABLE |
| ExternalGroundingManifest | linker congelado | sí (input) | sí | ext_manifest_hash | track IA_FIXED |
| OracleInputManifest | subset roles | sí (roles) | sí | oracle_input_hash | IA_ORACLE |
| QueryStructure | parse AST | n/a | sí | structure_hash | diagnostic |
| MethodFailure | método | sí | sí | status | runtime |
| SystemFailure | infra/endpoint | n/a | sí | status | adjudicación |
| GlobalDatasetDefect | gold/grafo | n/a | sí | defect_id | adjudicación global |

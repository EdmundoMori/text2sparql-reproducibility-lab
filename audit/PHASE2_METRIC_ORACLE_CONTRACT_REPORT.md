# PHASE2_METRIC_ORACLE_CONTRACT_REPORT — Prompt 18

**RUN_ID:** `20260722T093257Z` · **metric_contract_version:** `0.1.0-documentary` · Coste 0.00  
**Gate:** `METRIC_ORACLE_CONTRACT_DOCUMENTED_READY_FOR_ADAPTER_CONTRACTS`

## 1. Resumen ejecutivo
Se fijó el contrato documental de métricas comunes, canonicalización RDF/SPARQL, oracle/grounding, fallos/denominadores y análisis estadístico. Nada implementado ni ejecutado. G4 sigue pendiente; G5 documentary satisfecho; G5 runtime pending.

## 2. Gate de entrada
Prompt 17 gate `DATASET_PROVENANCE_DOCUMENTED_READY_FOR_METRIC_ORACLE_CONTRACT`; tip `dd6a0119…`; T3.

## 3–4. Alcance / fuera
Documental: fórmulas, schemas, vectores. Fuera: parsers, evaluadores, adapters, gold materialization, SPARQL, benchmarks.

## 5. Referencias normativas
SPARQL 1.1 Query/Protocol/Results; RDF 1.1; XSD; RFC 3986; Unicode NFC. Solo HTML oficial (consulta documental futura). Prompt 18: sin red a endpoints.

## 6–8. Principios, objetos, gold
Ver `METRIC_NORMATIVE_PRINCIPLES.md`, `EVALUATION_OBJECT_MODEL.md`, `GOLD_EVALUATION_CONTRACT.md`. Estado gold: `GOLD_MATERIALIZATION_PENDING`.

## 9–10. Query forms y safety
SELECT_ROWSET/AGGREGATE/ASK soportados documentalmente; CONSTRUCT/DESCRIBE out; UPDATE prohibido. Safety: UNSAFE→0.

## 11–12. RDF terms y result tables
`RDF_TERM_CANONICALIZATION_V1`; primary `SET_OF_ROWS`; empty≠no_output; multi-column correlation preserved.

## 13–15. Answer / Exact / Validity
Macro Answer P/R/F1 primary; empty/empty=1; failures=0 in denom. Exact Accuracy. Validity/coverage rates with denominators shown.

## 16–18. SPARQL canon / structure / IRI
Conservative V1; structure diagnostic; query_grounding ≠ linking; hallucination needs dictionary (pending).

## 19–20. Oracle y linking
`ORACLE_CONTRACT_DEFINED`; observability classes; sgpt_q ≠ sgpt_qk; fixed external separate.

## 21–23. Gold mat / defects / failure scoring
Protocol + adjudication + `PHASE2_FAILURE_SCORING_MATRIX.csv`.

## 24–27. Aggregation / replicates / stats / claim boundary
Macro primary; bootstrap_seed 2026072201; 10000 replicates; Holm; no cross-track confirmatory.

## 28–32. Mapping / vectors / schemas / risks / versioning
Native≠common numeric; 36 vectors NOT executed; schemas valid; risk register; version `0.1.0-documentary`.

## 33–36. G4 / G5 / adapters / benchmark
G4: `G4_RUNTIME_PIN_NOT_SATISFIED`. G5 documentary: satisfied. G5 runtime: pending. Adapters false. Benchmark NOT_CURRENTLY_ELIGIBLE.

## 37. PE5–PE8
PE5: protocol_and_metric_contract_defined_pending_benchmark  
PE6: diagnostic_metric_contract_defined_pending_execution  
PE7/PE8: not_started

## 38. Siguiente
T4 — Prompt 19 adapter contracts (documental).

## 39–40. Objetivo / conclusión
Secuencia largo plazo intacta. Contrato listo para T4; **no** benchmark-ready.

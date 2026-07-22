# PHASE2_COMMON_EVALUATION_PROTOCOL_FRAMEWORK_REPORT — Prompt 16

**RUN_ID:** `20260722T083201Z`  
**Gate:** `COMMON_PROTOCOL_FRAMEWORK_DEFINED_READY_FOR_DATASET_PROVENANCE`  
**Coste:** USD 0.00 · PROTOCOL_FRAMEWORK_ONLY · sin adapters · sin benchmark

## 1. Resumen ejecutivo

Se define el marco científico del protocolo común Text-to-SPARQL: tracks ortogonales (información ≠ estilo de ejecución), datasets candidatos (QALD-9 Plus primario; LC-QuAD 2.0 secundario), familias de métricas, contratos I/O, políticas anti-fuga, denominadores con fallos, y gates G0–G9. Pins de dataset/grafo y detalle métrico quedan pending (T2/T3). Adapters false. Benchmark no ejecutado.

## 2. Gate de entrada

`PHASE1_CLOSED_READY_FOR_COMMON_EVALUATION_PROTOCOL_DEFINITION` + `RESIDUAL_METHOD_BLOCKERS_PRESERVED`.

## 3–5. Objetivo / alcance / fuera de alcance

Definir framework. Fuera: pins exactos, hashes, código métricas, adapters, benchmark, downloads.

## 6–7. Métodos y outcomes Fase 1

sparql_llm/sgpt smoke_only; mkgqagent/rdfconfig_llm/cot_sparql blocked; firesparql not_reproducible; tebaqa HISTORICAL_ONLY. Outcomes **intactos**.

## 8–13. Semántica y ejes

Ver `COMMON_PROTOCOL_TERMINOLOGY.md` y `TRACK_TAXONOMY.md`.

## 14. Asignación candidata

`PHASE2_TRACK_ASSIGNMENT_MATRIX.csv` — status `CANDIDATE_TRACK_ASSIGNMENT` (no BENCHMARK_READY). sgpt_q ≠ sgpt_qk.

## 15–17. Datasets / splits / evaluable set

PRIMARY QALD9_PLUS_EN_DBPEDIA; SECONDARY LCQUAD2; DATASET_PIN_PENDING. Policies en docs del RUN_ID.

## 18–20. Graph / input / output

GRAPH_SNAPSHOT_PENDING; CommonInput/Output contracts definidos.

## 21–23. Oracle / modelos / prompts

ORACLE_CONTRACT_PENDING detalle T3; model/LLM control; anti-test-leakage.

## 24–26. Métricas

Familias primarias/diagnósticas/operativas; METRIC_DETAIL_PENDING; linking NOT_OBSERVABLE si no hay outputs.

## 27–30. Failures / aggregation / randomness / stats

Denominador incluye fallos; sin ranking global; replicates framework; stats pending T3.

## 31–33. Comparability / schema / adapter boundary

Matrices CSV; JSON schema draft; adapters fuera de upstream; common_adapter_allowed=false.

## 34–35. Eligibility / riesgos

G0 satisfecho; G1 clasificable; G2+ pending. Risk register 23 entradas.

## 36–38. Pendientes T2 / T3 / T4

T2 dataset provenance; T3 metric/oracle; T4 adapter contracts.

## 39–40. Gate / siguiente

COMMON_PROTOCOL_FRAMEWORK_DEFINED_READY_FOR_DATASET_PROVENANCE → Prompt 17 (T2), no ejecutado.

## 41. PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_framework_defined_pending_benchmark |
| PE6 | diagnostic_metric_framework_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

PE1–PE4 **sin cambio**.

## 42–43. Objetivo largo plazo / conclusión

Secuencia intacta. Framework listo para provenance documental; no benchmark-ready.

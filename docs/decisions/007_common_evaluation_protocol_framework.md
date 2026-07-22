# Decisión 007 — Framework del protocolo común de evaluación

**ID:** `007_common_evaluation_protocol_framework`  
**Fecha:** 2026-07-22 · **Prompt 16** · **RUN_ID:** `20260722T083201Z`  
**Coste:** 0.00

## Decisiones

1. Framework común de evaluación **definido** (documental).
2. Tracks ortogonales: information-access principal; execution-style como tag.
3. Dataset primario candidato: **QALD-9 Plus EN DBpedia**.
4. Dataset secundario candidato: **LC-QuAD 2.0**.
5. No ranking cross-track; no score agregado; no success-only denominators.
6. sgpt_q y sgpt_qk separados; oracle ≠ question-only; domain ≠ DBpedia common.
7. `common_adapter_allowed=false`; benchmark no ejecutado.
8. Gate: `COMMON_PROTOCOL_FRAMEWORK_DEFINED_READY_FOR_DATASET_PROVENANCE`.
9. Siguiente: **T2 / Prompt 17** (dataset version & provenance), sin descargas.

## No decide

pins/hashes/endpoints verificados; implementación adapters; ejecución benchmark.

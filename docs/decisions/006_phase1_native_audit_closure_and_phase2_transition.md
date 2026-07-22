# Decisión 006 — Cierre Fase 1 y transición a protocolo común

**ID:** `006_phase1_native_audit_closure_and_phase2_transition`  
**Fecha:** 2026-07-22  
**Prompt:** 15  
**Coste:** USD 0.00

## 1. Contexto

Laboratorio text2sparql-reproducibility-lab; política ZERO_COST; Q11 seleccionado en 14D.

## 2. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

## 3. Métodos activos

sparql_llm, mkgqagent, rdfconfig_llm, sgpt, cot_sparql, firesparql.

## 4. Referencia histórica

tebaqa — `HISTORICAL_ONLY`; fuera del denominador.

## 5. Evidencia

Matrices Prompt 15 + audits WAVE_A–C + smokes sparql_llm/sgpt + cierre Z3.

## 6. Resultados individuales

Ver `PHASE1_FINAL_METHOD_OUTCOMES.csv`.

## 7. Smokes

sparql_llm CORE_OFFLINE; sgpt Z2/Z3 (load/forward/one-step). Etiquetados `SMOKE_ONLY_NOT_REPRODUCTION`.

## 8. Bloqueos

mkgqagent, rdfconfig_llm, cot_sparql — legales/hardware/artefactos.

## 9. No reproducibles

firesparql — trainer/runner ausentes; licencia código no confirmada; results ≠ reproducción.

## 10–13. PE1–PE4

PE1 substantially_answered; PE2 partial_evidence; PE3 not_started (`no_comparable_original_metric_run_available`); PE4 substantially_answered_for_current_portfolio.

## 14. Tracks

Separados: e2e schema; agentic; domain schema; oracle grounding; external grounding; domain ORKG. Sin comparación directa entre tracks.

## 15. Gate global

`PHASE1_CLOSED_READY_FOR_COMMON_EVALUATION_PROTOCOL_DEFINITION` + `RESIDUAL_METHOD_BLOCKERS_PRESERVED`.

## 16. Residual blockers

LICENSE (varios); COST online; MISSING_CHECKPOINT/TRAINER/RUNNER; HARDWARE; METRIC_AMBIGUITY; GOLD_GROUNDING.

## 17. Elegibilidad Fase 2

Matriz `COMMON_EVALUATION_PROTOCOL_ELIGIBILITY_MATRIX.csv` — diseño de protocolo; no adapters.

## 18. Adapters

`common_adapter_allowed=false` para todos.

## 19. Reapertura Fase 1

Solo con nueva evidencia nativa proporcional (p. ej. licencia, artefactos paper, política de coste) — no por instrumentación.

## 20. Próximo paso

Prompt 16 — definición documental del protocolo común (T1). No ejecutar aquí.

## 21. Claim boundary

Ningún método `reproduced`/`partially_reproduced`; sin Table 4; sin PE3 resuelto.

## 22. Decisión

Cerrar Fase 1 nativa; habilitar **solo** la definición documental de Fase 2; adapters off.

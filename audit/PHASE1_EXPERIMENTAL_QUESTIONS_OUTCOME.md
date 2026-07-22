# PHASE1_EXPERIMENTAL_QUESTIONS_OUTCOME — Prompt 15

**Fecha:** 2026-07-22 · Coste 0.00

## PE1 — ¿Qué métodos Text-to-SPARQL existen y cómo se relacionan paper↔código?

**Estado:** `substantially_answered`

- Seis métodos activos incluidos y auditados (`INCLUDE_PRIMARY` / `INCLUDE_CONDITIONAL`).
- TeBaQA separado como `HISTORICAL_ONLY` (fuera del denominador).
- Evidencia consolidada: mapping, licencias, datasets, métricas, entornos.

## PE2 — ¿Qué puede ejecutarse de forma nativa / smoke?

**Estado:** `partial_evidence`

| Método | Superficie verificada |
|---|---|
| sparql_llm | CORE_OFFLINE Docker py311 (`EXECUTION_VERIFIED`); online `BLOCKED_POLICY` |
| sgpt | env Z2; model load; forward; reduced train path (`REDUCED_TRAINING_PATH_VERIFIED`) |
| mkgqagent | ninguna ejecución (legal) |
| rdfconfig_llm | ninguna ejecución (legal + Ruby) |
| cot_sparql | ninguna ejecución (legal + HW + artefactos) |
| firesparql | inventario de results (`RESULT_FILE_VERIFIED`) ≠ run propio |

No confundir entorno/import/smoke con reproducción del artículo.

## PE3 — ¿Se obtienen métricas originales comparables?

**Estado:** `not_started`  
**Qualifier:** `no_comparable_original_metric_run_available`

- Ninguna ejecución produjo métricas originales comparables del paper.
- Losses técnicas SGPT ≠ Table 4 / Answer F1.
- Results FIRESPARQL versionados ≠ ejecución propia.
- PE3 sin evidencia experimental comparable.

## PE4 — ¿Cuáles son las barreras de reproducibilidad?

**Estado:** `substantially_answered_for_current_portfolio`

La matriz final cubre los seis métodos activos y las barreras dominantes (LICENSE, COST/POLICY, MISSING_*, HARDWARE, METRIC_AMBIGUITY, GOLD_GROUNDING, DOMAIN). Gap residual: detalle fino de algunos endpoints/API mutables ya documentado históricamente; no bloquea el cierre de auditoría nativa.

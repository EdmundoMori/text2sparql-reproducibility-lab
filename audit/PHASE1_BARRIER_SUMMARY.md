# PHASE1_BARRIER_SUMMARY — Prompt 15

**Fecha:** 2026-07-22 · Coste 0.00 · documental  
**Fuente:** `audit/PHASE1_FINAL_BARRIER_MATRIX.csv` (+ histórico `REPRODUCIBILITY_BARRIER_MATRIX.csv`)

## Conteos descriptivos (no score)

| method_id | barriers_in_final_matrix | tipos dominantes |
|---|---|---|
| sparql_llm | 2 | COST/POLICY, ENDPOINT_DRIFT |
| mkgqagent | 2 | LICENSE, DOMAIN_HARDCODING |
| rdfconfig_llm | 2 | LICENSE, DEPENDENCY_DRIFT (Ruby) |
| sgpt | 3 | MISSING_CHECKPOINT, METRIC_AMBIGUITY, GOLD_GROUNDING |
| cot_sparql | 3 | LICENSE, HARDWARE, MISSING_DATA |
| firesparql | 4 | MISSING_TRAINER, MISSING_EXECUTION_RUNNER, LICENSE, OTHER (results≠repro) |

## Lectura científica

- Más barreras ≠ peor método; reflejan límites legales, de máquina, de artefactos o de claim boundary.
- Limitaciones de laptop (6 GiB) no se convierten en juicio de calidad del paper.
- Resultados versionados FIRESPARQL y losses técnicas SGPT **no** cierran PE3.

## Resolvabilidad ZERO_COST

Ninguna barrera dominante restante es resoluble de forma proporcional bajo ZERO_COST de modo que cambie `reproduction_status` hacia métricas del artículo sin nueva política/presupuesto/artefactos.

# COMPARABILITY_RULES

**RUN_ID:** `20260722T083201Z`

## Condiciones necesarias (todas)

dataset+versión; split; idioma; graph snapshot o endpoint contract; information-access track; adaptation regime compatible; model-control regime; item scope pre-registrado; timeout/execution policy; metric definition; test-set seal.

## Obligatorio

| Comparación | Veredicto |
|---|---|
| IA_Q_ONLY vs IA_ORACLE_GROUNDING | DIRECT_COMPARISON_FORBIDDEN |
| IA_Q_ONLY vs IA_FIXED_EXTERNAL_GROUNDING | DIRECT_COMPARISON_FORBIDDEN |
| IA_DOMAIN_NATIVE vs DBpedia common | DIRECT_COMPARISON_FORBIDDEN |
| MC_NATIVE vs MC_CONTROLLED | reportar separado |
| agentic vs single-pass (mismo IA) | calidad comparable si resto coincide; reportar coste/llamadas/latencia |
| cross-track | DESCRIPTIVE_CROSS_TRACK_ONLY |

## Prohibido

ranking global; score agregado único; ordenar tracks distintos por una métrica; BEST_METHOD / WINNER / STATE_OF_THE_ART.

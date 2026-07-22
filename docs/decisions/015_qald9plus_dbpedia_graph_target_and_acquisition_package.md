# Decisión 015 — Objetivo de grafo DBpedia 2016-10 y paquete de adquisición (QALD-9 Plus EN/DBpedia)

**Fecha:** 2026-07-22 · **RUN_ID:** `20260722T120239Z` · **Prompt:** 23

## Decisiones

1. **Target primario:** `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` (release **2016-10**), condicionado a cierre de file scope.
2. **Scope:** endpoint-equivalent (core resuelto + links + LHD), no todo el release.
3. **Endpoint público actual:** rechazado como primary reproducible.
4. **Common rebase:** fallback explícito `COMMON_GRAPH_REBASE`, no sustituto nativo.
5. **Query-coverage subgraph:** rechazado como primary.
6. **Adquisición / despliegue:** **no** ejecutados.
7. **Recursos:** `CONDITIONAL_HIGH_RISK` (disco OK; RAM/WSL riesgo; scope condicional).
8. **Human gate:** `NOT_READY_CONDITIONAL`.
9. **Siguiente acción:** `CLOSE_DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_FILE_SCOPE` (Prompt 23B).

## Gate

`DBPEDIA_2016_10_NATIVE_GRAPH_TARGET_SELECTED_PACKAGE_CONDITIONAL_FILE_SCOPE`

## No implica

G4 PASS · autorización de descarga · carga Virtuoso · elegibilidad de benchmark.

# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-22  
**Tras:** Prompt 23 — DBpedia graph target (`20260722T120239Z`) · gate `DBPEDIA_2016_10_NATIVE_GRAPH_TARGET_SELECTED_PACKAGE_CONDITIONAL_FILE_SCOPE`

## Prompt recomendado (único)

**Título:** Prompt 23B — Cierre documental del file scope endpoint-equivalent DBpedia 2016-10 (33 unavailable `*_en_uris_*`, rol de ontología, resolución `core/`→`core-i18n/en`), ZERO_COST, sin descargar grafos ni ejecutar SPARQL.

**Acción:** CLOSE_DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_FILE_SCOPE

**Restricciones:** ZERO_COST; documental; sin GET de RDF/dumps; sin Docker pull; sin Virtuoso; sin SPARQL; sin gold; sin adapters; sin benchmark; sin auth automática.

## Contexto obligatorio

- Primary target ya seleccionado: `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT`
- Fallback: `COMMON_GRAPH_REBASE` (no ejecutar)
- Available: 81 files / 5023159516 bytes
- Blockers: 33 checksum-listed files HTTP 404; LHD sin MD5 en core checksums; ontology optional unknown
- Human form: `NOT_READY_CONDITIONAL` hasta cerrar scope
- QALD sealed/consumed; LC-QuAD HOLD; G4 runtime not satisfied

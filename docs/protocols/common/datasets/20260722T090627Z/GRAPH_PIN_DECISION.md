# GRAPH_PIN_DECISION

**RUN_ID:** `20260722T090627Z` · GRAPH_SNAPSHOT_ACQUISITION_PENDING

## Hallazgos

- QALD-9 Plus: KG DBpedia/Wikidata; **sin** dump URL/checksum en repo; endpoints GERBIL históricos no consultados.
- LC-QuAD 2.0: README **Dbpedia2018** + Wikidata; no dump fijado; **GRAPH_YEAR_REPORTED** ≠ snapshot pin.
- No asumir mismo DBpedia entre QALD-9 Plus y LC-QuAD 2.0.

## Estrategias futuras

**A. dataset-native graph reconstruction** — si existe release exacto.

**B. lab common graph rebase** — requiere revalidar gold, recalcular answers, etiqueta COMMON_GRAPH_REBASE; no presentarse como nativo original.

Estado: **GRAPH_SNAPSHOT_NOT_PUBLISHED** / acquisition pending. G4 runtime pin **no** satisfecho.

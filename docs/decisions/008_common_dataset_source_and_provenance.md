# Decisión 008 — Fuentes, pins y provenance de datasets comunes

**ID:** `008_common_dataset_source_and_provenance`  
**Fecha:** 2026-07-22 · **Prompt 17** · **RUN_ID:** `20260722T090627Z`  
**Coste:** 0.00

## Decisiones

1. Fuente primaria QALD-9 Plus: repositorio de autores `Perevalov/qald_9_plus`.
2. Pin inmutable QALD: `8eb038a61e1bc09cbd21640aa667a1714f53cda4` (`CURRENT_SOURCE_SNAPSHOT_NOT_PUBLICATION_RELEASE`).
3. Fuente primaria LC-QuAD 2.0: `AskNowQA/LC-QuAD2.0`.
4. Pin inmutable LC-QuAD: `0a5f8f85b6f863c3b80f0fa02839e25d438af3ae` (mismo qualifier temporal).
5. Jerarquía: authors repo > HF mirror/builder > method-local derivatives; HF **no** byte-identical asumido.
6. Vistas lógicas: `QALD9_PLUS_EN_DBPEDIA` (PRIMARY), `QALD9_PLUS_EN_WIKIDATA`, `LCQUAD2_DBPEDIA18` (SECONDARY DBpedia), `LCQUAD2_WIKIDATA` (extensión).
7. Representación LC-QuAD seleccionada para protocolo DBpedia: **LCQUAD2_DBPEDIA18** (candidata secundaria); no agregar con Wikidata.
8. Splits: train/test oficiales; test sellado; development solo `DERIVED_DEV_SPEC_DEFINED_NOT_APPLIED`.
9. Hashes: distinguir commit/tree/blob/OID/ETag/SHA-256; checksums publicados de archivo = NOT_PUBLISHED.
10. Graph provenance documentada; snapshot **pending**; no inferir release DBpedia mensual.
11. Payload **no adquirido**; status `SOURCE_PROVENANCE_DOCUMENTED_PAYLOAD_NOT_ACQUIRED`.
12. Gate: `DATASET_PROVENANCE_DOCUMENTED_READY_FOR_METRIC_ORACLE_CONTRACT`.
13. Siguiente: **T3 / Prompt 18** (métricas/oracle documental).

## No decide

DATASET_READY; GRAPH_PINNED; adquisición; adapters; benchmark; selectores JSON exactos sin payload.

# QALD-9 → QALD-9 Plus graph lineage

**RUN_ID:** `20260722T120239Z`  
**Tags:** `QALD9PLUS_DBPEDIA_LINEAGE_INFERRED_HIGH_CONFIDENCE` · `QALD9_NATIVE_GRAPH_DBPEDIA_2016_10` (target) · `INFERENCE` where noted

## QALD-9 challenge (dataset side)

| Campo | Evidencia |
|---|---|
| Source repo | `ag-sc/QALD` path `9/data/` |
| Train file | `qald-9-train-multilingual.json` (GitHub API size 3199127) |
| Test file | `qald-9-test-multilingual.json` (GitHub API size 1065192) |
| Counts (QALD-9 Plus README alignment) | train **408** / test **150** (EN DBpedia view) |
| Explicit paper quote "DBpedia 2016-10" in this metadata pass | **NOT_RETRIEVED** (Crossref/arXiv/HOBBIT HTML did not yield a QALD-9 overview paper with that string) |

## DBpedia historical endpoint (graph side)

Official page https://www.dbpedia.org/resources/sparql/ states that **before** Latest Core collections, the public endpoint loaded the **2016-10** dataset from:

1. `http://downloads.dbpedia.org/2016-10/links/`
2. `http://downloads.dbpedia.org/2016-10/core/`
3. `.../core-i18n/en/instance_types_lhd_dbo_en.ttl.bz2`
4. `.../core-i18n/en/instance_types_lhd_ext_en.ttl.bz2`

**Tag:** `HISTORICAL_ENDPOINT_SCOPE_DOCUMENTED` · `DBPEDIA_2016_10_RELEASE_VERIFIED` (release exists and is documented).

## Hypothesis outcomes

| ID | Statement | Outcome |
|---|---|---|
| H1 | QALD-9 used DBpedia 2016-10 | **INFERENCE_HIGH_CONFIDENCE**: QALD-era systems used the public DBpedia endpoint; that endpoint historically served 2016-10. Direct QALD-9 challenge paper sentence not captured in this pass → not `QALD9_GRAPH_VERSION_PRIMARY_EVIDENCE_VERIFIED` from paper text alone. |
| H2 | QALD-9 Plus inherits DBpedia queries/answers from QALD-9 and adds translations + Wikidata | **SUPPORTED**: arXiv abs/2202.00120 — extends QALD-9 with translations; transfers SPARQL from DBpedia to Wikidata. README: based on `ag-sc/QALD` `9/data`. **No byte-identity claim** between Plus and QALD-9 payloads. |
| H3 | Primary target = DBPEDIA_2016_10_QALD9_NATIVE_GRAPH | **SELECTED** as scientific primary. |
| H4 | Current public endpoint not reproducible primary | **CONFIRMED** (Latest Core mutable). |
| H5 | Common rebase is separate variant | **ACCEPTED** as fallback only. |

## Lineage decision

`QALD9PLUS_DBPEDIA_LINEAGE_INFERRED_HIGH_CONFIDENCE`

Direct: Plus extends QALD-9; DBpedia SPARQL transferred to Wikidata implies DBpedia side retained.  
Indirect: historical DBpedia endpoint = 2016-10.  
Not claimed: Plus JSON byte-identical to QALD-9; gold answers still valid on reconstructed graph.

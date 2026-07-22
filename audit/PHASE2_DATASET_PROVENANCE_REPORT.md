# PHASE2_DATASET_PROVENANCE_REPORT — Prompt 17

**RUN_ID:** `20260722T090627Z`  
**Fecha:** 2026-07-22  
**Coste externo:** 0.00 USD  
**Gate:** `DATASET_PROVENANCE_DOCUMENTED_READY_FOR_METRIC_ORACLE_CONTRACT`

## 1. Resumen ejecutivo

Se documentó la procedencia de **QALD-9 Plus** y **LC-QuAD 2.0** con metadata pública y auditoría read-only de copias locales ya existentes. Se fijaron commits inmutables de repositorios de autores, se separaron mirrors/derivados, se definieron vistas lógicas por idioma/KG, y se dejó explícito que **payloads no fueron adquiridos** y que **G4 runtime pin no está satisfecho**.

## 2. Gate de entrada

- Prompt 16 gate: `COMMON_PROTOCOL_FRAMEWORK_DEFINED_READY_FOR_DATASET_PROVENANCE`
- Prompt 16 RUN_ID: `20260722T083201Z`
- ARTIFACT Prompt 16: `ee3ae4a20c2243f3f432ef0097ad2bfcd4f46382`
- Tip remoto inicial Prompt 17: `ba306d069910e3807bd211cc7416c1e88e637e86`
- Acción: **T2 — DATASET_VERSION_AND_PROVENANCE_PROTOCOL**

## 3. Alcance

Metadata GitHub/HF/Crossref/arXiv; árboles Git; README/LICENSE/CITATION; lectura local de copias preexistentes; contratos de vistas/splits; matrices de licencias/hashes/grafos/endpoints.

## 4. Fuera de alcance

Descargas de payloads; archives; HF `/resolve/`; `load_dataset`; clones de datasets; PDFs; dumps RDF; consultas SPARQL; adapters; métricas ejecutadas; benchmark.

## 5. Política de red

Allowlist; solo GET/HEAD metadata; cero payload dataset; log en `logs/dataset-provenance/20260722T090627Z/network.log`; SHA-256 de respuestas en `metadata.sha256`.

## 6. Jerarquía de fuentes

Orden: OFFICIAL_PAPER → OFFICIAL_AUTHOR_REPOSITORY → RELEASE/TAG → HOMEPAGE → AUTHOR_MAINTAINED → COMMUNITY_MIRROR → METHOD_LOCAL_DERIVATIVE → TERTIARY_CATALOG.  
Detalle: `docs/protocols/common/datasets/20260722T090627Z/SOURCE_HIERARCHY.md` · `audit/PHASE2_DATASET_SOURCE_MATRIX.csv`.

## 7. Temporal pinning

| Dataset | Pin | Tipo |
|---|---|---|
| QALD-9 Plus | `8eb038a61e1bc09cbd21640aa667a1714f53cda4` | CURRENT_SOURCE_SNAPSHOT_NOT_PUBLICATION_RELEASE (sin tags/releases) |
| LC-QuAD 2.0 | `0a5f8f85b6f863c3b80f0fa02839e25d438af3ae` | CURRENT_SOURCE_SNAPSHOT_NOT_PUBLICATION_RELEASE (sin tags/releases) |

Ver `TEMPORAL_PIN_DECISIONS.md`.

## 8. QALD-9 Plus

- Paper DOI 10.1109/ICSC52841.2022.00045 · arXiv 2202.00120
- Repo: Perevalov/qald_9_plus
- Archivos: `data/qald_9_plus_{train,test}_{dbpedia,wikidata}.json`
- Counts reportados EN DBpedia: train **408** / test **150**
- License: **CC BY 4.0** (`LICENSE_FILE_VERIFIED`)
- Vista primaria: **QALD9_PLUS_EN_DBPEDIA**

## 9. LC-QuAD 2.0

- Paper DOI 10.1007/978-3-030-30796-7_5
- Repo: AskNowQA/LC-QuAD2.0 · files `dataset/train.json`, `dataset/test.json`
- README: Wikidata + Dbpedia2018
- Sin LICENSE en tree → `LICENSE_SCOPE_UNCLEAR`; HF card reporta cc-by-3.0 (no sustituye autores)
- Vistas: **LCQUAD2_DBPEDIA18** (secundario DBpedia) · **LCQUAD2_WIKIDATA** (extensión)

## 10. Representaciones

Separadas: authors repo, HF mirror/builder, mKGQAgent train derivative, SGPT original/processed.  
Ningún mirror/derivado es canónico común. Matriz: `PHASE2_DATASET_REPRESENTATION_MATRIX.csv`.

## 11. Copias locales

- mKGQAgent QALD train EN: n=408; experience pool; **usable_as_common_canonical=false**
- SGPT LC-QuAD: 21497/2389/5969; campo `sparql_wikidata`; **no** sustituyen split oficial  
Matriz: `PHASE2_LOCAL_DATASET_COPY_LINEAGE.csv`.

## 12. Archivos

Inventario metadata-only: `DATASET_FILE_MANIFEST.csv` (tamaños + git blob OIDs; `payload_downloaded=false` remoto).

## 13. Hash semantics

Commit SHA ≠ tree OID ≠ blob OID ≠ SHA-256 local ≠ ETag. Checksums de archivo publicados: **NOT_PUBLISHED**. Política: `DATASET_HASH_POLICY.md`.

## 14. Licencias

QALD: LICENSE file CC BY 4.0. LC-QuAD authors: scope unclear; HF card reported only. Diseño documental permitido; adquisición futura requiere gate explícito. No asesoramiento jurídico.

## 15. Vistas lógicas

`DATASET_VIEW_CONTRACTS.yaml`: QALD9_PLUS_EN_DBPEDIA, QALD9_PLUS_EN_WIKIDATA, LCQUAD2_DBPEDIA18, LCQUAD2_WIKIDATA.

## 16. Splits

Oficiales train/test documentados. Test **sellado**. Sin validation oficial en authors trees.

## 17. Development derivado

`DERIVED_DEV_SPEC_DEFINED_NOT_APPLIED` — solo desde train; IDs determinísticos futuros; ratio pendiente; **ningún ID seleccionado** sin payload.

## 18. Idiomas

QALD multilingual; vista común primaria **en**. LC-QuAD 2.0 inglés.

## 19. Knowledge graphs

QALD: DBpedia y Wikidata en archivos separados. LC-QuAD: DBpedia2018 + Wikidata en mismos archivos (selectores pendientes de payload).

## 20. Graph provenance

QALD: GRAPH_VERSION_NOT_SPECIFIED. LC-QuAD DBpedia: GRAPH_YEAR_REPORTED (2018) sin release mensual. Snapshot **no publicado**. No inferir dump.

## 21. Endpoints

Solo URLs reportadas (GERBIL links QALD). `endpoint_queried=false` universal. Sin ASK/SELECT/CONSTRUCT.

## 22. Drift

Pins = HEAD actual de authors repos; drift futuro posible hasta freeze de adquisición. Qualifier CURRENT_SOURCE_SNAPSHOT… explícito.

## 23. Riesgos

- Confundir derivados SGPT/mKGQ con canónico
- Confundir Git SHA con SHA-256
- Inferir versión DBpedia
- Mezclar respuestas entre grafos distintos
- Tratar HF license card como LICENSE de autores LC-QuAD

## 24. Payload status

`DATASET_PAYLOAD_NOT_ACQUIRED` · status máximo `SOURCE_PROVENANCE_DOCUMENTED_PAYLOAD_NOT_ACQUIRED` · **no** DATASET_READY.

## 25. G4 status

`G4_RUNTIME_PIN_NOT_SATISFIED` — provenance documental ≠ pin runtime de dataset+graph.

## 26. Gate

`DATASET_PROVENANCE_DOCUMENTED_READY_FOR_METRIC_ORACLE_CONTRACT`  
Qualifiers: DATASET_PAYLOAD_NOT_ACQUIRED; GRAPH_SNAPSHOT_ACQUISITION_PENDING; LOCAL_SHA256_PENDING_CONTROLLED_ACQUISITION; G4_RUNTIME_PIN_NOT_SATISFIED.

## 27. Siguiente acción

**T3 — METRIC_SPECIFICATION_AND_ORACLE_CONTRACT** → Prompt 18 (documental; sin implementar métricas ni consultas).

## 28. PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_framework_defined_pending_benchmark (+ evidencia preparatoria provenance) |
| PE6 | diagnostic_metric_framework_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

Evidencia: dataset_source_provenance_documented; payload_not_acquired; graph_snapshot_pending. PE5 **no** iniciado experimentalmente.

## 29. Objetivo largo plazo

Secuencia intacta: reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

## 30. Conclusión conservadora

Prompt 17 cierra T2 a nivel documental. No habilita adapters, benchmark, ni adquisición. G4 permanece pendiente hasta adquisición controlada de payload+graph.

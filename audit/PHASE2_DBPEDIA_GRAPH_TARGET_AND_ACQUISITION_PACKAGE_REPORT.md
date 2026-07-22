# PHASE2 — DBpedia graph target and acquisition package report

**Prompt:** 23 · **RUN_ID:** `20260722T120239Z` · **Cost:** 0.00

## 1. Resumen ejecutivo

Objetivo científico primario: **DBpedia 2016-10 endpoint-equivalent** para `QALD9_PLUS_EN_DBPEDIA`. Endpoint público mutable rechazado. Common rebase = fallback separado. Paquete metadata: **81** archivos disponibles (**5023159516** bytes comprimidos); **33** blockers 404. Gate: **`DBPEDIA_2016_10_NATIVE_GRAPH_TARGET_SELECTED_PACKAGE_CONDITIONAL_FILE_SCOPE`**. Payload **no** adquirido. G4 runtime **no** satisfecho.

## 2. Gate de entrada

Prompt 22 `LCQUAD2_SCOPE_CLARIFIED_ALL_REPRESENTATIONS_HOLD` · QALD acquired/sealed · auth consumed · action `GRAPH_ACQUISITION_OR_REBASE_DECISION`.

## 3. Alcance

Documental metadata-only: lineage QALD, opciones de grafo, scope endpoint-equivalent, inventario HEAD/listing, licencia, recursos, manifests, gate.

## 4. Fuera de alcance

RDF GET, dumps, Docker pull, Virtuoso, SPARQL, gold, métricas, adapters, benchmark, auth automática, reuse auth QALD.

## 5. QALD-9 evidence

Repo `ag-sc/QALD` `9/data` presente. Afirmación paper explícita "underlying RDF dataset DBpedia 2016-10" **no recuperada** en este pase metadata. Endpoint DBpedia histórico documentado como 2016-10.

## 6. QALD-9 Plus lineage

arXiv 2202.00120: extiende QALD-9; traduce; transfiere SPARQL DBpedia→Wikidata. Tag: `QALD9PLUS_DBPEDIA_LINEAGE_INFERRED_HIGH_CONFIDENCE`.

## 7. Graph options

Matriz `audit/PHASE2_DBPEDIA_GRAPH_OPTION_MATRIX.csv` — A selected conditional; C/E/F rejected; D fallback.

## 8. Target decision

Primary A · Fallback D · see `GRAPH_TARGET_DECISION.md`.

## 9. DBpedia 2016-10

Release verificada en downloads.dbpedia.org; DataID metadata capturada.

## 10. Endpoint-equivalent scope

Four-bullet official list; `core/` resuelto vía checksums → `core-i18n/en`; LHD añadidos; links inventariados.

## 11. Release / core / endpoint differences

RELEASE ≠ CORE ≠ ENDPOINT_EQUIVALENT. No descargar todo 2016-10.

## 12. File inventory

`PHASE2_DBPEDIA_2016_10_FILE_MANIFEST.csv` + YAML manifest. Available 81; unavailable 33.

## 13. Serialization

ttl.bz2 core/LHD; links as published; no ttl+tql duplicates.

## 14. Checksums

MD5 publicados core/links; LHD sin md5 en core checksums; ETag ≠ checksum; SHA-256 publicados no disponibles.

## 15–16. License / attribution

CC BY-SA 3.0 + GFDL evidencia About; draft attribution `DRAFT_NOT_APPLIED`; linksets terceros UNKNOWN.

## 17–18. Resources / machine

Disk OK (~918 GiB free). WSL RAM 7.4 GiB → `CONDITIONAL_HIGH_RISK`. Compose ausente.

## 19. Deployment profiles

YAML profiles A–E documentary; ZERO_COST bloquea servidor de pago auto-seleccionado.

## 20. Endpoint contract

Skeleton only; no image digest.

## 21–22. Native vs rebase

Native primary; rebase boundary documented; no mislabel.

## 23. Gold compatibility

Historical answers **not** asserted valid until graph execution.

## 24–25. Validation / acquisition manifests

Future stages listed; acquisition `NOT_ACQUIRED`; auth `UNSIGNED`.

## 26. Human gate

`NOT_READY_CONDITIONAL` — blockers de file scope.

## 27. Risks

`PHASE2_DBPEDIA_GRAPH_RISK_REGISTER.csv`.

## 28–33. Gates / adapters / benchmark

G3G n/a change · G4 target documented / runtime **NOT_SATISFIED** · G5 runtime pending · G6D documented · G6I pending · adapters **false** · benchmark **NOT_CURRENTLY_ELIGIBLE**.

## 34. Gate

`DBPEDIA_2016_10_NATIVE_GRAPH_TARGET_SELECTED_PACKAGE_CONDITIONAL_FILE_SCOPE`

## 35. Next action

**`CLOSE_DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_FILE_SCOPE`** (Prompt **23B** documentary). Reserved later: Prompt 24B acquisition (after human auth) — not now.

## 36. PE5–PE8

Preparatory evidence added; no new PE results.

## 37. Long-term objective

Intact: native → common eval → case study → errors → Text-to-SQL → new method → ablations.

## 38. Conservative conclusion

Select the scientifically correct graph **before** acquiring/deploying. Target selected; package **conditional** on file-scope closure; nothing downloaded.

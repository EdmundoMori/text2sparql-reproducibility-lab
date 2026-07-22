# PHASE2_QALD9PLUS_ACQUISITION_EXECUTION_REPORT — Prompt 21B / T6B

**execution_run_id:** `20260722T111153Z`  
**authorization_id:** `AUTH_QALD9PLUS_T6B_20260722T105246Z_EMO_01` · **CONSUMED**  
**Gate:** `QALD9PLUS_CONTROLLED_ACQUISITION_PASS_VALIDATED`  
**Coste:** 0.00

## Resumen
Adquisición controlada de exactamente 4 archivos QALD-9 Plus EN/DBpedia desde pin `8eb038a61e1bc09cbd21640aa667a1714f53cda4`.  
Tamaños y Git blob OIDs verificados. SHA-256 locales calculados. JSON válido. Conteos 408/150.  
Test sellado. Payloads solo en `workdir/` (gitignore). Autorización consumida.

## Archivos

| path | size | blob OID | sha256 (12) |
|---|---:|---|---|
| train DBpedia JSON | 6371289 | cce48cbdf2af… | 95e1644fbcbf… |
| test DBpedia JSON | 1424744 | 06cc04be82be… | 6d3367b1231a… |
| LICENSE | 18650 | 2f244ac81403… | 7e7170e3cebf… |
| CITATION.cff | 1191 | 4506fd12bdff… | 40c2e632613e… |

Total recibido: **7815874**

## Validación
- Conteos: train 408 / test 150 · MATCH
- EN coverage: 408 / 150
- SPARQL field coverage: 408 / 150 (presencia; sin imprimir)
- Duplicados intra-split: 0
- Solape IDs train∩test: 150 · interpretado como numeración independiente por split
- Test: SEALED · contenido no impreso · no usado para prompts

## No realizado
grafos · SPARQL · gold · adapters · métricas · benchmark · LC-QuAD · Wikidata · mirrors

## Gates de fase
G4 sigue pendiente (grafo) · G5 runtime pending · G6I pending · adapters false · benchmark no elegible

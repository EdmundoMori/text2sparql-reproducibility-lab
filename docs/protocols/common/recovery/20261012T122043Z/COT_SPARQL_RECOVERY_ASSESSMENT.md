# CoT-SPARQL recovery assessment

**phase1:** blocked · LICENSE absent (GH 404 reconfirmed) · embeddings/parquet/pkl absent · CodeLlama-34B exceeds local 6GB VRAM.

## Native reference

34B remains **native reference**. No invented smaller unofficial variant.
No official smaller model variant declared in-repo for substitution (static).

## Variants

| Variant | Status |
|---|---|
| COT_NATIVE_FAITHFUL | requires LICENSE + artifacts + high VRAM/external zero-cost GPU |
| COT_ZERO_COST_CONTROLLED_VARIANT | only if scientifically justified later; **not invented here** |

## Recoverability

- native: **R4** (license/artifacts) + **R5** (compute)
- common: same; until then **R6**
- Blockers: B_LEGAL, B_ARTIFACT, B_HARDWARE, B_MODEL, B_SERVICE(linkers), B_GRAPH

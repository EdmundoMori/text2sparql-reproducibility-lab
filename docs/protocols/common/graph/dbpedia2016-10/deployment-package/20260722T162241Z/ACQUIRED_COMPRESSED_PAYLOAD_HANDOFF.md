# Acquired compressed payload handoff

**RUN_ID:** `20260722T162241Z` · Tag: `ACQUIRED_COMPRESSED_PAYLOAD_HANDOFF_VERIFIED`

## Verification method

Manifests + `stat` only. **No** content read, **no** decompression, **no** SHA-256 recalculation of 6.45 GiB.

## Result

| Check | Value |
|---|---|
| expected files | 114 |
| present | 114 |
| missing | [] |
| extras | [] |
| total bytes | 6925795437 |
| expected bytes | 6925795437 |
| bytes match | True |
| size mismatches | [] |
| destination | `workdir/graphs/dbpedia/2016-10/endpoint-equivalent/compressed` |
| free disk (bytes) | 977903906816 |
| auth id | `AUTH_DBPEDIA2016_10_ACQ_20260722T134313Z_EMO_01` |
| auth status | `CONSUMED_AFTER_PASS` |
| acquisition status | `ACQUIRED_VALIDATED_WORKDIR_ONLY` |
| gitignored | yes (`workdir/`) |

Evidence: `audit/PHASE2_DBPEDIA_DEPLOYMENT_HANDOFF_MATRIX.csv`

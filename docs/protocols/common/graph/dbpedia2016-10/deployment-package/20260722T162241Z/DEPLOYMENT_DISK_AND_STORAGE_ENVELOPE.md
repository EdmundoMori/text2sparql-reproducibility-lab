# Disk and storage envelope

**RUN_ID:** `20260722T162241Z` · Tag: `DEPLOYMENT_RESOURCE_ENVELOPE_DOCUMENTED`

## Measured

- Compressed exact: **6925795437** bytes (114 files).
- Free disk now: **910.8 GiB**.

## Uncompressed size

**No official uncompressed total** found for this exact 114-file endpoint-equivalent set
(`UNCOMPRESSED_SIZE_OFFICIAL_METADATA_VERIFIED` = false).

Scenarios use ratio heuristics tagged `PLANNING_ASSUMPTION_NOT_MEASUREMENT` /
`UNCOMPRESSED_SIZE_SCENARIO_ESTIMATE`.

See `audit/PHASE2_DBPEDIA_DEPLOYMENT_DISK_SCENARIOS.csv`.

Conservative recommended envelope on the order of **~280 GiB** peak planning
(with compressed retained + temp + DB + logs + margin). Current free disk
(~911 GiB) **covers disk** scenarios; disk is not the primary blocker.

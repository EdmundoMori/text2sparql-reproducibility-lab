# Checksum coverage closure

**RUN_ID:** `20260722T132719Z`  
Tags: `CHECKSUM_COVERAGE_PARTIAL` · `POST_DOWNLOAD_SHA256_REQUIRED`

| Metric | Value |
|---|---|
| Files with published MD5 | 112 / 114 (98.2456%) |
| Bytes with published MD5 | 6839826862 / 6925795437 (98.7587%) |
| No published checksum | 2 LHD files |

## Rules

- ETag ≠ checksum
- Published MD5 = integrity aid, not modern crypto guarantee
- After acquisition: local compressed SHA-256 for **every** file
- MD5/size mismatch → FAIL
- No mirrors to fill missing checksums

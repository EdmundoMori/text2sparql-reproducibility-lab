# LHD component and checksum decision

**RUN_ID:** `20260722T132719Z`

| File | URL | Size | Published MD5 |
|---|---|---:|---|
| instance_types_lhd_dbo_en.ttl.bz2 | core-i18n/en/… | 39643080 | **not in core/_checksums.md5** |
| instance_types_lhd_ext_en.ttl.bz2 | core-i18n/en/… | 46325495 | **not in core/_checksums.md5** |

## Requirement

**Required** — explicitly listed on www.dbpedia.org/resources/sparql/ historical load list.

## Checksum policy

Absence of published MD5 ≠ file-scope blocker.  
Acquire with: exact URL + exact size + network log + **mandatory local SHA-256** after download.

# Core alias and canonical path resolution

**RUN_ID:** `20260722T132719Z`  
Tags: `RESOLVED_CORE_ALIAS` · `RESOLVED_CANONICAL_PATH`

## What `/2016-10/core/` is

Apache directory listing with DataID, `_checksums.md5`, and many `.ttl.bz2` entries sized ~90 bytes (symlink stubs). **HEAD of those URLs returns 404.**

## Relationship to `core-i18n/en/`

`core/_checksums.md5` maps most English core datasets to `./core-i18n/en/...` — those resolve for non-`en_uris` files.

## `*_en_uris_*` exception

Checksum text claims `en/` but payloads are under `core-i18n/{lang}/`.  
All 33 blockers: HEAD 200 + matching lang `_checksums.md5` MD5.

## Final rule

- Do **not** acquire via broken `core/` URLs.
- Canonical URLs only.
- Each basename appears **once** in the final manifest.

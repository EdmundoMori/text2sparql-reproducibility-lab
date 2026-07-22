# Resolver root-cause analysis (Prompt 23B)

**RUN_ID:** `20260722T132719Z`

## Finding

Prompt 23 mapped every `core/_checksums.md5` entry to `core-i18n/en/<filename>`.
For 33 `*_en_uris_<lang>.ttl.bz2` members, that path returns **HTTP 404**.

## Root cause (not a urljoin bug)

1. `core/` Apache listing shows ~90-byte symlink stubs → HEAD 404.
2. `core/_checksums.md5` writes paths as `./core-i18n/en/<file>` even for `*_en_uris_<lang>` files.
3. Actual payloads live under **`core-i18n/<lang>/`**, not `en/`.
4. Prompt 23 did not probe language directories after en/ 404.

`urllib.parse.urljoin` trailing-slash handling was not the failure mode for these 33.

## Guardrails preserved

- No GET of RDF/bz2 payloads
- HEAD-only for candidates
- Host allowlist
- No mirrors

## Fix applied

Resolver gains a **metadata-only fallback**: if HEAD to checksum-indicated path 404s and filename matches `*_en_uris_<lang>.ttl.bz2`, probe `core-i18n/<lang>/<filename>` before declaring unavailable.

Offline synthetic tests in `logs/.../resolver-tests.log`.

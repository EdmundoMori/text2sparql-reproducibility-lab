# Allowlist canonical path reconciliation

**RUN_ID:** `20260722T134313Z` · **Prompt:** 23C · **Network:** none

## Inconsistencia detectada

Prompt 23B generó `allowed_exact_paths` con prefijo **`//2016-10/...`**.

Causa: concatenación `'/' + urlsplit(source_url).path` cuando `path` ya empieza por `/`, produciendo doble slash.

## Por qué no basta normalizar en HTTP

El allowlist afirma igualdad exacta con el manifest. Depender de que un cliente colapse `//` ocultaría mismatches y permitiría paths no canónicos en el artefacto versionado.

## Distinción

| Concepto | Ejemplo |
|---|---|
| Manifest URL | `https://downloads.dbpedia.org/2016-10/core-i18n/en/labels_en.ttl.bz2` |
| URL path | `/2016-10/core-i18n/en/labels_en.ttl.bz2` |
| Allowlist path (antes) | `//2016-10/core-i18n/en/labels_en.ttl.bz2` |
| Allowlist path (después) | `/2016-10/core-i18n/en/labels_en.ttl.bz2` |

## Fix

Regenerar `allowed_payload_exact_paths` = `{urlsplit(u).path for u in manifest.files}` ordenado; separar checksum/metadata; sin red.

## Comprobación

- before: 114 double-slash payload paths · 0 exact matches
- after: 114 paths · set equality PASS
- scope científico (114 / 6925795437 / hash) **sin cambio**
- cero descarga

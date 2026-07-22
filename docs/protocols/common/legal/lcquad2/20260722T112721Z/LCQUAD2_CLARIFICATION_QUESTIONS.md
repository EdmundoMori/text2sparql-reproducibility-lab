# LCQUAD2_CLARIFICATION_QUESTIONS

**RUN_ID:** `20260722T112721Z` · T6C

1. ¿Existe licencia explícita en el pin de la fuente principal? → **No** (`AUTHORS_REPO_LICENSE_ABSENT_AT_PIN`).
2. ¿Existe en HEAD actual? → **No** (pin==HEAD).
3. ¿Declaración oficial README/homepage/release/issue? → README sin licencia; homepage no disponible; tags/releases vacíos; issues license search 0.
4. ¿Quién mantiene HF `mohnish/lc_quad`? → Namespace `mohnish`; commits posteriores mayoritariamente staff HF (`albertvillanova`, `lhoestq`, `system`).
5. ¿Vinculación explícita con autores? → **AUTHORSHIP_LINKAGE_UNVERIFIED** (username ≠ prueba de identidad).
6. ¿Cuándo apareció CC BY 3.0? → `ad2a5cfa3f43d76fefdae813bfd9bfab34258061` · 2022-08-26 · título “Fix missing tags in dataset cards (#4896)”.
7. ¿Quién la añadió? → Actor username `albertvillanova` · clase `PLATFORM_STAFF_OR_HF_DATASETS_MAINTAINER` (no prueba de autor del dataset).
8. ¿Qué revisión/archivos cubre? → Dataset card YAML `license: cc-by-3.0` en representación HF; alcance respecto al authors payload: **UNKNOWN**.
9. ¿HF obtiene bytes del authors repo? → Histórico: builder `_URL=…/archive/master.zip`. Actual: `_URL=data.zip` (sibling HF). Homepage citada.
10. ¿Commit/branch/archive? → Histórico: branch `master` mutable. Actual: `data.zip` en repo HF (no descargado).
11. ¿Checksum? → **No** en builder (`BUILDER_ARCHIVE_CHECKSUM_METADATA` ausente).
12. ¿Conserva DBpedia18/Wikidata? → Sí en features: `sparql_wikidata`, `sparql_dbpedia18` (card/builder).
13. ¿Alternativa bajo política lab? → **No** (autoridad/lineage insuficientes) → HOLD.
14. ¿UNKNOWN? → Autoridad real de `mohnish`; cobertura legal del payload authors; byte-equivalence; checksums.
15. ¿Cerrar T6C sin adquisición? → **Sí** (este gate).

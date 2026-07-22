# TEMPORAL_PIN_DECISIONS

**RUN_ID:** `20260722T090627Z`

## QALD-9 Plus

| Campo | Valor |
|---|---|
| Publicación paper | ICSC 2022 (Crossref print 2022-01); arXiv 2202.00120 |
| Repo | https://github.com/Perevalov/qald_9_plus |
| Default branch | main |
| Tags/releases | **ninguno** (metadata API) |
| Current HEAD | `8eb038a61e1bc09cbd21640aa667a1714f53cda4` (2022-08-31) |
| Selección | **CURRENT_SOURCE_SNAPSHOT_NOT_PUBLICATION_RELEASE** |
| Razón | No hay tag/release oficial; se fija HEAD inmutable con qualifier |
| Drift | Commits posteriores a paper (fixes IDs/answers 2022-04..08) |

## LC-QuAD 2.0

| Campo | Valor |
|---|---|
| Publicación paper | ISWC 2019 (Crossref 2019) |
| Repo | https://github.com/AskNowQA/LC-QuAD2.0 |
| Default branch | master |
| Tags/releases | **ninguno** |
| Dataset files añadidos | commit `ee469725ca6c` (2019-07-03) `Add dataset` |
| Current HEAD | `0a5f8f85b6f863c3b80f0fa02839e25d438af3ae` (2021-03-15) |
| Selección | **CURRENT_SOURCE_SNAPSHOT_NOT_PUBLICATION_RELEASE** |
| Razón | Sin tag; HEAD inmutable; train/test aparecen desde 2019-07-03 |
| Drift | HEAD añade `entities_covered` / predicates (2021) — payloads dataset no leídos |

**Regla:** no seleccionar `main`/`master` mutable como pin; se usa SHA completo.

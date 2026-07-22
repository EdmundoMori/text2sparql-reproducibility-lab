# HUMAN_QALD9PLUS_ACQUISITION_APPROVAL

**Estado:** `SIGNED_APPROVED_CONSUMED` · autorización ejecutada en T6B

| Campo | Valor |
|---|---|
| Proyecto | text2sparql-reproducibility-lab |
| Prompt 21A RUN_ID | `20260722T105246Z` |
| Scope | QALD9PLUS_EN_DBPEDIA_T6B |
| Source | `Perevalov/qald_9_plus` @ `8eb038a61e1bc09cbd21640aa667a1714f53cda4` |
| Tree OID | `7159958810958ff185187cf603e2c4a997dc2df9` |
| Licencia | CC-BY-4.0 |
| Coste máximo USD | 0.00 |
| Destino | `workdir/datasets/qald9_plus/8eb038a61e1bc09cbd21640aa667a1714f53cda4/` |
| Total bytes | 7815874 |
| authorization_id | `AUTH_QALD9PLUS_T6B_20260722T105246Z_EMO_01` |

## Archivos

| Path | size | git_blob_oid |
|---|---:|---|
| data/qald_9_plus_train_dbpedia.json | 6371289 | cce48cbdf2af7f5e8ce59308dda667de7fc209b8 |
| data/qald_9_plus_test_dbpedia.json | 1424744 | 06cc04be82be7c807631a419670fb011a9565ec1 |
| LICENSE | 18650 | 2f244ac814036ecd9ba9f69782e89ce6b1dca9eb |
| CITATION.cff | 1191 | 4506fd12bdff0cbe14dd40a92a193c38cb747bc7 |

## Network allowlist
`raw.githubusercontent.com`, `api.github.com` · repo/commit/paths exactos · resto DENY.

## Atribución
Ver draft `QALD9PLUS_ATTRIBUTION_MANIFEST_DRAFT.yaml` (CC BY 4.0; authors desde CITATION.cff).

## Acciones autorizables (futuro T6B)
descarga de los cuatro · validación hashes/JSON/conteos · almacenamiento workdir · test seal · logs.

## Acciones prohibidas
grafos · SPARQL · adapters · métricas · gold · benchmark · LC-QuAD · Wikidata JSON · mirrors · archives.

## Stop conditions
blob/size mismatch · oversized · redirect no allowlisted · HTML-as-JSON · count mismatch condicional · cualquier coste >0.

## Consumo
La autorización se consume tras un intento PASS/FAIL/ABORT.

---

### Casillas (sin marcar)

[x] Apruebo la descarga de los dos JSON DBpedia.
[x] Apruebo la descarga de LICENSE y CITATION.cff.
[x] Apruebo validación de hashes, JSON y conteos.
[x] Apruebo el almacenamiento bajo workdir.
[x] Confirmo que no autorizo grafos, SPARQL, adapters ni benchmark.
[x] Confirmo que la autorización se consumirá tras un intento.

| Campo | Valor |
|---|---|
| Approver | EDMUNDO MORI ORRILLO |
| Date | 2026-07-22 |
| Decision | APPROVED |
| Signature/confirmation | Confirmo expresamente la autorización y acepto consumo tras un único intento. |

**Firmado por el investigador. Consumido en ejecución `20260722T111153Z` (PASS).**

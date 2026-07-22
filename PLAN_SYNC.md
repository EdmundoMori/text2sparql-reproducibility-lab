# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **23B** — file-scope closure)  
**Fase:** 1 **cerrada** · 2 **file scope CLOSED** · human acquisition auth **pending**  
**SHA inicial 23B:** `9b0a56273505cb9967d0f505ed3ba216e92287b2`  
**File-scope RUN_ID:** `20260722T132719Z`  

> ZERO_COST. Gate `DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_FILE_SCOPE_CLOSED_PARTIAL_PUBLISHED_CHECKSUMS_READY_FOR_HUMAN_ACQUISITION_AUTHORIZATION`.  
> 33/33 blockers resueltos → canónico `core-i18n/{lang}/`.  
> Final: **114** files / **6925795437** bytes · MD5 98.2456% files / 98.7587% bytes · 2 LHD sin MD5.  
> Ontology excluida. Form `READY_UNSIGNED`. Payload **NOT_ACQUIRED**.  
> QALD sealed/consumed · LC-QuAD HOLD · G4 runtime **no** · adapters **false** · benchmark **no**.  
> Siguiente: **HUMAN_DBPEDIA_2016_10_GRAPH_ACQUISITION_AUTHORIZATION** (no prompt ejecutable). Prompt 24B reservado.  
> Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 23B — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T132719Z` |
| Gate | `DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_FILE_SCOPE_CLOSED_PARTIAL_PUBLISHED_CHECKSUMS_READY_FOR_HUMAN_ACQUISITION_AUTHORIZATION` |
| Blockers | 33 in → 33 resolved → 0 unresolved required |
| Ontology | NOT_DOCUMENTED_AS_ENDPOINT_COMPONENT |
| Final files / bytes | 114 / 6925795437 |
| Checksum | partial MD5; SHA-256 post-download required |
| Form | `READY_UNSIGNED` |
| Acquisition / deployment | NOT_ACQUIRED / NOT_DEPLOYED |
| Coste | 0.00 |

---

## 3. Metadata Prompt 23 (reconciliada)

| Campo | SHA |
|---|---|
| initial HEAD | `831f34b8aa488d17200a29ec9d04c76796adbbcf` |
| ARTIFACT_COMMIT | `e24e36c2cc65692b981e7f1e7990d4bfcce496c7` |
| publication metadata commit | `9b0a56273505cb9967d0f505ed3ba216e92287b2` |
| remote tip final post-23 | `9b0a56273505cb9967d0f505ed3ba216e92287b2` |

---

## 4. Siguiente acción (única)

**HUMAN_DBPEDIA_2016_10_GRAPH_ACQUISITION_AUTHORIZATION** — HUMAN_GATE_REQUIRED.

No prompt Cursor ejecutable. Reservado: **Prompt 24B** (adquisición compressed-only tras aprobación). Adquisición ≠ despliegue.

---

## 5. Registro Prompt 23B

| Campo | Valor |
|---|---|
| commit inicial | `9b0a56273505cb9967d0f505ed3ba216e92287b2` |
| ARTIFACT_COMMIT | *(post-commit)* |
| publication metadata commit | *(post-push tip; max 2 commits)* |
| push | pending |

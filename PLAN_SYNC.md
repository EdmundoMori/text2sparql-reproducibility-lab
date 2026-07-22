# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **23C** — static consistency)  
**Fase:** 1 **cerrada** · 2 **static consistency PASS** · human auth **pending**  
**SHA inicial 23C:** `db2debaec4063b4145a3c83f533dc31a2f4ae9a9`  
**Consistency RUN_ID:** `20260722T134313Z`  

> ZERO_COST · **sin red**. Gate `DBPEDIA_ACQUISITION_PACKAGE_STATIC_CONSISTENCY_VERIFIED_READY_FOR_HUMAN_AUTHORIZATION`.  
> Fix: allowlist `//` → `/` · 114/114 set equality. Scope 114 / 6925795437 intacto.  
> Form READY_UNSIGNED · auth UNSIGNED · NOT_ACQUIRED.  
> Siguiente: **HUMAN_DBPEDIA_2016_10_GRAPH_ACQUISITION_AUTHORIZATION**. Prompt 24B reservado.  
> Objetivo largo plazo intacto.

---

## 1. Objetivo

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 23C — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T134313Z` |
| Inconsistencia | 114 paths `//2016-10/...` en allowlist |
| After | 114 `/2016-10/...` · equality PASS |
| Validator | STATIC_CONSISTENCY_PASS |
| Form | READY_UNSIGNED |
| Coste / red | 0.00 / none |

---

## 3. Metadata Prompt 23B (reconciliada)

| Campo | SHA |
|---|---|
| initial HEAD | `9b0a56273505cb9967d0f505ed3ba216e92287b2` |
| ARTIFACT_COMMIT | `5fbbcc47a5a4d28c264ec6c20c4a6212ac870904` |
| publication metadata commit | `db2debaec4063b4145a3c83f533dc31a2f4ae9a9` |
| remote tip final post-23B | `db2debaec4063b4145a3c83f533dc31a2f4ae9a9` |
| push | confirmed |

Gate histórico 23B conservado (file-scope closed partial checksums).

---

## 4. Siguiente acción

**HUMAN_DBPEDIA_2016_10_GRAPH_ACQUISITION_AUTHORIZATION** — HUMAN_GATE_REQUIRED.  
No prompt Cursor ejecutable. Reservado: **Prompt 24B**.

---

## 5. Registro Prompt 23C

| Campo | Valor |
|---|---|
| commit inicial | `db2debaec4063b4145a3c83f533dc31a2f4ae9a9` |
| ARTIFACT_COMMIT | *(post-commit)* |
| publication metadata commit | *(post-push tip; max 2 commits)* |
| push | pending |

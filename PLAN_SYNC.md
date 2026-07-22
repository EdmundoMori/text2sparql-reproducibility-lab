# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **21A** — QALD acquisition authorization package)  
**Fase:** 1 **cerrada** · 2 **T6A package ready** (human authorization pending)  
**SHA inicial 21A:** `7628a8c68c9070819dab8a221c71d54341ba62b6`  
**Acquisition package RUN_ID:** `20260722T105246Z`  

> ZERO_COST. Gate `QALD9PLUS_ACQUISITION_PACKAGE_READY_FOR_HUMAN_AUTHORIZATION`.  
> Scope: 4 archivos QALD EN/DBpedia · total **7815874** · pin `8eb038a61e1bc09cbd21640aa667a1714f53cda4` · tree `7159958810958ff185187cf603e2c4a997dc2df9`.  
> Authorization **UNSIGNED** · acquisition **NOT_ACQUIRED** · form humano pendiente.  
> G4 **no** · G5 runtime **pending** · G6D **sí** · G6I **pending**. Adapters **false**. Benchmark **no**.  
> Siguiente: **decisión humana** (no Cursor prompt ejecutable). Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 21A — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T105246Z` |
| Gate | **QALD9PLUS_ACQUISITION_PACKAGE_READY_FOR_HUMAN_AUTHORIZATION** |
| Source pin | `8eb038a61e1bc09cbd21640aa667a1714f53cda4` |
| Tree OID | `7159958810958ff185187cf603e2c4a997dc2df9` |
| Files | train/test DBpedia JSON + LICENSE + CITATION.cff |
| Total bytes | 7815874 |
| Attribution | DRAFT_NOT_APPLIED |
| Test seal | PLAN_DEFINED (not sealed) |
| Authorization | UNSIGNED |
| Acquisition | NOT_ACQUIRED |
| Coste | 0.00 · no download · no T6B |

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_metric_adapter_and_legal_contracts_defined_pending_assets_implementation_and_benchmark |
| PE6 | diagnostic_metric_observability_and_legal_boundaries_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

---

## 3. Metadata Prompt 20 (reconciliada)

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `127362e3d706a668f528a54371f0ab1bdb6cb8cb` |
| publication metadata commit | `7628a8c68c9070819dab8a221c71d54341ba62b6` |
| remote tip final post-20 | `7628a8c68c9070819dab8a221c71d54341ba62b6` |

---

## 4. Siguiente paso (humano; único)

**HUMAN_QALD9PLUS_ACQUISITION_AUTHORIZATION**

Formulario UNSIGNED: `docs/protocols/common/acquisition/qald9plus/20260722T105246Z/HUMAN_QALD9PLUS_ACQUISITION_APPROVAL.md`

**No** hay Prompt Cursor ejecutable hasta decisión humana.  
Prompt 21B queda **reservado / no autorizado**.

Cola: `audit/PHASE2_POST_T6A_QUEUE.csv`.

---

## 5. Registro Prompt 21A

| Campo | Valor |
|---|---|
| commit inicial | `7628a8c68c9070819dab8a221c71d54341ba62b6` |
| ARTIFACT_COMMIT | `2a2e6610d6f7ddd2b087a28eac856316196061a8` |
| publication metadata commit | *(post-push tip; max 2 commits)* |
| push | pending |

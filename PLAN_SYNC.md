# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **21B** — QALD controlled acquisition T6B)  
**Fase:** 1 **cerrada** · 2 **QALD EN/DBpedia adquirido y validado** (grafo y LC-QuAD pendientes)  
**SHA inicial 21B:** `4a790711453c8c3801a9f08915bedb710613b883`  
**Execution RUN_ID:** `20260722T111153Z`  
**authorization_id:** `AUTH_QALD9PLUS_T6B_20260722T105246Z_EMO_01` · **CONSUMED**

> ZERO_COST. Gate `QALD9PLUS_CONTROLLED_ACQUISITION_PASS_VALIDATED`.  
> 4 archivos verificados · total 7815874 · test SEALED · payloads en workdir only.  
> G4 **no** · G5 runtime **pending** · G6I **pending**. Adapters **false**. Benchmark **no**.  
> Siguiente: **Prompt 22 / T6C** (LC-QuAD license clarification). Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 21B — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T111153Z` |
| Auth | `AUTH_QALD9PLUS_T6B_20260722T105246Z_EMO_01` CONSUMED |
| Gate | **QALD9PLUS_CONTROLLED_ACQUISITION_PASS_VALIDATED** |
| Counts | train 408 / test 150 |
| Test seal | SEALED |
| Graph | still pending |
| Coste | 0.00 |

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_metric_adapter_and_legal_contracts_defined_pending_assets_implementation_and_benchmark |
| PE6 | diagnostic_metric_observability_and_legal_boundaries_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

---

## 3. Metadata Prompt 21A (reconciliada)

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `2a2e6610d6f7ddd2b087a28eac856316196061a8` |
| publication metadata commit | `4a790711453c8c3801a9f08915bedb710613b883` |
| remote tip final post-21A | `4a790711453c8c3801a9f08915bedb710613b883` |

---

## 4. Siguiente prompt (único)

**Prompt 22 — Clarificación documental de licencia/alcance de LC-QuAD 2.0 o representación alternativa, ZERO_COST, sin descargar payloads.**

Acción: **T6C**. **No ejecutado en 21B.**

---

## 5. Registro Prompt 21B

| Campo | Valor |
|---|---|
| commit inicial | `4a790711453c8c3801a9f08915bedb710613b883` |
| ARTIFACT_COMMIT | `0439421345cc63d167589f5ac399c97cc432eff2` |
| publication metadata commit | *(post-push tip; max 2 commits)* |
| push | pending |

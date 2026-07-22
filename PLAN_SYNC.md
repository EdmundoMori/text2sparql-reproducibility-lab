# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-22 (Prompt **19** — adapter contracts)  
**Fase:** 1 **cerrada** · 2 **G6D documental** (T5 legal pending)  
**SHA inicial 19:** `39bddbb2c85bce866d41d020f7ea5b50ce4fa45e`  
**Adapter RUN_ID:** `20260722T095602Z`  
**adapter_contract_version:** `0.1.0-documentary`

> ZERO_COST. Gate `ADAPTER_CONTRACTS_DOCUMENTED_READY_FOR_LEGAL_ELIGIBILITY_RECHECK`. G6D **sí** · G6I **pending**. Adapters **false**. Benchmark **no**. Objetivo largo plazo intacto.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 19 — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20260722T095602Z` |
| Gate | **ADAPTER_CONTRACTS_DOCUMENTED_READY_FOR_LEGAL_ELIGIBILITY_RECHECK** |
| G6D / G6I | documented / pending |
| Contratos | SPARQL-LLM (generate-only + feedback) · SGPT q/qk · mKG legal-blocked · RDFConfig domain + DBpedia **negative** · CoT native/frozen · FIRE raw/cleaned/RAG · TeBaQA historical |
| Vectors | 42 · NOT_EXECUTED |
| Candidates after gates | sparql_llm · sgpt_q/qk (current allowed=false) |
| G3/G4/G5 | legal recheck pending / G4 no / G5 runtime pending |
| Coste | 0.00 |

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | protocol_metric_and_adapter_contracts_defined_pending_implementation_and_benchmark |
| PE6 | diagnostic_metric_and_adapter_observability_contracts_defined_pending_execution |
| PE7 | not_started |
| PE8 | not_started |

---

## 3. Metadata Prompt 18 (reconciliada)

| Campo | SHA |
|---|---|
| ARTIFACT_COMMIT | `09f38f5fc77302dff235651375120415f2213399` |
| publication metadata commit | `39bddbb2c85bce866d41d020f7ea5b50ce4fa45e` |
| remote tip final post-18 | `39bddbb2c85bce866d41d020f7ea5b50ce4fa45e` |

---

## 4. Siguiente prompt (único)

**Prompt 20 — Revalidación documental de licencias y gate de elegibilidad legal para adapters, datasets y artefactos de Fase 2, ZERO_COST, sin descargar ni implementar.**

Fuente: `audit/NEXT_AFTER_ADAPTER_CONTRACT_DECISION.md` (T5). **No ejecutado en 19.**

---

## 5. Registro Prompt 19

| Campo | Valor |
|---|---|
| commit inicial | `39bddbb2c85bce866d41d020f7ea5b50ce4fa45e` |
| ARTIFACT_COMMIT | *(se registra tras commit)* |
| publication metadata commit | *(tip remoto = publication commit; max 2 commits)* |
| push | pending |

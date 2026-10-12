# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-10-12 (Prompt **25R2** — ZERO_COST recovery protocol)  
**Fase:** 1 **cerrada** · 2 **recovery protocol defined** · fairness **pending**  
**SHA inicial 25R2:** `3c57735c4e1f7100fc5e98c54a6505767951e61a`  
**Recovery protocol RUN_ID:** `20261012T125143Z`  

> Protocol `1.0.0-25R2` · Gate `ZERO_COST_METHOD_RECOVERY_PROTOCOL_DEFINED_READY_FOR_FAIR_COMPARISON_CONTRACT`.  
> RG0–RG9 · state machine · effort parity · controlled variants · no execution.  
> Priority: A sparql/sgpt · B rdfconfig/mkg · C cot · D fire · E tebaqa.  
> QALD/DBpedia preserved · deploy deferred · G4 NOT_SATISFIED · adapters false.  
> Siguiente: **DEFINE_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT** (Prompt_25R3).  
> Objetivo largo plazo intacto.

---

## 1. Objetivo

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 25R2 — resumen

| Campo | Valor |
|---|---|
| RUN_ID | `20261012T125143Z` |
| Protocol | `1.0.0-25R2` |
| Methods / matrix rows | 7 / 9 |
| Gate | `ZERO_COST_METHOD_RECOVERY_PROTOCOL_DEFINED_READY_FOR_FAIR_COMPARISON_CONTRACT` |
| Next | `DEFINE_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT` |
| Coste / exec / train | 0.00 / no / no |

---

## 3. Metadata Prompt 25R1 (reconciliada)

| Campo | SHA |
|---|---|
| initial HEAD | `763b7953a1dea907c3250cc05896d2f985454118` |
| ARTIFACT_COMMIT | `82f0d28ac0d45cb342202e77be86cfb4a650fb57` |
| publication metadata commit | `3c57735c4e1f7100fc5e98c54a6505767951e61a` |
| remote tip final post-25R1 | `3c57735c4e1f7100fc5e98c54a6505767951e61a` |
| push | confirmed |

---

## 4. Siguiente acción

**DEFINE_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT** — GO_NEXT_ZERO_COST.  
**Prompt_25R3**. No 25B / profile / deploy / train / recovery execution / benchmark aún.

---

## 5. Registro Prompt 25R2

| Campo | Valor |
|---|---|
| commit inicial | `3c57735c4e1f7100fc5e98c54a6505767951e61a` |
| ARTIFACT_COMMIT | *(post-commit)* |
| publication metadata commit | *(post-commit tip; max 2 commits)* |
| push | pending |

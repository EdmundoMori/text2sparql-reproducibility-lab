# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt **14A** — protocolo Z3 documental)  
**Fase:** 1 — native audit; **abierta**  
**SHA inicial 14A:** `9d7f9412c663544251c73582f7b6c7db79446555`

> ZERO_COST. Z1/Z2 cerrados. Z3 **protocolo definido**. Sin GPT-2 download, sin train, sin model load.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Metadata Prompt 13B (reconciliada)

| Campo | Valor |
|---|---|
| ARTIFACT_COMMIT | `15e918540b7de616751ce06b96ef8de4f25f0f75` |
| CONTENT_HEAD | `15e918540b7de616751ce06b96ef8de4f25f0f75` |
| publication metadata commits | `f753cbf6…`, `979d7275…`, `94ef66a2…` |
| remote tip after 13B publication | `9d7f9412c663544251c73582f7b6c7db79446555` |

---

## 3. Prompt 14A — resumen

| Campo | Valor |
|---|---|
| Acción | PZ1 protocolo Z3 |
| RUN_ID | `20260721T134213Z` |
| Gate | **`READY_FOR_Z3_ARTIFACT_PREFLIGHT_AUTHORIZATION`** |
| Variante | lcquad2 QUESTION_ONLY CPU |
| Subset | 1/1/1 uids 8714 / 3988 / 6077 |
| Expected optimizer steps | **1** (validar pre-run) |
| GPT-2 | `openai-community/gpt2` @ `607a30d783dfa663caf39e06633721c8d4cfcd7e` |
| tensorboardX | `2.5.1` |
| Descargas / install / load / forward / train | **0** |
| Coste | **0.00** |
| Auths | 2 formularios UNSIGNED |
| `reproduction_status` | `audit_only` |

Informe: [`audit/sgpt/Z3_REDUCED_TRAINING_PROTOCOL_REPORT.md`](audit/sgpt/Z3_REDUCED_TRAINING_PROTOCOL_REPORT.md)

---

## 4. Siguiente prompt (único)

Tras firma de `HUMAN_Z3_ARTIFACT_AND_MODEL_PREFLIGHT_APPROVAL.md`:

**Prompt 14B — Descarga controlada de artefactos GPT-2 y preflight offline de carga SGPT Z3, ZERO_COST, sin train.**

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 5. PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 6. Registro Prompt 14A

| Campo | Valor |
|---|---|
| commit inicial | `9d7f9412c663544251c73582f7b6c7db79446555` |
| ARTIFACT_COMMIT | PENDING_ARTIFACT |
| FINAL_HEAD / CONTENT tip | PENDING_FINAL |
| push | pending |

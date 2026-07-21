# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt **13A** — build SGPT Z2)  
**Fase:** 1 — native audit; **abierta**  
**SHA inicial 13A:** `8fbacdf07b0446dd16ed68cafe0c453fd9479b37`  
**RUN_ID:** `20260721T114919Z`

> ZERO_COST. Z2 CPU **construido** y preflight **PASS**. Sin GPT-2 / spaCy models / NLTK data / train.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Prompt 13A — resumen

| Campo | Valor |
|---|---|
| Aprobador | EDMUNDO MORI ORRILLO |
| Imagen base digest | `sha256:314bc2fb…` verificado |
| Imagen lab | `text2sparql-lab/sgpt-z2-py38:20260721T114919Z` |
| torch | `1.13.1+cpu` |
| transformers | `4.25.1` |
| Clasificación | **`Z2_ENV_IMPORT_DATA_METRIC_PASS`** |
| Gate | **`Z2_ENV_READY_PREFLIGHT_PASS`** |
| GPT-2 / spaCy / NLTK data | no descargados |
| Coste | **0.00** |
| `reproduction_status` | `audit_only` |

Informe: [`audit/sgpt/Z2_BUILD_AND_PREFLIGHT_REPORT.md`](audit/sgpt/Z2_BUILD_AND_PREFLIGHT_REPORT.md)

---

## 3. Siguiente prompt (único)

**Prompt 13B — Cierre documental del entorno SGPT Z2 y decisión de cola ZERO_COST (sin Z3; sin train).**

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 4. PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence (Z2 env+preflight) |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 5. Registro Prompt 13A

| Campo | Valor |
|---|---|
| commit inicial | `8fbacdf07b0446dd16ed68cafe0c453fd9479b37` |
| RUN_ID | `20260721T114919Z` |
| gate | `Z2_ENV_READY_PREFLIGHT_PASS` |
| commit final | `bca804c3a49127adee8208a17c50ac96b20bbf1e` |
| push | done |

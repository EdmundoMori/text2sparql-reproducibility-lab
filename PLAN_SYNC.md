# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt **12B** — pins SGPT)  
**Fase:** 1 — native audit; **abierta**  
**SHA inicial 12B:** `392c101ef4f0defde8b19c6c49eac0064dc6954a`  
**RUN_ID:** `20260721T113310Z`

> ZERO_COST. Sin install/pull/train. Gate: **READY_FOR_Z2_DOWNLOAD_AUTHORIZATION**.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Metadata commits

| Prompt | Artifact commit | Final HEAD |
|---|---|---|
| 12 | `dbdefdf4bffc04d5f7ea231ee068e7b9cdfaeea6` | `392c101ef4f0defde8b19c6c49eac0064dc6954a` |
| **12B** | `89785fddc3b8c75d6a805631fa3f98d009f33efd` | _(tras push)_ |

---

## 3. Prompt 12B — resumen

| Campo | Valor |
|---|---|
| Ancla temporal | 2022-12 (requirements + TF 4.25.1) |
| Python | 3.8.20-slim-bookworm |
| Digest amd64 | `sha256:314bc2fb0714b7807bf5699c98f0c73817e579799f2d91567ab7e9510f5601a5` |
| torch Z2 | `torch==1.13.1+cpu` (sha256 wheel `4a8b8483…`) |
| Transformers | **4.25.1** SELECTED_CANDIDATE_UNTESTED |
| Símbolos | all present (`OFFICIAL_SOURCE_TAG_VERIFIED`) |
| Pins directos | constraints native + Z2 (candidato ≠ lock) |
| Transitivas | METADATA_KNOWN_NOT_LOCKED |
| spaCy / NLTK / GPT-2 | deferred downloads; GPT-2 out of Z2 |
| Gate | **READY_FOR_Z2_DOWNLOAD_AUTHORIZATION** |
| Descargas binarias / installs / train / infer | **0 / 0 / 0 / 0** |
| Coste | **0.00** |
| `reproduction_status` | `audit_only` |

Informe: [`audit/sgpt/PIN_RESOLUTION_REPORT.md`](audit/sgpt/PIN_RESOLUTION_REPORT.md)

---

## 4. Siguiente prompt (único)

**Prompt 13A — Autorización y descarga controlada de imagen y paquetes SGPT Z2 + construcción del entorno CPU, ZERO_COST, sin GPT-2, sin modelos spaCy, sin train.**

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

## 6. Registro Prompt 12B

| Campo | Valor |
|---|---|
| commit inicial | `392c101ef4f0defde8b19c6c49eac0064dc6954a` |
| RUN_ID | `20260721T113310Z` |
| gate | `READY_FOR_Z2_DOWNLOAD_AUTHORIZATION` |
| commit final | `89785fddc3b8c75d6a805631fa3f98d009f33efd` |
| push | confirmado en origin/main |

# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia:** ChatGPT (planificador) e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt **12** — entorno SGPT documental)  
**Fase:** 1 — native audit; **abierta**  
**SHA inicial Prompt 12:** `d7b199c9caf8035e88eedf717ab7926dcc2d7a11`

> ZERO_COST activo. Sin OpenRouter / train / GPT-2 download en este prompt.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Metadata commits (corrección)

| Prompt | Artifact commit | Final HEAD |
|---|---|---|
| 11 | `ee477c9d1d37b86d03593c141cd90577f7f1ba43` | `a2478b721970444401bd7edae313e1e1aa81926e` |
| **11C** | `32f597c006d95b5603bf2fc4f5c18f423df28ca8` | `d7b199c9caf8035e88eedf717ab7926dcc2d7a11` |

No denominar artifact commit como HEAD final.

---

## 3. Prompt 12 — resumen

| Campo | Valor |
|---|---|
| Método | `sgpt` |
| Acción | Z1 SGPT_ENVIRONMENT_DEFINITION |
| Gate entorno | **`CONDITIONAL_DEPENDENCY_RESOLUTION`** |
| Python declarado | **3.8** |
| torch declarado | **1.13.1** |
| transformers pin | **UNKNOWN** (unpinned) |
| Perfiles | A NATIVE_DECLARED; B Z2; C Z3 blocked |
| GPT-2 | not_downloaded |
| Checkpoints SGPT | NOT_FOUND |
| Z2 | specified_not_executed |
| Z3 | blocked_pending_Z2_and_download_authorization |
| Descargas / train / infer | **0 / 0 / 0** |
| Coste externo | **0.00** |
| `reproduction_status` | `audit_only` |
| `native_audit_complete` | `false` |
| `common_adapter_allowed` | `false` |

Informe: [`audit/sgpt/ENVIRONMENT_DEFINITION_REPORT.md`](audit/sgpt/ENVIRONMENT_DEFINITION_REPORT.md)

---

## 4. Siguiente prompt (único)

**Prompt 12B — Resolución documental de pins SGPT mediante metadata oficial y compatibilidad, ZERO_COST, sin instalación.**

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

## 6. Registro Prompt 12

| Campo | Valor |
|---|---|
| commit inicial | `d7b199c9caf8035e88eedf717ab7926dcc2d7a11` |
| gate | `CONDITIONAL_DEPENDENCY_RESOLUTION` |
| commit final | `dbdefdf4bffc04d5f7ea231ee068e7b9cdfaeea6` |
| push | confirmado en origin/main |

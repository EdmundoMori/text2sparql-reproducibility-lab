# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador) e investigador.  
**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-21 (Prompt 10B — embedding + índice + preflight)  
**Fase:** 1 — native audit; **abierta**  
**Commit inicial 10B:** `96d5bab9556065cd0cd5785327475565ce910cba`  
**RUN_ID:** `20260721T092249Z`

> Smoke ≠ PE3. Caché/índice en `workdir/` **no** van a Git. MCP público ≠ pin local.

---

## 1. Objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

---

## 2. Completado reciente

| # | Prompt | Resultado |
|---|---|---|
| 5B | CORE_OFFLINE | `smoke_only` |
| 9 | Protocolo API/SIB | CONDITIONAL_GO → LOCAL_CHAT_API_ONE_QUESTION |
| 10 | Env agent + docs | index blocked (sin caché) |
| **10B** | Download e5-large + index + preflight | **`ENVIRONMENT_READY_INDEX_READY_PREFLIGHT_PASS`** |

---

## 3. Prompt 10B — resumen

| Campo | Valor |
|---|---|
| Autorización | EDMUNDO MORI ORRILLO, 2026-07-21 |
| Modelo | `intfloat/multilingual-e5-large` (exacto) |
| Procedencia | FastEmbed 0.8.0 → GCS `fast-multilingual-e5-large.tar.gz` (HF metadata `qdrant/multilingual-e5-large-onnx`) |
| Caché | ~2.1 GiB en workdir (**gitignored**) |
| Índice | 12 pts, dim 1024, Cosine, `INDEX_VERIFIED` |
| Preflight | pass — `/chat`,`/mcp`,`/openapi.json`; **sin** POST `/chat` |
| LLM / SPARQL / POST | **0 / 0 / 0** |
| Gate | **CONDITIONAL_GO** (presupuesto/modelo) |
| `reproduction_status` | `smoke_only` |

Informe: [`audit/sparql_llm/LOCAL_CHAT_API_EMBEDDING_INDEX_PREFLIGHT_REPORT.md`](audit/sparql_llm/LOCAL_CHAT_API_EMBEDDING_INDEX_PREFLIGHT_REPORT.md)

---

## 4. Siguiente prompt

**Prompt 11 — Cierre de presupuesto, selección de modelo y gate final para LOCAL_CHAT_API_ONE_QUESTION**

No gastar clave hasta firma. No biodata. No otros métodos.

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 5. PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence (online path prepared; smoke no ejecutado) |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 6. Changelog

| Fecha | Cambio |
|---|---|
| 2026-07-21 | Prompt 10 env ready; index blocked |
| 2026-07-21 | Prompt 10B cache+index+preflight pass; next=Prompt 11 |

---

## 7. Registro Prompt 10B

| Campo | Valor |
|---|---|
| commit inicial | `96d5bab9556065cd0cd5785327475565ce910cba` |
| RUN_ID | `20260721T092249Z` |
| clasificación | `ENVIRONMENT_READY_INDEX_READY_PREFLIGHT_PASS` |
| commit final | `c3ad6c03daec5226f9ccd808294c0a1165d54975` (artefactos); HEAD `f823615cd69c34989c5933a3340213401c91303a` |
| push | confirmado en origin/main |

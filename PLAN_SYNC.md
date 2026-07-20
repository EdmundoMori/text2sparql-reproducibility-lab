# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador de prompts) y el investigador.  
**Repo GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-20 (Prompt 7A — CoT-SPARQL WAVE_C static → **audit_only**)  
**Fase lab:** 1 — native audit; WAVE_C parcial (cot_sparql complete; firesparql pending)  
**Commit inicial 7A:** `562b5f1108e3289ae5b93668f2bd9d994d0a5b28`

> Instrucción para el planificador: lee este archivo primero. **No asumas reproducción experimental**: clonar ≠ ejecutar ≠ reproducir un paper.

---

## 1. Objetivo del laboratorio (recordatorio)

Laboratorio local Text-to-SPARQL: auditar y, cuando sea posible, reproducir métodos publicados; luego evaluación común; a largo plazo, KG de descubrimiento de modelos de IA y método nuevo con ablaciones.

| Documento | Ruta |
|---|---|
| Contexto | [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) |
| Protocolo | [`RESEARCH_PROTOCOL.md`](RESEARCH_PROTOCOL.md) |
| Máquina | [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md) |
| Métodos | [`METHOD_REGISTRY.yaml`](METHOD_REGISTRY.yaml) |
| Pins | [`REPOSITORIES.lock.yaml`](REPOSITORIES.lock.yaml) |

---

## 2. Bucle Cursor ↔ ChatGPT

Detalle: [`docs/plan-sync/PLANNER_LOOP.md`](docs/plan-sync/PLANNER_LOOP.md). Tras cada prompt: actualizar PLAN_SYNC + índice + **commit/push**.

---

## 3. Qué se ha completado (prompts ejecutados)

| # | Prompt / acción | Resultado clave | Docs específicos |
|---|---|---|---|
| 0–4B | Fundación → entornos WAVE_A | Specs + gates | ver histórico |
| 5A | sparql CORE_OFFLINE host Py3.10 | **setup_failed** | [`audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md`](audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md) |
| 5B | sparql CORE_OFFLINE Docker Py3.11 | **smoke_only** | [`audit/sparql_llm/CORE_OFFLINE_PY311_SMOKE_REPORT.md`](audit/sparql_llm/CORE_OFFLINE_PY311_SMOKE_REPORT.md) |
| 6 | SGPT WAVE_B static | **audit_only** (static complete) | [`audit/sgpt/STATIC_AUDIT.md`](audit/sgpt/STATIC_AUDIT.md) |
| 7A | CoT-SPARQL WAVE_C static | **audit_only** (static complete; no install) | [`audit/cot_sparql/STATIC_AUDIT.md`](audit/cot_sparql/STATIC_AUDIT.md), [`audit/WAVE_C_STATIC_AUDIT_MATRIX.csv`](audit/WAVE_C_STATIC_AUDIT_MATRIX.csv) |

---

## 4. Hallazgos críticos

### 4.1 Máquina
WSL2 ~7.4 GiB RAM; RTX 4050 **6 GiB**; Compose ABSENT; Ruby ABSENT; Python 3.10.12.

### 4.2 Ondas
| Wave | Estado |
|---|---|
| A | static + env; sparql smoke_only |
| B | SGPT static complete |
| C | **7A cot_sparql complete**; **firesparql pending 7B** |
| D | tebaqa excluido |

### 4.3 Prompt 7A (CoT-SPARQL) — bloqueos
- Pin `063edd98…`; **LICENSE_NOT_CONFIRMED**; LICENSE ausente.  
- **No end-to-end:** EL/RL externos + one-shot retrieval con anotaciones gold de train + LLM GPTQ.  
- Embeddings/parquet `temp/*` **NOT_FOUND** (URLs externas README).  
- CodeLlama-34B-Instruct-GPTQ: **blocked** en 6 GiB.  
- `requirements.txt` = export Conda, no pip.  
- Validación = HTTP 200 a endpoints (no sintaxis local).  
- Anomalías: assert pregunta vacía; Falcon `None`; RL Wikidata `propertyLabel` vs `itemLabel`.  
- Datasets: solo train (QALD-9 350, QALD-10 412, LC-QuAD2 21497, VQuAnDa 3500); sin test/eval scripts.  
- `reproduction_status: audit_only`; `common_adapter_allowed: false`; `native_audit_complete: false`.

### 4.4 Lo que NO se ha hecho
- Install/ejecución CoT-SPARQL o FIRESPARQL.  
- Descarga embeddings/GPTQ.  
- Train SGPT; smoke API sparql; adapters; WAVE_C 7B.

---

## 5. Estado de reproducción

- `sparql_llm`: **smoke_only** (5B); 5A setup_failed.  
- `sgpt`: **audit_only** (WAVE_B static).  
- `cot_sparql`: **audit_only** (WAVE_C 7A static).  
- `firesparql`: **audit_only** (static **pending** 7B).  
- Ninguno `reproduced` / `partially_reproduced`.

---

## 6. Siguiente prompt recomendado

1. **Prompt 7B — Auditoría estática FIRESPARQL (WAVE_C)** (prioridad).  
2. No install CoT; no CodeLlama; no Falcon/Spotlight calls.  
3. Objetivo largo plazo: reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 7. Índice de artefactos

→ [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md)

---

## 8. Changelog

| Fecha | Cambio |
|---|---|
| 2026-07-20 | Prompt 5B smoke_only; Prompt 6 SGPT WAVE_B |
| 2026-07-20 | Prompt 7A CoT-SPARQL WAVE_C static; next=7B FIRESPARQL |

---

## 9. Registro de publicación

### 5A / 5B / 6 (históricos)
Ver commits previos en GitHub `main` (`setup_failed` / `smoke_only` / SGPT static).

### 7A (este prompt)
| Campo | Valor |
|---|---|
| alcance | CoT-SPARQL WAVE_C static audit |
| commit inicial | `562b5f1108e3289ae5b93668f2bd9d994d0a5b28` |
| resultado | **audit_only** (static complete; no execution) |
| commit final | `e1fe1fa96859779b633cade3dc70259d95e28c57` |
| rama | `main` |
| push | confirmado en origin/main (`aa97fff297dcb1bb173acd4ea9a7f86d7fab6d93`) |
| artefactos | `audit/cot_sparql/*`, `audit/WAVE_C_STATIC_AUDIT_MATRIX.csv` |

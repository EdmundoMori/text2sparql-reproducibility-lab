# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador de prompts) y el investigador.  
**Repo GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-20 (Prompt 7B — FIRESPARQL WAVE_C static → **audit_only**; **WAVE_C complete**)  
**Fase lab:** 1 — native audit; WAVE_A–C static complete  
**Commit inicial 7B:** `465755282cd3d44cc9f6918b707328ddf621bfb2`

> Instrucción para el planificador: lee este archivo primero. **No asumas reproducción experimental**: clonar ≠ ejecutar ≠ reproducir un paper. Resultados versionados en `results/` ≠ reproducidos localmente.

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

Detalle: [`docs/plan-sync/PLANNER_LOOP.md`](docs/plan-sync/PLANNER_LOOP.md).

---

## 3. Qué se ha completado (prompts ejecutados)

| # | Prompt / acción | Resultado clave | Docs específicos |
|---|---|---|---|
| 5A | sparql CORE_OFFLINE host Py3.10 | **setup_failed** | [`audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md`](audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md) |
| 5B | sparql CORE_OFFLINE Docker Py3.11 | **smoke_only** | [`audit/sparql_llm/CORE_OFFLINE_PY311_SMOKE_REPORT.md`](audit/sparql_llm/CORE_OFFLINE_PY311_SMOKE_REPORT.md) |
| 6 | SGPT WAVE_B static | **audit_only** | [`audit/sgpt/STATIC_AUDIT.md`](audit/sgpt/STATIC_AUDIT.md) |
| 7A | CoT-SPARQL WAVE_C static | **audit_only** | [`audit/cot_sparql/STATIC_AUDIT.md`](audit/cot_sparql/STATIC_AUDIT.md) |
| 7B | FIRESPARQL WAVE_C static | **audit_only**; **WAVE_C complete** | [`audit/firesparql/STATIC_AUDIT.md`](audit/firesparql/STATIC_AUDIT.md), [`audit/WAVE_C_STATIC_AUDIT_MATRIX.csv`](audit/WAVE_C_STATIC_AUDIT_MATRIX.csv) |

---

## 4. Hallazgos críticos

### 4.1 Máquina
WSL2 ~7.4 GiB RAM; RTX 4050 **6 GiB**; Compose ABSENT; Ruby ABSENT; Python 3.10.12.

### 4.2 Ondas
| Wave | Estado |
|---|---|
| A | static + env; sparql smoke_only |
| B | SGPT static complete |
| C | **complete** (7A cot_sparql + 7B firesparql) |
| D | tebaqa excluido |

### 4.3 Prompt 7B (FIRESPARQL) — bloqueos
- Pin `48d6f168…`; **LICENSE_NOT_CONFIRMED** (MIT HF checkpoint **no** licencia el código GitHub).  
- **Trainer LoRA/SFT ausente** en repo; evidencia externa LLaMa-Factory; `merge_models/` ABSENT; HPs LoRA UNKNOWN.  
- Pipeline: zero/one-shot/FT/RAG → GPT-4o cleaning → ORKG exec (**runner CODE_NOT_FOUND**) → BLEU/ROUGE/EM.  
- README dice QLever; árbol real = `step3_*_against_orkg`. Requirements “Coming soon”.  
- Paths `xueli_data/` / Snellius / macOS absolutos.  
- SciQA test **513** OK; ~60 configs step1; results versionados ≠ reproducción.  
- Generalidad: **domain_specific_reimplementation_required** (ORKG/SciQA).  
- `reproduction_status: audit_only`; `common_adapter_allowed: false`; `native_audit_complete: false`.

### 4.4 Lo que NO se ha hecho
- Install/inferencia/train FIRESPARQL o CoT.  
- Download checkpoint 8B; OpenAI/Groq/QLever calls.  
- Prompt 8 gate comparativo.  
- Adapters / evaluación común / caso de estudio.

---

## 5. Estado de reproducción

- `sparql_llm`: **smoke_only** (5B); 5A setup_failed.  
- `sgpt` / `cot_sparql` / `firesparql`: **audit_only** (static complete).  
- Ninguno `reproduced` / `partially_reproduced`.

---

## 6. Siguiente prompt recomendado

1. **Prompt 8 — Síntesis comparativa y gate de auditoría nativa** (prioridad).  
2. No train/infer FIRESPARQL; no cuantizar 8B como “reproducción”.  
3. Objetivo largo plazo: reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 7. Índice de artefactos

→ [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md)

---

## 8. Changelog

| Fecha | Cambio |
|---|---|
| 2026-07-20 | Prompt 7A CoT-SPARQL WAVE_C static |
| 2026-07-20 | Prompt 7B FIRESPARQL WAVE_C static; WAVE_C complete; next=Prompt 8 gate |

---

## 9. Registro de publicación

### 5A / 5B / 6 / 7A (históricos)
Ver GitHub `main`.

### 7B (este prompt)
| Campo | Valor |
|---|---|
| alcance | FIRESPARQL WAVE_C static audit |
| commit inicial | `465755282cd3d44cc9f6918b707328ddf621bfb2` |
| resultado | **audit_only** (static complete; WAVE_C complete) |
| commit final | *(tras push)* |
| rama | `main` |
| push | pendiente |
| artefactos | `audit/firesparql/*`, `audit/WAVE_C_STATIC_AUDIT_MATRIX.csv` |

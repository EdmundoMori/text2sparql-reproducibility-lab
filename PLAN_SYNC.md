# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador de prompts) y el investigador.  
**Repo GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-20 (Prompt 8 — síntesis comparativa y gate de auditoría nativa)  
**Fase lab:** 1 — native audit; WAVE_A–C static complete; **gate comparativo cerrado; Fase 1 no cerrada**  
**Commit inicial 8:** `dbb21de570e4da2647fcfe774a91590e086d9542`

> Instrucción para el planificador: lee este archivo primero. **No asumas reproducción experimental**: clonar ≠ ejecutar ≠ reproducir un paper. Resultados versionados en `results/` ≠ reproducidos localmente. Smoke ≠ PE3.

---

## 1. Objetivo del laboratorio (recordatorio)

Laboratorio local Text-to-SPARQL: auditar y, cuando sea posible, reproducir métodos publicados; luego evaluación común; a largo plazo, KG de descubrimiento de modelos de IA y método nuevo con ablaciones.

**Secuencia completa (no saltar):**
reproducción nativa → evaluación común → caso de estudio → análisis de errores → transferencia Text-to-SQL → método nuevo → ablaciones.

| Documento | Ruta |
|---|---|
| Contexto | [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) |
| Protocolo | [`RESEARCH_PROTOCOL.md`](RESEARCH_PROTOCOL.md) |
| Máquina | [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md) |
| Métodos | [`METHOD_REGISTRY.yaml`](METHOD_REGISTRY.yaml) |
| Pins | [`REPOSITORIES.lock.yaml`](REPOSITORIES.lock.yaml) |
| Gate nativo | [`audit/NATIVE_AUDIT_COMPARATIVE_GATE.md`](audit/NATIVE_AUDIT_COMPARATIVE_GATE.md) |
| Decisión siguiente | [`audit/NEXT_EXECUTION_DECISION.md`](audit/NEXT_EXECUTION_DECISION.md) |

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
| 8 | Gate comparativo nativo | **GO_NEXT** = protocolo API/SIB `sparql_llm` (documental) | [`audit/NATIVE_AUDIT_COMPARATIVE_GATE.md`](audit/NATIVE_AUDIT_COMPARATIVE_GATE.md), [`audit/NEXT_EXECUTION_DECISION.md`](audit/NEXT_EXECUTION_DECISION.md) |

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
| Gate | Prompt 8: dos colas (reproducción vs baselines); **exactamente un GO_NEXT** |

### 4.3 Prompt 8 — síntesis del gate
- **No** ranking único opaco; regla lexicográfica documentada.  
- Dimensiones separadas: valor baseline / reproducibilidad nativa / factibilidad / legal (por operación) / adaptabilidad.  
- **GO_NEXT único:** definición documental del protocolo API/SIB de `sparql_llm` (`protocol_definition`) → Prompt 9 **sin llamadas de API**.  
- Portafolio: conservar diversidad (schema/RAG; agentic; schema-guided; generative; CoT+grounding; FT dominio).  
- Tracks incompatibles no se comparan en una sola tabla de rendimiento.  
- `native_audit_complete=false`; `common_adapter_allowed=false`; estados de reproducción **sin cambio**.

### 4.4 Lo que NO se ha hecho (y se aplaza)
- Smoke API SPARQL-LLM (espera protocolo).  
- Train reducido SGPT; env CoT; install Ruby; run mKGQAgent; recomputar métricas FIRESPARQL; download checkpoints.  
- Adapters / evaluación común / caso de estudio.  
- Cierre de Fase 1.

---

## 5. Estado de reproducción

- `sparql_llm`: **smoke_only** (5B); 5A setup_failed; gate `GO_NEXT` → protocolo API/SIB.  
- `mkgqagent` / `rdfconfig_llm`: **audit_only**; `HOLD_LEGAL`.  
- `sgpt`: **audit_only**; `HOLD_MISSING_MODEL`.  
- `cot_sparql`: **audit_only**; `HOLD_HARDWARE`.  
- `firesparql`: **audit_only**; `HOLD_MISSING_CODE`.  
- Ninguno `reproduced` / `partially_reproduced`.

### PE1–PE4 (conservador)
| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 6. Siguiente prompt recomendado

1. **Prompt 9 — Definición documental del protocolo API/SIB de SPARQL-LLM (sin llamadas de API)** (único GO_NEXT).  
2. No smoke API hasta GO del protocolo; no train/infer otros métodos.  
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
| 2026-07-20 | Prompt 8 gate comparativo; GO_NEXT=protocolo API/SIB sparql_llm; next=Prompt 9 |

---

## 9. Registro de publicación

### 5A / 5B / 6 / 7A / 7B (históricos)
Ver GitHub `main`.

### 8 (este prompt)
| Campo | Valor |
|---|---|
| alcance | Síntesis comparativa + gate auditoría nativa (documental) |
| commit inicial | `dbb21de570e4da2647fcfe774a91590e086d9542` |
| resultado | **GO_NEXT** = protocolo API/SIB `sparql_llm`; Fase 1 no cerrada |
| commit final | *(se rellena tras push)* |
| rama | `main` |
| push | *(pendiente)* |
| artefactos | `audit/NATIVE_AUDIT_*`, `NEXT_EXECUTION_DECISION.md`, `docs/decisions/003_*`, `METHOD_REGISTRY.yaml` v0.11 |

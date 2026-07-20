# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador de prompts) y el investigador.  
**Repo GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-20 (Prompt 9 — protocolo API/SIB SPARQL-LLM documental)  
**Fase lab:** 1 — native audit; **Fase 1 abierta**  
**Commit inicial 9:** `3d89a8d61f3fed8eecec8e49f6b79baccf677a76`

> Instrucción para el planificador: lee este archivo primero. Clonar ≠ ejecutar ≠ reproducir. Smoke ≠ PE3. MCP público ≠ ejecución del commit pin.

---

## 1. Objetivo del laboratorio (recordatorio)

**Secuencia completa:**
reproducción nativa → evaluación común → caso de estudio → análisis de errores → transferencia Text-to-SQL → método nuevo → ablaciones.

| Documento | Ruta |
|---|---|
| Contexto | [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) |
| Protocolo | [`RESEARCH_PROTOCOL.md`](RESEARCH_PROTOCOL.md) |
| Máquina | [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md) |
| Métodos | [`METHOD_REGISTRY.yaml`](METHOD_REGISTRY.yaml) |
| Pins | [`REPOSITORIES.lock.yaml`](REPOSITORIES.lock.yaml) |
| Protocolo API/SIB | [`docs/protocols/sparql_llm/API_SIB_PROTOCOL.md`](docs/protocols/sparql_llm/API_SIB_PROTOCOL.md) |
| GO/NO-GO futuro | [`docs/protocols/sparql_llm/FUTURE_API_SMOKE_GONOGO.md`](docs/protocols/sparql_llm/FUTURE_API_SMOKE_GONOGO.md) |

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
| 7B | FIRESPARQL WAVE_C static | **audit_only**; WAVE_C complete | [`audit/firesparql/STATIC_AUDIT.md`](audit/firesparql/STATIC_AUDIT.md) |
| 8 | Gate comparativo nativo | **GO_NEXT** → protocolo API/SIB | [`audit/NATIVE_AUDIT_COMPARATIVE_GATE.md`](audit/NATIVE_AUDIT_COMPARATIVE_GATE.md) |
| 9 | Protocolo API/SIB sparql_llm | **CONDITIONAL_GO** → `LOCAL_CHAT_API_ONE_QUESTION` | [`docs/protocols/sparql_llm/API_SIB_PROTOCOL.md`](docs/protocols/sparql_llm/API_SIB_PROTOCOL.md) |

---

## 4. Hallazgos críticos

### 4.1 Prompt 9 — protocolo API/SIB
- Superficies separadas: PUBLIC_MCP_REMOTE, LOCAL_MCP_STDIO, LOCAL_MCP_STREAMABLE_HTTP, LOCAL_FASTAPI_CHAT, FULL_CHAT_STACK, MANUAL_BENCHMARK, BIODATA_BENCHMARK, TEXT2SPARQL_VIRTUOSO (**blocked**).  
- **MCP público ≠ nativo** (solo `external_service_availability_check`).  
- `/chat`: `max_tokens`/`temperature` del body **no** se propagan; `validate_output` **mismatched** vs `enable_output_validation` (`CODE_VERIFIED`).  
- `enable_sparql_execution=false` evita ejecución SPARQL en el agente (`CODE_VERIFIED`).  
- Import de `agent/main` / `index_resources` implica Qdrant + FastEmbed + posible `auto_init`.  
- **Acción futura única:** `LOCAL_CHAT_API_ONE_QUESTION`.  
- **Gate:** `CONDITIONAL_GO` (índice, Py3.11, OPENROUTER, presupuesto pendientes).  
- Presupuesto: `PROPOSED` en `API_BUDGET_AND_SAFETY.md` — requiere firma del investigador.  
- Estados: `smoke_only`; `native_audit_complete=false`; `common_adapter_allowed=false`.

### 4.2 Máquina
WSL2 ~7.4 GiB; RTX 4050 6 GiB; Compose ABSENT; Ruby ABSENT; Python 3.10.12 (agent online → patrón Docker Py3.11).

### 4.3 Lo que NO se ha hecho
- Ninguna llamada API/MCP/SPARQL/OpenRouter.  
- Ningún índice, embedding download, Qdrant init.  
- Smoke online / biodata / Virtuoso.  
- Otros métodos; adapters; cierre Fase 1.

---

## 5. Estado de reproducción

- `sparql_llm`: **smoke_only** (5B); protocolo online **CONDITIONAL_GO**.  
- Resto activos: **audit_only** (HOLD_* del gate 8).  
- Ninguno `reproduced` / `partially_reproduced`.

### PE1–PE4
| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence (CORE_OFFLINE; online protocolizado sin ejecutar) |
| PE3 | not_started |
| PE4 | partial_evidence |

---

## 6. Siguiente prompt recomendado

1. **Prompt 10 — Preparación de entorno e índice mínimo para smoke LOCAL_CHAT_API de SPARQL-LLM (sin llamadas LLM)**  
2. No gastar clave hasta índice + presupuesto firmado + GO técnico.  
3. Objetivo largo plazo intacto (secuencia §1).

→ [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md)

---

## 7. Índice de artefactos

→ [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md)

---

## 8. Changelog

| Fecha | Cambio |
|---|---|
| 2026-07-20 | Prompt 8 gate; GO_NEXT=protocolo API/SIB |
| 2026-07-20 | Prompt 9 protocolo API/SIB; CONDITIONAL_GO=LOCAL_CHAT_API_ONE_QUESTION; next=Prompt 10 índice mínimo |

---

## 9. Registro de publicación

### 8 (previo)
HEAD previo: `3d89a8d61f3fed8eecec8e49f6b79baccf677a76`

### 9 (este prompt)
| Campo | Valor |
|---|---|
| alcance | Protocolo documental API/SIB sparql_llm (sin llamadas) |
| commit inicial | `3d89a8d61f3fed8eecec8e49f6b79baccf677a76` |
| modalidad futura | `LOCAL_CHAT_API_ONE_QUESTION` |
| gate | `CONDITIONAL_GO` |
| commit final | `385e829b67df77b56f4f4732a40af0361cb69ab1` |
| rama | `main` |
| push | confirmado en origin/main |
| artefactos | `docs/protocols/sparql_llm/*`, `audit/sparql_llm/API_SIB_PROTOCOL_READINESS.md` |

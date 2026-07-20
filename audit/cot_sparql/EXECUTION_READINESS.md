# Execution readiness — CoT-SPARQL (WAVE_C)

**Fecha:** 2026-07-20  
**method_id:** `cot_sparql`  
**pinned_commit:** `063edd9868425e54010a0cb49ce585ed2186be4d` (`PIN`)  
**reproduction_status (lab):** `audit_only` — **sin cambio**  
**inclusion:** `INCLUDE_CONDITIONAL`  
**common_adapter_allowed:** `false`  
**feasibility_class:** `requires_external_gpu`

---

## Estados por capacidad

| Capacidad | Estado | Bloqueo / evidencia |
|---|---|---|
| `DATA_ONLY` | **ready** | checksums + conteos datasets |
| `DEPENDENCY_INSTALL` | **legally_blocked / conditional** | `LICENSE_NOT_CONFIRMED` + requirements Conda-as-pip |
| `RETRIEVAL_SMOKE` | **blocked** | parquet/pkl `NOT_FOUND` |
| `LINKER_SMOKE` | **conditional** | necesita spaCy models + APIs externas |
| `model_smoke` | **blocked** | CodeLlama-34B GPTQ ⊄ 6 GiB |
| `end_to_end` | **not_ready** | unión de bloqueos anteriores |
| `native_reproduction` | **not_ready** | GPU externa + artefactos + eval ausente |
| `COMMON_EVALUATION_ADAPTATION` | **legally_blocked** | licencia no confirmada |

---

## next_safe_action

**`Prompt_7B_FIRESPARQL_static_audit`** — completar WAVE_C con FIRESPARQL (fila matriz `pending_prompt_7B`).  
No instalar deps CoT-SPARQL; no adaptar adapters; no afirmar métricas paper como verificadas.

---

## Clasificación host (RTX 4050 6 GiB)

| Dimensión | Veredicto |
|---|---|
| Factibilidad local full paper | **not_ready / requires_external_gpu** |
| DATA_ONLY | **ready** |
| Smoke LLM 34B | **blocked** |
| Smoke con LLM menor | posible futuro etiquetado **no-native** (`README` permite cambio modelo) — **no** ejecutado aquí |

---

## Artefactos de esta pasada

Ver `STATIC_AUDIT.md` §26 y checklist del agente.

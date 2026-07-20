# EXECUTION_READINESS — firesparql

**Fecha:** 2026-07-20  
**method_id:** `firesparql`  
**pinned_commit:** `48d6f168e4c1dd3dc467553aef370299911d4e76` (`PIN`)  
**reproduction_status (lab):** `audit_only`  
**inclusion:** `INCLUDE_CONDITIONAL`  
**common_adapter_allowed:** `false`  
**license_status:** `LICENSE_NOT_CONFIRMED`

---

## Estados por capacidad

| Capacidad | Estado | Notas |
|---|---|---|
| `DATA_ONLY_AUDIT` | **ready** | inventario + sha256 |
| `METRICS_OFFLINE_SMOKE` | **conditional** | pandas/nltk/rouge + path fixes; legally_blocked adapters |
| `RESULTS_RECOMPUTATION_SMOKE` | **conditional** | solo CSVs presentes (23 results) |
| `CHECKPOINT_METADATA_CHECK` | **conditional** | necesitaría HF — **no ahora** |
| `3B_INFERENCE_SMOKE` | **conditional** | VRAM tight; download; LICENSE código |
| `8B_CHECKPOINT_INFERENCE` | **blocked** | 6 GiB sin quant; quant ≠ paper |
| `RAG_SMOKE` | **blocked** | Groq + chromadb + APIs |
| `CLEANING_SMOKE` | **blocked** | OpenAI |
| `QLEVER_EXECUTION` | **blocked** | `CODE_NOT_FOUND` + endpoints |
| `FINE_TUNING_REPRODUCTION` | **not_ready** | trainer ausente; LLaMa-Factory externo |
| `END_TO_END_NATIVE_REPRODUCTION` | **not_ready** | unión de bloqueos |
| `COMMON_EVALUATION_ADAPTATION` | **legally_blocked** | LICENSE_NOT_CONFIRMED |

---

## next_safe_action

**`Prompt_8_native_audit_comparative_gate`**

No instalar deps; no descargar pesos; no llamar APIs; no modificar `upstream/`; no afirmar métricas paper como `RESULT_VERIFIED`.

---

## WAVE_C

Fila `cot_sparql` **preservada**; fila `firesparql` **completa** en `../WAVE_C_STATIC_AUDIT_MATRIX.csv`.

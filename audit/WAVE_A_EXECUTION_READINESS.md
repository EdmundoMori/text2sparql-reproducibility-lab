# WAVE_A_EXECUTION_READINESS

**Fecha:** 2026-07-19  
**Actualizado por:** Prompt 5A (CORE_OFFLINE attempt → **setup_failed**)

---

## sparql_llm

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** |
| environment_definition | **ready** (documentado) |
| offline_smoke_ready | **blocked_on_host_python** (3.10 vs `typing.Required`) |
| api_smoke_ready | **blocked_until_core_import** |
| native_reproduction_ready | **conditional** / Virtuoso **blocked** |
| legal_adapter_gate | **allowed** (MIT) — `common_adapter_allowed` false |
| last_run | `20260719T112306Z` → `setup_failed` |
| next_safe_action | Instalar/usar Python **≥3.11** (prompt tooling) y reintentar CORE_OFFLINE; **no** patch upstream en silencio |
| evidence_required_before_execution | `python3.11` disponible; re-run harness |

---

## mkgqagent / rdfconfig_llm

Sin cambios de ejecución (4B). Seguir diferidos. Ruby ABSENT; LICENSE_NOT_CONFIRMED.

---

## Orden recomendado

1. **Prompt 5B:** disponer Python 3.11+ en WSL (o documentar bloqueo) y reintentar sparql CORE_OFFLINE.  
2. No agent/API hasta import OK.  
3. Virtuoso sigue bloqueado.

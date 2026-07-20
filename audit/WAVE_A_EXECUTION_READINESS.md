# WAVE_A_EXECUTION_READINESS

**Fecha:** 2026-07-20  
**Actualizado por:** Prompt 5B (CORE_OFFLINE py311 Docker → `smoke_only`)

---

## sparql_llm

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** |
| environment_definition | **ready** (+ container_py311 docs) |
| offline_smoke_ready | **validated_in_python311_container** |
| api_smoke_ready | **conditional** |
| native_reproduction_ready | **conditional** benches SIB; **blocked** Text2SPARQL+Virtuoso |
| legal_adapter_gate | **allowed** (MIT) — `common_adapter_allowed` sigue false |
| reproduction_status | **smoke_only** (5B); 5A permanece setup_failed |
| next_safe_action | **No** tercer CORE_OFFLINE; pasar a **auditoría estática SGPT (WAVE_B)** |
| evidence_required_before_execution | API smokes futuros: key + Py3.11 container pattern; no Virtuoso |

---

## mkgqagent

Sin cambio material por 5B: offline NOT_READY; api CONDITIONAL; native not_ready_or_weak; legal blocked.

---

## rdfconfig_llm / companion

Sin cambio material: Ruby ABSENT; generator LICENSE_NOT_CONFIRMED; workdir obligatorio.

---

## Orden recomendado

1. **Prompt 6 — SGPT WAVE_B static audit** (prioridad).  
2. Diferir API/MCP sparql, mkgq, rdfconfig.  
3. Mantener TEXT2SPARQL_VIRTUOSO bloqueado.

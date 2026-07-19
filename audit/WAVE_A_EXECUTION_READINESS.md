# WAVE_A_EXECUTION_READINESS

**Fecha:** 2026-07-19  
**Actualizado por:** Prompt 4B (environment definition documental)  
**Install/ejecución:** ninguna.

Specs: `environments/` · Matriz: `audit/WAVE_A_ENVIRONMENT_DEFINITION_MATRIX.csv` · Gaps: `audit/WAVE_A_ENVIRONMENT_GAPS.md`

---

## sparql_llm

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** |
| environment_definition | **ready** (documentado; no instalado) |
| offline_smoke_ready | **conditional** → listo para prompt de *install+import* CORE_OFFLINE |
| api_smoke_ready | **conditional** (tras CORE_OFFLINE + key) |
| native_reproduction_ready | **conditional** benches SIB; **blocked** Text2SPARQL+Virtuoso local |
| legal_adapter_gate | **allowed** (MIT) — `common_adapter_allowed` sigue false |
| next_safe_action | **Prompt 5A:** install CORE_OFFLINE + import/validate smoke (`smoke_only`) |
| evidence_required_before_execution | Elegir venv+pip vs Poetry; no Virtuoso; no modificar upstream |

---

## mkgqagent

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** (online); offline **partial** |
| environment_definition | **ready** (documentado; gaps requests/single-agent) |
| offline_smoke_ready | **no** (NOT_READY) |
| api_smoke_ready | **conditional** |
| native_reproduction_ready | **not_ready_or_weak** |
| legal_adapter_gate | **blocked** |
| next_safe_action | Diferir hasta después de sparql CORE_OFFLINE; resolver single-agent sin patch |
| evidence_required_before_execution | Key; legal; RAM; no adapters |

---

## rdfconfig_llm (generator)

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** |
| environment_definition | **ready** (documentado; Ruby ABSENT) |
| offline_smoke_ready | **no** |
| api_smoke_ready | **conditional** (API + Ruby + workdir + missing deps) |
| native_reproduction_ready | **conditional** (prefer Zenodo; workdir) |
| legal_adapter_gate | **blocked** (HEAD) |
| next_safe_action | No antes de sparql CORE; primero runtime Ruby (prompt host) si se prioriza |
| evidence_required_before_execution | Ruby/Bundler; workdir; no in-place sparql.yaml |

---

## rdfconfig_llm_rdf-config (companion)

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** |
| environment_definition | **ready** (docs); runtime host **blocked** (Ruby ABSENT) |
| offline_smoke_ready | **conditional** (tras instalar Ruby/Bundler) |
| api_smoke_ready | **n/a** |
| native_reproduction_ready | **no** solo |
| legal_adapter_gate | **allowed** (MIT) |
| next_safe_action | Opcional tras Ruby; no sustituye paper |
| evidence_required_before_execution | Ruby version; documentar árbol usado |

---

## Orden recomendado

1. **Prompt 5A — sparql_llm CORE_OFFLINE** install + import/validate (`smoke_only`).  
2. No Virtuoso. No multi-método.  
3. API smokes / mkgq / rdfconfig solo después y uno a uno.

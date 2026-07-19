# WAVE_A_EXECUTION_READINESS

**Fecha:** 2026-07-19  
**Alcance:** solo WAVE_A (`sparql_llm`, `mkgqagent`, `rdfconfig_llm` + companion).  
**Ninguna instalación ni ejecución realizada en este prompt.**

---

## sparql_llm

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** |
| environment_definition | **partial** (pyproject claro; host sin uv; Compose ausente) |
| offline_smoke_ready | **conditional** (tras install deps core + VoID local) |
| api_smoke_ready | **conditional** (API key OpenRouter/OpenAI-compatible + install) |
| native_reproduction_ready | **conditional** (benchmarks presentes; coste/API; stack compose) |
| legal_adapter_gate | **allowed** (MIT) — protocolo: aún `common_adapter_allowed: false` hasta native audit |
| next_safe_action | Definir entorno de instalación **solo lectura de specs** o Prompt 4B: environment definition + offline import smoke de `validate_sparql`/loaders **sin** declarar reproducción |
| evidence_required_before_execution | Confirmar gestor (pip/Poetry vs uv); política Compose→`docker run` Qdrant; presupuesto API; no tocar upstream |

---

## mkgqagent

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** (online); offline pool build **partial** |
| environment_definition | **partial** (requirements sin pins; endpoints hardcode) |
| offline_smoke_ready | **no** (carga FAISS+e5 implica download/modelo; no es offline puro) |
| api_smoke_ready | **conditional** (`OPENAI_API_KEY`; endpoint WSE; RAM e5) |
| native_reproduction_ready | **conditional** / débil (script offline ausente; hosts externos) |
| legal_adapter_gate | **blocked** |
| next_safe_action | Documentar plan de smoke API aislado **sin** adapters; verificar alcanzabilidad endpoints; advertir LICENSE |
| evidence_required_before_execution | Key OpenAI; prueba DNS/HTTP a `141.57.8.18`; espacio RAM WSL; aceptación legal smoke-only |

---

## rdfconfig_llm (generator)

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** |
| environment_definition | **partial** (requirements incompletos vs evaluador; Ruby) |
| offline_smoke_ready | **no** (OpenAI obligatorio para generación) |
| api_smoke_ready | **conditional** (OpenAI + bundle rdf-config + deps extra) |
| native_reproduction_ready | **conditional** (notebooks/CV script; mutación sparql.yaml) |
| legal_adapter_gate | **blocked** (HEAD); Zenodo CC-BY separado |
| next_safe_action | Spec de entorno en copia de trabajo fuera de upstream; completar lista deps; smoke 1 pregunta |
| evidence_required_before_execution | Ruby/Bundler disponibles; key OpenAI; path rdf-config fijado; no escribir en upstream vendorizado |

---

## rdfconfig_llm_rdf-config (companion)

| Dimensión | Valor |
|---|---|
| static_understanding | **complete** |
| environment_definition | **ready** (Gemfile) a nivel docs |
| offline_smoke_ready | **yes** (tras `bundle install` futuro) |
| api_smoke_ready | **n/a** |
| native_reproduction_ready | **no** solo — insuficiente para paper |
| legal_adapter_gate | **allowed** (MIT) |
| next_safe_action | Opcional: smoke CLI listando queries de un config; no sustituye generator |
| evidence_required_before_execution | Ruby version; elegir pin companion vs copia vendored y documentar |

---

## Orden recomendado (siguiente prompt del plan)

1. **No** lanzar smoke API multi-método todavía.  
2. Preferir **Prompt 4B — Environment definition WAVE_A** (archivos `environments/`, deps exactas, comandos futuros, degradaciones Compose/uv/Ruby) **sin install**, o un **smoke offline mínimo solo `sparql_llm` validate/loaders** si se prioriza señal CODE_VERIFIED ejecutable.  
3. Smokes API: un método por prompt; empezar por `sparql_llm` (MIT) antes que mkgqagent/rdfconfig (legal blocked).  
4. Mantener WAVE_B/C fuera de alcance.

# Environment spec — rdfconfig_llm

**Generator commit:** `fe63171d3c8b9679779749ee11f731b2a8318053` — `LICENSE_NOT_CONFIRMED`  
**Companion pin lab:** `cccc581c16f0b24865030bc5459475a9d0fcbd5f` — MIT  
**Host Ruby/Bundler:** **ABSENT** (2026-07-19)  
**Estado:** documentado, no instalado; **ninguna copia de ejecución creada**.

---

## A. GENERATOR_PYTHON

| Pieza | Rol |
|---|---|
| OpenAI API | `gpt-4-1106-preview` en `gpt_excute.py` |
| prompt_maker / text_extractor | variables + parameters |
| SPARQL_generator | orquestación |
| SPARQL_executer | HTTP endpoints |
| results_evaluater | Jaccard (`pandas`, `munkres`, `scipy`, `tqdm` — **MISSING_UPSTREAM** vs `requirements.txt`) |

## B. RDF_CONFIG_RUBY

| Pieza | Rol |
|---|---|
| Ruby + Bundler | **ABSENT en host** — bloquea smoke generator hasta instalar runtime (futuro, no 4B) |
| CLI `bundle exec rdf-config` | YAML → SPARQL |
| Sin LLM | |

Ver `source_selection.md` para GitHub HEAD vs Zenodo vs rdf-config incluido vs companion.

## Regla crítica de workspace

El generator **appendea** a `sparql.yaml` → **nunca** ejecutar in-place sobre `upstream/`.  
Usar workspace descartable (`EXECUTION_WORKSPACE_POLICY.md`).

## Artefactos

`dependency_manifest.yaml`, `environment_variables.md`, `source_selection.md`, `future_commands.md`.

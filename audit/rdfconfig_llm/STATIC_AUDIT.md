# STATIC_AUDIT — rdfconfig_llm (generador Python, WAVE_A)

**Fecha:** 2026-07-19  
**Pinned commit:** `fe63171d3c8b9679779749ee11f731b2a8318053`  
**Upstream:** `upstream/rdfconfig_llm/`  
**Companion audit:** [`COMPANION_RDF_CONFIG_AUDIT.md`](COMPANION_RDF_CONFIG_AUDIT.md)  
**Etiquetas:** `README_REPORTED` | `CODE_VERIFIED` | `PAPER_REPORTED` | `NOT_FOUND` | `UNKNOWN`

---

## 1. Identificación y commit

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `rdfconfig_llm` | lab |
| repo | scott2121/sparql_query_generator | lock |
| tag | `v1.0.0` | lock |
| Vendored rdf-config copy | `upstream/rdfconfig_llm/rdf-config/` | `CODE_VERIFIED` SETUP.md L13–19 |
| Companion pin separado | `upstream/rdfconfig_llm_rdf-config` @ `cccc581c…` | lock (MIT) |

## 2. Relación paper↔repositorio

| Afirmación | Etiqueta |
|---|---|
| Paper Bioinformatics 2026 DOI 10.1093/bioinformatics/btag174 | `PAPER_REPORTED` |
| Método: LLM propone variables/params → rdf-config construye SPARQL | `CODE_VERIFIED` `SPARQL_generator.py:28-72` + `rdf_config_executer.py` |
| Zenodo v1.0.0 CC-BY-4.0 | `PAPER_REPORTED` / evidence closure — **no transferir a HEAD GitHub** |

## 3. Estado legal

| Artefacto | Status | Evidencia |
|---|---|---|
| GitHub HEAD generator | `LICENSE_NOT_CONFIRMED` | **no** LICENSE file |
| Zenodo archive v1.0.0 | CC-BY-4.0 (metadata) | lab `LICENSE_MATRIX` |
| Vendored `rdf-config/` dentro del generator | MIT típico dbcls | ver companion; **no** implica licencia del wrapper Python |
| Gate adapters | **blocked** para código generator HEAD | inspección OK |

## 4. Arquitectura

Frontera Python↔Ruby (`CODE_VERIFIED`):

1. **Python LLM** (`functions/gpt_excute.py`): `OpenAI` model `gpt-4-1106-preview` → texto.  
2. **Python extract** (`text_extractor.py`): variables + parameters.  
3. **Python escribe** `sparql.yaml` entry (`rdf_config_executer.create_strain_text`).  
4. **Ruby rdf-config** via `bundle exec rdf-config --config config/{db} --sparql {id}` (`execute_rdf_config` L33-51).  
5. **Python ejecuta** SPARQL en endpoints (`SPARQL_executer.py`) y evalúa Jaccard (`results_evaluater.py`).

```mermaid
flowchart LR
  Q[NL question] --> PM[prompt_maker]
  PM --> GPT[excute_gpt OpenAI]
  GPT --> EX[extract variables/params]
  EX --> YAML[append sparql.yaml]
  YAML --> RUBY["bundle exec rdf-config --sparql"]
  RUBY --> SQ[SPARQL string]
  SQ --> EP[execute_query endpoint]
  EP --> JAC[evaluate_jaccard]
```

## 5. Diagrama Mermaid

Ver §4.

## 6. Entry points

| Entrypoint | Evidencia |
|---|---|
| Notebooks `demo_propose*.ipynb`, `demo_baseline_prompt_tuning.ipynb` | `README_REPORTED` + presencia |
| `leave-one-set-out.py` | fine-tune CV + Jaccard — `CODE_VERIFIED` L1-45,613 |
| Funciones importables `sparql_gen`, `generate_one_sparql` | `SPARQL_generator.py:28,98` |
| No CLI Python unificado | `NOT_FOUND` |

## 7. Componentes y responsabilidades

| Path | Rol |
|---|---|
| `functions/prompt_maker.py` | rellena prompts |
| `functions/gpt_excute.py` | llamada OpenAI |
| `functions/text_extractor.py` | parse variables/params |
| `functions/SPARQL_generator.py` | orquesta LLM→rdf-config |
| `functions/rdf_config_executer.py` | frontera Ruby |
| `functions/SPARQL_executer.py` | HTTP SPARQL |
| `functions/results_evaluater.py` | Jaccard / matching columnas |
| `questions/json_format/{bgee,rhea,uniprot,uniprot_and_bgee}.json` | datasets |
| `data/prompt/` (paths env) | prompts/variables JSON |
| `rdf-config/config/{db}/` | model.yaml + sparql.yaml schemas |

## 8. Entrada y salida observables

| | Valor |
|---|---|
| Entrada | pregunta + db + prompt_id |
| Intermedio | `llm_variable`, `llm_parameter`, `llm_rdf_result` (SPARQL) |
| Salida eval | scores Jaccard sobre bindings |

## 9. Dependencias y runtimes

| Runtime | Evidencia |
|---|---|
| Python: `requirements.txt` = dotenv, openai, rdflib, requests | `CODE_VERIFIED` |
| **Gap:** `results_evaluater.py` importa `pandas`, `munkres`, `scipy`, `tqdm` **no** listados en requirements | `CODE_VERIFIED` gap |
| Ruby + Bundler para rdf-config | `SETUP.md` L13–17 |
| OpenAI API obligatoria para generación | `gpt_excute.py` |

## 10. Variables de entorno y secretos

Desde `.env_sample` `CODE_VERIFIED`:

- `OPENAI_API_KEY`
- `PATH_RDF_CONFIG`, `PATH_DIR`
- `PATH_PROMPTS`, `PATH_VARIABLES`
- `ENDPOINT_BGEE`, `ENDPOINT_UNIPROT`, `ENDPOINT_RHEA`, `ENDPOINT_UNIPROT_AND_BGEE`

`leave-one-set-out.py` también rota `OPENAI_API_KEY2`, … 

## 11. Servicios externos

- OpenAI Chat Completions.  
- Endpoints biodata públicos (Bgee, UniProt, Rhea, rdfportal).  

## 12. Datasets y splits

| Path | DBs |
|---|---|
| `questions/json_format/*.json` | bgee, rhea, uniprot, uniprot_and_bgee |
| `questions/ttl_format/` | RDF questions |
| Dificultad EASY/MEDIUM/HARD | `README_REPORTED` |
| Leave-one-set-out folds | `leave-one-set-out.py` `DB_LIST` L45 |

## 13. Modelos y checkpoints

| Modelo | Evidencia |
|---|---|
| `gpt-4-1106-preview` default generation | `gpt_excute.py:7` |
| Fine-tuning OpenAI jobs | `leave-one-set-out.py` (FT API) |
| Checkpoints locales | `NOT_FOUND` (API-side FT) |

## 14. Prompts

Paths env `PATH_PROMPTS` / `PATH_VARIABLES` → `data/prompt/prompts.json`, `variables.json` (`.env_sample`).

## 15. Evaluación y métricas originales

| Métrica | Evidencia |
|---|---|
| Jaccard sobre resultados bindings | `evaluate_jaccard` `results_evaluater.py:219` |
| Notebooks demo reproducen workflow paper-like | `README_REPORTED` |
| Tablas paper exactas | requieren ejecución — **no** hechas |

## 16. Comando documentado por autores

`SETUP.md` + workflow README L17–65: clone → `bundle install` en rdf-config → `.env` → `pip install -r requirements.txt` → abrir `demo_propose.ipynb`.

## 17. Comando todavía no verificado

bundle/pip/notebooks/API — **no ejecutados**.

## 18. Compatibilidad estimada con la máquina

| Aspecto | Clase |
|---|---|
| Generación vía API + Ruby rdf-config | `feasible_using_api` si Ruby/Bundler instalados |
| Fine-tune OpenAI (`leave-one-set-out.py`) | coste/API; no GPU local |
| RAM | moderada (sin LLM local) |

## 19. Riesgos de ejecución

- LICENSE_NOT_CONFIRMED generator.  
- `requirements.txt` incompleto vs evaluador.  
- `PATH_RDF_CONFIG` debe apuntar al vendored `rdf-config/` (o companion pin — **pueden divergir**).  
- `create_strain_text` **muta** `sparql.yaml` (append) — riesgo de ensuciar upstream si se ejecuta in-place (**no** ejecutar sobre árbol vendorizado sin copia).  
- Typo repo en SETUP (`sparql_query_generater`).  

## 20. Diferencias README↔código

| Tema | Detalle |
|---|---|
| requirements mínimos | insuficientes para Jaccard |
| rdf-config incluido vs companion pin lab | dos árboles; SETUP usa el incluido |
| “benchmark tool” | notebooks + script FT; poca CLI |

## 21. Artefactos ausentes

- LICENSE en HEAD  
- requirements completos  
- CLI estable no-notebook  

## 22. Ruta mínima para smoke futuro

1. Copia de trabajo **fuera** de `upstream/` o worktree desechable.  
2. Ruby+bundle en `rdf-config/`.  
3. `.env` con keys/paths/endpoints.  
4. pip deps **incluyendo** pandas/munkres/scipy/tqdm.  
5. Una pregunta vía `generate_one_sparql` o celda notebook.  
6. Etiquetar `smoke_only`. Sin adapters.

## 23. Ruta necesaria para reproducción nativa

Correr notebooks/`leave-one-set-out` alineados al paper; fijar modelo GPT; endpoints; Jaccard; comparar tablas Bioinformatics. Preferir Zenodo CC-BY si se redistribuye.

## 24. Gate legal para futuras adaptaciones

**blocked** para HEAD GitHub generator. Companion MIT ≠ permiso sobre wrapper Python.

## 25. Conclusión conservadora

Frontera Python(LLM vars)↔Ruby(SPARQL) **claramente CODE_VERIFIED**. Smoke **conditional** (API+Ruby+deps gap). Legal **blocked**. `audit_only`.

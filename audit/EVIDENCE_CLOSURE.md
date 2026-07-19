# EVIDENCE_CLOSURE

**Fecha:** 2026-07-18  
**Alcance:** Cierre de evidencias pendientes del Prompt 2 **antes de clonar**  
**Clones:** ninguno  
**Ejecuciones:** ninguna  
**Artefactos hermanos:** `LICENSE_MATRIX.csv`, `RESULT_EVIDENCE_MATRIX.csv`, `PUBLICATION_STATUS.csv`

---

## 1. Licencias (solo archivo LICENSE / API SPDX / declaración explícita no-README)

| method_id / repo | Estado | SPDX | Fuente exacta |
|---|---|---|---|
| **mkgqagent** `WSE-research/text2sparql-agent` | `LICENSE_NOT_CONFIRMED` | UNKNOWN | Sin LICENSE; GitHub API `license=null`; `CITATION.cff` sin campo `license` |
| **cot_sparql** `dice-group/CoT-Sparql` | `LICENSE_NOT_CONFIRMED` | UNKNOWN | Sin LICENSE; GitHub API `license=null` |
| **firesparql** `sherry-pan/FIRESPARQL` | `LICENSE_NOT_CONFIRMED` | UNKNOWN | Sin LICENSE; GitHub API `license=null`. CC BY-NC-ND del PDF SciTePress aplica al **artículo**, no al código |
| **firesparql** HF `Sherry791/Meta-Llama-3-8B-Instruct-ft4sciqa` | Confirmado (modelo) | MIT | Frontmatter `license: mit` en README del modelo HF |
| **rdfconfig_llm** `scott2121/sparql_query_generator` (GitHub) | `LICENSE_NOT_CONFIRMED` | UNKNOWN | Sin LICENSE raíz; API `license=null`. Claim MIT del README **no** usado |
| **rdfconfig_llm** Zenodo `10.5281/zenodo.18539214` (v1.0.0) | Confirmado (depósito) | CC-BY-4.0 | Zenodo API `metadata.license.id=cc-by-4.0` |
| **rdfconfig_llm** `dbcls/rdf-config` | Confirmado | MIT | Archivo `LICENSE` + GitHub API SPDX MIT |
| sparql_llm / sgpt | Confirmado (referencia) | MIT | `LICENSE.txt` / `LICENSE.md` |

**Implicación:** código público ≠ derecho de reutilización confirmado para mkgqagent, cot_sparql, firesparql (GitHub) y HEAD de scott2121. El depósito Zenodo CC-BY-4.0 **no** sustituye automáticamente la licencia del árbol GitHub HEAD.

---

## 2. SPARQL-LLM — venue y estado formal

| Campo | Valor verificado |
|---|---|
| Estado | **preprint under review** |
| arXiv | `2512.14277` / DOI `10.48550/arXiv.2512.14277` |
| Comentario Atom arXiv | `"17 pages, 8 figures, 1 table. Under Review"` |
| OpenAlex | `type=preprint`; `is_accepted=false`; `is_published=false`; `version=submittedVersion` |
| DOI de editorial (ACM TWEB u otro) | **UNKNOWN / no encontrado** (Crossref no devolvió artículo TWEB; OpenAlex solo arXiv) |
| Metadatos HTML arXiv | Emite `booktitle: ACM Transactions on the Web Journal (TWEB)` + `copyright: acmlicensed` — **no** se interpreta como aceptación/publicación sin DOI editorial |
| Accepted manuscript | **UNKNOWN** (sin evidencia de aceptación) |
| Artículo publicado | **false** (con la evidencia actual) |

Trabajo relacionado **sí publicado** en CEUR Vol-3953 (README del repo): *LLM-based SPARQL Query Generation…* — distinto del manuscrito “SPARQL-LLM: Real-Time…”.

---

## 3. SGPT — Tabla 4 (valores reportados; no reproducidos)

**Fuente primaria:** HTML del DOI `10.1109/ACCESS.2022.3188714` (Table 4).  
**Modelo:** GPT-2 **117M** (decoder) + stack de Transformer-encoders (paper §V-B).  
**Partición:** **test** (splits originales Table 2: LC-QuAD 2.0 6046 / VQuAnDa 1000 / QALD-9 150; QALD-9 solo inglés).  
**Validación:** 10–15% del train (paper); no es la partición de Table 4.

### Configuración `SGPT_Q` (sin K)

| Dataset | BLEU | F1 | SP-BLEU | SP-F1 | Entity K |
|---|---:|---:|---:|---:|---|
| LC-QuAD 2.0 | 60.50 | 83.45 | 63.59 | 86.22 | no |
| VQuAnDa | 63.82 | 87.08 | 63.82 | 87.08 | no |
| QALD-9 (en) | 29.95 | 60.22 | 32.12 | 64.57 | no |

### Configuración `SGPT_Q,K` (entidades proporcionadas como K)

| Dataset | BLEU | F1 | SP-BLEU | SP-F1 | Entity K |
|---|---:|---:|---:|---:|---|
| LC-QuAD 2.0 | 73.78 | 89.04 | 77.85 | 92.27 | provided_entities_as_K |
| VQuAnDa | 72.58 | 88.87 | 72.58 | 88.87 | provided_entities_as_K |
| QALD-9 (en) | 35.68 | 67.82 | 41.88 | 72.98 | provided_entities_as_K |

**Entity linking gold:** el paper (§IV-A) define K como *“entities mentioned in the question are provided”*. No usa la etiqueta “gold EL”. Se registra como `provided_entities_as_K`. Procedencia exacta de los IDs en el experimento (anotaciones del dataset vs otro oráculo): **UNKNOWN** hasta inspección de código (sin clonar aún). README: flag `--knowledge` (solo entidades).

Filas baseline NSpM / SQG / TeBaQA: ver `RESULT_EVIDENCE_MATRIX.csv`.

---

## 4. Relación artículo ↔ repositorio

| method_id | Relación | Evidencia |
|---|---|---|
| sparql_llm | **Repositorio oficial de autores** (SIB / mismos autores del preprint) | README cita arXiv:2512.14277; org `sib-swiss`; `fork=false` |
| mkgqagent | **Repositorio oficial de autores** | Paper/CITATION.cff apuntan a `WSE-research/text2sparql-agent`; autores Perevalov & Both; `fork=false` |
| cot_sparql | **Repositorio oficial de autores** (DICE) | Paper footnote `https://github.com/dice-group/CoT-Sparql`; `fork=false` |
| firesparql | **Repositorio oficial de autores** | Paper/README `sherry-pan/FIRESPARQL`; autora Xueli Pan; durante review hubo URL anónima (anonymous.4open) — el repo actual es la publicación de código; `fork=false` |
| rdfconfig_llm (generator) | **Repositorio oficial del entorno experimental del paper** | Bioinformatics Availability → `scott2121/sparql_query_generator` + Zenodo |
| rdfconfig_llm (rdf-config) | **Dependencia / companion oficial** (DBCLS; coautor Katayama) | Paper usa RDF-config; `dbcls/rdf-config` MIT |
| sgpt | **Repositorio oficial de autores** | Paper footnote `rashad101/SGPT-SPARQL-query-generation`; `fork=false` |
| tebaqa | **Repositorio oficial de autores** (DICE) | README/paper `dice-group/TeBaQA` |

Ninguno de los candidatos auditados se clasifica aquí como fork no oficial ni implementación independiente. **Código parcial:** CoT-Sparql (datasets train parciales en árbol; embeddings externos); FIRESPARQL (requirements “Coming soon”); SGPT (afirma “code and model” pero **sin** pesos `.pt`/`.bin` en el árbol Git).

---

## 5. Disponibilidad de artefactos (árbol Git HEAD vía API; sin clonar)

| method_id | Checkpoints | Datasets procesados | Prompts | Scripts evaluación | Instrucciones repro |
|---|---|---|---|---|---|
| mkgqagent | No en repo (LLM vía API) | Sí (`data/datasets/`, experience-pool FAISS) | Sí (`prompts/*.py`) | Sí (`data/evaluation/*.yaml` + `text2sparql-client` documentado) | Sí (`README.adoc`, Dockerfile) |
| cot_sparql | No en repo (HF externos) | Parcial (`dataset/*.json` train; embeddings vía URL externa) | No como archivos dedicados (prompt en código/`main.py`) | No script eval dedicado en árbol | Sí (`README.md`, `environment.yml`) |
| firesparql | **Fuera del repo:** HF modelo; 0 `.pt`/`.bin` en Git | Sí (`experiment_datasets/sciqa/…`) | Sí (miles de prompts/contextos en `results/…`) | Sí (`codes/bleu_rouge.py`, `exact_match.py`, …) | **Parcial** (README Requirements: “Coming soon”) |
| rdfconfig_llm | N/A (API LLM) | Sí (`questions/…`, `data/prompt/…`) | Sí (`data/prompt/prompts.json`) | Sí (`functions/results_evaluater.py`) | Sí (`README.md`, `SETUP.md`) |
| rdf-config | N/A | Schemas YAML en repo | N/A | N/A (generador SPARQL, no KGQA eval) | Sí (`README.md`) |
| sgpt | **Ausentes** en árbol (0 checkpoints) pese a claim “open source … model” | Sí (`data/{lcquad2,qald9,vquanda}/`) | N/A (modelo entrenado) | Sí (`eval.py`, `utils/metrics.py`) | Sí (`README.md`, `train.py`) |
| sparql_llm | N/A (API LLM) | No datasets benchmark embebidos en árbol | Sí (`src/.../prompts.py`, notebooks) | Sí (`tests/text2sparql/evaluate.sh`) | Sí (README + compose; **Compose plugin ausente en host**) |

---

## 6. Estados que permanecen UNKNOWN

- DOI editorial ACM TWEB para SPARQL-LLM.  
- Aceptación formal del manuscrito SPARQL-LLM (solo “Under Review”).  
- Licencia SPDX de GitHub para mkgqagent, cot_sparql, firesparql, scott2121 HEAD.  
- Equivalencia legal Zenodo CC-BY-4.0 ↔ GitHub HEAD de scott2121.  
- Procedencia exacta de entidades K en SGPT Table 4 (`gold` vs otras).  
- Ubicación de pesos SGPT “model” anunciados en el paper (no en árbol actual).

---

## 7. Efecto sobre inclusión (sin cambiar gates de clon)

No se reclasifica a `EXCLUDE_NOT_REPRODUCIBLE` únicamente por `LICENSE_NOT_CONFIRMED`: el estudio interno sigue siendo posible; la **redistribución/adaptación** queda legalmente condicionada.  
`common_adapter_allowed` permanece `false` hasta auditoría nativa con clone.

**ADVERTENCIA [licencia]:** reutilizar/adaptar código de repos `LICENSE_NOT_CONFIRMED` es riesgoso.  
**SOLUCIÓN:** contactar autores o limitar uso a lectura/ejecución local sin redistribuir; preferir artefactos con MIT/AGPL/CC-BY confirmados.  
**CONTINÚO:** matrices actualizadas; sin clonar.

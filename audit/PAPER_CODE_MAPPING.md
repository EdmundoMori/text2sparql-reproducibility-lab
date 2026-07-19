# PAPER_CODE_MAPPING

**Auditoría:** Prompt 2 — verificar artículo, código y evidencia  
**Fecha:** 2026-07-18  
**Fuentes:** repositorios GitHub oficiales + artículos/preprints enlazados desde esos repos o DOI oficiales  
**Clones:** ninguno (no se clonó `upstream/`)  
**Regla:** campos no verificados en fuente primaria = `UNKNOWN`

---

## sparql_llm

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `sparql_llm` | lab |
| Nombre exacto (método) | SPARQL-LLM | arXiv:2512.14277; README sib-swiss/sparql-llm |
| Artículo principal | SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions | https://arxiv.org/abs/2512.14277 |
| Autores | Panayiotis Smeros; Vincent Emonet; Ruijie Wang; Ana-Claudia Sima; Tarcisio Mendes de Farias | arXiv HTML / bibtex del README |
| Año | 2025 | arXiv bibtex del README |
| Venue | Preprint arXiv (`cs.IR`); metadatos del HTML mencionan ACM TWEB — **estado de publicación formal: UNKNOWN** más allá del preprint | arXiv HTML |
| DOI / ID | `10.48550/arXiv.2512.14277` / arXiv:2512.14277 | arXiv |
| Artículo relacionado (repo) | LLM-based SPARQL Query Generation from Natural Language over Federated Knowledge Graphs | CEUR-WS Vol-3953/355.pdf (citado en README) |
| Repositorio oficial | https://github.com/sib-swiss/sparql-llm | GitHub API |
| Licencia | MIT (SPDX) | GitHub API `license.spdx_id` |
| Rama principal | `main` | GitHub API |
| Última actividad (push) | 2026-05-19T16:43:59Z | GitHub API |
| Lenguaje(s) | Python (+ TypeScript/HTML UI; GitHub marca predominante Jupyter Notebook) | GitHub `/languages` |
| Framework | LangChain-compatible loaders; MCP; Docker/`compose.yml`; paquete PyPI `sparql-llm` | README |
| Dataset original | TEXT2SPARQL Challenge 2025 (DBpedia EN/ES, Corporate); ejemplos LC-QuAD + QALD-9+ para DBpedia | arXiv HTML §evaluación |
| Knowledge graph original | Endpoints SIB (UniProt, Bgee, …) en despliegue; evaluación challenge sobre DBpedia + Corporate KG | README + paper |
| Métrica original | F1 Score (protocolo TEXT2SPARQL / `text2sparql-client`); también runtime y coste | paper |
| Resultado principal reportado | +24% F1 vs ganadores del challenge en DBpedia (EN) y (ES); hasta 36× más rápido; ≤ $0.01/pregunta | paper abstract/§resultados |
| Modelos disponibles | Usa LLMs vía API (p. ej. GPT-4o / GPT-4o-mini / GPT-oss-120b en paper); no se audita checkpoint propio del método | paper + README |
| Datos disponibles | Ejemplos/metadata de endpoints; datasets del challenge son externos | README / paper |
| Instrucciones de reproducción | Sí: PyPI/`uvx`, Docker compose, indexing scripts | README |
| Necesita API | **Sí** (LLM OpenAI-compatible; endpoints SPARQL) | README |
| Notas | Requiere metadata VoID/ejemplos en endpoints | README |

---

## mkgqagent

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `mkgqagent` | lab |
| Nombre exacto | mKGQAgent | README.adoc; CITATION.cff |
| Artículo | Text-to-SPARQL Goes Beyond English: Multilingual Question Answering Over Knowledge Graphs through Human-Inspired Reasoning | CEUR Vol-4094 paper6; arXiv:2507.16971 |
| Autores | Aleksandr Perevalov; Andreas Both | CITATION.cff / paper |
| Año | 2025 | CEUR / CITATION.cff |
| Venue | First International TEXT2SPARQL Challenge co-located with Text2KG at ESWC 2025; CEUR-WS Vol. 4094, pp. 77–93 | CITATION.cff |
| DOI / ID | Preprint DOI `10.48550/arXiv.2507.16971`; CEUR PDF https://ceur-ws.org/Vol-4094/paper6.pdf (DOI CEUR del proceedings: UNKNOWN) | CITATION.cff |
| Repositorio oficial | https://github.com/WSE-research/text2sparql-agent | GitHub |
| Licencia | **UNKNOWN** (GitHub `license: null`; sin LICENSE file; CITATION.cff sin campo license) | GitHub API + listing |
| Rama principal | `main` | GitHub API |
| Última actividad (push) | 2026-07-07T08:59:37Z | GitHub API |
| Lenguaje(s) | Python | GitHub `/languages` |
| Framework | FastAPI, LangGraph/LangChain, FAISS, sentence-transformers; Docker image `wseresearch/kgqagent-text2sparql` | README.adoc / requirements.txt |
| Dataset original | QALD-9-plus (preliminar); TEXT2SPARQL 2025 DBpedia + Corporate (challenge) | paper + README.adoc |
| Knowledge graph original | DBpedia; Corporate KG del challenge | README.adoc |
| Métrica original | Macro F1 | paper |
| Resultado principal reportado | 1er lugar TEXT2SPARQL 2025 (Overall + DBpedia Spanish); Macro F1 EN QALD-9-plus = **54.83%** (GPT-4o) | paper Fig.4 / Table 1; README awards |
| Modelos disponibles | Proprietary/open LLMs vía API (GPT-4o, GPT-3.5, etc.); embedding local `intfloat/multilingual-e5-large`; experience pool FAISS en `data/` | README.adoc |
| Datos disponibles | Subsets train / experience pool / corporate TTL en repo | README.adoc |
| Instrucciones de reproducción | Sí (venv, Docker, `text2sparql-client`) | README.adoc |
| Necesita API | **Sí** (`OPENAI_API_KEY` requerido) | README.adoc |

---

## cot_sparql

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `cot_sparql` | lab |
| Nombre exacto | COT-SPARQL / CoT-Sparql | paper PDF; repo |
| Artículo | Generating SPARQL from Natural Language Using Chain-of-Thoughts Prompting | https://doi.org/10.3233/SSW240028 |
| Autores | Hamada M. Zahera; Manzoor Ali; Mohamed Ahmed Sherif; Diego Moussallem; Axel-Cyrille Ngonga Ngomo | PDF autores |
| Año | 2024 | DOI / RIS Uni Paderborn / PDF |
| Venue | SEMANTiCS 2024 (Amsterdam); IOS Press Studies on the Semantic Web | DOI / RIS |
| DOI / ID | `10.3233/SSW240028` | DOI |
| Repositorio oficial | https://github.com/dice-group/CoT-Sparql | GitHub |
| Licencia | **UNKNOWN** (GitHub `license: null`; sin LICENSE file) | GitHub API |
| Rama principal | `main` | GitHub API |
| Última actividad (push) | 2024-06-03T13:26:40Z | GitHub API |
| Lenguaje(s) | Python (+ Jupyter) | GitHub `/languages` |
| Framework | Prompting LLM local (ej. CodeLlama-34B-Instruct-GPTQ); sentence embeddings `all-MiniLM-L6-v2`; conda/`requirements.txt` | README |
| Dataset original | LC-QuAD 2.0, VQuAnDa, QALD-9, QALD-10 | paper §4.1; README |
| Knowledge graph original | DBpedia; Wikidata | paper / README |
| Métrica original | BLEU, F1 (query); F1-QALD / GERBIL (QA); % queries válidas | paper §4.3 |
| Resultado principal reportado | Mejora F1 **+4.4%** (QALD-10) y **+3.0%** (QALD-9) vs SOTA (abstract); F1-QALD **63.87** en pilot QALD-10 (COT-SPARQL ent+rel); F1 query p.ej. 89.36 VQuAnDa / 70.45 QALD-9 | paper abstract + Tables 2–4 |
| Modelos disponibles | Modelos HF citados (CodeLlama GPTQ, etc.); no checkpoint propio del método en HF auditado aquí | paper footnotes / README |
| Datos disponibles | Datasets en carpeta `dataset`; embeddings externos vía URL dice-research | README |
| Instrucciones de reproducción | Sí (`main.py --model_path --kb --question`) | README |
| Necesita API | **No obligatorio** si se sirve LLM local; endpoints SPARQL DBpedia/Wikidata sí | README / paper |

---

## firesparql

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `firesparql` | lab |
| Nombre exacto | FIRESPARQL | paper / README |
| Artículo | FIRESPARQL: A LLM-Based Framework for SPARQL Query Generation over Scholarly Knowledge Graphs | DOI 10.5220/0013774000004000; arXiv:2508.10467 |
| Autores | Xueli Pan; Victor de Boer; Jacco van Ossenbruggen | SciTePress / arXiv |
| Año | 2025 | SciTePress / DOI |
| Venue | IC3K 2025 — KDIR (SCITEPRESS), pp. 123–134 | SciTePress |
| DOI / ID | `10.5220/0013774000004000`; arXiv:2508.10467 | DOI / arXiv |
| Repositorio oficial | https://github.com/sherry-pan/FIRESPARQL | paper + GitHub |
| Licencia | **UNKNOWN** (GitHub `license: null`; sin LICENSE file). Paper: CC BY-NC-ND 4.0 para el PDF SciTePress | GitHub API; SciTePress PDF |
| Rama principal | `main` | GitHub API |
| Última actividad (push) | 2025-05-28T10:00:52Z | GitHub API |
| Lenguaje(s) | Jupyter Notebook (predominante) / scripts Python en `codes/` | GitHub API + README |
| Framework | LoRA fine-tuning LLaMA-3; opcional RAG; QLever para ejecución | paper / README |
| Dataset original | SciQA benchmark | paper §5.1; README |
| Knowledge graph original | ORKG (Open Research Knowledge Graph) | paper |
| Métrica original | BLEU-4, ROUGE-1/2/L, RelaxedEM (success/all) | paper |
| Resultado principal reportado | FT LLaMA-3-8B-Instruct 15 epochs: BLEU-4 **0.77**, ROUGE-L **0.90**, RelaxedEM(all) **0.85** | paper abstract / README tabla |
| Modelos disponibles | https://huggingface.co/Sherry791/Meta-Llama-3-8B-Instruct-ft4sciqa | README |
| Datos disponibles | `experiment_datasets/sciqa/` en repo; resultados en `results/` | README |
| Instrucciones de reproducción | Parcial: scripts presentes; README §Requirements: *“Coming soon or to be added here…”* | README |
| Necesita API | **No** para FT local; LLM opcional en cleaning; entrenamiento paper en **1× NVIDIA H100** | paper §5 |

---

## rdfconfig_llm

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `rdfconfig_llm` | lab |
| Nombre exacto | Accurate SPARQL generation via in-context learning and schema-based query construction (método LLM + RDF-config) | Bioinformatics paper |
| Artículo | Accurate SPARQL generation via in-context learning and schema-based query construction | `10.1093/bioinformatics/btag174` |
| Autores | Hikaru Nagazumi; Yuki Moriya; Shuichi Kawashima; Toshiaki Katayama; Kana Shimizu | PMC author contributions |
| Año | 2026 (Bioinformatics 2026 Apr 8; 42(5):btag174) | PMC / DOI |
| Venue | Bioinformatics (Oxford University Press) | DOI |
| DOI / ID | `10.1093/bioinformatics/btag174`; Zenodo código `10.5281/zenodo.18539213` | DOI / paper availability |
| Repositorio oficial (método) | https://github.com/scott2121/sparql_query_generator | paper |
| Repositorio companion | https://github.com/dbcls/rdf-config | paper + README |
| Licencia | README del generador declara **MIT** para archivos del repo; **no hay LICENSE file** en GitHub API (`license: null`). `dbcls/rdf-config`: MIT (SPDX) | README scott2121; GitHub API dbcls |
| Rama principal | `main` (generator); `master` (rdf-config) | GitHub API |
| Última actividad | generator push 2026-02-09; rdf-config push 2026-07-16 | GitHub API |
| Lenguaje(s) | Jupyter/Python (generator); Ruby (rdf-config) | GitHub API |
| Framework | OpenAI API + RDF-config (Ruby/bundler); notebooks `demo_propose.ipynb` | README / SETUP.md (referenciado) |
| Dataset original | Preguntas propias UniProt / Rhea / Bgee / UniProt&Bgee en `questions/` | paper + README |
| Knowledge graph original | UniProt, Rhea, Bgee (endpoints RDF life-science) | paper |
| Métrica original | Jaccard similarity entre tablas de resultados (execution-based) | paper |
| Resultado principal reportado | Proposed method Jaccard: UniProt **0.601**, Rhea **0.834**, Bgee **0.623**, UniProt&Bgee **0.569** (supera fine-tuning y prompt-tuning) | paper Table 2 |
| Modelos disponibles | LLM vía API (paper usa `gpt-4o-mini` en baselines); no checkpoint propio del método | paper |
| Datos disponibles | JSON/TTL questions en repo; schemas rdf-config | README / paper |
| Instrucciones de reproducción | Sí (README workflow + SETUP.md) | README |
| Necesita API | **Sí** (`OPENAI_API_KEY`) | README |

---

## sgpt

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `sgpt` | lab |
| Nombre exacto | SGPT | IEEE Access paper / README |
| Artículo | SGPT: A Generative Approach for SPARQL Query Generation From Natural Language Questions | `10.1109/ACCESS.2022.3188714` |
| Autores | Md Rashad Al Hasan Rony; Uttam Kumar; Roman Teucher; Liubov Kovriguina; Jens Lehmann | README citation / DOI |
| Año | 2022 | IEEE Access / README |
| Venue | IEEE Access, Vol. 10, pp. 70712–70723 | README bibtex |
| DOI / ID | `10.1109/ACCESS.2022.3188714` | DOI |
| Repositorio oficial | https://github.com/rashad101/SGPT-SPARQL-query-generation | paper footnote / GitHub |
| Licencia | MIT (`LICENSE.md`) | GitHub API + LICENSE.md |
| Rama principal | `main` | GitHub API |
| Última actividad (push) | 2024-09-15T09:21:37Z | GitHub API |
| Lenguaje(s) | Python | GitHub API |
| Framework | PyTorch; spaCy; GPT-2 (117M) decoder + Transformer encoders | paper §V-B; README |
| Dataset original | LC-QuAD 2.0; VQuAnDa; QALD-9 | paper §V-A |
| Knowledge graph original | Wikidata (LC-QuAD 2.0); DBpedia (VQuAnDa, QALD-9) | paper |
| Métrica original | BLEU, F1; propuestos SP-BLEU, SP-F1 | paper §V-C |
| Resultado principal reportado | Supera baselines seq2seq/template en los tres datasets (Table 4). **Celdas numéricas exactas de Table 4: UNKNOWN** en esta auditoría (extracción OCR/HTML incompleta del PDF). No se usan cifras citadas solo desde papers posteriores. | paper Table 4 |
| Modelos disponibles | Entrenamiento desde código; checkpoints en `runs/` si se generan — presencia de pesos preentrenados publicados: **UNKNOWN** sin clonar | README |
| Datos disponibles | Datasets públicos referenciados; scripts train/eval | README |
| Instrucciones de reproducción | Sí (`train.py`, `eval.py`, conda/pip) | README |
| Necesita API | **No** | README |

---

## tebaqa

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `tebaqa` | lab |
| Nombre exacto | TeBaQA (Template-Based Question Answering) | README / paper |
| Artículo | Knowledge Graph Question Answering Using Graph-Pattern Isomorphism | `10.3233/SSW210038`; también arXiv:2103.06752 |
| Autores | Daniel Vollmers; Rricha Jalota; Diego Moussallem; Hardik Topiwala; Axel-Cyrille Ngonga Ngomo; Ricardo Usbeck | DOI / README citation |
| Año | 2021 | DOI / arXiv |
| Venue | Further with Knowledge Graphs (Studies on the Semantic Web, IOS Press) | DOI page |
| DOI / ID | `10.3233/SSW210038`; arXiv:2103.06752 | DOI / README |
| Repositorio oficial | https://github.com/dice-group/TeBaQA | GitHub |
| Licencia | AGPL-3.0 | GitHub API + LICENSE |
| Rama principal | `master` | GitHub API |
| Última actividad (push) | 2023-10-30T15:28:03Z | GitHub API |
| Lenguaje(s) | Java | GitHub API |
| Framework | Microservicios Java; Elasticsearch 6.6.1; CoreNLP; scripts Docker/`build-script.sh` | README |
| Dataset original | QALD-8, QALD-9, LC-QuAD v1, LC-QuAD v2 | paper / README Evaluation |
| Knowledge graph original | DBpedia (principal); Wikidata (LC-QuAD v2) | paper |
| Métrica original | QALD F-Measure (GERBIL); Precision/Recall | paper Table 2 |
| Resultado principal reportado | QALD-8: QALD F-Measure **0.556** (SOTA en paper); QALD-9: **0.374**; LC-QuAD v1 F-Measure **0.30** | paper Table 2 / texto |
| Modelos disponibles | Clasificadores ML (WEKA); no LLM; índices ES externos | paper / README |
| Datos disponibles | Dumps/índices DBpedia 2016-10 vía Hobbit data URL | README |
| Instrucciones de reproducción | Sí (local scripts + Docker scripts) | README |
| Necesita API | **No** (endpoints SPARQL/ES locales o remotos) | README |

---

## Resumen de incertidumbre global

| Tema | Estado |
|---|---|
| Commits exactos | UNKNOWN (sin clonar; se fijarán en `REPOSITORIES.lock.yaml`) |
| Licencias sin SPDX | mkgqagent, cot_sparql, firesparql, scott2121 generator → UNKNOWN/claim-only |
| Números Table 4 SGPT | UNKNOWN hasta extracción completa del PDF IEEE |
| Publicación formal TWEB de SPARQL-LLM | UNKNOWN más allá de arXiv |

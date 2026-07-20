# Inventario de repositorio — CoT-SPARQL (WAVE_C)

**Fecha auditoría:** 2026-07-20  
**Upstream:** `upstream/cot_sparql/`  
**Pinned commit:** `063edd9868425e54010a0cb49ce585ed2186be4d` (`PIN`)  
**Lab HEAD al inicio:** `562b5f1108e3289ae5b93668f2bd9d994d0a5b28` (`PIN`)  
**Etiquetas:** `PIN` | `CODE_VERIFIED` | `DATA_VERIFIED` | `README_REPORTED` | `PAPER_REPORTED` | `EXTERNAL_ARTIFACT_REFERENCED` | `NOT_FOUND` | `UNKNOWN`

**Restricción:** solo lectura de `upstream/`; **sin** install, import de `torch`/`transformers`/`spacy`/módulos del proyecto, descargas ni modificación de `upstream/`.

---

## Identificación

| Campo | Valor | Evidencia |
|---|---|---|
| method_id | `cot_sparql` | lab `METHOD_REGISTRY.yaml` |
| remoto | https://github.com/dice-group/CoT-Sparql | `REPOSITORIES.lock.yaml` |
| rama | `main` | `PIN` / lock |
| commit pin | `063edd9868425e54010a0cb49ce585ed2186be4d` | `PIN` / `.git_local` HEAD |
| licencia | **ABSENT** → `LICENSE_NOT_CONFIRMED` / SPDX `UNKNOWN` | `licenses/cot_sparql/`; `LICENSE_MATRIX.csv` |
| paper | SEMANTiCS 2024 / IOS SSW, DOI [10.3233/SSW240028](https://doi.org/10.3233/SSW240028) | `PIN` / `PAPER_REPORTED` |
| inclusion | `INCLUDE_CONDITIONAL` | lab |
| reproduction_status | `audit_only` | lab |
| common_adapter_allowed | `false` | lab |
| feasibility_class | `requires_external_gpu` | lab |

---

## Escala del árbol

| Métrica | Valor | Evidencia |
|---|---|---|
| Archivos (excl. `.git_local`) | **22** | `CODE_VERIFIED` / `audit/CLONING_REPORT.md` |
| Tamaño árbol (`du`) | **~64 M** (≈51 M excl. `.git_local` en host) | `REPO` / cloning report |
| Suma bytes contenido (checksums) | **52 853 967 ≈ 50.4 MiB** (lista SHA; ~52.8 MB reportado lab) | `DATA_VERIFIED` `logs/static-audit-cot-sparql/all_file_checksums.sha256` |
| Checksums SHA-256 | `logs/static-audit-cot-sparql/all_file_checksums.sha256` | `DATA_VERIFIED` |
| AST health | `logs/static-audit-cot-sparql/ast_health.json` — 5 `.py` parse OK | `CODE_VERIFIED` |

---

## Árbol lógico (código y config)

| Path | Rol | Evidencia |
|---|---|---|
| `main.py` | CLI + carga GPTQ + prompt CoT + generación + validación | `CODE_VERIFIED` |
| `contexta.py` | entity linking + relation extraction (DBpedia/Wikidata) | `CODE_VERIFIED` |
| `contextb.py` | recuperación one-shot por embeddings MiniLM | `CODE_VERIFIED` |
| `validation.py` | extracción SPARQL + “validez” vía HTTP a endpoints | `CODE_VERIFIED` |
| `spacy_component.py` | factory spaCy `rebel` (REBEL) | `CODE_VERIFIED` |
| `environment.yml` | Conda env `sparqlgen`, Python 3.10 (~178 líneas) | `CODE_VERIFIED` |
| `requirements.txt` | **export Conda** (`pkg=ver=build`), no pip puro | `CODE_VERIFIED` |
| `README.md` | install / wget embeddings / `main.py` ejemplo | `README_REPORTED` |
| `temp/embeddings.ipynb` | construcción parquet/pkl de ejemplos | `CODE_VERIFIED` |
| `temp/gitignore` | ignora artefactos en `temp/` | `CODE_VERIFIED` |
| `dataset/*.json` | trains embebidos (sin test/val) | `DATA_VERIFIED` |
| `NL-SPARQL.ipynb`, `Other_LLMs/*.ipynb` | notebooks exploratorios / otros LLMs | `CODE_VERIFIED` |
| `COTs-SPARQL.svg`, `arch.png`, `COTs-SPARQL.pdf` | figuras / PDF | `REPO` |
| `LICENSE*` | **ausente** | `NOT_FOUND` |

---

## Datos embebidos (train only)

| Path | Conteos / notas | Evidencia |
|---|---|---|
| `dataset/qald_10_train.json` | 412 preguntas (formato QALD-10 `questions`) | `DATA_VERIFIED` |
| `dataset/train_lcquad2.json` | 21497 | `DATA_VERIFIED` |
| `dataset/train_qald.json` | 350 (estilo QALD-9) | `DATA_VERIFIED` |
| `dataset/train_vquanda.json` | 3500 | `DATA_VERIFIED` |
| `dataset/*test*` / `*val*` | **ausentes** | `NOT_FOUND` |

Detalle + SHA-256: `DATASET_INVENTORY.csv`, `DATASET_PROVENANCE_AND_SPLITS.md`.

---

## Artefactos externos / ausentes en clon

| Artefacto | Estado local | Evidencia |
|---|---|---|
| `temp/embeddings_{dbpedia,wikidata}.pkl` | **NOT_FOUND** (gitignore) | `CODE_VERIFIED` + `EXTERNAL_ARTIFACT_REFERENCED` README |
| `temp/{dbpedia,wikidata}_examples.parquet` | **NOT_FOUND** | idem |
| CodeLlama-34B-Instruct-GPTQ (HF) | no vendored | `README_REPORTED` / `EXTERNAL_ARTIFACT_REFERENCED` |
| `all-MiniLM-L6-v2`, `en_core_web_lg`, `Babelscape/rebel-large` | no vendored | `CODE_VERIFIED` imports |
| Predicciones / métricas / scripts eval | **NOT_FOUND** | `CODE_VERIFIED` |
| Checkpoint fine-tune propio del método | **NOT_FOUND** (usa LLM base GPTQ) | `PAPER_REPORTED` / repo |

Inventario externo: `EXTERNAL_ARTIFACT_INVENTORY.csv`.

---

## Conclusión inventario

El clon aporta **código de inferencia prompt-based** + **datasets train** + notebooks de embeddings; **no** aporta LICENSE, embeddings/parquet de recuperación, pesos LLM, ni harness de evaluación paper. Ver `STATIC_AUDIT.md`.

# REPOSITORY_INVENTORY — firesparql

**Fecha:** 2026-07-20  
**method_id:** `firesparql`  
**upstream:** `upstream/firesparql/`  
**pinned_commit:** `48d6f168e4c1dd3dc467553aef370299911d4e76` (`PIN`)  
**remoto:** https://github.com/sherry-pan/FIRESPARQL.git (`CODE_VERIFIED` remote)

---

## Tamaño y conteos (`REPO` / shell)

| Ámbito | Valor | Evidencia |
|---|---|---|
| Árbol total | ~598 M | `du` |
| Archivos (excl. `.git_local` prune) | ~71954 | `find` |
| Bajo `results/` | ~71904 archivos | `find` |
| `codes/` | ~3.0 M | `du` |
| `experiment_datasets/` | ~96 M | `du` |
| `results/` | ~458 M | `du` |

El repositorio es **results-heavy**: la masa dominante son textos generados / limpios / CSV de ejecución, no el código de entrenamiento.

---

## Top-level presente

| Path | Rol | Evidencia |
|---|---|---|
| `README.md` | overview + tabla métricas + HF link | `README_REPORTED` |
| `codes/` | generación, cleaning, métricas, shells Snellius | `CODE_VERIFIED` |
| `experiment_datasets/` | SciQA + DBLP + prep scripts | `DATA_VERIFIED` |
| `results/` | step1…step5 + `context_from_rag/` | `RESULT_FILE_VERIFIED` |
| `.gitignore` | ignore rules | `CODE_VERIFIED` |

---

## Ausentes críticos (`NOT_FOUND`)

| Artefacto | Estado |
|---|---|
| `LICENSE` / `LICENSE.md` | **ABSENT** → `LICENSE_NOT_CONFIRMED` |
| `requirements.txt` | **ABSENT** (README: Requirements *Coming soon*) |
| `environment.yml` | **ABSENT** |
| `Dockerfile` | **ABSENT** |
| `CITATION` / `CITATION.cff` | **ABSENT** |
| `merge_models/` | **ABSENT** (referenciado por `run_all_generate.sh`) |
| Trainer LoRA (`peft` / `LoraConfig` / `SFTTrainer` / `train*.py`) | **ABSENT** |

---

## `codes/` (scripts principales)

Generación: `generate_sparql_{cuda,mps}.py`, `generate_sparql_one_shot_cuda.py`, `generate_sparql_rag_{cuda,mps}.py`, `generate_context_rag.py`.  
Post: `sparql-cleaning-llm.py`.  
Eval: `bleu_rouge.py`, `exact_match.py`, `accumulate_exact_match.py`.  
Batch: `run_all_{generate,cleaning,bleu_rouge,exact_match}.sh`.  
Notebooks: `merge_sparql.ipynb`, `ploting.ipynb`.  
Doc auxiliar: `codes/readme.md`.

AST parse OK en muestra de `.py` (`logs/static-audit-firesparql/ast_health.json`, `CODE_VERIFIED`).

---

## `experiment_datasets/`

- `sciqa/` — splits JSON + `project_data/` (test 513, train 1795, most_similar, FT json, orkg-property, handcrafted).  
- `dblp/` — train/valid/test JSON + `project_data/` (FT 7000, test 2000).  
- `codes/` — transformaciones JSON→instruction y `one_shot_mapping.py` (paths absolutos LLaMa-Factory).

---

## `results/` (estructura real vs README)

| Dir real | README claim | Nota |
|---|---|---|
| `step1_generated_text/` | OK | familias vanilla / one_shot / ft / vanilla_rag / ft_rag |
| `step2_clean_sparql/` | OK | + CSVs `bleu_rouge_results_*.csv` |
| `step3_sparql_running_against_orkg/` | README: `…_against_qlever` | **MISMATCH** nombre |
| `step4_accumulated_success_sparql/` | README: `…_success_metrics` | **MISMATCH** nombre; contiene `success_ids_*.txt` |
| `step5_error_analysis/` | OK | 2 CSV |
| `context_from_rag/` | OK | contextos Groq/etc. |

---

## Conclusión inventario

Repo **clonable y rico en resultados versionados**, pero **pobre en definición de entorno y en código de entrenamiento**. Los resultados versionados **≠** reproducción local (`INFERENCE`).

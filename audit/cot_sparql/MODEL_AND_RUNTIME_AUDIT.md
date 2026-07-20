# Modelo y runtime — CoT-SPARQL

**Fecha:** 2026-07-20  
**Host lab:** RTX 4050 ≈6 GiB VRAM; Python 3.10.12; WSL (`MACHINE_PROFILE.md`)  
**Etiquetas:** `CODE_VERIFIED` | `README_REPORTED` | `PAPER_REPORTED` | `EXTERNAL_ARTIFACT_REFERENCED` | `INFERENCE`

---

## LLM principal

| Campo | Valor | Evidencia |
|---|---|---|
| Ejemplo README | `TheBloke/CodeLlama-34B-Instruct-GPTQ` | `README_REPORTED` |
| Carga | `AutoGPTQForCausalLM.from_quantized` | `main.py` L69–76 `CODE_VERIFIED` |
| `model_basename` | `"model"` | L67–70 |
| `trust_remote_code` | `True` | L72 |
| `device` | `"cuda:0"` (hardcoded) | L73 |
| `use_safetensors` | `True` | L71 |
| Pipeline | `text-generation`, `device_map="auto"`, `do_sample=True` | L79–85 |
| Fine-tune del método | **no** — prompting sobre LLM cuantizado externo | `CODE_VERIFIED` / `PAPER_REPORTED` |

### Factibilidad host

CodeLlama-**34B** GPTQ **no es factible** en 6 GiB VRAM para smoke nativo (`INFERENCE` / lab `requires_external_gpu`). README permite “change the model based on the available system” (`README_REPORTED`) — cualquier sustitución deja de ser reproducción paper-scale (`INFERENCE`).

---

## Modelos auxiliares

| Modelo | Uso | Evidencia |
|---|---|---|
| `all-MiniLM-L6-v2` | embeddings retrieval | `contextb.py` L9 |
| `en_core_web_lg` | base spaCy EL/RL | `contexta.py` |
| `Babelscape/rebel-large` | RL Wikidata | `contexta.py` L37; `spacy_component.py` |

Todos requieren descarga HF/spaCy; **no** vendored (`EXTERNAL_ARTIFACT_REFERENCED`).

---

## Runtime / entorno

| Artefacto | Contenido | Evidencia |
|---|---|---|
| `environment.yml` | name `sparqlgen`; `python=3.10.0`; pip: auto-gptq, torch 2.1.1, transformers 4.32.1, sentence-transformers, spacy, spacy-dbpedia-spotlight, spacyfishing, … (~178 líneas) | `CODE_VERIFIED` |
| `requirements.txt` | cabecera Conda export `pkg=ver=build` | `CODE_VERIFIED` |
| README “Without Conda” | `pip install -r requirements.txt` | `README_REPORTED` — **contradice** formato Conda (`CODE_VERIFIED` mismatch) |
| `Accelerator` | importado unused | `main.py` L3 |

---

## Estados smoke (lab)

| Capacidad | Estado |
|---|---|
| `model_smoke` | **blocked** (34B GPTQ / VRAM) |
| `end_to_end` | **not_ready** |
| `native` | **not_ready** |
| `DATA_ONLY` | **ready** |
| `DEPENDENCY_INSTALL` | **legally_blocked/conditional** (`LICENSE_NOT_CONFIRMED` + conda vs pip) |
| `LINKER_SMOKE` | **conditional** (APIs + spaCy) |
| `RETRIEVAL_SMOKE` | **blocked** sin parquet/pkl |
| `COMMON_EVALUATION_ADAPTATION` | **legally_blocked** |

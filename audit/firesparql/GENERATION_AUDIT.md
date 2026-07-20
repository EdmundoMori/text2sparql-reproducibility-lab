# GENERATION_AUDIT — firesparql

**Fecha:** 2026-07-20

---

## Scripts

| Script | Device | Evidencia |
|---|---|---|
| `codes/generate_sparql_cuda.py` | CUDA si disponible else CPU; `device_map="auto"` | `CODE_VERIFIED` |
| `codes/generate_sparql_mps.py` | fuerza `device_map={"": "cpu"}` pese a nombre MPS | `CODE_VERIFIED` |
| `codes/generate_sparql_one_shot_cuda.py` | como cuda zero-shot + ejemplo | `CODE_VERIFIED` |
| `codes/generate_sparql_rag_cuda.py` / `_mps.py` | RAG + `max_new_tokens=1024` | `CODE_VERIFIED` |

Batch: `codes/run_all_generate.sh` → `merge_models/$MODEL` + `xueli_data/.../test_questions.csv`.

---

## Hiperparámetros de generación (`CODE_VERIFIED`)

| Parámetro | Zero / one-shot | RAG gen |
|---|---|---|
| dtype | `torch.float16` | `torch.float16` |
| `device_map` | `"auto"` (cuda) | `"auto"` |
| `temperature` | `0.7` | no pasado a `generate` (default HF) |
| longitud | `max_length=512` | `max_new_tokens=1024` |
| `do_sample` | **no explícito**; implicado por temp (`INFERENCE` de intención) | n/a |
| chat template | tokens Llama-3 `<|begin_of_text|>…` | idem |

---

## Prompt zero-shot (ORKG hardcoded)

Texto fijo en `generate_sparql_cuda.py`: describe ORKG, pide solo SPARQL, inserta `Input Question`. **Domain-specific** — no genérico KG.

One-shot: añade Example Question + Example SPARQL (`train_query` gold).  
RAG: **prompt2 activo** (prompt1 comentado); contexto opcional; strip `<think>…</think>`.

---

## Salidas

`{output_dir}/{question_id}.txt` con secciones Question / Generated SPARQL.  
Familias versionadas en `results/step1_generated_text/` (~60 configs útiles con 513 txt; ver `RESULTS_INVENTORY.csv`).

---

## Riesgos

- Paths `xueli_data` / `merge_models` rompen ejecución out-of-box.  
- Sampling no determinista (temp 0.7) → necesidad de 3 rounds en results.  
- Sin seed fijada en scripts (`NOT_FOUND`).  
- 8B fp16 en 6 GiB: **blocked** sin quant ≠ paper.

# ONE_SHOT_RETRIEVAL_AUDIT — firesparql

**Fecha:** 2026-07-20  
**Veredicto:** one-shot **no** es end-to-end en un solo script; retrieval offline + generación separados.

---

## Retrieval (`experiment_datasets/codes/one_shot_mapping.py`)

| Aspecto | Valor | Evidencia |
|---|---|---|
| Encoder | `SentenceTransformer('all-MiniLM-L6-v2')` | `CODE_VERIFIED` |
| Similaridad | cosine (`sklearn`) | `CODE_VERIFIED` |
| k | 1 (`np.argmax`) | `CODE_VERIFIED` |
| Ejemplo inyectado | `train_query` **gold** del train pair | `CODE_VERIFIED` |
| Paths I/O | absolutos `/Users/sherrypan/GitHub/LLaMa-Factory/xueli_data/...` | `CODE_VERIFIED` |
| Artefacto vendido | `most_similar_questions.csv` n=513 | `DATA_VERIFIED` |

Campos CSV: `id,test_question,test_query,best_train_question,train_query`  
sha256: `9b4150dd3c3eafc760bec6049d18c8fbf6fe8d50c4288ee4715759864d06f4fe` (`DATA_VERIFIED`).

---

## Generación (`codes/generate_sparql_one_shot_cuda.py`)

Lee el CSV precomputado; **no** recalcula embeddings. Prompt incluye ejemplo gold. Gen: `max_length=512`, `temperature=0.7`, fp16, `device_map=auto`.

---

## Implicaciones de auditoría

- Filtrar “dynamic example retrieval” en matriz WAVE_C: **sí** (MiniLM cosine argmax k=1), pero **offline** y con **leak de gold SPARQL de train** en el prompt (diseño few-shot clásico; no EL/RL).  
- Reproducir mapping exige relocatar paths + deps `sentence-transformers` (no instalado en esta pasada).  
- Results: `results/step1_generated_text/one_shot/` 6 configs × 513 (`RESULT_FILE_VERIFIED`).

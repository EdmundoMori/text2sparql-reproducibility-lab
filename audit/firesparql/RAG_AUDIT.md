# RAG_AUDIT — firesparql

**Fecha:** 2026-07-20  
**Veredicto readiness:** `RAG_SMOKE = blocked` (Groq + APIs + chromadb + paths).

---

## Etapa contexto — `codes/generate_context_rag.py`

| Parámetro | Valor | Evidencia |
|---|---|---|
| LLM | Groq `deepseek-r1-distill-llama-70b` | `CODE_VERIFIED` |
| Auth | `GROQ_API_KEY` via dotenv | `CODE_VERIFIED` |
| temp LLM | 0.5 | `CODE_VERIFIED` |
| Vector DB | `chromadb.EphemeralClient()` | `CODE_VERIFIED` |
| Embeddings | `HuggingFaceEmbedding("BAAI/bge-small-en")` | `CODE_VERIFIED` |
| Index docs | `xueli_data/sciqa/project_data/rag_files` | `CODE_VERIFIED` |
| Sample props en prompt | primeros **20** de `orkg-property.json` | `CODE_VERIFIED` |
| Stack | LlamaIndex `VectorStoreIndex` + Chroma | `CODE_VERIFIED` |

Salida: `results/context_from_rag/{model}/{id}.txt` (hay variantes deepseek / llama-3.3 / mixtral / prompt1–3) (`RESULT_FILE_VERIFIED`).

Nota: el sample de 20 propiedades es **prefijo de lista**, no retrieval semántico sobre las 9062 (`CODE_VERIFIED`) — el retrieval Chroma indexa `rag_files`, pero el user_query también embebe un JSON sample truncado.

---

## Etapa generación — `generate_sparql_rag_{cuda,mps}.py`

- Limpia contexto con regex `<think>…</think>`.  
- **prompt2** activo (contexto RAG opcional); prompt1 comentado.  
- `max_new_tokens=1024`; fp16; cuda `device_map=auto`.  
- Comentarios de ejemplo usan `merge_models/...` + `xueli_data/...`.

---

## Posición paper/README

README: RAG **no** mejora y puede introducir ruido (`README_REPORTED`). Familias `vanilla_rag` / `ft_rag` en results permiten contraste (`RESULT_FILE_VERIFIED`).

---

## Bloqueos

No ejecutar RAG_SMOKE aquí: secretos, red, chromadb, descarga BGE, paths `xueli_data`.

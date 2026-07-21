# Política de índice mínimo — SPARQL-LLM LOCAL_CHAT_API

**Fecha:** 2026-07-21  
**Prompt:** 10  
**Etiqueta:** `LAB_MINIMAL_INDEX`  
**Acción futura:** `LOCAL_CHAT_API_ONE_QUESTION`  
**Gate:** permanece `CONDITIONAL_GO` (este documento no autoriza descarga de embeddings ni LLM).

---

## 1. Decisión Qdrant (este prompt)

| Opción | Decisión |
|---|---|
| Modo | **Qdrant embebido** (`vectordb_url` = path local) |
| Servicio Qdrant | **No** |
| Docker Compose | **No** |
| Puertos | **No** |
| Colección | Una sola: `lab_minimal_uniprot_void` |
| Persistencia | Descartable bajo `workdir/runs/.../qdrant` (gitignored) |
| `index_entities` | **No** |
| Catálogo SIB completo | **No** |
| `init_vectordb()` completo | **No** (recorre endpoints/homepages online) |

---

## 2. Fuente de documentos

- **Única fuente:** `tests/void_uniprot.ttl` (fixture local del commit pin).  
- Endpoint lógico declarado: `https://sparql.uniprot.org/sparql/` (URL en payloads; **cero** consultas de red en Prompt 10).  
- Sin `homepage_url`, sin `examples_file` remoto, sin labels vía SPARQL.  
- Máximo propuesto: **12** documentos.  
- `doc_type`: `SPARQL endpoints classes schema`.  
- `source_scope`: `LAB_MINIMAL_INDEX`.

---

## 3. Separación de artefactos

| Artefacto | Requiere embeddings | Estado posible sin descarga |
|---|---|---|
| Documentos (`minimal-documents.jsonl`) | No | Preparables ahora |
| Índice Qdrant (vectores) | Sí (`intfloat/multilingual-e5-large`) | Solo con `complete_exact_model_cache` |

---

## 4. Embedding

- Modelo exacto: `intfloat/multilingual-e5-large`.  
- **No** sustituir por otro modelo.  
- **No** descargar en Prompt 10.  
- Si la caché exacta está ausente → `environment_ready_index_blocked_pending_embedding_download_approval`.

---

## 5. Interpretación científica

`LAB_MINIMAL_INDEX` es un **preflight funcional** del laboratorio.

**No** es:

- el índice nativo del paper;
- el índice del benchmark biodata;
- una reproducción de métricas TREC.

---

## 6. Desviaciones de Settings respecto a defaults upstream

Documentadas fuera del JSON (ver `minimal_local_chat_settings.json` + report):

- `default_max_try_fix_sparql=0` — desviación de seguridad para acotar futuro smoke a **máximo propuesto 2** llamadas LLM (extract + call_model).  
- `default_max_tokens=512` — **no** es límite efectivo en la rama OpenRouter del commit fijado (`CODE_VERIFIED`).  
- `auto_init=false` — evita `init_vectordb` en startup.

# LOCAL_CHAT_API — descarga controlada e índice mínimo (Prompt 10B)

**Fecha:** 2026-07-21  
**RUN_ID:** `20260721T092249Z`  
**Parent prep:** `20260721T084637Z`  
**method_id:** `sparql_llm`  
**upstream pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**lab HEAD inicial:** `96d5bab9556065cd0cd5785327475565ce910cba`

---

## 1. Autorización

| Campo | Valor |
|---|---|
| Aprobador | EDMUNDO MORI ORRILLO |
| Fecha | 2026-07-21 |
| Modelo | `intfloat/multilingual-e5-large` (exacto) |
| Artefacto | `environments/sparql_llm/preparations/20260721T092249Z/EMBEDDING_DOWNLOAD_AUTHORIZATION.md` |

---

## 2. Clasificación final

**`ENVIRONMENT_READY_INDEX_READY_PREFLIGHT_PASS`**

| Dimensión | Estado | Evidencia |
|---|---|---|
| Descarga embeddings | **ok** (único modelo autorizado) | `CACHE_VERIFIED` |
| Carga offline | **ok** dim=1024 | `CACHE_VERIFIED` |
| Índice LAB_MINIMAL | **INDEX_VERIFIED** (12 pts) | `INDEX_VERIFIED` |
| Preflight FastAPI | **pass** (`/chat`,`/mcp`,`/openapi.json`) | `EXECUTION_VERIFIED` |
| POST `/chat` | **0** | |
| LLM | **0** | |
| SPARQL endpoints | **0** (fallo cerrado en prefix fetch) | |
| Gate smoke | permanece **CONDITIONAL_GO** | presupuesto/modelo pendientes |

---

## 3. Procedencia del artefacto (FastEmbed 0.8.0)

| Campo | Valor |
|---|---|
| Requested / resolved | `intfloat/multilingual-e5-large` |
| HF source (metadata) | `qdrant/multilingual-e5-large-onnx` |
| URL efectiva | `https://storage.googleapis.com/qdrant-fastembed/fast-multilingual-e5-large.tar.gz` |
| Tamaño cache | 2 252 995 903 bytes (~2.1 GiB) |
| Archivos | 13 |
| Nota | Imagen trae `HF_HUB_OFFLINE=1` → HF API no alcanzable; fallback GCS del mismo registro FastEmbed |

Caché en `workdir/runs/sparql-llm-embedding-index/20260721T092249Z/embedding_cache` (**gitignored**).

---

## 4. Índice

- Colección `lab_minimal_uniprot_void`
- 12 puntos, Cosine, dim 1024
- `source_scope=LAB_MINIMAL_INDEX`
- Qdrant path local gitignored (~168 KiB metadatos/segmentos)

---

## 5. Preflight

- Import `sparql_llm.agent.main.app` con Settings mínimo + índice montado
- GET `/openapi.json` → 200
- Sin POST `/chat`, sin LLM, `--network none`
- CWD = `upstream/sparql_llm` (solo para rutas relativas `webapp/assets`; código del paquete = site-packages)

---

## 6. Estados experimentales (sin cambio indebido)

- `reproduction_status`: **smoke_only** (sigue siendo el de 5B)
- `native_audit_complete`: **false**
- `common_adapter_allowed`: **false**
- No `partially_reproduced` / `reproduced`

---

## 7. Siguiente prompt

**Prompt 11 — Cierre de presupuesto, selección de modelo y gate final para LOCAL_CHAT_API_ONE_QUESTION**

No ejecutar smoke `/chat` hasta firma de presupuesto y modelo.

---

## 8. Artefactos versionables

| Ruta | Rol |
|---|---|
| `scripts/preparation/sparql_llm_download_embedding.py` | Descarga controlada |
| `environments/sparql_llm/preparations/20260721T092249Z/` | Auth + result |
| `logs/preparation/sparql-llm-embedding-index/20260721T092249Z/` | Logs/checksums (sin pesos) |
| Este informe | Síntesis |

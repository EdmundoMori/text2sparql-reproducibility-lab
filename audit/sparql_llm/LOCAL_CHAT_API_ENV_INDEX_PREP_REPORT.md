# LOCAL_CHAT_API — preparación de entorno e índice mínimo (Prompt 10)

**Fecha:** 2026-07-21  
**RUN_ID:** `20260721T084637Z`  
**method_id:** `sparql_llm`  
**upstream pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**lab HEAD inicial:** `45605d47983961210679fdd8d6b39577eafee1ec`  
**Acción futura:** `LOCAL_CHAT_API_ONE_QUESTION`  
**Gate online:** permanece **CONDITIONAL_GO**

---

## 1. Clasificación final

**`ENVIRONMENT_READY_INDEX_BLOCKED_PENDING_EMBEDDING_DOWNLOAD_APPROVAL`**

| Dimensión | Estado | Evidencia |
|---|---|---|
| Entorno agent Py3.11 | **ready** | `ENVIRONMENT_VERIFIED` — imagen Docker |
| Documentos mínimos VoID | **ready** (12) | `EXECUTION_VERIFIED` — `--network none` |
| Caché `intfloat/multilingual-e5-large` | **absent** | `NOT_FOUND` |
| Índice Qdrant LAB_MINIMAL | **blocked** | no construido |
| Preflight FastAPI | **not_run** | requiere índice |
| LLM / POST /chat | **0** | `EXECUTION_VERIFIED` por ausencia |
| Endpoints SPARQL | **0** | `EXECUTION_VERIFIED` |

---

## 2. Imagen

| Campo | Valor |
|---|---|
| Tag | `text2sparql-lab/sparql-llm-agent-py311:20260721T084637Z` |
| Image ID | `sha256:d51c8d45a460891ec0b63334c185f49546ddd030f0007ef5402b7f8287e8ded0` |
| Base | `python@sha256:b18992999dbe963a45a8a4da40ac2b1975be1a776d939d098c647482bcad5cba` |
| Dockerfile | `environments/sparql_llm/Dockerfile.agent-py311` |
| Install | `.[agent]` non-editable; no import en build |
| Paquete | sparql-llm **0.1.4**; fastembed 0.8.0; qdrant-client 1.18.0; langgraph 1.2.9; fastapi 0.139.2 |

---

## 3. Settings y política

- `environments/sparql_llm/minimal_local_chat_settings.json` — UniProt + void local; `auto_init=false`; `default_max_try_fix_sparql=0`.  
- `environments/sparql_llm/MINIMAL_INDEX_POLICY.md` — Qdrant path embebido; etiqueta `LAB_MINIMAL_INDEX`.  
- Desviaciones: `preparations/<RUN_ID>/deviations.md`.

---

## 4. Documentos

- Fuente: `void_uniprot.ttl` local.  
- 12 clases (IRI ordenados), `doc_type=SPARQL endpoints classes schema`, `source_scope=LAB_MINIMAL_INDEX`.  
- Sin labels remotos, sin homepage, sin red.  
- Artefactos: `logs/preparation/sparql-llm-local-chat-api/20260721T084637Z/minimal-documents.{jsonl,manifest.json}`.

---

## 5. Caché e índice

- Inventario: `preparations/.../embedding_cache_inventory.json` → **absent**.  
- **No** se inicializó `TextEmbedding`.  
- **No** se descargó el modelo.  
- **No** `build-index` / `verify-index`.  
- **No** preflight `agent.main`.

---

## 6. Presupuesto (actualizado, no firmado)

Ver `docs/protocols/sparql_llm/API_BUDGET_AND_SAFETY.md`:

- `MIN_EXPECTED_LLM_CALLS_PER_QUESTION = 2` (`CODE_VERIFIED`).  
- `MAX_LLM_CALLS = 2` (`PROPOSED`) solo con `max_try_fix_sparql=0`.  
- OpenRouter **no** aplica `max_tokens` → bloqueador.  
- Aprobador / USD / descarga embeddings: **pendientes**.

---

## 7. Qué no es este run

- No es smoke_only nuevo (conserva 5B).  
- No es reproducción ni benchmark.  
- No es índice del paper.  
- No abre adapters ni Fase 2.

---

## 8. Siguiente prompt recomendado

**Prompt 10B — Descarga controlada y fijación de caché `intfloat/multilingual-e5-large` + construcción del índice mínimo**, previa **autorización explícita** del investigador.

Tras índice + preflight: Prompt 11 (presupuesto/modelo/gate final) antes de `/chat`.

---

## 9. Artefactos

| Ruta | Rol |
|---|---|
| `environments/sparql_llm/Dockerfile.agent-py311` | Imagen agent |
| `environments/sparql_llm/minimal_local_chat_settings.json` | Settings |
| `environments/sparql_llm/MINIMAL_INDEX_POLICY.md` | Política índice |
| `environments/sparql_llm/preparations/20260721T084637Z/` | Manifest/result |
| `scripts/preparation/sparql_llm_minimal_index.py` | Docs/index lab |
| `scripts/preparation/sparql_llm_local_chat_preflight.py` | Preflight (no ejecutado) |
| `logs/preparation/sparql-llm-local-chat-api/20260721T084637Z/` | Logs |

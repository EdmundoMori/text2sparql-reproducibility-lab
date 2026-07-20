# API_SIB_PROTOCOL_READINESS — sparql_llm (Prompt 9)

**Fecha:** 2026-07-20  
**Tipo:** readiness documental (sin ejecución online)  
**Pinned commit:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Lab HEAD inicial:** `3d89a8d61f3fed8eecec8e49f6b79baccf677a76`

---

## 1. Veredicto

| Campo | Valor |
|---|---|
| Protocolo API/SIB | **COMPLETO** (14 artefactos) |
| Gate hacia smoke | **CONDITIONAL_GO** |
| Acción futura única | **LOCAL_CHAT_API_ONE_QUESTION** |
| `reproduction_status` | `smoke_only` (sin cambio) |
| `native_audit_complete` | `false` (sin cambio) |
| `common_adapter_allowed` | `false` (sin cambio) |
| PE3 | no declarado |

---

## 2. Cumplimiento de mínimos (NEXT_EXECUTION_DECISION §10)

| # | Mínimo | Estado | Artefacto |
|---|---|---|---|
| 1 | Endpoints / entrypoints | OK | `EXECUTION_SURFACES.csv`, contratos |
| 2 | Claves / env (nombres) | OK | `CONFIGURATION_MATRIX.csv`, budget |
| 3 | Request/response | OK | `CHAT_API_CONTRACT.md`, `MCP_CONTRACT.md` |
| 4 | Offline vs online | OK | `OFFLINE_ONLINE_BOUNDARY.md` |
| 5 | Éxito/fallo smoke futuro | OK | `FUTURE_API_SMOKE_GONOGO.md`, L0 en benchmarks |
| 6 | Checklist GO/NO-GO | OK | `FUTURE_API_SMOKE_GONOGO.md` |

---

## 3. Hechos CODE_VERIFIED críticos capturados

- Import-time `get_mcp_app()` en `agent/main.py`.  
- Campos `ChatCompletionRequest` y configurable parcial.  
- Mismatch `validate_output` vs `enable_output_validation` (request ignorado).  
- `messages[-10:]`, `recursion_limit=25`, Bearer opcional.  
- OpenRouter sin `max_tokens` en rama; else con `max_tokens`/`max_retries=2`.  
- Settings defaults (vectordb path, e5-large, bm25, auto_init, LLM default, etc.).  
- MCP tools/resource/CLI anomalía `--http`.  
- `TextEmbedding` + QdrantClient import-time.  
- Grafo default y `enable_sparql_execution=false` omite SPARQL.  
- Benchmarks manual + biodata (flags `/chat`).  

---

## 4. Bloqueadores que mantienen CONDITIONAL_GO

1. Python 3.11 runtime (patrón Docker 5B).  
2. Qdrant path/URL.  
3. FastEmbed `intfloat/multilingual-e5-large`.  
4. `init_vectordb` o índice prebuilt.  
5. `OPENROUTER_API_KEY`.  
6. SETTINGS mínimo (UniProt `void_file` local).  
7. Aprobación presupuesto investigador.

---

## 4b. Clasificación de readiness (Prompt 9 §19)

| Capacidad | Estado |
|---|---|
| `protocol_definition` | **ready** |
| `local_mcp_stdio` | **conditional** (índice/embeddings) |
| `local_mcp_http` | **conditional** |
| `local_chat_api` | **conditional** (acción seleccionada; CONDITIONAL_GO) |
| `public_mcp_check` | **external_service_only** |
| `manual_benchmark` | **not_ready** (coste; aplazado) |
| `biodata_benchmark` | **not_ready** / **blocked** por coste y complejidad |
| `native_partial_attempt` | **not_ready** |
| `native_full_attempt` | **not_ready** |
| TEXT2SPARQL_VIRTUOSO | **blocked** |

---

## 5. Inventario de artefactos Prompt 9

Todos bajo `docs/protocols/sparql_llm/` salvo readiness y log:

1. `API_SIB_PROTOCOL.md` (26 secciones)  
2. `EXECUTION_SURFACES.csv` (8 superficies)  
3. `MCP_CONTRACT.md`  
4. `CHAT_API_CONTRACT.md`  
5. `MODEL_PROVIDER_MATRIX.csv`  
6. `CONFIGURATION_MATRIX.csv`  
7. `NETWORK_AND_SIDE_EFFECT_MATRIX.csv`  
8. `OFFLINE_ONLINE_BOUNDARY.md`  
9. `SIB_BENCHMARK_PROTOCOL.md`  
10. `FUTURE_SMOKE_CANDIDATES.csv` (A–F)  
11. `API_BUDGET_AND_SAFETY.md`  
12. `FUTURE_API_SMOKE_GONOGO.md`  
13. `audit/sparql_llm/API_SIB_PROTOCOL_READINESS.md` (este)  
14. `logs/sparql-llm-api-sib-protocol/commands.log`

---

## 6. Restricciones respetadas

Sin installs, imports ejecutados de upstream, API calls, Docker nuevo, embeddings/Qdrant/SPARQL/benchmarks ejecutados. Solo lectura de código pin y escritura documental en el lab.

---

## 7. Next prompt title

`Prompt 10 — Preparación de entorno e índice mínimo para smoke LOCAL_CHAT_API de SPARQL-LLM (sin llamadas LLM)`

---

## 8. Resumen ejecutivo

El camino nativo condicional queda protocolizado: **LOCAL_CHAT_API_ONE_QUESTION** bajo gate **CONDITIONAL_GO**. El MCP público queda etiquetado como chequeo de servicio externo. El siguiente trabajo es preparación de entorno/índice **sin LLM**, no el smoke de pregunta todavía.

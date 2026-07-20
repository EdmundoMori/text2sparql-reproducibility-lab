# Frontera offline / online — SPARQL-LLM

**Commit pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Propósito:** separar lo ya verificado offline de lo que exige red para el smoke futuro `LOCAL_CHAT_API_ONE_QUESTION`.

---

## 1. Offline ya cubierto (CORE_OFFLINE)

| Ítem | Estado | Evidencia |
|---|---|---|
| Import/validate con artefactos locales en Py3.11 (Docker 5B) | `smoke_only` | `EXECUTION_VERIFIED` `CORE_OFFLINE_PY311_SMOKE_REPORT.md` |
| Host Py3.10 | `setup_failed` | `EXECUTION_VERIFIED` 5A |
| Virtuoso / TEXT2SPARQL local | bloqueado | registry / MACHINE_PROFILE |

**Conclusión:** la frontera offline de loaders/validación **no** se reabre en Prompt 9; no tercer CORE_OFFLINE.

---

## 2. Zona híbrida (índice / embeddings)

| Componente | Offline posible | Online por defecto | Evidencia |
|---|---|---|---|
| `TextEmbedding(multilingual-e5-large)` | solo con cache/modelo ya presente | descarga al construir | `CODE_VERIFIED` import-time |
| Qdrant `data/vectordb` | path local sin red si índice existe | init puede tocar endpoints/homepages | `CODE_VERIFIED` |
| `void_file` UniProt `./tests/void_uniprot.ttl` | lectura local | endpoint URL sigue en Settings | `CODE_VERIFIED` |
| Scraping `homepage_url` | omitiendo endpoints con homepage | httpx GET | `CODE_VERIFIED` |

Prompt 10 (previsto) prepara esta zona **sin** llamadas LLM.

---

## 3. Online obligatorio para Chat API smoke

| Dependencia | Motivo | Mitigación |
|---|---|---|
| `OPENROUTER_API_KEY` + API OpenRouter | default model `openrouter/...` | presupuesto `MAX_QUESTIONS=1` |
| Proceso FastAPI `/chat` | superficie seleccionada | runtime Py3.11 |
| Retrieval Qdrant | nodo `retrieve` en grafo default | índice mínimo previo |

---

## 4. Online opcional / desactivable

| Dependencia | Flag | Default | Para smoke |
|---|---|---|---|
| Ejecución SPARQL en agent | `enable_sparql_execution` | `True` | **False** (`CODE_VERIFIED` omite `query_sparql`) |
| Tool MCP `execute_sparql_query` | no llamar / `use_tools=False` | tools off | mantener default |
| Langfuse / Sentry | env vacíos | off | off |
| MCP público | no usar como nativo | — | solo availability check |

---

## 5. Qué NO cruza a “reproducción nativa”

| Acción | Clasificación |
|---|---|
| Llamar `https://chat.expasy.org/mcp` | `external_service_availability_check` |
| Benchmark biodata completo | online pesado; aplazado; no Prompt 9/10 smoke mínimo |
| Declarar PE3 tras 1 pregunta | **prohibido** |

---

## 6. Diagrama textual de fronteras

```text
[CORE_OFFLINE smoke_only]
        |
        |  (Prompt 9: solo documentación)
        v
[Prompt 10: entorno + índice mínimo — sin LLM]
        |
        |  (tras CONDITIONAL_GO → GO de presupuesto)
        v
[LOCAL_CHAT_API_ONE_QUESTION]
   - OpenRouter: SÍ (1 pregunta)
   - SPARQL agent-exec: NO (flag false)
   - MCP público: NO como nativo
```

---

## 7. Implicación para el gate

Mientras B1–B7 de `API_SIB_PROTOCOL.md` §23 no estén cerrados, el gate permanece **CONDITIONAL_GO**. Cruzar a ejecución LLM sin índice/runtime/clave/presupuesto constituye **NO-GO** operativo.

# Protocolo documental de benchmarks SIB — SPARQL-LLM

**Commit pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Estado Prompt 9:** solo documentación — **prohibida** la ejecución de benchmarks, llamadas LLM, endpoints SPARQL y builds de índice.

---

## 1. Mapa de scripts

| Script | Rol | Evidencia |
|---|---|---|
| `tests/benchmark.py` | Evaluación manual hand-curated | `CODE_VERIFIED` |
| `tests/benchmark_biodata.py` | Evaluación biodata KFold + pytrec | `CODE_VERIFIED` |
| `tests/text2sparql/*` | Pipeline TEXT2SPARQL / Virtuoso | bloqueado localmente (registry) |

---

## 2. Benchmark manual (`benchmark.py`)

### 2.1 Datos

- Lista Python `example_queries`: pares pregunta / endpoint / query SPARQL de referencia (`CODE_VERIFIED`).  
- No es un split formal train/test; es suite curada.

### 2.2 Ejecución observada en código

- Usa `load_chat_model` y/o `httpx` hacia `http://localhost:8000/chat` (`CODE_VERIFIED`).  
- Logging a `data/benchmarks/` con prefijo temporal (`CODE_VERIFIED`).  
- Puede invocar `query_sparql` / extracción de queries (`CODE_VERIFIED` imports).

### 2.3 Implicaciones de red

Online: LLM + opcionalmente Chat API local + endpoints SPARQL. **Fuera de alcance** del smoke `LOCAL_CHAT_API_ONE_QUESTION`.

---

## 3. Benchmark biodata (`benchmark_biodata.py`)

### 3.1 Endpoints de evaluación

```text
https://sparql.uniprot.org/sparql
https://www.bgee.org/sparql/
https://sparql.cellosaurus.org/sparql
```

(`CODE_VERIFIED`)

### 3.2 Split

- `KFold(n_splits=3, shuffle=True, random_state=42)` (`CODE_VERIFIED`).  
- `LIMIT_FOR_DEV = None` (sin reducción; comentario permite 4 en dev) (`CODE_VERIFIED`).

### 3.3 Modelos listados

- `openrouter/openai/gpt-4o-mini`  
- `openrouter/openai/gpt-oss-120b`  
- `openrouter/openai/gpt-5`  

(`CODE_VERIFIED`)

### 3.4 Interacción con Chat API

POST `http://localhost:8000/chat` con:

- `validate_output: True`  
- `enable_sparql_execution: False`  

(`CODE_VERIFIED`)

Después, el script ejecuta el SPARQL generado **por separado** y compara con referencias.

### 3.5 Métricas

- `pytrec_eval` con `set_P`, `set_recall`, `set_F` (`CODE_VERIFIED`).  
- Cache de referencias: `data/biodata_ref_results_cache.json` (`CODE_VERIFIED`).  
- Colección vectorial referenciada: `expasy` (`CODE_VERIFIED`).

### 3.6 Por qué no es el smoke futuro inmediato

Coste multi-modelo × 3 folds × endpoints; red SPARQL intensa; no acotado a `MAX_QUESTIONS=1`. Rol: **L2** aplazado tras evidencia PE2 mínima.

---

## 4. Tres niveles de evaluación (protocolo lab)

| Nivel | Nombre | Alcance | Estado |
|---|---|---|---|
| **L0** | Smoke Chat API 1 pregunta | `LOCAL_CHAT_API_ONE_QUESTION`; `enable_sparql_execution=false`; sin métricas paper | **seleccionado** (futuro; gate CONDITIONAL_GO) |
| **L1** | Manual reducido | Subconjunto de `example_queries` tras L0 estable | documental / aplazado |
| **L2** | Biodata KFold + pytrec | Script completo biodata | documental / aplazado; no PE3 automático |

L0 **no** reproduce tablas del paper. L2 es el camino más cercano a evidencia de métricas SIB, pero requiere presupuesto y entorno mayores.

---

## 5. Criterios de éxito/fallo por nivel (propuestos)

### L0 (`PROPOSED`)

- Éxito: 1 respuesta Chat API no vacía sobre código pin; sin SPARQL agent-exec; logs experimentales.  
- Fallo: >1 pregunta LLM; init descontrolado; uso de MCP público como nativo.

### L1 (`PROPOSED`)

- Éxito: N≤presupuesto preguntas manuales con registro comparable; mismos flags de red.  
- Fallo: drift de modelo/settings no documentado.

### L2 (`PROPOSED`)

- Éxito: corrida biodata con seed 42 y métricas pytrec archivadas + deviations.  
- Fallo: cache/ref ausente sin política; gasto multi-modelo no aprobado.

---

## 6. Relación con PE1–PE4

| Pregunta | Relación |
|---|---|
| PE2 | L0 aporta evidencia parcial de ejecutabilidad online controlada |
| PE3 | Ningún nivel en Prompt 9; L2 futuro tampoco declara PE3 sin comparación paper explícita |
| PE4 | Matrices de red/barreras de este protocolo |

---

## 7. Stop conditions específicas de benchmarks

- No ejecutar `benchmark.py` ni `benchmark_biodata.py` en Prompt 9.  
- No descargar ni refrescar `biodata_ref_results_cache.json` aquí.  
- No presentar métricas README/paper como `EXECUTION_VERIFIED` del lab.

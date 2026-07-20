# Auditoría de recuperación y prompt — CoT-SPARQL

**Fecha:** 2026-07-20  
**Etiquetas:** `CODE_VERIFIED` | `README_REPORTED` | `DATA_VERIFIED` | `EXTERNAL_ARTIFACT_REFERENCED` | `NOT_FOUND` | `INFERENCE`

---

## Recuperación (Context B)

| Aspecto | Valor | Evidencia |
|---|---|---|
| Encoder | `SentenceTransformer('all-MiniLM-L6-v2')` cargado **al import** | `contextb.py` L9 `CODE_VERIFIED` |
| Métrica | `cosine_similarity` + `np.argmax` | L41–43 `CODE_VERIFIED` |
| k efectivo | **1** (one-shot / nearest neighbor) | L43–48 `CODE_VERIFIED` |
| Relación con `--top_k` CLI | **ninguna** — `top_k` es sampling del LLM | `main.py` L20, L86 vs retrieval |
| Artefactos DBpedia | `temp/embeddings_dbpedia.pkl` + `temp/dbpedia_examples.parquet` | L20–22; **NOT_FOUND** en repo |
| Artefactos Wikidata | `temp/embeddings_wikidata.pkl` + `temp/wikidata_examples.parquet` | L26–28; **NOT_FOUND** |
| URL descarga | README wget vía `anon.to` → `files.dice-research.org/.../COT-SPARQLGEN/` | `README_REPORTED` / `EXTERNAL_ARTIFACT_REFERENCED` |
| Columnas parquet | `question`, `query`, `entities`, `relations` | L44–47 `CODE_VERIFIED` |

Formato del ejemplo inyectado (`CODE_VERIFIED` L24/L30):

```
[question]: … 
[Entities]: …
[Relations]:…
[SPARQL]: …
```

### Procedencia del contenido gold en el ejemplo

| KB | Fuente notebook | Anotaciones | Evidencia |
|---|---|---|---|
| Wikidata | `train_lcquad2` → `new_LabelsEnt` / `newPredLabels` / `sparql_wikidata` → `wikidata_examples.parquet` | **gold train** | `temp/embeddings.ipynb` cells 3,6,7 `CODE_VERIFIED` |
| DBpedia | `concat(train_qald, train_vquanda)` con `entities`/`relations` gold | **gold train** | cells 9–14 `CODE_VERIFIED`; escritura parquet/pkl DBpedia **no** en notebook restante → `INFERENCE` que el artefacto descargado sigue ese diseño + `contextb` lo espera |

**Implicación:** el “one-shot” filtra un ejemplo **con anotaciones gold del train**, no predicciones EL/RL del mismo stack que Context A (`INFERENCE` / `CODE_VERIFIED` contraste).

---

## Construcción del prompt (Context A + CoT)

`main.py` `prompt_building` L32–45 (`CODE_VERIFIED`):

1. Bloque `[INST]` con tarea “convert question to SPARQL” para `kb`.  
2. Texto CoT explícito: **“Let's think step by step”**.  
3. Inyecta **un** ejemplo vía `cb.example_generation(kb, question)` entre `<examples>…</examples>`.  
4. Cierra `[/INST]`.  
5. Concatena `\n [question]:` + question + `\n [Entities] :` + `ca.entity_linking` + `\n[Relations]:` + `ca.relation_extraction`.

No hay plantillas externas en disco: el prompt vive **en código** (`METHOD_REGISTRY` / `CODE_VERIFIED`).

---

## Generación

| Parámetro | Default | Rol | Evidencia |
|---|---|---|---|
| `temperature` | 0.1 | sampling | `main.py` L21, L87 |
| `max_length` | 700 | longitud generación | L22, L88 |
| `repetition_penalty` | 1.1 | | L23, L89 |
| `top_k` | 10 | **nucleus/top-k sampling**, no retrieval | L20, L86 |
| `num_return_sequences` | 1 | una hipótesis | L24, L90 |
| Postproceso | `split('[/INST]')[1]` | toma continuación | L61 |

Si validación falla: mensaje “try again” — **sin** repair loop, **sin** re-sample, **sin** ranking multi-candidato (`main.py` L96–100 `CODE_VERIFIED`).

---

## Riesgos de retrieval/prompt

- Sin parquet/pkl → crash inmediato al abrir archivos (`NOT_FOUND`).  
- Import de `contextb` fuerza MiniLM (+ red/HF) incluso antes de CLI útil.  
- Ejemplo gold + EL/RL runtime pueden **divergir** en formato/calidad (`INFERENCE`).  
- Notebook incompleto para export DBpedia (sin `to_parquet`/`pickle` dbpedia en celdas finales) — reproducir embeddings propios requiere completar notebook (`CODE_VERIFIED` gap).

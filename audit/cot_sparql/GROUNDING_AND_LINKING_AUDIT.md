# Auditoría de grounding / linking — CoT-SPARQL

**Fecha:** 2026-07-20  
**Etiquetas:** `CODE_VERIFIED` | `EXTERNAL_ARTIFACT_REFERENCED` | `INFERENCE` | `UNKNOWN`

---

## Entity linking (`contexta.entity_linking`)

| KB | Mecanismo | Salida | Evidencia |
|---|---|---|---|
| `dbpedia` | `spacy.load('en_core_web_lg')` + pipe `dbpedia_spotlight` | `(text, kb_id_)` por ent | L13–18 `CODE_VERIFIED` |
| otro / `wikidata` | mismo `en_core_web_lg` + pipe `entityfishing` | `text: wd:{kb_qid}` | L19–23 `CODE_VERIFIED` |

Notas:

- Carga spaCy **por llamada** a `entity_linking` (coste repetido) (`CODE_VERIFIED`).  
- Depende de servicios Spotlight / Entity-Fishing en red (`EXTERNAL_ARTIFACT_REFERENCED`).  
- **Sin timeout** explícito en estas pipes (`CODE_VERIFIED` ausencia).

---

## Relation extraction (`contexta.relation_extraction`)

### DBpedia — Falcon API

1. `POST https://labs.tib.eu/falcon/api?mode=long` con `{"text": ...}` (`L79–98`).  
2. Si status ≠ 200 o excepción → retorna **`None`**.  
3. Caller: `format_output(query_falcon_api(question)['relations'])` (`L33`).  

**Anomalía:** si API falla, `None['relations']` → **TypeError** (`CODE_VERIFIED`).  
**Anomalía:** **sin timeout** en `requests.post` (`CODE_VERIFIED`).  
`format_output` mapea `surfaceform` → `URI` (`L100–106`).

### Wikidata — REBEL + lookup SPARQL

1. Carga `en_core_web_lg` + pipe `rebel` (`Babelscape/rebel-large`, `device:0`) (`L36–38`).  
2. Por cada relación en `doc._.rel`, llama `execute_sparql_query(rel_dict['relation'])` (`L39–41`).  
3. SPARQL selecciona `?item ?itemLabel` filtrando `rdfs:label` (`L50–59`).  
4. Pero el código lee `result['propertyLabel']['value']` (`L73–74`).  

**Anomalía CODE_VERIFIED:** claves SPARQL (`item`/`itemLabel`) ≠ clave leída (`propertyLabel`) → IDs de relación **probablemente vacíos/rotos**.  
Además, el literal `label` se concatena sin comillas SPARQL consistentes (línea comentada `#label = f'"{label}"'`) → riesgo de query inválida (`CODE_VERIFIED` / `INFERENCE`).  
**Sin timeout** en `requests.get` a Wikidata (`L69`).

Componente REBEL: `spacy_component.py` factory `rebel` + `pipeline("text2text-generation")` (`CODE_VERIFIED`).

---

## Ontología / schema

| Pregunta | Respuesta | Evidencia |
|---|---|---|
| ¿Carga OWL / TBox? | No | `NOT_FOUND` / `CODE_VERIFIED` |
| ¿Domain-range checks? | No | `CODE_VERIFIED` |
| ¿KG en generación LLM? | Solo vía strings EL/RL en prompt | `CODE_VERIFIED` |
| ¿Validación semántica? | No — solo HTTP 200 | `validation.py` |

---

## Matriz

Ver `GROUNDING_COMPONENT_MATRIX.csv`.

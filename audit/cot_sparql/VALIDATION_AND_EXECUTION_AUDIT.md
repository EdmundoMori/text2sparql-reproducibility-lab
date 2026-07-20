# Validación y ejecución SPARQL — CoT-SPARQL

**Fecha:** 2026-07-20  
**Etiquetas:** `CODE_VERIFIED` | `INFERENCE` | `NOT_FOUND`

---

## Extracción del string SPARQL (`formate_output`)

| Caso | Comportamiento | Evidencia |
|---|---|---|
| Contiene ` ``` ` | `split('```')[1]` | `validation.py` L19–20 |
| Contiene `[sparql]:` | `split('[sparql]:')[1]` | L21–22 |
| Ninguno | `'no sparql'` | L23–24 |

No usa parser SPARQL local (`rdflib` está en deps pero **no** en `validation.py`) (`CODE_VERIFIED` / `NOT_FOUND` uso).

---

## `check_sparql_query_validity`

1. Endpoints: Wikidata `https://query.wikidata.org/sparql` o DBpedia `https://dbpedia.org/sparql` (`L43–46`).  
2. `requests.get(url, params={'query': query}, headers=…)` **sin timeout** (`L60`).  
3. Si `status_code == 200` → `(True, "The SPARQL query is syntactically valid.")` (`L63–64`).  
4. En caso contrario → mensaje de error con `response.text` (`L65–66`).

### Limitaciones `CODE_VERIFIED`

| Limitación | Detalle |
|---|---|
| No es parse sintáctico local | Confía en HTTP del endpoint |
| Resultado vacío + 200 | Sigue “válido” |
| Sin distinción ASK/SELECT/CONSTRUCT | Ningún chequeo de forma |
| Sin repair | `main` solo imprime “try again” |
| Sin ranking multi-hipótesis | `num_return_sequences=1` default |
| Red obligatoria | Offline → fallará |

`validate_sparql` solo llama al checker si `output != 'no sparql'`; si es `'no sparql'`, `is_valid` permanece **True** por defecto (`L7–16`) — **anomalía**: ausencia de SPARQL extraíble se trata como válido (`CODE_VERIFIED`).

---

## Ejecución de respuestas / Answer F1

**NOT_FOUND** en código: no hay comparación de bindings, GERBIL client, ni métricas F1-QALD implementadas. Solo claim paper (`PAPER_REPORTED` vía mapping).

# Anomalías y riesgos — CoT-SPARQL

**Fecha:** 2026-07-20  
**Etiquetas:** `CODE_VERIFIED` | `README_REPORTED` | `INFERENCE` | `NOT_FOUND`

---

## Anomalías CODE_VERIFIED (prioridad)

| ID | Ubicación | Descripción | Impacto |
|---|---|---|---|
| A1 | `main.py` L106 | Assert question: falta coma → concat de strings; vacío **pasa** | CLI no rechaza pregunta vacía |
| A2 | `main.py` L105 | Typo `provde` en mensaje assert kb | Cosmético |
| A3 | `contexta.py` L33+L89–95 | Falcon retorna `None` → `None['relations']` | Crash DBpedia RL |
| A4 | `contexta.py` L54–74 | SPARQL pide `?item`/`?itemLabel` pero lee `propertyLabel` | RL Wikidata vacío/roto |
| A5 | `validation.py` L7–16 | `is_valid=True` por defecto; `'no sparql'` no invalida | Falso positivo de validez |
| A6 | `validation.py` L63–64 | HTTP 200 ⇒ “syntactically valid” | No es parse local; vacío OK |
| A7 | `contextb.py` L9 | MiniLM load at import | Side-effect red/HF al importar |
| A8 | `main.py` L3, L12 | `Accelerator` unused; `filterwarnings("ignore")` | Ruido / dead code |
| A9 | requests Falcon/Wikidata/validation | Sin `timeout=` | Cuelgues indefinidos |
| A10 | `requirements.txt` vs README | Export Conda; README dice pip | Install path engañoso |
| A11 | `temp/` embeddings | Referenciados; gitignored; **NOT_FOUND** | Bloquea retrieval |
| A12 | `embeddings.ipynb` | Construye Wikidata parquet/pkl; **no** escribe artefactos DBpedia | Gap reproducir embeddings propios |
| A13 | `num_return_sequences=1` + no repair | Invalid → solo mensaje | Sin búsqueda automática |
| A14 | `--top_k` naming | Sampling ≠ retrieval k | Confusión operativa |

---

## Riesgos lab / legales / hardware

| Riesgo | Clase | Nota |
|---|---|---|
| `LICENSE_NOT_CONFIRMED` | legal | `common_adapter_allowed: false`; no adaptar |
| CodeLlama-34B GPTQ en 6 GiB | hardware | `model_smoke` / native **blocked** |
| APIs EL/RL de terceros | disponibilidad | Spotlight, Entity-Fishing, Falcon, endpoints KG |
| `trust_remote_code=True` | seguridad | carga código remoto HF |
| Divergencia gold example vs EL/RL runtime | metodológica | few-shot gold vs linking live |

---

## Lo que NO es anomalía de código pero sí gap

- Ausencia total de eval harness / predicciones (`NOT_FOUND`) — gap de reproducibilidad paper.  
- Solo trains en `dataset/` — no permite re-correr tablas test sin datos externos (`NOT_FOUND`).

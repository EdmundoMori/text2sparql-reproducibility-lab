# STATIC_CODE_HEALTH — firesparql

**Fecha:** 2026-07-20  
**Restricción:** parse AST / lectura estática; **sin** import `torch`/`pandas`/`chromadb` del proyecto.

---

## AST / sintaxis

Muestra en `logs/static-audit-firesparql/ast_health.json`: todos los `.py` de `codes/` y `experiment_datasets/codes/` marcados `"ok": true` (`CODE_VERIFIED` via ast).

| Archivo | Líneas (aprox.) | Imports notables |
|---|---|---|
| `generate_sparql_cuda.py` | 77 | torch, transformers, pandas |
| `generate_sparql_mps.py` | 84 | idem; `device_map={"": "cpu"}` |
| `generate_sparql_one_shot_cuda.py` | 102 | idem |
| `generate_sparql_rag_cuda.py` | 160 | + re (`<think>` strip) |
| `generate_sparql_rag_mps.py` | 163 | idem |
| `generate_context_rag.py` | 147 | chromadb, llama_index, groq |
| `sparql-cleaning-llm.py` | 203 | openai, dotenv (código legacy comentado arriba) |
| `bleu_rouge.py` | 106 | nltk, rouge, pandas, dotenv |
| `exact_match.py` | 64 | pandas, argparse |
| `accumulate_exact_match.py` | 32 | stdlib only; paths hardcodeados |
| `one_shot_mapping.py` | 51 | sentence_transformers, sklearn |
| `SciQA-training-transformation.py` | 30 | json |
| `dblp-training-transformation.py` | 30 | json |

---

## Hallazgos de salud (estáticos)

| Hallazgo | Severidad | Evidencia |
|---|---|---|
| Paths absolutos macOS `/Users/sherrypan/...` | alta p/repro | `one_shot_mapping.py`, notebooks |
| Paths runtime `xueli_data/...` ≠ layout `experiment_datasets/` | alta | generate_*, bleu_rouge, RAG |
| `merge_models/` ausente | bloqueante FT infer local | `run_all_generate.sh` |
| `temperature=0.7` sin `do_sample=True` explícito | media | HF puede warn/ignorar sampling (`CODE_VERIFIED`; comportamiento exacto `UNKNOWN` sin ejecución) |
| `accumulate_exact_match.py` hardcodea carpeta/epochs | media | no CLI genérica |
| `sparql-cleaning-llm.py` duplica bloque legacy comentado | baja | ruido mantenimiento |
| Sin `requirements.txt` / pins | alta | `NOT_FOUND` |
| Shells orientados a cluster Snellius | media | `run_all_*.sh` |
| Notebooks con outputs embebidos (`ploting.ipynb`) | baja | métricas hardcodeadas en celdas |

---

## Código de ejecución SPARQL

**`CODE_NOT_FOUND`:** no hay runner QLever/ORKG en `codes/`. Solo artefactos bajo `results/step3_sparql_running_against_orkg/`.

---

## Veredicto salud

El código de **inferencia / cleaning / métricas léxicas** es pequeño, legible y parseable. La salud de **reproducción** es mala por paths, secretos API, pesos ausentes y trainer ausente — no por sintaxis rota.

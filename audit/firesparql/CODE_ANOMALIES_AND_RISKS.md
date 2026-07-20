# CODE_ANOMALIES_AND_RISKS — firesparql

**Fecha:** 2026-07-20

---

## Anomalías / mismatches

| ID | Descripción | Evidencia |
|---|---|---|
| A1 | README “Under Review” vs paper IC3K 2025 publicado DOI | `README_REPORTED` vs `PAPER_REPORTED`/`PIN` |
| A2 | README step3 `against_qlever` vs dir `against_orkg` | `MISMATCH` |
| A3 | README step4 `…_success_metrics` vs `…_success_sparql` | `MISMATCH` |
| A4 | Claim QLever sin runner en código | `README_REPORTED` + `CODE_NOT_FOUND` |
| A5 | Requirements “Coming soon” + sin env files | `NOT_FOUND` |
| A6 | LICENSE ausente; MIT solo HF model card | `LICENSE_NOT_CONFIRMED` |
| A7 | Trainer ausente; paths LLaMa-Factory | `NOT_FOUND` + `CODE_VERIFIED` |
| A8 | `merge_models/` referenciado y ABSENT | `CODE_VERIFIED`/`NOT_FOUND` |
| A9 | `xueli_data` vs `experiment_datasets` | layout mismatch |
| A10 | `generate_sparql_mps.py` usa CPU map | nombre engañoso |
| A11 | `temperature=0.7` sin `do_sample` explícito | riesgo sampling HF |
| A12 | Cleaning gpt-4o = posible reparación semántica | prompt `CODE_VERIFIED` |
| A13 | `sparql_results.csv` solo 23/65 | completitud parcial |
| A14 | One-shot rounds con summaries numéricos idénticos en sample | posible copia artefactos (`RESULT_FILE_VERIFIED` observación) |
| A15 | `accumulate_exact_match.py` hardcodeado; RelaxedEM no calculado en script | `CODE_VERIFIED` |
| A16 | RAG sample 20 props = slice lista, no top-k sobre 9062 | `CODE_VERIFIED` |
| A17 | ft_rag dirs vacíos / incompletos (0 o 440 txt) | `RESULT_FILE_VERIFIED` |

---

## Riesgos de ejecución

- OOM 8B en 6 GiB; quant rompe fidelidad paper.  
- Coste/no-determinismo OpenAI + Groq.  
- Endpoint ORKG drift temporal vs results congelados.  
- Riesgo legal adapters sin LICENSE repo.  
- Re-entrenamiento no documentado → resultados FT no regenerables nativamente.

---

## Lo que **no** es anomalía

Presencia masiva de `results/` es diseño del repo (artefactos paper), no corrupción — pero **no** sustituye reproducción.

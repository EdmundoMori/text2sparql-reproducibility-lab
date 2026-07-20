# RESULT_PROVENANCE_AND_COMPLETENESS — firesparql

**Fecha:** 2026-07-20  
**Inventario config-level:** `RESULTS_INVENTORY.csv` (69 filas unión step1∪step3; **65** summaries; **23** `sparql_results`).

---

## Completitud por etapa

| Etapa | Completitud | Evidencia |
|---|---|---|
| step1 | ~60 configs; mayoría 513 txt; ft_rag irregular (0/440/513) | `RESULT_FILE_VERIFIED` / `step1_configs.json` |
| step2 | alineado a step1 en familias principales + CSVs BLEU/ROUGE | `RESULT_FILE_VERIFIED` |
| step3 summaries | 65 | `RESULT_FILE_VERIFIED` |
| step3 results CSV | **23** solo (one_shot, vanilla_rag, subset ft_rag incl. nested `prompt2/`) | `RESULT_FILE_VERIFIED` |
| step4 | success_ids por familia (ft 36, etc.); nombre dir ≠ metrics | `RESULT_FILE_VERIFIED` |
| step5 | 2 CSV error analysis | `RESULT_FILE_VERIFIED` |
| context_from_rag | varios modelos/prompts | `RESULT_FILE_VERIFIED` |

---

## Provenance

- Resultados = **artefactos versionados de corridas autores** (Snellius shells, paths Sherry), **no** prueba de reproducibilidad local (`INFERENCE`).  
- One-shot: tres rounds comparten a veces la misma fila summary numérica en inventario (posible copia/`RESULT` anomaly) — ver `CODE_ANOMALIES_AND_RISKS.md`.  
- FT: summaries de ejecución presentes sin `sparql_results` → EM no recomputable desde CSV faltante.

---

## Relación con paper

Tabla README (FT 15ep, one-shot, zero-shot) es **`PAPER_REPORTED`/`README_REPORTED`**. Los CSV locales de BLEU/ROUGE/EM permiten auditoría de **consistencia aproximada** en smokes futuros, pero esta pasada **no** recompute ni valida igualdad numérica exacta con la tabla.

**Versioned results ≠ local reproduction.**

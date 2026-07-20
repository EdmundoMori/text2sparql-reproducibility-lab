# EXECUTION_AND_QLEVER_AUDIT — firesparql

**Fecha:** 2026-07-20  
**Veredicto:** `QLEVER_EXECUTION = blocked` — **`CODE_NOT_FOUND`** para runner QLever/ORKG. **No se inventa** código de ejecución.

---

## README vs árbol

| Claim | Realidad | Evidencia |
|---|---|---|
| “Using Qlever for sparql execution” | sin script QLever | `README_REPORTED` vs `CODE_NOT_FOUND` |
| README tree: `step3_sparql_running_against_qlever/` | dir real: `results/step3_sparql_running_against_orkg/` | `MISMATCH` `RESULT_FILE_VERIFIED` |

---

## Artefactos de ejecución presentes

- **65** `sparql_summary.csv` (`RESULT_FILE_VERIFIED`).  
- **23** `sparql_results.csv` (parcial; incl. anidados `ft_rag/prompt2/...`) (`RESULT_FILE_VERIFIED`).  

Campos summary (`CODE_VERIFIED` header):

`model,total_queries,success_count,fail_count,null_count,success_percentage,fail_percentage,null_percentage`

---

## Evaluación post-ejecución (sí hay código)

`codes/exact_match.py`: compara sets parseados de `message` vs `gt_message` en filas `status==SUCCESS`; escribe `success_ids_{model}.txt` y resume EM (`CODE_VERIFIED`).

Sin `sparql_results.csv` no se puede recomputar EM para esa config — mayoría FT solo tienen summary (`RESULT_FILE_VERIFIED`).

---

## Readiness

| Capacidad | Estado |
|---|---|
| Releer summaries existentes | possible (`RESULTS_RECOMPUTATION_SMOKE` conditional) |
| Re-ejecutar queries contra endpoint | **blocked** (sin runner + endpoint/config `UNKNOWN`) |
| Afirmar motor = QLever | **no** — solo claim README |

UNKNOWNs: URL endpoint, autenticación, timeouts, si ORKG live ≠ snapshot paper.

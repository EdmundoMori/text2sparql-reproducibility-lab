# ANSWER_METRIC_CONTRACT

**Primary:** Answer Precision / Recall / F1 · aggregation: **macro per item**

P = predicted canonical row set · G = gold canonical row set · TP = |P ∩ G|

- Precision = TP/|P| if |P|>0
- Recall = TP/|G| if |G|>0
- F1 = harmonic mean if P+R>0

## Casos especiales
| Caso | P | R | F1 | Exact |
|---|---|---|---|---|
| A valid empty / valid empty | 1 | 1 | 1 | 1 |
| B valid empty / nonempty G | 0 | 0 | 0 | 0 |
| C nonempty P / empty G | 0 | 0 | 0 | 0 |
| D NO_OUTPUT / TIMEOUT / INVALID / EXEC_ERROR / ABSTENTION | 0 | 0 | 0 | 0 |

Fallos ≠ conjunto vacío válido. Solo `final_sparql` cuenta. Diagnostics: micro P/R/F1, median F1, exact count, N/D.

# METRICS_AUDIT — firesparql

**Fecha:** 2026-07-20

---

## BLEU / ROUGE — `codes/bleu_rouge.py`

| Aspecto | Detalle | Evidencia |
|---|---|---|
| Métricas | BLEU-4 (NLTK), ROUGE-1/2/L (`rouge` pkg) | `CODE_VERIFIED` |
| Hipótesis | texto cleaned generado | `CODE_VERIFIED` |
| Referencia | gold `query` en `xueli_data/.../test_questions.csv` | `CODE_VERIFIED` |
| Artefactos | `results/step2_clean_sparql/bleu_rouge_results_{ft,ft_rag,one_shot,vanilla,vanilla_rag}.csv` | `RESULT_FILE_VERIFIED` |

Header ejemplo FT: `BLEU-4,ROUGE-1,ROUGE-2,ROUGE-L,Model,Epoch,Round,Folder`.

---

## Exact match ejecución — `codes/exact_match.py`

Compara multisets/tuples de celdas TSV en `message` vs `gt_message` tras éxito HTTP/status `SUCCESS`. Emite EM sobre success y over-all (`CODE_VERIFIED`).

Summaries agregados: `results/step3_.../exact_match_summary_{ft,ft_rag,oneshot,vanilla,vanilla_rag}.csv` (`RESULT_FILE_VERIFIED`).

---

## RelaxedEM — `accumulate_exact_match.py`

Une IDs de éxito de **3 rounds** en un `set` y hace `print(len(unique_ids))` (`CODE_VERIFIED`).  
**INFERENCE** lab: RelaxedEM ≈ `|unión éxitos| / 513`. El script **no** divide ni escribe métrica nombrada; paths hardcodeados a un experimento ft_rag 20ep.

`ploting.ipynb` hardcodea series métricas (`CODE_VERIFIED` notebook).

---

## Tabla paper (no re-verificada aquí)

FT 8B 15ep: BLEU 0.77, R1 0.91, R2 0.86, RL 0.90, RelaxedEM 0.85; one-shot; zero-shot (`PAPER_REPORTED`/`README_REPORTED`).

---

## Readiness métricas

| Capacidad | Estado |
|---|---|
| `METRICS_OFFLINE_SMOKE` | **conditional** — necesita pandas/nltk/rouge + path fixes; adapters legalmente bloqueados |
| `RESULTS_RECOMPUTATION_SMOKE` | **conditional** — solo donde existen CSVs (`sparql_results` parcial) |

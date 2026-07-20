# Inventario de checkpoints y resultados — SGPT

**Fecha:** 2026-07-20  
**Commit:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` (`PIN`)

---

## Checkpoints

| Artefacto esperado | Estado en clon | Evidencia |
|---|---|---|
| `runs/sgpt/{dataset}/` (README eval) | **ausente** | `NOT_FOUND` / `REPO` |
| `checkpoint-{global_step}/` por época | **ausente** | `NOT_FOUND` |
| `pytorch_model.bin` / safetensors | **ausente** | `NOT_FOUND` |
| `training_args.bin` | **ausente** | `NOT_FOUND` |
| Tokenizer files (`vocab.json`, `merges.txt`, `tokenizer.json`) | **ausente** (se descargan de HF `gpt2` al entrenar) | `NOT_FOUND` + `CODE_VERIFIED` train path |

**Impacto:** inferencia / eval con `--generate` **bloqueada** hasta entrenar o aportar pesos externos. Etiqueta de readiness: `inference_with_checkpoint = blocked`.

---

## Resultados de evaluación en repo

| Artefacto | Estado | Evidencia |
|---|---|---|
| `outputs/` / `outputs/predictions_*.json` | **ausente** | `NOT_FOUND` |
| `eval_results.txt` | **ausente** | `NOT_FOUND` |
| TensorBoard / `events.out.tfevents*` | **ausente** | `NOT_FOUND` |
| Tablas paper (BLEU/F1/SP-*) | solo en paper / lab matrix | `PAPER_REPORTED` → `audit/RESULT_EVIDENCE_MATRIX.csv` |

---

## Resultados paper (no reproducidos aquí)

Valores Table 4 SGPT_* están catalogados como **Reported only** en `audit/RESULT_EVIDENCE_MATRIX.csv` y mapeados a flags CLI en `PAPER_TABLE4_CODE_MAPPING.csv`. Esta auditoría estática **no** re-ejecuta métricas.

---

## Criterio de selección de checkpoint (código)

`CODE_VERIFIED` (`train.py`):

- Guarda checkpoint **cada época** (`checkpoint-{global_step}`).
- Guarda modelo final bajo `runs/sgpt/{dataset}/`.
- `global_eval` se asigna pero **no** se compara para retención “best-only”.
- Criterio de selección para Table 4: **UNKNOWN** / unclear en código.

---

## Conclusión

Sin pesos ni predicciones en el árbol: cualquier camino de smoke de inferencia queda **blocked**; la evidencia cuantitativa del paper permanece `PAPER_REPORTED` únicamente.

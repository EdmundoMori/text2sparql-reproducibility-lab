# Auditoría de métricas — SGPT

**Fecha:** 2026-07-20  
**Fuente:** `eval.py`, `utils/metrics.py` (`CODE_VERIFIED`)  
**Commit:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` (`PIN`)

---

## Qué se mide

Solo métricas **léxicas** sobre strings SPARQL predichos vs gold:

| Métrica | Notas | Evidencia |
|---|---|---|
| BLEU | n-gram overlap | `CODE_VERIFIED` |
| Unigram P / R | precisión/recall unigrama | `CODE_VERIFIED` |
| SP-BLEU / SP-* | con normalización de variables | `CODE_VERIFIED` |
| METEOR | | `CODE_VERIFIED` |
| ROUGE | | `CODE_VERIFIED` |
| F1 / SP-F1 | derivados de P/R | `CODE_VERIFIED` |

**No** hay:

- ejecución SPARQL contra KG,
- Answer F1 / accuracy de respuestas,
- Exact Match almacenado como métrica primaria en el `result` dict.

Table 4 del paper reporta BLEU / F1 / SP-BLEU / SP-F1 como léxicas (`PAPER_REPORTED`).

---

## Anomalías (`CODE_VERIFIED`)

| ID | Hallazgo | Impacto |
|---|---|---|
| A1 | Cada `metric.update` se llama **dos veces** por ejemplo (`eval.py` ~L143–149) | Métricas no-SP **doble-cuentan** el mismo par |
| A2 | En path SP: primera update **raw**, segunda **normalizada** (variables) | SP-* mezclan señales; no es “solo normalizado” |
| A3 | Clases `BLEU` y `SPBLEU` **idénticas**; distinción solo por inputs | Naming engañoso |
| A4 | F1 y SP-F1 se **imprimen** pero **no** se insertan en el `result` dict | Artefacto JSON incompleto vs consola |
| A5 | Si `pre + rec == 0`, riesgo de **división por cero** en F1 | Crash / NaN potencial |

Cualquier smoke futuro de eval debe documentar A1–A5; no asumir paridad numérica directa con Table 4 sin control de estas rutas.

---

## Relación con Table 4

Valores paper → `audit/RESULT_EVIDENCE_MATRIX.csv` y `PAPER_TABLE4_CODE_MAPPING.csv`.  
Estado: **PAPER_REPORTED only** — no reproducidos en esta pasada estática.

# CODE_TEMPORAL_ANCHOR — SGPT
**RUN_ID:** `20260721T113310Z`
**Evidencia:** GitHub API (`OFFICIAL_METADATA_VERIFIED`)

| Archivo | Fecha (más reciente en muestra) | SHA corto | Mensaje |
|---|---|---|---|
| `requirements.txt` | 2022-12-28T17:04:09Z | 44d757ea | added files |
| `train.py` | 2023-10-14T18:07:07Z | ae797dff | :bug: bugfix training epoch from config file |
| `eval.py` | 2022-12-28T17:04:09Z | 44d757ea | added files |
| `scripts/model.py` | 2022-12-28T17:04:09Z | 44d757ea | added files |
| `utils/metrics.py` | 2023-10-14T18:10:26Z | f4727ed4 | :bug: bugfix: error in evaluation metric meteor |
| `README.md` | 2024-09-15T09:21:37Z | 1f6964d1 | Update README.md |

## Conclusiones

- `requirements.txt` con `torch==1.13.1` aparece en historial el **2022-12-28**.
- El pin del laboratorio (`1f6964d1…`) es posterior y **no** demuestra refresh del stack de dependencias.
- Paper 2022; seleccionar Transformers de la misma ventana temporal.

**Etiqueta:** `TEMPORAL_ANCHOR_VERIFIED` (ventana 2022-12) con incertidumbre residual en el primer commit absoluto → no `UNKNOWN` total.

# TRANSFORMERS_PIN_DECISION

**RUN_ID:** `20260721T113310Z`

## Selección

| Campo | Valor |
|---|---|
| **SELECTED_CANDIDATE_UNTESTED** | `transformers==4.25.1` |
| Upload PyPI | 2022-12-01T21:17:38Z |
| Requires-Python | `>=3.7.0` |
| Tag fuente | `v4.25.1` |
| Runner-up | `4.26.1` |
| Símbolos requeridos | **todos presentes** en fuente etiquetada (incl. reexport `modeling_utils` → `pytorch_utils` para Conv1D/prune) |
| Runtime | **no** verificado |

## Justificación

1. Ventana temporal alineada con torch 1.13.1 y `requirements.txt` (2022-12).  
2. Conserva `AdamW` exportable desde `transformers`.  
3. Conserva imports SGPT `from transformers.modeling_utils import Conv1D, …`.  
4. No se eligió la versión más nueva a propósito.

## No afirmado

- compatibilidad runtime con torch 1.13.1  
- equivalencia paper  

**Etiquetas:** `OFFICIAL_METADATA_VERIFIED`, `OFFICIAL_SOURCE_TAG_VERIFIED`, `PROPOSED_UNTESTED`, `DIRECT_PIN_CANDIDATE`

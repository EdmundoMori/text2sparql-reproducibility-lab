# Z2_DATA_METRIC_PREFLIGHT_SPEC — futuro (no ejecutar en Prompt 12)

## Objetivo

Tras resolución de pins/entorno: evidencia de que imports mínimos + contrato de datos + métricas unitarias funcionan en CPU, sin GPT-2 ni train.

## Evidencia nueva esperada

`EXECUTION_VERIFIED` débil de import/data/metric — **no** PE3.

## Permitido (futuro)

- Imports de stdlib + deps resueltas del perfil Z2  
- Lectura read-only de JSON de datos o fixtures sintéticos  
- Llamadas a funciones de `utils/metrics.py` con strings sintéticos  

## Prohibido

- Cargar GPT-2  
- `AutoTokenizer.from_pretrained` / `from_pretrained` de pesos  
- `train.py` / `eval.py` `__main__`  
- Red  
- GPU  
- Checkpoint  
- Table 4 / Answer F1 / SPARQL  

## Clasificaciones de resultado

| Código | Significado |
|---|---|
| `Z2_ENV_IMPORT_DATA_METRIC_PASS` | imports+data contract+metrics OK |
| `Z2_ENV_SETUP_FAILED` | entorno no instalable |
| `Z2_IMPORT_COMPATIBILITY_FAILED` | símbolo Transformers/torch roto |
| `Z2_DATA_CONTRACT_FAILED` | datos/paths/schema |
| `Z2_METRIC_UNIT_FAILED` | métricas unitarias |
| `Z2_UNEXPECTED_NETWORK_ABORT` | red detectada |
| `Z2_RESOURCE_ABORT` | RAM/CPU/timeout |

Ninguna = entrenamiento o reproducción.

# Z2_PREFLIGHT_SCOPE_AND_LIMITATIONS — Prompt 13B

**RUN_ID:** `20260721T114919Z`  
**Harness:** `scripts/smoke/sgpt_z2_offline_preflight.py`  
**Clasificación 13A:** `Z2_ENV_IMPORT_DATA_METRIC_PASS`  
**Resultado científico permitido:** entorno + preflight **core**, **no** ejecución de modelo.

---

## Imports verificados

| Módulo / símbolo | Evidencia |
|---|---|
| `torch` (`1.13.1+cpu`, CUDA false) | `PACKAGE_RUNTIME_VERIFIED` |
| `transformers` (`4.25.1`) | `PACKAGE_RUNTIME_VERIFIED` |
| `numpy`, `tqdm`, `nltk` (paquete) | instalados en freeze; imports vía entorno |
| Símbolos históricos: AdamW, AutoConfig, AutoTokenizer, PreTrainedModel, get_linear_schedule_with_warmup, ACT2FN, Conv1D, find_pruneable_heads_and_indices, prune_conv1d_layer, GPT2PreTrainedModel | `SYMBOL_IMPORT_VERIFIED` |

## Imports **no** verificados

- `scripts.model` completo (módulo SGPT)
- `train.py` / `eval.py`
- loaders / clases dataset upstream
- `utils.dptree` (prohibido; carga spaCy lg + GPT-2)

## Datos

- LC-QuAD2 test leído con **stdlib** (`json`) desde harness del laboratorio.
- `n_records=5969` (`DATA_CONTRACT_VERIFIED`).
- **No** se ejercitó la clase dataset upstream (`z2_dataset_class_status: not_tested`).

## Métricas

Ejecutadas con **strings idénticos** (unidad sintética):

- BLEU, SPBLEU, ROUGE, UnigramMetric, SPUnigramMetric → score 1.0  
- Etiqueta: `CORE_METRIC_UNIT_VERIFIED`

## No probado

- Double-update del loop eval
- F1 persistido
- División por cero en métricas
- METEOR
- NGramDiversity
- Recursos / corpus NLTK
- Pipeline completo de evaluación
- Forward / generation / training step

## Sobre `forbidden_not_imported=true`

Es una **declaración del harness** basada en su scope y código (no importó GPT-2 weights, spaCy models, NLTK data, dptree, train/eval).  
**No** es una auditoría completa de `sys.modules` ni un escaneo forense del contenedor más allá del scan documental 13A.

## Logs ausentes en el run

| Archivo pedido en lectura 13B | Estado |
|---|---|
| `logs/.../network-audit.md` | `NOT_FOUND` (evidencia de red: `--network none` + NetworkGuard del harness) |
| `logs/.../integrity-checks.log` | `NOT_FOUND` (integridad cubierta por digest/freeze/pip-check documentados) |

## Conclusión

Z2 aporta evidencia de **entorno CPU aislado + preflight core**.  
**No** aporta model execution, training, inference ni Table 4.

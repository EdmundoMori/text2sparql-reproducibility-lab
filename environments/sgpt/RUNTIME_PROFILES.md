# RUNTIME_PROFILES — SGPT

**Prompt:** 12  
**Coste externo:** $0.00  
**Evidencia:** README / requirements / params.json / AST / MACHINE_PROFILE

---

## PERFIL A — `NATIVE_DECLARED`

Refleja lo **declarado** por upstream (no resuelto en este lab):

| Ítem | Valor | Evidencia |
|---|---|---|
| Python | 3.8 | README_REPORTED |
| torch | `==1.13.1` | CODE_VERIFIED requirements |
| transformers | sin pin | CODE_VERIFIED |
| requirements.txt | 8 líneas | CODE_VERIFIED |
| spaCy model | `en_core_web_sm` (README) | README_REPORTED |
| Nota spaCy | `dptree.py` usa `en_core_web_lg` | CODE_VERIFIED divergencia |
| GPT-2 | `model_name_or_path: gpt2` | params.json CODE_VERIFIED |
| Train README | `--epochs 40` | README_REPORTED |
| params.json | `num_train_epochs: 70` | CODE_VERIFIED drift README↔config |
| Launch | single GPU `train.py` o `torch.distributed.launch` | README_REPORTED |
| Conda | README usa conda create | README_REPORTED; host Conda ABSENT |

**Estado máximo:** `documented_not_resolved`

---

## PERFIL B — `Z2_CPU_DATA_METRIC_PREFLIGHT`

Finalidad **futura** (no ejecutada en Prompt 12):

- importar módulos mínimos tras resolución de deps;
- cargar contratos/datos o fixtures;
- probar normalización/métricas con fixtures sintéticos;
- **no** GPT-2 / checkpoint / train / inferencia / GPU / Table 4 / Answer F1;
- red bloqueada; coste externo 0.

**Estado:** `proposed_pending_dependency_resolution`

---

## PERFIL C — `Z3_REDUCED_TRAINING_SMOKE`

Finalidad **futura**:

- pocos registros; batch reducido; steps mínimos;
- GPT-2 base (descarga futura con autorización explícita);
- checkpoint **nuevo del laboratorio**;
- etiqueta obligatoria `REDUCED_TRAINING_SMOKE` — **no** Table 4;
- GPU local condicional (6 GiB) o CPU fallback;
- **no** antes de Z2.

**Estado:** `blocked_pending_Z2_and_download_authorization`

# Dependencias y runtime — SGPT

**Fecha:** 2026-07-20  
**Commit:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` (`PIN`)  
**Host lab:** ver `MACHINE_PROFILE.md`

---

## Dependencias declaradas

| Componente | Declaración | Evidencia |
|---|---|---|
| Python | **3.8** (README badge / conda) | `README_REPORTED` |
| `torch` | `==1.13.1` | `CODE_VERIFIED` `requirements.txt` |
| `transformers` | **sin pin** | `CODE_VERIFIED` |
| spaCy + `en_core_web_sm` | requerido (download) | `README_REPORTED` |
| NLTK | requerido (métricas) | `CODE_VERIFIED` / requirements |
| NVIDIA Apex | opcional fp16 | `README`/código |
| `optuna-dashboard` | declarado en requirements | `CODE_VERIFIED` |
| `tensorboardx` | declarado | `CODE_VERIFIED` |

**Esta auditoría no ejecutó** `pip install`, ni imports de `torch` / `transformers` / `spacy` / `nltk` / `sgpt`.

---

## Host lab vs requisitos

| Recurso | Host | Requisito / paper | Clase |
|---|---|---|---|
| Python | **3.10.12** | 3.8 README | mismatch menor; `UNKNOWN` compat exacta sin smoke |
| GPU VRAM | RTX 4050 **6 GiB** | paper **2×12 GB** | insuficiente para paridad paper |
| RAM WSL | **~7.4 GiB** | train + datos + HF cache | presión alta |
| CUDA / torch | driver OK; toolkit `nvcc` ausente | torch 1.13.1 + CUDA wheel | install futuro |
| Conda | **ausente** en host | README usa conda | pip/venv alternativo |
| Red | necesaria 1ª vez para `gpt2` HF | sí | bloquea offline cold start |

---

## Factibilidad por modo

| Modo | Estado | Notas |
|---|---|---|
| `DATA_ONLY_CHECK` | **ready** | conteos/checksums ya hechos |
| IMPORT smoke | **conditional** | necesita env + red para `gpt2`/deps; no verificado |
| INFERENCE | **blocked** | sin checkpoint |
| `REDUCED_TRAINING_SMOKE` | **conditional** (futuro) | batch↓ / epochs↓ / subset; no paridad Table 4 |
| `NATIVE_REPRODUCTION` | **not_ready** | VRAM, epochs, selection criterion, mismatch test 5969↔6046, anomalías métricas |

---

## Riesgos de instalación futura

- `transformers` unpinned → drift API vs torch 1.13.1.
- spaCy model download + NLTK data.
- Apex si se fuerza fp16.
- OOM en 6 GiB con batch efectivo 16 y seq defaults.
- Path `eval_only` incompleto (`pass`).

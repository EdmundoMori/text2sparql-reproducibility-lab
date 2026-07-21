# Z2_BUILD_AND_PREFLIGHT_REPORT — Prompt 13A

**Fecha:** 2026-07-21  
**RUN_ID:** `20260721T114919Z`  
**Aprobador:** EDMUNDO MORI ORRILLO (`HUMAN_DECISION_VERIFIED`)  
**Coste monetario externo:** **0.00**  
**Clasificación:** **`Z2_ENV_IMPORT_DATA_METRIC_PASS`**

---

## 1. Autorización

Ver `environments/sgpt/builds/20260721T114919Z/Z2_DOWNLOAD_BUILD_AUTHORIZATION.md`.

## 2. Imagen base

| Campo | Valor |
|---|---|
| Referencia | `python@sha256:314bc2fb0714b7807bf5699c98f0c73817e579799f2d91567ab7e9510f5601a5` |
| RepoDigest verificado | `python@sha256:314bc2fb…` |
| Arquitectura | amd64 |
| Pull | OK |

## 3. Imagen lab construida

| Campo | Valor |
|---|---|
| Tag | `text2sparql-lab/sgpt-z2-py38:20260721T114919Z` |
| Id | `sha256:75ab83f202a5…` |
| Size | ~1.05 GB |
| Dockerfile | `environments/sgpt/builds/20260721T114919Z/Dockerfile.z2-py38` |

**No versionada en Git** (solo Dockerfile + logs).

## 4. Pins directos verificados (`pip freeze`)

| Paquete | Instalado |
|---|---|
| torch | **1.13.1+cpu** |
| transformers | **4.25.1** |
| numpy | 1.23.5 |
| tqdm | 4.64.1 |
| nltk | 3.8.1 |

`pip check`: **No broken requirements found.**  
CUDA: **false**

## 5. Transitivas

Resueltas por pip en build (p. ej. `tokenizers==0.13.3`, `huggingface_hub==0.36.2`, …). **Pins directos no alterados.** Freeze completo: `logs/environment-z2-build-sgpt/20260721T114919Z/pip-freeze.txt`.

## 6. Prohibidos respetados

- Sin pesos GPT-2 / tokenizer files HF  
- Sin `en_core_web_*`  
- Sin corpus NLTK  
- Sin Apex/CUDA/NCCL  
- Sin `train.py` / `eval.py` / `utils.dptree`  
- Upstream montado **read-only**  

Scan: solo código fuente `transformers/models/gpt2/*.py` (librería), caché HF ~16 K (version.txt).

## 7. Preflight offline (`--network none` + NetworkGuard)

| Check | Resultado |
|---|---|
| Import torch/transformers/símbolos | PASS |
| Data LC-QuAD2 test n=5969 | PASS |
| Métricas sintéticas BLEU/SPBLEU/ROUGE/unigram | PASS |
| Red durante probe | bloqueada |

## 8. No afirmado

- Table 4 / PE3  
- Answer F1 / SPARQL  
- Native reproduction  
- Z3 training  

## 9. Estados

| Campo | Valor |
|---|---|
| `reproduction_status` | `audit_only` |
| `native_audit_complete` | `false` |
| `common_adapter_allowed` | `false` |
| `z2_preflight_status` | `Z2_ENV_IMPORT_DATA_METRIC_PASS` |
| `environment_gate` | `Z2_ENV_READY_PREFLIGHT_PASS` |
| Z3 | sigue blocked |

## 10. Siguiente paso sugerido

Documental o smoke reducido posterior **solo** con nueva autorización (p. ej. NLTK data / Z3 GPT-2). No ejecutar Z3 ahora.

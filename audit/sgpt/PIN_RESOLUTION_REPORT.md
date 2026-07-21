# PIN_RESOLUTION_REPORT — SGPT Prompt 12B

**Fecha:** 2026-07-21  
**RUN_ID:** `20260721T113310Z`  
**Upstream pin:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b`  
**Coste externo:** **0.00**  
**Install / wheel download / image pull / train / infer:** **0**

---

## 1. Objetivo

Resolver documentalmente pins directos y artefactos candidatos para un futuro entorno SGPT **Z2 CPU**.

## 2. Alcance

Solo metadata/fuente oficial allowlisted. Sin instalación ni descarga de binarios/modelos.

## 3. Política ZERO_COST

`MAX_EXTERNAL_MONETARY_COST_USD=0.00` vigente.

## 4. Fuentes oficiales

PyPI JSON; download.pytorch.org índices; Docker Hub auth+manifests; GitHub API/raw (SGPT, transformers, nltk); Hugging Face API `gpt2` metadata.

## 5. Ancla temporal

`requirements.txt` con torch 1.13.1 en historial **2022-12-28**; Transformers **4.25.1** (upload 2022-12-01). Commit lab posterior no prueba refresh de deps.

## 6–7. Python / imagen

`python:3.8.20-slim-bookworm`  
list `sha256:1d52838af602b4b5a831beb13a0e4d073280665ea7be7f69ce2382f29c5a613f`  
amd64 `sha256:314bc2fb0714b7807bf5699c98f0c73817e579799f2d91567ab7e9510f5601a5`  
Debian/glibc; no Alpine; no pull.

## 8. PyTorch

Declarado `torch==1.13.1`. Z2: **`torch==1.13.1+cpu`** (`PROPOSED_Z2_CPU_BUILD_VARIANT`), wheel `torch-1.13.1+cpu-cp38-cp38-linux_x86_64.whl`, sha256 `4a8b8483…`. No descargada.

## 9–10. Transformers / símbolos

**Seleccionado:** `transformers==4.25.1` (`SELECTED_CANDIDATE_UNTESTED`).  
Runner-up: 4.26.1.  
Todos los símbolos requeridos presentes en tag `v4.25.1` (Conv1D vía reexport `modeling_utils`→`pytorch_utils`). **No** RUNTIME_VERIFIED.

## 11–12. Directas / transitivas

Matrices CSV + constraints candidatos. Transitivas: `TRANSITIVE_METADATA_KNOWN` desde Requires-Dist (**no** lock).

## 13–15. spaCy / NLTK / GPT-2

spaCy 3.4.4 candidato perfil A; modelos deferred; `dptree` denylist Z2.  
NLTK 3.8.1; recursos deferred; Z2 core metrics sin corpus.  
GPT-2: metadata only; `DEFERRED_Z3`; not_downloaded.

## 16–17. Perfiles

Native-declared constraints vs Z2-cpu constraints (archivos `constraints.*.txt`).

## 18. Allowlist/denylist

`Z2_IMPORT_SCOPE.csv` — deniega train/eval/model weights/dptree/qald9 BaseDataset.

## 19–22. Riesgos / desviaciones / no descargado / no runtime

EOL Python 3.8; `+cpu` ≠ paper exact; transitivas no fijadas; mutable HF `main`; sin IMPORT_VERIFIED.

## 23. Gate

**`READY_FOR_Z2_DOWNLOAD_AUTHORIZATION`**

## 24. Siguiente paso

**Prompt 13A — Autorización y descarga controlada de imagen y paquetes SGPT Z2 + construcción del entorno CPU, ZERO_COST, sin GPT-2, sin modelos spaCy, sin train.**

## 25–27. PE / Table 4 / conclusión

PE2 prep documental; PE3 not_started; Table 4 **no** reproducida. Pins candidatos listos para autorización de descarga — **no** entorno construido.

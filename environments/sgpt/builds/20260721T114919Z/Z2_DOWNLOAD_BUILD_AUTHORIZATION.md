# Z2_DOWNLOAD_BUILD_AUTHORIZATION — Prompt 13A

**APPROVER_NAME:** EDMUNDO MORI ORRILLO  
**DECISION_DATE:** 2026-07-21  
**EVIDENCE_TAG:** HUMAN_DECISION_VERIFIED  
**MAX_EXTERNAL_MONETARY_COST_USD:** 0.00  
**RUN_ID:** 20260721T114919Z

## Autorizado

1. Imagen `python:3.8.20-slim-bookworm` / digest amd64 `sha256:314bc2fb0714b7807bf5699c98f0c73817e579799f2d91567ab7e9510f5601a5`
2. Paquetes de `constraints.z2-cpu.direct.candidate.txt` (+ transitivas necesarias)
3. Verificación nombres/fuentes/versiones/tamaños/hashes
4. Cachés fuera de Git
5. Entorno Docker CPU aislado
6. Solo: python --version, pip check/freeze, inspección, import probes Z2, tests sintéticos sin modelos/corpus/red

## No autorizado

GPT-2 / tokenizer / pesos; spaCy models; NLTK data; Apex; CUDA/NCCL; APIs de pago; train/eval/dptree; Table 4; SPARQL; modificar upstream; versionar imágenes/wheels/cachés/modelos.

## Abort conditions

digest mismatch; torch wheel wrong; transformers ≠ 4.25.1; need GPT-2/spaCy/NLTK corpus; upstream change required; monetary cost; disk/RAM insufficient; silent pin change; network during offline probe.

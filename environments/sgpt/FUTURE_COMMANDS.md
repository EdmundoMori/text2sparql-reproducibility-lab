# FUTURE_COMMANDS — SGPT

**Prompt 13A ejecutado:** pull digest + build Z2 + preflight offline.  
Comandos restantes siguen **bloqueados** hasta nueva autorización.

## Ya ejecutado (13A) — referencia

```bash
# HECHO en 13A — no re-ejecutar sin necesidad
# docker pull python@sha256:314bc2fb0714b7807bf5699c98f0c73817e579799f2d91567ab7e9510f5601a5
# docker build -f environments/sgpt/builds/20260721T114919Z/Dockerfile.z2-py38 ...
# docker run --network none ... python scripts/smoke/sgpt_z2_offline_preflight.py
```

## Descargas / Z3 (siguen prohibidos sin nueva autorización)

```bash
# REQUIRES_EXPLICIT_DOWNLOAD_AUTHORIZATION
# python -m spacy download en_core_web_sm
# python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('gpt2')"
# python -m nltk.downloader ...
# train.py / eval.py / utils.dptree
```

## Z3

```bash
# DO_NOT_RUN_IN_PROMPT_12
# REQUIRES_EXPLICIT_DOWNLOAD_AUTHORIZATION
# blocked until Z2 + download auth
```

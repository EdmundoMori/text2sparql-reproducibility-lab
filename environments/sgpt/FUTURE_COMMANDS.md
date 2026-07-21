# FUTURE_COMMANDS — SGPT (documental)

Todos los comandos: **DO_NOT_RUN_IN_PROMPT_12**

## Digest / imagen

```bash
# DO_NOT_RUN_IN_PROMPT_12
# docker pull ...@sha256:<RESOLVED>
# docker image inspect --format '{{.Id}}' ...
```

## Build futuro

```bash
# DO_NOT_RUN_IN_PROMPT_12
# docker build -f environments/sgpt/Dockerfile.native-py38.template ...
```

## pip check / freeze (dentro de env futuro)

```bash
# DO_NOT_RUN_IN_PROMPT_12
# pip check
# pip freeze
```

## Import probe

```bash
# DO_NOT_RUN_IN_PROMPT_12
# python -c "import torch, transformers, nltk, spacy, numpy, tqdm"
```

## Z2 data/metric preflight

```bash
# DO_NOT_RUN_IN_PROMPT_12
# python scripts/smoke/sgpt_z2_data_metric_preflight.py   # (aún no existe)
```

## Descargas

```bash
# DO_NOT_RUN_IN_PROMPT_12
# REQUIRES_EXPLICIT_DOWNLOAD_AUTHORIZATION
# python -m spacy download en_core_web_sm
# python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('gpt2')"
```

## Z3

```bash
# DO_NOT_RUN_IN_PROMPT_12
# REQUIRES_EXPLICIT_DOWNLOAD_AUTHORIZATION
# blocked until Z2 + download auth
```

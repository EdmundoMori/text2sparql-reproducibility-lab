# PYTHON_BASE_IMAGE_DECISION

**RUN_ID:** `20260721T113310Z`  
**Selección:** `python:3.8.20-slim-bookworm`  
**Evidencia:** Docker Hub registry manifests (`CONTAINER_MANIFEST_VERIFIED`)

| Campo | Valor |
|---|---|
| Tag | `3.8.20-slim-bookworm` |
| Manifest list digest | `sha256:1d52838af602b4b5a831beb13a0e4d073280665ea7be7f69ce2382f29c5a613f` |
| linux/amd64 digest | `sha256:314bc2fb0714b7807bf5699c98f0c73817e579799f2d91567ab7e9510f5601a5` |
| OS base | Debian Bookworm (glibc) |
| Alpine | **no** |
| latest | **no** |
| Arquitectura | linux/amd64 |
| Python | CPython 3.8.20 (último patch 3.8 como mitigación operativa, no paridad paper) |
| EOL Python 3.8 | sí (riesgo seguridad histórico documentado) |
| docker pull en 12B | **no** |

Alias observado: tag `3.8-slim-bookworm` comparte el mismo list digest que `3.8.20-slim-bookworm` en este snapshot.

**Estado:** `DIRECT_PIN_CANDIDATE` / `PROPOSED_UNTESTED` (no RUNTIME_VERIFIED)

# CONTAINER_STRATEGY — SGPT

**Prompt:** 12  
**Docker build en este prompt:** **no**

| Hecho host | Valor | Evidencia |
|---|---|---|
| Conda | ABSENT | MACHINE_VERIFIED |
| Docker CLI/daemon | presente | MACHINE_VERIFIED |
| Python host | 3.10.12 ≠ README 3.8 | MACHINE_VERIFIED / README_REPORTED |
| Compose plugin | ABSENT | MACHINE_VERIFIED |
| nvcc | ABSENT | MACHINE_VERIFIED |

## Preferencia futura

- Contenedor **Python 3.8** (perfil NATIVE_DECLARED).  
- Imagen base fijada por **digest** (aún **no** resuelto → placeholder).  
- No `latest`.  
- No Conda en contenedor salvo decisión posterior.  
- No Compose.  
- No apt sin justificación.  
- `workdir/` descartable; caches fuera de Git.  
- upstream montado **read-only** o copia descartable — nunca escritura en `upstream/sgpt`.

Ver `Dockerfile.native-py38.template` — **TEMPLATE_ONLY / DO_NOT_BUILD**.

## Prompt 12B

Digest resuelto: `python@sha256:314bc2fb…` (`3.8.20-slim-bookworm`). Dockerfile candidato: `Dockerfile.z2-py38.candidate` — **DO_NOT_BUILD_IN_PROMPT_12B**.

## Prompt 13A (ejecutado)

- Build: `environments/sgpt/builds/20260721T114919Z/Dockerfile.z2-py38`
- Imagen local (fuera de Git): `text2sparql-lab/sgpt-z2-py38:20260721T114919Z`
- Upstream montado **read-only**; caches/wheels/imagen **no** versionados.
- Gate: `Z2_ENV_READY_PREFLIGHT_PASS`

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

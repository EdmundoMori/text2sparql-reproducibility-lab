# sparql_llm CORE_OFFLINE — contenedor Python 3.11

**Prompt:** 5B  
**RUN_ID:** `20260720T134943Z`  
**Prior run (5A):** `20260719T112306Z` (`setup_failed` on host Python 3.10)

## Imagen base

| Campo | Valor |
|---|---|
| Tag solicitado | `python:3.11-slim-bookworm` |
| RepoDigest | `python@sha256:b18992999dbe963a45a8a4da40ac2b1975be1a776d939d098c647482bcad5cba` |
| Image ID | `sha256:7e666cfcc7bd4c47b26b7a5ec0116d80e9bc5415ea06c0dc0bd117a50e9fa6c6` |
| Arch | amd64 |
| Python en contenedor | 3.11.15 |

Plantilla: [`Dockerfile.core-offline-py311`](Dockerfile.core-offline-py311) (FROM por digest).

## Imagen del lab (local, no versionada en Git)

`text2sparql-lab/sparql-llm-core-offline:20260720T134943Z`

## Política de red

- `docker pull` / `docker build`: red permitida (resolver deps PyPI).  
- Smoke / import probe / pip inspect post-build: `--network none`.

## Notas

- No Compose. No GPU. No instalar Python 3.11 en WSL.  
- `--read-only` **no viable**: import escribe bajo home (p. ej. `/root/.data` vía deps). Smoke válido sin RO + `--network none`.  
- Harness: una corrección mínima LAB (`socket.create_connection` a nivel módulo; sin asignar `socket.socket.connect`).

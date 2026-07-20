# CORE_OFFLINE_PY311_SMOKE_REPORT — sparql_llm

**RUN_ID:** `20260720T134943Z`  
**Resultado:** `smoke_only`  
**Smoke ≠ reproducción del paper.**  
**Prior run 5A:** `20260719T112306Z` = `setup_failed` (conservado).

---

## 1. Objetivo

Reintentar CORE_OFFLINE con Python 3.11 en Docker (sin instalar Python en WSL), tras el fallo de import en 3.10 por `typing.Required`.

## 2. Commits

| | SHA |
|---|---|
| Lab inicial | `6ca23b10f429c209d6e255519be7aac517a41f83` |
| Upstream pin | `3748730e3bd2df2595280b918269fdaadb9fc0c3` |

## 3. Entorno

| Campo | Valor |
|---|---|
| Base | `python@sha256:b18992999dbe963a45a8a4da40ac2b1975be1a776d939d098c647482bcad5cba` |
| Python | 3.11.15 |
| Package | sparql-llm 0.1.4 |
| pip check | OK |
| Red en smoke | `--network none` |

Ver `environments/sparql_llm/container_py311.md`.

## 4. Procedimiento

1. Copia descartable del pin → build-context.  
2. `docker pull` + Dockerfile por digest + `docker build`.  
3. Import probe (`--network none`) → OK.  
4. Harness: fallo LAB en guard de sockets → corrección mínima del harness.  
5. Intento con `--read-only` → no viable (`/root/.data`).  
6. Harness viable (`--network none`, FS escribible) → **PASS**.

## 5. Dependencias resueltas

Ver `logs/smoke/sparql_llm-core-offline-py311/20260720T134943Z/pip-freeze.txt` (entorno del run; no pins upstream).

## 6–7. Checks

| Check | Resultado |
|---|---|
| Build imagen | PASS |
| pip check | PASS |
| Python 3.11.x | PASS (3.11.15) |
| Version 0.1.4 | PASS |
| Import | PASS |
| SPARQL parse | PASS |
| VoID local (162 classes) | PASS |
| Query válida 0 issues | PASS |
| Predicado inválido detectado | PASS (1 issue) |
| Red durante smoke | PASS (0) |
| Upstream intacto | PASS |

## 8. Evidencia local / sin modelos

- Smoke con `--network none`.  
- Sin LLM/API/endpoints.  
- Sin pesos nuevos versionados en el repo.

## 9. Upstream intacto

`git diff -- upstream/sparql_llm` vacío.

## 10. Estado asignado

- `experiment_status`: **smoke_only**  
- `METHOD_REGISTRY.reproduction_status`: **smoke_only**  
- `native_audit_complete`: **false**  
- `common_adapter_allowed`: **false**  
- Run 5A permanece **setup_failed**  
- Hallazgo: metadata `requires-python>=3.10` inconsistente con uso de `typing.Required`

## 11. Limitaciones

Solo CORE_OFFLINE. No paper eval. No agent/MCP/API.

## 12. Próximo paso

**Auditoría estática SGPT (WAVE_B)** — no tercer reintento CORE_OFFLINE inmediato.

## 13. Distinción

`smoke_only` ≠ `reproduced` / `partially_reproduced`.

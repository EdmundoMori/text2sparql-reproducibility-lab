# CORE_OFFLINE_SMOKE_REPORT — sparql_llm

**RUN_ID:** `20260719T112306Z`  
**Resultado:** `setup_failed`  
**Smoke ≠ reproducción del paper.**

---

## 1. Objetivo

Instalar el pin `3748730e…` desde copia descartable e intentar micro-smoke local (import, VoID file, validate_sparql) sin red/LLM/endpoints.

## 2. Commits

| | SHA |
|---|---|
| Lab inicial | `46d3713128f0f70907ed5086179f0eee204fac62` |
| Upstream pin | `3748730e3bd2df2595280b918269fdaadb9fc0c3` |

## 3. Entorno

- Host Python: **3.10.12** (solo `python3`; sin 3.11).  
- pip: 22.0.2.  
- Install OK en `/tmp/sparql_llm_5a_venv` (venv workdir RO en sandbox).  
- Package metadata: **sparql-llm 0.1.4**.  
- `pip check`: OK.

## 4. Procedimiento

1. Copia `upstream/sparql_llm` → `workdir/runs/.../source` (sin `.git_local`).  
2. `pip install <source>` no editable, sin extras.  
3. Probe `import sparql_llm` → **falló**.  
4. Harness funcional no ejecutado.

## 5. Dependencias resueltas

Ver `logs/smoke/sparql_llm-core-offline/20260719T112306Z/pip-freeze.txt`.

## 6–7. Checks

| Check | Resultado |
|---|---|
| Install local non-editable | PASS |
| pip check | PASS |
| Metadata version 0.1.4 | PASS |
| Import package | **FAIL** (`typing.Required` on 3.10) |
| VoID / validate harness | NOT REACHED |
| Upstream intact | PASS |
| No HF model weights | PASS |

## 8. Evidencia operación local

- Fallo de import es local (stdlib typing).  
- No se llamó a endpoints ni LLM.  
- Harness con network guard no llegó a ejecutarse.

## 9. Upstream intacto

`git diff -- upstream/sparql_llm` vacío; pin lock sin cambios.

## 10. Estado asignado

- `experiment_status`: **setup_failed**  
- `METHOD_REGISTRY.reproduction_status`: **setup_failed**  
- `native_audit_complete`: **false**  
- `common_adapter_allowed`: **false**  
- No `smoke_only` / `reproduced` / `partially_reproduced`

## 11. Limitaciones

- Host sin Python ≥3.11.  
- Código pin usa `typing.Required` incompatible con 3.10.  
- No se autorizó patch ni instalar Python 3.11 en este prompt.

## 12. Próximo paso recomendado

**Prompt 5A-bis / 5B tooling:** instalar Python 3.11+ en el host (deadsnakes/apt — prompt dedicado) **o** documentar bloqueo permanente CORE_OFFLINE en 3.10 y reintentar smoke con 3.11, sin modificar upstream.  
No avanzar a agent/API hasta import CORE_OFFLINE OK.

## 13. Distinción

Este intento **no** es reproducción científica del artículo SPARQL-LLM.

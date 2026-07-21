# GO/NO-GO — Futuro smoke API SPARQL-LLM

**Fecha protocolo:** 2026-07-20  
**Pinned commit:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Lab HEAD inicial Prompt 9:** `3d89a8d61f3fed8eecec8e49f6b79baccf677a76`

---

## 1. Decisión (MANDATORY — no cambiar)

| Campo | Valor |
|---|---|
| **Selected future action** | `LOCAL_CHAT_API_ONE_QUESTION` |
| **Gate** | ~~`CONDITIONAL_GO`~~ → **`NO_GO_ECONOMIC`** (2026-07-21; ZERO_USD) |
| **reproduction_status** | permanece `smoke_only` |
| **native_audit_complete** | permanece `false` |
| **common_adapter_allowed** | permanece `false` |

### Por qué esta acción

Ejecuta el código anclado vía FastAPI `/chat` + LangGraph; aporta mejor evidencia PE2 que el MCP público; `enable_sparql_execution` puede ser `false` para reducir red SPARQL (`CODE_VERIFIED` en `validation.py`; biodata usa `False` en `/chat`).

### Por qué CONDITIONAL_GO (no GO)

Bloqueadores abiertos:

1. Runtime Python 3.11 (patrón Docker 5B).  
2. Path o URL Qdrant.  
3. Descarga FastEmbed `multilingual-e5-large`.  
4. `init_vectordb` o índice prebuilt.  
5. `OPENROUTER_API_KEY`.  
6. `SETTINGS` mínimo (UniProt + `void_file` local).  
7. Aprobación de presupuesto del investigador.

### Qué no es nativo

`PUBLIC_MCP_REMOTE` (`https://chat.expasy.org/mcp`) → solo `external_service_availability_check`.

---

## 2. Exactamente una acción seleccionada

| Candidato | Estado |
|---|---|
| A PUBLIC_MCP_REMOTE_SERVICE_CHECK | no seleccionado (solo `external_service_availability_check`) |
| B LOCAL_MCP_STDIO_TOOL_SMOKE | no seleccionado |
| C LOCAL_MCP_HTTP_TOOL_SMOKE | no seleccionado |
| **D LOCAL_CHAT_API_ONE_QUESTION** | **SELECCIONADO** (`CONDITIONAL_GO`) |
| E REDUCED_MANUAL_BENCHMARK | no seleccionado (aplazado) |
| F REDUCED_BIODATA_BENCHMARK | no seleccionado (aplazado) |

---

## 3. Checklist hacia GO (técnico)

| # | Ítem | Prompt 9 | Necesario para GO |
|---|---|---|---|
| 1 | Protocolo documental (6 mínimos) | **DONE** | sí |
| 2 | Contratos Chat/MCP + matrices | **DONE** | sí |
| 3 | Runtime Py3.11 usable | pendiente | sí |
| 4 | Índice/Qdrant mínimo | pendiente | sí |
| 5 | FastEmbed disponible/cache | pendiente | sí |
| 6 | SETTINGS mínimo UniProt void | pendiente | sí |
| 7 | `OPENROUTER_API_KEY` aislada | pendiente | sí |
| 8 | Presupuesto firmado (`API_BUDGET_AND_SAFETY`) | pendiente | sí |
| 9 | `enable_sparql_execution=false` en plan de request | documentado | sí |
| 10 | Confirmación de no usar MCP público como nativo | documentado | sí |

**Resultado actual:** `CONDITIONAL_GO` — protocolo listo; entorno/clave/presupuesto no.

---

## 4. Criterios NO-GO (hard)

Declarar **NO-GO** (o mantener bloqueo) si:

- Se pretende smoke sin Py3.11 viable.  
- Se requiere Virtuoso/Compose ausente como único camino.  
- Presupuesto no aprobado o `MAX_QUESTIONS`>1 sin nueva decisión.  
- Único camino disponible es MCP público remoto.  
- Se quiere declarar PE3 / `partially_reproduced` solo con protocolo o 1 pregunta.  
- Se abren adapters (`common_adapter_allowed` debe seguir false).

---

## 5. Criterios de éxito del futuro smoke (cuando gate pase a GO)

1. Código ejecutado = pin `3748730…`.  
2. Exactamente 1 pregunta vía `POST /chat`.  
3. `enable_sparql_execution=false` efectivo.  
4. Artefactos experimentales (manifest, result, deviations, logs).  
5. Sin cambio de `reproduction_status` salvo decisión posterior explícita.  
6. Etiquetar evidencia `EXECUTION_VERIFIED` solo para lo observado.

---

## 6. Próximo prompt (título exacto)

`Prompt 10 — Preparación de entorno e índice mínimo para smoke LOCAL_CHAT_API de SPARQL-LLM (sin llamadas LLM)`

**Fuera de Prompt 10:** llamadas LLM; benchmarks; MCP público como nativo; cambio de estados de reproducción.

---

## 7. Mapeo a mínimos de NEXT_EXECUTION_DECISION §10

| Mínimo | Artefacto |
|---|---|
| Endpoints/entrypoints | `EXECUTION_SURFACES.csv`, contratos |
| Claves/env | `CONFIGURATION_MATRIX.csv`, `API_BUDGET_AND_SAFETY.md` |
| Request/response | `CHAT_API_CONTRACT.md`, `MCP_CONTRACT.md` |
| Offline vs online | `OFFLINE_ONLINE_BOUNDARY.md` |
| Éxito/fallo futuro smoke | este doc §5 + `SIB_BENCHMARK_PROTOCOL.md` L0 |
| Checklist GO/NO-GO | este doc §3–§4 |

**Veredicto Prompt 9:** definición de protocolo **completa**; ejecución smoke **no autorizada** aún (`CONDITIONAL_GO`).

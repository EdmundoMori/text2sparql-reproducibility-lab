# ECONOMIC_NO_GO_DECISION — Smoke online LOCAL_CHAT_API_ONE_QUESTION

**RUN_ID_refusal:** `20260721T103536Z`  
**RUN_ID_gate_modelo (Prompt 11):** `20260721T100618Z`  
**Fecha:** 2026-07-21  
**Aprobador:** EDMUNDO MORI ORRILLO

---

## Decisión humana (vinculante)

| Campo | Valor |
|---|---|
| Política de coste | **SOLO $0** |
| Prompt 12 (POST `/chat`) | **NO AUTORIZADO** |
| Creación de clave OpenRouter | **NO AUTORIZADA** |
| Uso de clave OpenRouter | **NO AUTORIZADO** |
| Llamadas a modelos de pago | **NO AUTORIZADAS** |
| POST `/chat` | **NO AUTORIZADO** |
| Inferencias LLM | **0** (permanece) |

Texto de política (investigador):

> SOLO $0, SIN PROMPT 12.  
> No autorizo la creación ni el uso de una clave OpenRouter.  
> No autorizo POST `/chat` ni llamadas a modelos de pago.  
> Solicito documentar el NO-GO económico del smoke online y volver a ejecutar el gate comparativo para seleccionar la siguiente acción de investigación sin coste de API.

---

## Veredicto de gate online

| Campo | Valor |
|---|---|
| **online_smoke_gate** | **`NO_GO_ECONOMIC`** |
| Mapeo a valores Prompt 11 | `NO_GO_OTHER` (motivo: política ZERO_USD del investigador) |
| Modelo documentalmente seleccionado | permanece registrado (`openrouter/openai/gpt-4o-mini-2024-07-18`) — **no** aprobado para gastar |
| MAX_OPENROUTER_USD | **rechazado** (presupuesto efectivo **$0**) |
| human_llm_approval_status | **REFUSED_ZERO_USD** |
| Prompt 12 chat smoke | **CANCELLED** |

Etiqueta: `HUMAN_APPROVAL_REQUIRED` resuelta como **rechazo** (no como firma de gasto).

---

## Qué se conserva

- Entorno agent Py3.11, caché e5-large, `LAB_MINIMAL_INDEX`, preflight FastAPI  
- Snapshot OpenRouter, cota teórica, pregunta/request congelados (histórico documental)  
- `reproduction_status: smoke_only`  
- `native_audit_complete: false`  
- `common_adapter_allowed: false`  
- Fase 1 abierta  

## Qué no se hará bajo esta política

- Crear/usar `OPENROUTER_API_KEY`  
- Prompt 12 de ejecución `/chat`  
- Sustituir silenciosamente por modelo “free” o LLM local sin nuevo gate  

---

## Siguiente paso

Re-gate comparativo nativo con restricción dura **API_COST_USD = 0** → ver:

- `audit/NATIVE_AUDIT_COMPARATIVE_GATE_RERUN_ZERO_USD.md`  
- `audit/NEXT_EXECUTION_DECISION.md`  
- `docs/decisions/004_economic_nogo_online_smoke_and_re_gate.md`

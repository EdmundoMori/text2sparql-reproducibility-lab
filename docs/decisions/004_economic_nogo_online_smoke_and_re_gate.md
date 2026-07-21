# Decisión 004 — NO-GO económico del smoke online y re-gate ZERO_USD

**Fecha:** 2026-07-21  
**Estado:** Activa  
**Fase lab:** 1 — native audit (no cerrada)  
**Aprobador de política de coste:** EDMUNDO MORI ORRILLO  
**Artefactos:**  
- `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/ECONOMIC_NO_GO_DECISION.md`  
- `audit/NATIVE_AUDIT_COMPARATIVE_GATE_RERUN_ZERO_USD.md`  
- `audit/NEXT_EXECUTION_DECISION.md`  
- `audit/NATIVE_REPRODUCTION_QUEUE.csv`

---

## Contexto

Tras Prompt 11, el smoke `LOCAL_CHAT_API_ONE_QUESTION` estaba en `READY_FOR_HUMAN_APPROVAL` (modelo y cota documentados; entorno/índice/preflight listos). El investigador fijó política **SOLO $0**: sin clave OpenRouter, sin POST `/chat`, sin Prompt 12 de inferencia de pago.

## Decisiones

1. **`online_smoke_gate = NO_GO_ECONOMIC`** para `LOCAL_CHAT_API_ONE_QUESTION` mientras rija ZERO_USD.  
2. **Cancelar** el Prompt 12 de ejecución `/chat`.  
3. **No** crear ni usar claves OpenRouter bajo esta política.  
4. **Re-gate** comparativo con restricción `API_COST_USD = 0`.  
5. **Nueva acción `GO_NEXT`:** cierre documental legal/fuente de `rdfconfig_llm`.  
6. **Nuevo título operativo:** `Prompt 12 — Cierre documental legal/fuente de rdfconfig_llm (ZERO_USD, sin installs)`.  
7. Conservar `smoke_only` / `audit_only`, `native_audit_complete=false`, `common_adapter_allowed=false`; Fase 1 abierta.  
8. La ADR 003 permanece como histórico del primer gate; esta ADR **actualiza** la cola operativa.

## Alternativas rechazadas ahora

| Alternativa | Veredicto |
|---|---|
| Ejecutar `/chat` con $0.10 | Rechazada por política ZERO_USD |
| Modelo OpenRouter “free” sin nuevo gate | Rechazada (no sustituir en silencio) |
| LLM local como drop-in | Rechazada sin nuevo gate de desviación |
| MCP público como nativo | Rechazada |
| GO_NEXT = tercer CORE_OFFLINE | Rechazada (poca evidencia nueva) |

## Consecuencias

- Presupuesto OpenRouter efectivo = **$0**.  
- Evidencia PE2 online de sparql_llm permanece **no ejercida** (no es fallo de prep técnica).  
- El planificador debe proponer el Prompt 12 **legal rdfconfig**, no el chat smoke.

## Limitaciones

- NO_GO económico ≠ invalidación científica de SPARQL-LLM.  
- El re-gate no instala Ruby ni ejecuta rdfconfig.  
- PE3 sigue `not_started`.

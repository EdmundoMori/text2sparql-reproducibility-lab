# NEXT_EXECUTION_DECISION — Re-gate ZERO_USD (2026-07-21)

**Fecha:** 2026-07-21  
**RUN_ID:** `20260721T103536Z`  
**Gate:** `audit/NATIVE_AUDIT_COMPARATIVE_GATE_RERUN_ZERO_USD.md`  
**ADR:** `docs/decisions/004_economic_nogo_online_smoke_and_re_gate.md`  
**Estado:** documental — sin installs, sin API de pago, sin POST `/chat`

**Supersede parcial:** la decisión operativa de Prompt 8 hacia smoke API queda **anulada por NO_GO_ECONOMIC**; el informe Prompt 8 permanece como histórico.

---

## 1. Acción seleccionada

Cierre **documental** de licencia y fuente canónica del generador RDF-config (`rdfconfig_llm`): contrastar HEAD del repo vs artefacto Zenodo/companion, registrar SPDX/archivo de licencia o confirmar `LICENSE_NOT_CONFIRMED` con evidencia etiquetada.

## 2. Método o prerrequisito

**Método:** `rdfconfig_llm`  
**Prerrequisito:** static audit WAVE_A completo; companion MIT ya separado; generador aún `LICENSE_NOT_CONFIRMED`.

## 3. Tipo

`legal_closure` (documental)

## 4. Evidencia que la justifica

| Hecho | Etiqueta |
|---|---|
| Rechazo ZERO_USD del smoke online sparql_llm | HUMAN (Mori 2026-07-21) |
| Prep online sparql_llm lista pero sin gastar | ENVIRONMENT_VERIFIED / CODE_VERIFIED |
| Protocolo API/SIB ya definido | CODE_VERIFIED (Prompt 9) |
| Generador rdfconfig LICENSE_NOT_CONFIRMED | LEGAL (WAVE_A) |
| Ruby ABSENT en host — no instalar ahora | MACHINE_PROFILE |
| Regla lexicográfica bajo API_COST=0 | INFERENCE (criterio de gate) |

## 5. Valor científico esperado

Desbloquear (o cerrar motivadamente) el HOLD_LEGAL de una baseline schema-guided distinta de SPARQL-LLM, sin coste de API y sin fingir ejecución Ruby.

## 6. Qué pregunta experimental ayuda a responder

- **PE4:** ¿la barrera es solo LICENSE o también divergencia HEAD/Zenodo?  
- **PE1/PE2 (condicional):** aclara si un futuro entorno Ruby es legalmente defendible.  
- **No PE3.**

## 7. Recursos

- Lectura de `upstream/rdfconfig_llm`, audits WAVE_A, Zenodo/metadata pública si hace falta.  
- Sin pip/Ruby install; sin OpenRouter; sin GPU.

## 8. Riesgos

- Confundir companion MIT con licencia del generador (mitigar: separar artefactos).  
- Presión a instalar Ruby en el mismo prompt (mitigar: solo legal_closure).  
- Tratar NO_GO económico de sparql_llm como fallo técnico (mitigar: etiquetar COST).

## 9. Restricciones

- **Prohibido:** OpenRouter / claves / POST `/chat` / modelos de pago.  
- **Prohibido:** install Ruby/Bundler; adapters; cambiar `reproduction_status`; cerrar Fase 1.  
- Conservar `common_adapter_allowed=false`.

## 10. Criterio GO (éxito del siguiente prompt)

Entregar documento de cierre legal/fuente que incluya, como mínimo:

1. Fuente canónica evaluada (repo HEAD, Zenodo, companion).  
2. Estado de licencia del **generador** con etiqueta LEGAL_VERIFIED / NOT_CONFIRMED / UNKNOWN.  
3. Relación companion MIT vs generador.  
4. Implicación para isolated_internal_execution y adapters.  
5. GO/NO-GO hacia definición de entorno Ruby (sin instalarlo aún).

## 11. Criterio NO-GO

No instalar Ruby ni ejecutar el generador si el cierre legal no lo permite.

## 12. Título del siguiente prompt

**Prompt 12 — Cierre documental legal/fuente de rdfconfig_llm (ZERO_USD, sin installs)**

> Nota: el antiguo Prompt 12 (`LOCAL_CHAT_API_ONE_QUESTION`) está **CANCELLED** por `NO_GO_ECONOMIC`.

## 13. Qué no hacer

- No resucitar Prompt 12 chat sin nueva política de presupuesto.  
- No usar MCP público como evidencia nativa.  
- No train SGPT / CoT / FIRESPARQL APIs.

## 14. Estados a conservar

| Campo | Valor |
|---|---|
| sparql_llm `reproduction_status` | `smoke_only` |
| resto | `audit_only` |
| `native_audit_complete` | `false` |
| `common_adapter_allowed` | `false` |
| sparql_llm `online_smoke_gate` | `NO_GO_ECONOMIC` |

## 15. Relación con el objetivo del laboratorio

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

Bajo ZERO_USD, la reproducción nativa avanza por **cierres documentales/legales** y evidencias offline ya obtenidas, no por smoke LLM de pago.

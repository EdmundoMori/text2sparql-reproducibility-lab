# Decisión 004 — Política de coste cero y deferral del smoke online

**Fecha:** 2026-07-21  
**Estado:** Activa  
**Prompt:** 11C  
**Fase:** 1 — native audit (abierta)  
**Aprobador:** EDMUNDO MORI ORRILLO  
**Evidencia:** `HUMAN_DECISION_VERIFIED` — “elijo coste 0”

**Supersede:** `004_economic_nogo_online_smoke_and_re_gate.md` (registro interino pre-11C; conservar como histórico).

---

## 1. Contexto

Tras Prompt 11, el smoke `LOCAL_CHAT_API_ONE_QUESTION` estaba técnicamente preparable (`READY_FOR_HUMAN_APPROVAL`). El investigador eligió coste monetario externo cero.

## 2. Decisión

1. `MAX_EXTERNAL_MONETARY_COST_USD = 0.00`.  
2. `online_smoke_gate = NO_GO_ECONOMIC_ZERO_COST_POLICY`.  
3. Prompt 12 chat: **cancelled/deferred indefinitely**.  
4. OpenRouter / paid LLM / paid cloud: **not authorized**.  
5. Re-gate de cola nativa bajo coste cero (artefactos `audit/ZERO_COST_*`).  
6. Exactamente una acción `GO_NEXT_ZERO_COST` (ver `NEXT_ZERO_COST_EXECUTION_DECISION.md`).  
7. Conservar `smoke_only` / `audit_only`, `native_audit_complete=false`, `common_adapter_allowed=false`.

## 3. Alcance

Laboratorio completo mientras rija la política; no solo sparql_llm.

## 4. Alternativas consideradas

| Alternativa | Veredicto |
|---|---|
| Autorizar $0.10 OpenRouter | Rechazada (“elijo coste 0”) |
| Modelo “free” OpenRouter | NOT_SELECTED (mutabilidad; no fijado) |
| LLM local como reproducción OpenRouter | SUBSTITUTION_NOT_NATIVE |
| Ejecutar acción seleccionada en 11C | Prohibido (solo documental) |

## 5. Consecuencias

- PE2 online: `deferred_by_zero_cost_policy` (no fallo técnico).  
- Cola operativa pasa a `ZERO_COST_NATIVE_REPRODUCTION_QUEUE.csv`.  
- `NATIVE_REPRODUCTION_QUEUE.csv` (Prompt 8) se conserva como snapshot histórico.

## 6. Evidencia que se conserva

CORE_OFFLINE; env/índice/preflight; protocolo API/SIB; audits; portafolio; artefactos Prompt 11 (modelo/cota como propuesta histórica).

## 7. Evidencia que no se obtendrá (bajo esta política)

POST `/chat` nativo con OpenRouter; fracción PE2 online vía LLM de pago.

## 8. Riesgos

- Sesgo a métodos offline-only.  
- Confundir NO-GO económico con software roto.  
- Sustituciones locales presentadas como nativas.

## 9. Condición de revisión

Nueva autorización explícita del investigador.

## 10. Relación con PE1–PE4

PE1 substantially_answered; PE2 partial_evidence (online deferred); PE3 not_started; PE4 partial_evidence.

## 11. Relación con el objetivo de largo plazo

La secuencia científica permanece; Fase 1 avanza por acciones ZERO_USD legales y locales.

# HUMAN_ZERO_COST_DECISION — Política de coste cero

**decision_id:** `ZERO_COST_POLICY_2026-07-21`  
**DECISION_DATE:** 2026-07-21  
**APPROVER_NAME:** EDMUNDO MORI ORRILLO  
**EVIDENCE_TAG:** `HUMAN_DECISION_VERIFIED`  
**Prompt:** 11C  
**RUN_ID_policy_formalization:** documental sobre gate modelo `20260721T100618Z`

---

## Texto recibido (investigador)

> elijo coste 0

Interpretación operativa obligatoria (Prompt 11C):

| Campo | Valor |
|---|---|
| `MAX_EXTERNAL_MONETARY_COST_USD` | **0.00** |
| `paid_api_execution_allowed` | **false** |
| `OPENROUTER_API_KEY_AUTHORIZED` | **false** |
| `POST_CHAT_AUTHORIZED` | **false** |
| `PROMPT_12_AUTHORIZED` | **false** |
| `PAID_CLOUD_COMPUTE_AUTHORIZED` | **false** |
| `PAID_LLM_AUTHORIZED` | **false** |

Contexto adicional del mismo día (misma política): rechazo explícito de clave OpenRouter, POST `/chat` y Prompt 12 de pago — ver también `ECONOMIC_NO_GO_DECISION.md` (interino) y este documento (formal 11C).

---

## Alcance de la decisión (zero-cost decision scope)

Aplica a **todo el laboratorio** mientras no haya nueva autorización explícita:

- sin APIs de pago;
- sin claves con saldo/facturación;
- sin cloud GPU/CPU de pago;
- sin LLMs hospedados de pago;
- sin OpenRouter (incluido “free” como sustituto no fijado);
- sin POST `/chat` del smoke online sparql_llm.

No invalida evidencia técnica ya obtenida (CORE_OFFLINE, env agent, caché e5, índice, preflight, audits, portafolio).

---

## Evidencia que permanece válida

- Prompt 5B CORE_OFFLINE `smoke_only`  
- Prompts 9–11 protocolo/prep/modelo (documental)  
- Prompt 10/10B entorno + índice + preflight  
- Auditorías WAVE_A–C  
- Portafolio de baselines  

## Condición de revisión

Solo una **nueva autorización explícita** del investigador puede:

- elevar `MAX_EXTERNAL_MONETARY_COST_USD` por encima de 0;
- autorizar clave OpenRouter / POST `/chat` / Prompt 12 chat;
- autorizar compute o LLM de pago.

Cursor no inventa firma manuscrita; esta decisión queda versionada con nombre y fecha del aprobador.

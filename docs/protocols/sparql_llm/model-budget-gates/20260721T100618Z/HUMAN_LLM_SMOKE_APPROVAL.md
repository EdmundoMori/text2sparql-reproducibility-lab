# HUMAN_LLM_SMOKE_APPROVAL — Prompt 11

**RUN_ID:** `20260721T100618Z`  
**Estado:** **REFUSED_ZERO_USD** (2026-07-21) — no se autoriza gasto.  
**Etiqueta:** resolución humana = rechazo económico (no firma de smoke).

---

## Resolución humana registrada

| Campo | Valor |
|---|---|
| Aprobador | EDMUNDO MORI ORRILLO |
| Fecha | 2026-07-21 |
| Política | SOLO $0; SIN Prompt 12 chat |
| Clave OpenRouter | no autorizada (crear ni usar) |
| POST `/chat` / modelos de pago | no autorizados |
| Gate resultante | `NO_GO_ECONOMIC` |
| Artefacto | `ECONOMIC_NO_GO_DECISION.md` |

El bloque de aprobación de gasto **no** se completa. Queda como registro histórico de lo que se habría requerido.

---

## Bloque de aprobación (NO USADO — rechazo vigente)

```text
APPROVAL_FOR: LOCAL_CHAT_API_ONE_QUESTION
LAB: text2sparql-reproducibility-lab
RUN_ID_GATE: 20260721T100618Z
APPROVER_NAME: _______________________________
APPROVAL_DATE: _______________________________

I AUTHORIZE a single controlled smoke with ALL of the following constraints:

1. MODEL_EXACT: openrouter/openai/gpt-4o-mini-2024-07-18
   OPENROUTER_SLUG: openai/gpt-4o-mini-2024-07-18
2. OBSERVED_PRICES_USD_PER_TOKEN (snapshot Prompt 11):
   prompt=0.00000015  completion=0.0000006
3. MAX_OPENROUTER_USD: 0.10
4. DEDICATED_KEY_REQUIRED: yes
   SUGGESTED_KEY_NAME: text2sparql-lab-local-chat-smoke-2026-07-21
   KEY_HARD_LIMIT_USD: 0.10
   KEY_NO_RESET: preferred if UI allows
   KEY_EXPIRY: 24-48 hours preferred
   KEY_MUST_NOT_BE_PERSONAL_GENERAL_KEY: yes
5. QUESTION_EXACT:
   How can I retrieve active site annotations in UniProt?
6. LOGICAL_LLM_INVOCATIONS: 2 (extract_user_question + call_model)
7. POSSIBLE_HTTP_ATTEMPTS: up to 6 (OpenAI SDK max_retries=2 ⇒ ≤3 per logical call)
8. enable_sparql_execution: false
9. use_tools: false
10. stream: false
11. NO benchmark / NO biodata / NO public MCP as native evidence
12. NO Virtuoso / NO adapters / NO upstream edits
13. After smoke: revoke or delete the dedicated key
14. I AUTHORIZE future Prompt 12 to perform ONE POST /chat under these constraints
15. I ACKNOWLEDGE:
    - max_tokens in HTTP body is ignored by the pinned handler
    - OpenRouter branch does not pass max_tokens to ChatOpenAI
    - TWO_CALL_BOUND ≈ USD 0.058; theoretical retry-amplified ceiling ≈ USD 0.174 if every attempt billed (UNKNOWN whether retries bill)
    - success is functional smoke_only evidence, NOT paper reproduction / NOT PE3
    - residual retry risk is accepted under the USD 0.10 hard key limit

CONFIRMATION_TEXT (type exactly):
I APPROVE LOCAL_CHAT_API_ONE_QUESTION UNDER THE PROMPT 11 CONSTRAINTS

SIGNATURE_OR_TYPED_NAME: _______________________________
```

---

## Lo que Prompt 11 ya fijó (no reescribir)

- Modelo y precios snapshot  
- Pregunta y request spec  
- Settings: `max_try_fix_sparql=0`, UniProt+void, índice lab  

## Lo que Prompt 11 NO hizo

- Crear/verificar la clave  
- Firmar por el investigador  
- Ejecutar `/chat`

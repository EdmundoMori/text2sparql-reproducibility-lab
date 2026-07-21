# COST_BOUND — Prompt 11

**RUN_ID:** `20260721T100618Z`  
**Modelo seleccionado:** `openrouter/openai/gpt-4o-mini-2024-07-18`  
**OpenRouter slug:** `openai/gpt-4o-mini-2024-07-18`  
**Snapshot:** `2026-07-21T10:08:25Z`  
**Evidencia precios:** `OFFICIAL_METADATA_VERIFIED`

## Precios observados

| Campo | Valor |
|---|---|
| prompt_price_per_token | 1.5e-07 USD |
| completion_price_per_token | 6e-07 USD |
| context_length | 128000 |
| max_completion_tokens | 16384 |

## Llamadas

| Concepto | Valor | Evidencia |
|---|---|---|
| logical_llm_invocations_expected | **2** | CODE_VERIFIED (extract + call_model) |
| openai SDK max_retries (root client) | **2** | ENVIRONMENT_VERIFIED (openai 2.46.0) |
| possible_http_attempts_per_logical_invocation | **≤ 3** (= 1 + max_retries) | ENVIRONMENT_VERIFIED / INFERENCE de semántica OpenAI SDK |
| possible_http_attempts_total (2 logical) | **≤ 6** | COST_BOUND_DERIVED |
| provider fallbacks | **UNKNOWN** | no demostrado estáticamente para OpenRouter |
| billable on retry | **UNKNOWN** | no afirmar facturación de reintentos fallidos |

## Cotas

### TWO_CALL_BOUND (techo de tokens, 2 invocaciones exitosas a tope)

```
TWO_CALL_BOUND = 2 * (context_length * prompt_price + max_completion_tokens * completion_price)
               = 2 * (128000 * 1.5e-07 + 16384 * 6e-07)
               = 0.058061 USD
```

Etiqueta: `COST_BOUND_DERIVED` — **deliberadamente conservadora**; no es coste esperado.

### Worst-case si cada intento HTTP facturara el techo completo

```
WORST_CASE_INCLUDING_RETRIES = 2 * (1 + max_retries) * per_call_bound
                             = 0.174182 USD
```

Esto **supera** $0.10. Semántica de facturación en retries: **UNKNOWN**.

## Propuesta de límite de clave

| Campo | Valor | Etiqueta |
|---|---|---|
| MAX_OPENROUTER_USD propuesto | **0.10** | PROPOSED |
| Justificación | TWO_CALL_BOUND (0.0581) < 0.10; clave dedicada = corte duro | PROPOSED |
| Riesgo residual | worst-case teórico con retries facturados ~0.1742 | HUMAN_DECISION_REQUIRED |
| Decisión automática de subir presupuesto | **no** | regla Prompt 11 |

La protección primaria es la **clave dedicada con límite duro $0.10**, no `max_tokens` del body (ignorado en rama OpenRouter, CODE_VERIFIED).

## Estado

`HUMAN_APPROVAL_PENDING` + aceptación humana del riesgo residual de retries.

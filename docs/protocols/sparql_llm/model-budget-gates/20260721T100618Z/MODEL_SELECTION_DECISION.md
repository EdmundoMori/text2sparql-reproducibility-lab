# MODEL_SELECTION_DECISION — Prompt 11

**RUN_ID:** `20260721T100618Z`  
**Fecha snapshot:** ver `OPENROUTER_MODEL_SNAPSHOT.json`  
**Gate documental:** `READY_FOR_HUMAN_APPROVAL`

---

## 1. Modelo seleccionado

**OpenAI GPT-4o-mini (2024-07-18)** — slug fechado.

## 2. Slug de configuración (Settings / request `model`)

```text
openrouter/openai/gpt-4o-mini-2024-07-18
```

## 3. Slug OpenRouter real (tras split `openrouter/`)

```text
openai/gpt-4o-mini-2024-07-18
```

## 4. Metadata (`OFFICIAL_METADATA_VERIFIED`)

| Campo | Valor |
|---|---|
| name | OpenAI: GPT-4o-mini (2024-07-18) |
| context_length | 128000 |
| max_completion_tokens | 16384 |
| pricing.prompt | 0.00000015 USD/token |
| pricing.completion | 0.0000006 USD/token |
| tools / tool_choice / seed / temperature | soportados |
| modality | text(+image+file) → text |

## 5. Coste

- `TWO_CALL_BOUND` ≈ **$0.0581** (`COST_BOUND_DERIVED`)  
- `MAX_OPENROUTER_USD` propuesto: **$0.10** (`PROPOSED`)  
- Worst-case teórico con retries facturados ≈ **$0.174** → `HUMAN_DECISION_REQUIRED` residual  

## 6. Parámetros efectivos esperados (Settings mínimo)

| Parámetro | Valor |
|---|---|
| temperature | 0.0 (Configuration/Settings; body ignorado) |
| seed | 42 |
| max_try_fix_sparql | 0 |
| enable_sparql_execution | false (request) |
| use_tools | false |
| stream | false |

## 7. Relación con upstream

- Default Settings upstream: `openrouter/openai/gpt-5.2` — **no** usado en este smoke.  
- Benchmarks upstream referencian `gpt-4o-mini` / variantes — compatibilidad de familia, **no** equivalencia paper.

## 8. Desviación respecto al default

Desviación **intencional** hacia slug fechado de menor coste para smoke funcional L0.

## 9. Razón científica

Smoke de ejecutabilidad del commit pin + índice lab; maximiza reproducibilidad de slug (fechado) y observa extract+generate+validate sin afirmar métricas del paper.

## 10. Razón económica

Menor precio entre candidatos elegibles; TWO_CALL_BOUND < $0.10.

## 11. Limitaciones

- Alias `openai/gpt-4o-mini` no seleccionado (mutabilidad).  
- `gpt-5.2-20251211` **no existe** en metadata (404).  
- `max_tokens` no enforceado en rama OpenRouter.  
- Retries SDK pueden multiplicar intentos HTTP.  
- Mean-pooling FastEmbed warning ajeno al LLM.

## 12. Revalidación obligatoria

Revalidar metadata OpenRouter **inmediatamente antes** de Prompt 12 (precios/disponibilidad pueden cambiar). Si el slug desaparece o el precio rompe la cota → nuevo gate, no sustituir en silencio.

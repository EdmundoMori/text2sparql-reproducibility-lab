# LOCAL_CHAT_API_MODEL_BUDGET_FINAL_GATE_REPORT — Prompt 11

**Fecha:** 2026-07-21  
**RUN_ID:** `20260721T100618Z`  
**method_id:** `sparql_llm`  
**Pinned commit:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**HEAD inicial:** `df41c8c5ad7404c491cb0164dbba7be37b40a228`  
**Inferencias LLM / POST /chat / SPARQL:** **0 / 0 / 0**

---

## 1. Objetivo

Cerrar documentalmente prerrequisitos económicos y operativos del futuro smoke `LOCAL_CHAT_API_ONE_QUESTION`: snapshot OpenRouter, selección de un modelo, cota de coste, retries del cliente, pregunta/request congelados, formulario humano sin firmar, y gate máximo `READY_FOR_HUMAN_APPROVAL`. **Sin** inferencia ni claves.

## 2. Estado técnico

| Capacidad | Estado |
|---|---|
| Agent Py3.11 (`20260721T084637Z`) | ready |
| Embedding exact cache (`20260721T092249Z`) | ready |
| `LAB_MINIMAL_INDEX` | INDEX_VERIFIED |
| FastAPI startup preflight | pass |
| POST `/chat` | no ejecutado |
| LLM / SPARQL | 0 / 0 |
| `reproduction_status` | `smoke_only` |
| `native_audit_complete` | `false` |
| `common_adapter_allowed` | `false` |
| phase | `1_native_audit` |

## 3. Metadata oficial

- GET sin auth a `https://openrouter.ai/api/v1/models` y `https://openrouter.ai/api/v1/model/<slug>`.
- Catálogo completo solo en workdir; SHA-256: `876ea047203ab02b48463bbd74e4578866981fe61bf5d7d9fd0959d2f6395628`.
- Extracto versionado: `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/OPENROUTER_MODEL_SNAPSHOT.json`.
- Etiqueta: `OFFICIAL_METADATA_VERIFIED`.

## 4. Candidatos

| ID | Slug | Resultado |
|---|---|---|
| A | `openai/gpt-4o-mini-2024-07-18` | **SELECTED** |
| B | `openai/gpt-4o-mini` | alias mutable — deferred |
| C | `openai/gpt-5.2` | default upstream; mayor coste; temperature no en supported_parameters — deferred |
| D | `openai/gpt-5.2-20251211` | **NOT_FOUND** (404) |

## 5. Modelo seleccionado

- Config: `openrouter/openai/gpt-4o-mini-2024-07-18`
- OpenRouter: `openai/gpt-4o-mini-2024-07-18`
- Prompt: `$0.00000015`/token; completion: `$0.0000006`/token
- context_length: 128000; max_completion_tokens: 16384
- tools / seed / temperature: soportados

## 6. Compatibilidad

Cumple criterios 1–10 del Prompt 11 (disponibilidad, texto, tools, seed/temperature, pricing, context, max completion, slug fechado, referencia upstream de familia, menor coste). **No** se afirma equivalencia paper ni default upstream.

## 7. Retries / timeouts

| Campo | Valor |
|---|---|
| langchain-openai | 1.3.5 |
| openai | 2.46.0 |
| ChatOpenAI.max_retries Field | null |
| root OpenAI client `max_retries` | **2** |
| timeout cliente tipado | connect=5 / read-write-pool=600 |
| Upstream OpenRouter branch | no pasa max_retries ni max_tokens |

Detalle: `RESOLVED_CLIENT_DEFAULTS.md`.

## 8. Llamadas lógicas

`logical_llm_invocations_expected = 2` con `use_tools=false`, `default_max_try_fix_sparql=0`, `enable_sparql_execution=false`, `stream=false` (`CODE_VERIFIED`).

## 9. Intentos HTTP

- Por invocación lógica: ≤ `1 + max_retries` = **3**
- Total teórico (2 logical): ≤ **6**
- Provider fallbacks / billable on retry: **UNKNOWN**
- **No** se declara `HTTP_ATTEMPTS_MAX=2`.

## 10. Cota económica

```
TWO_CALL_BOUND ≈ USD 0.058061
WORST_CASE_INCLUDING_RETRIES (si cada attempt facturara techo) ≈ USD 0.174182
MAX_OPENROUTER_USD propuesto = 0.10 (PROPOSED)
```

No se subió el presupuesto automáticamente pese al worst-case teórico. Protección primaria: **clave dedicada con límite duro**.

## 11. Límite de clave

Exigido para Prompt 12 (no creado en Prompt 11):

- Nombre sugerido: `text2sparql-lab-local-chat-smoke-2026-07-21`
- Límite: **$0.10**; sin reset si UI lo permite; expiración 24–48 h
- No reutilizar clave personal general; revocar tras smoke

## 12. Pregunta

```text
How can I retrieve active site annotations in UniProt?
```

Congelada; `Active_Site_Annotation` en índice lab (contexto, no gold).

## 13. Request

`LOCAL_CHAT_SMOKE_REQUEST_SPEC.json` — documental; **no ejecutado**.

Notas `CODE_VERIFIED`: body `max_tokens`/`temperature` ignorados; `validate_output` no mapea a `enable_output_validation`; validación por default Settings; repair bloqueado por `max_try_fix_sparql=0`.

## 14. Desviaciones

- Modelo ≠ default upstream `openrouter/openai/gpt-5.2`
- `max_try_fix_sparql=0` vs upstream default 3
- Smoke L0 ≠ benchmark / paper metrics

## 15. Riesgos

1. `max_tokens` no enforceado en rama OpenRouter.  
2. Retries pueden elevar intentos HTTP (techo teórico > $0.10 si se facturaran).  
3. Precios/disponibilidad pueden cambiar antes de Prompt 12.  
4. Alias no usado; D ausente.

## 16. Gate

**`READY_FOR_HUMAN_APPROVAL`**

No GO. Sin firma + clave limitada no se autoriza POST `/chat`.

## 17. Autorización pendiente

Formulario: `HUMAN_LLM_SMOKE_APPROVAL.md` — **sin firmar**.  
Cursor no completa el nombre del investigador.

## 18. Siguiente paso

Tras firma humana + clave limitada verificada: **Prompt 12 — Ejecución controlada de LOCAL_CHAT_API_ONE_QUESTION**.  
Prompt 11 no redacta ni ejecuta Prompt 12.

## 19. Relación con PE2

Aporta evidencia documental de preparación online (modelo, cota, request). PE2 sigue **partial_evidence** hasta ejecución del smoke. No cierra PE3.

## 20. Smoke ≠ reproducción

Éxito futuro de `/chat` = smoke funcional (`smoke_only`). **No** implica `partially_reproduced` / `reproduced`. Fase 1 permanece abierta; `native_audit_complete=false`; `common_adapter_allowed=false`.

---

## Artefactos

Directorio: `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/`  
Logs: `logs/preparation/sparql-llm-model-budget-gate/20260721T100618Z/`

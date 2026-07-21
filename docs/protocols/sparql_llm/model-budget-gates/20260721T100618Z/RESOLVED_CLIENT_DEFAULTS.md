# RESOLVED_CLIENT_DEFAULTS — Prompt 11

**RUN_ID:** `20260721T100618Z`  
**Imagen:** `text2sparql-lab/sparql-llm-agent-py311:20260721T084637Z`  
**Inspección:** Docker `--network none`; sin claves; sin `agent.main`; sin FastEmbed; sin Qdrant.  
**Evidencia:** `ENVIRONMENT_VERIFIED` (pip freeze Prompt 10 + inspección en vivo).

---

## 1. Versiones resueltas

| Paquete | Versión |
|---|---|
| `langchain-openai` | 1.3.5 |
| `openai` | 2.46.0 |

Fuente adicional: `logs/preparation/sparql-llm-local-chat-api/20260721T084637Z/pip-freeze.txt`.

---

## 2. `ChatOpenAI` (langchain-openai) — campos

Inspección de `ChatOpenAI.model_fields` e instancia con `api_key` dummy (sin request):

| Campo | Default observado | Notas |
|---|---|---|
| `max_retries` | `null` en Field / instancia | No fijado explícitamente por langchain en este path |
| `request_timeout` | `null` | |
| `streaming` | `false` | |
| `temperature` | `null` hasta override | Upstream pasa `configuration.temperature` |
| `seed` | `null` hasta override | Upstream pasa `configuration.seed` |
| `max_tokens` | `null` | **Rama OpenRouter no lo pasa** (`CODE_VERIFIED` en `agent/utils.py`) |

---

## 3. Cliente OpenAI subyacente (`root_client`)

Tras construir `ChatOpenAI(...)`, `root_client` es `openai.OpenAI`:

| Atributo | Valor | Evidencia |
|---|---|---|
| `max_retries` | **2** | `ENVIRONMENT_VERIFIED` |
| `timeout` en cliente tipado OpenAI() directo | `Timeout(connect=5.0, read=600, write=600, pool=600)` | `ENVIRONMENT_VERIFIED` |
| `root_timeout` vía langchain wrapper | `None` visible en atributo | posiblemente delegado; **UNKNOWN** detalle exacto de httpx |

---

## 4. Semántica de retries

| Concepto | Valor | Etiqueta |
|---|---|---|
| `logical_llm_invocations` | 2 (extract + call_model) | `CODE_VERIFIED` |
| `max_retries` (OpenAI SDK) | 2 | `ENVIRONMENT_VERIFIED` |
| `possible_http_attempts_per_logical_invocation` | ≤ **1 + 2 = 3** | `INFERENCE` estándar SDK OpenAI (intento inicial + reintentos) |
| `possible_http_attempts` (2 logical) | ≤ **6** | `COST_BOUND_DERIVED` |
| `provider fallbacks` OpenRouter | UNKNOWN | no demostrado estáticamente |
| `billable requests` en reintento | UNKNOWN | no afirmar |

**No** se declara `HTTP_ATTEMPTS_MAX=2`.

---

## 5. Upstream OpenRouter branch (`CODE_VERIFIED`)

```python
ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model=model_name,  # tras split openrouter/
    temperature=configuration.temperature,
    api_key=...,
    seed=configuration.seed,
)
```

No pasa: `max_tokens`, `max_retries`, `timeout` explícitos → prevalecen defaults del stack resuelto.

---

## 6. Log

Ver `logs/preparation/sparql-llm-model-budget-gate/20260721T100618Z/client-defaults.log`.

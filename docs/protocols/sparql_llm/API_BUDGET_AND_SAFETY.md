# Presupuesto y seguridad API — SPARQL-LLM (futuro smoke)

**Estado:** valores marcados `PROPOSED` — **requieren aprobación explícita del investigador** antes de cualquier llamada LLM o descarga.  
**Commit pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3`  
**Acción cubierta:** `LOCAL_CHAT_API_ONE_QUESTION`

---

## 1. Principios

1. Mínima red necesaria.  
2. Una sola acción futura seleccionada.  
3. Secretos solo en entorno local gitignored; nunca en git.  
4. No confundir disponibilidad de servicio público con reproducción nativa.  
5. Prompt 9 **no** gasta presupuesto (cero llamadas).

---

## 2. Límites PROPOSED (aprobación pendiente)

| Parámetro | Valor PROPOSED | Justificación |
|---|---|---|
| `MAX_QUESTIONS` | **1** | Smoke PE2 mínimo |
| `MAX_LLM_MODELS` | **1** | Default Settings o override documentado único |
| `MAX_REPAIR_LOOPS_OBSERVED` | ≤ `default_max_try_fix_sparql` (3) | Bound de código; no aumentar |
| `enable_sparql_execution` | **false** | Omite `query_sparql` en agent path (`CODE_VERIFIED`) |
| `use_tools` | **false** | Camino grafo default |
| `stream` | **false** | Respuesta JSON auditable |
| `MAX_ENDPOINTS_IN_SETTINGS` | **1** (UniProt + void local) | Reducir indexación |
| `FORCE_INDEX` | **false** | Evitar reindex completo |
| `AUTO_INIT` | **false** si índice prebuilt; else init mínimo aprobado | Control de side-effects |
| `ALLOW_PUBLIC_MCP_AS_NATIVE` | **false** | Solo availability check |
| `ALLOW_BENCHMARK_SCRIPTS` | **false** en el smoke L0 | L1/L2 separados |
| `MAX_OPENROUTER_USD` | **TBD — investigador** | Rellenar antes de GO |
| `TIMEOUT_CHAT_SECONDS` | **120** (PROPOSED) | Evitar hang indefinido |
| `LOG_REDACTION` | obligatorio | API keys / Authorization |

---

## 3. Secretos y manejo

| Secreto | Almacenamiento | Exposición en artefactos |
|---|---|---|
| `OPENROUTER_API_KEY` | `.env` local / secret store | `[REDACTED]` |
| `CHAT_API_KEY` | opcional; si se usa, mismo tratamiento | `[REDACTED]` |
| `LOGS_API_KEY` | no necesario para smoke L0 | n/a |

Checklist seguridad (`PROPOSED`):

- [ ] `.env` en `.gitignore`  
- [ ] No pegar keys en markdown de audit  
- [ ] Rotar key si se filtra en logs  
- [ ] Desactivar Langfuse/Sentry en smoke  

---

## 4. Side-effects que requieren pre-aprobación (Prompt 10)

Aunque Prompt 10 no llama LLM, puede implicar:

- Descarga FastEmbed `intfloat/multilingual-e5-large`  
- Escritura en `data/vectordb`  
- Posible red a endpoints/homepages si `init_vectordb` corre con lista amplia  

Cada uno debe constar en el plan de Prompt 10 con opt-in.

---

## 5. Criterios de aborto de seguridad (futuro)

Abortar inmediatamente si:

1. Se supera `MAX_QUESTIONS`.  
2. Se detecta ejecución SPARQL no intencional (`enable_sparql_execution` no false).  
3. Se inicia biodata/benchmark completo.  
4. Se usa MCP público como evidencia nativa.  
5. El gasto estimado supera `MAX_OPENROUTER_USD`.

---

## 6. Registro de aprobación

| Campo | Valor |
|---|---|
| Aprobador | _pendiente_ |
| Fecha aprobación | _pendiente_ |
| `MAX_OPENROUTER_USD` aprobado | _pendiente_ |
| Notas | Gate actual: **CONDITIONAL_GO** hasta firmar esta sección |

Sin esta aprobación, el smoke LLM permanece bloqueado aunque el entorno técnico esté listo.

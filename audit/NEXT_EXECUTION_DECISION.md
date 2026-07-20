# NEXT_EXECUTION_DECISION — Prompt 8

**Fecha:** 2026-07-20  
**Artefacto de gate:** `audit/NATIVE_AUDIT_COMPARATIVE_GATE.md`  
**Estado:** documental únicamente — sin instalación ni ejecución

---

## 1. Acción seleccionada

Definición documental del protocolo API/SIB de SPARQL-LLM, sin llamadas de API, sin endpoints SPARQL vivos y sin nuevo smoke CORE_OFFLINE.

## 2. Método o prerrequisito

**Método:** `sparql_llm` (SPARQL-LLM).  
**Prerrequisito cubierto:** frontera offline (CORE_OFFLINE `smoke_only`, Prompt 5B) ya validada; falta protocolizar el camino online/API antes de cualquier smoke con clave.

## 3. Tipo

`protocol_definition`

## 4. Evidencia que la justifica

| Hecho | Etiqueta |
|---|---|
| Licencia MIT confirmada (`LICENSE.txt`) | LEGAL_VERIFIED |
| Static audit WAVE_A complete | CODE_VERIFIED |
| Prompt 5A host Py3.10 → `setup_failed` | EXECUTION_VERIFIED |
| Prompt 5B Docker Py3.11 → `smoke_only` CORE_OFFLINE | EXECUTION_VERIFIED |
| Virtuoso / TEXT2SPARQL local BLOCKED | CODE_VERIFIED / MACHINE_PROFILE |
| `api_smoke_ready: conditional` sin protocolo de shapes/límites | CODE_VERIFIED / INFERENCE |
| Único método con ejecución parcial; resto `audit_only` | EXECUTION_VERIFIED / CODE_VERIFIED |
| Regla lexicográfica: legal → evidencia nueva PE2 → protocolo indefinido → viable documental → valor distinto al smoke 5B → coste bajo → sin sustituir método | INFERENCE (criterio de gate) |

## 5. Valor científico esperado

Cerrar la especificación operativa del único camino nativo condicional viable tras el smoke offline: qué endpoints/API keys, formas request/response, límites offline vs online, y criterios de éxito/fallo de un smoke API futuro. Evita convertir un smoke API improvisado en “reproducción” y prepara evidencia incremental de PE2 sin fingir PE3.

## 6. Qué pregunta experimental ayuda a responder

- **PE2 (parcial):** acota qué fracción del método es ejecutable *online* de forma controlada, separada del CORE_OFFLINE ya verificado.  
- **PE4 (refino):** cataloga barreras API_MUTABILITY / ENDPOINT antes de gastar clave.  
- **No PE3:** el Prompt 9 no reproduce métricas del paper.

## 7. Recursos

- Solo lectura de `upstream/sparql_llm`, audits WAVE_A, `environments/sparql_llm/`.  
- Sin GPU, sin pip/Docker nuevo, sin red a APIs ni endpoints.  
- Tiempo: documental (horas, no cómputo).

## 8. Riesgos

- Sobre-especificar un protocolo que el código no implemente tal cual (mitigar: etiquetar CODE_VERIFIED vs README_REPORTED vs INFERENCE).  
- Presión a “probar ya” la API en el mismo prompt (mitigar: restricción dura sin llamadas).  
- Confundir protocolo con reproducción del paper (mitigar: stop conditions y estados `smoke_only` inalterados).

## 9. Restricciones

- Prosa técnica en español; solo documentación.  
- **Prohibido:** pip/conda/Docker/apt; imports upstream ejecutados; API calls; SPARQL endpoints; descargas; train/infer; adapters; cambiar `reproduction_status`; `native_audit_complete=true`; `common_adapter_allowed=true`.  
- No tercer CORE_OFFLINE.  
- No Virtuoso.

## 10. Criterio GO

El Prompt 9 se considera exitoso si entrega un documento de protocolo que incluya, como mínimo:

1. Endpoints / entrypoints API o MCP relevantes (rutas o comandos documentados).  
2. Claves/variables de entorno requeridas (nombres, no secretos).  
3. Formas request/response o contratos observables en código/README.  
4. Límites explícitos offline (ya cubierto por CORE_OFFLINE) vs online.  
5. Criterios de éxito y fallo para un **futuro** smoke API controlado.  
6. Checklist GO/NO-GO hacia ese smoke (sin ejecutarlo).

## 11. Criterio NO-GO

No proceder a smoke API (ni en Prompt 9 ni inmediato) si:

- Faltan shapes o claves documentadas con evidencia etiquetada.  
- Se requeriría Virtuoso o Compose ausente.  
- El único camino implica gasto no presupuestado o endpoints no acotados.  
- Se pretendiera declarar PE3 o `partially_reproduced` solo con protocolo.

## 12. Stop conditions

- Cualquier intento de llamada real a OpenRouter/OpenAI/SIB.  
- Cualquier install o rebuild de índice e5.  
- Modificar `upstream/`.  
- Abrir adapters o evaluación común.  
- Seleccionar un segundo GO_NEXT en paralelo.

## 13. Por qué las alternativas no fueron seleccionadas ahora

| Alternativa | Clase | Motivo de aplazamiento |
|---|---|---|
| SPARQL-LLM API smoke | GO_AFTER_ENVIRONMENT | Debe esperar al protocolo (esta decisión). |
| RDF-config source/license + Ruby | HOLD_LEGAL → GO_AFTER_ENVIRONMENT | Legal del generador primero; Ruby install no es GO_NEXT. |
| SGPT env / reduced train | HOLD_MISSING_MODEL / DOCUMENT_ONLY | Sin checkpoints; train reducido ≠ Table 4; métricas anómalas. |
| mKGQAgent run / env ejecutable | HOLD_LEGAL | LICENSE_NOT_CONFIRMED; hosts hardcodeados; double e5. |
| FIRESPARQL offline metrics | DOCUMENT_ONLY / HOLD_MISSING_CODE | Results≠repro; runner CODE_NOT_FOUND; trainer ausente. |
| CoT env / install | HOLD_HARDWARE + HOLD_LEGAL | 34B vs 6 GiB; embeddings ausentes; licencia no confirmada. |

## 14. Título exacto del próximo prompt

`Prompt 9 — Definición documental del protocolo API/SIB de SPARQL-LLM (sin llamadas de API)`

## 15. Alcance exacto del próximo prompt

Documentar endpoints, claves requeridas (nombres), formas request/response, límites offline vs online, y criterios de éxito/fallo para un smoke API controlado **futuro**. **Sin llamadas de API** en Prompt 9 si el alcance es solo protocolo. Preparar decisión GO/NO-GO para un smoke API posterior. No instalar, no ejecutar, no Virtuoso, no adapters, no cambiar estados de reproducción.

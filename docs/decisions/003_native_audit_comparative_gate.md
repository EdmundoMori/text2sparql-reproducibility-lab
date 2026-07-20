# Decisión 003 — Gate comparativo de auditoría nativa (Prompt 8)

**Fecha:** 2026-07-20  
**Estado:** Activa  
**Fase lab:** 1 — native audit (no cerrada)  
**Artefactos:** `audit/NATIVE_AUDIT_COMPARATIVE_GATE.md`, matrices CSV asociadas, `audit/NEXT_EXECUTION_DECISION.md`

---

## Contexto

Tras completar las auditorías estáticas WAVE_A–C, el laboratorio dispone de evidencia heterogénea: un único método con ejecución parcial (`sparql_llm`, `smoke_only` CORE_OFFLINE en Docker Py3.11) y cinco métodos en `audit_only`. Ninguno está `reproduced` ni `partially_reproduced`. Se requiere un gate formal que separe (a) cola de reproducción nativa, (b) portafolio científico de baselines, (c) barreras transversales y (d) una sola siguiente acción, sin puntuación opaca única.

## Decisión

1. **Exactamente una acción `GO_NEXT`:** definición documental del protocolo API/SIB de SPARQL-LLM (`protocol_definition`), sin llamadas de API.  
2. **Título del siguiente prompt:** `Prompt 9 — Definición documental del protocolo API/SIB de SPARQL-LLM (sin llamadas de API)`.  
3. **Conservar** diversidad metodológica en el portafolio de baselines aunque varios métodos no sean ejecutables en la laptop.  
4. **No cerrar** Fase 1; mantener `native_audit_complete: false` y `common_adapter_allowed: false` en todos los métodos activos.  
5. **No alterar** `reproduction_status` actuales (`sparql_llm=smoke_only`; resto `audit_only`).  
6. **TeBaQA** permanece `historical_reference` — mención breve, sin fila en matrices de los seis métodos activos.

## Alternativas consideradas y aplazadas

| Alternativa | Veredicto | Razón breve |
|---|---|---|
| Smoke API SPARQL-LLM inmediato | Aplazado (`GO_AFTER_ENVIRONMENT`) | Requiere protocolo previo. |
| Install Ruby / smoke RDF-config | Aplazado (`HOLD_LEGAL` → luego env) | Generador LICENSE_NOT_CONFIRMED; Ruby ABSENT. |
| Entorno o train reducido SGPT | Aplazado (`HOLD_MISSING_MODEL` / `DOCUMENT_ONLY`) | Checkpoints ausentes; no es Table 4. |
| Ejecutar mKGQAgent | Aplazado (`HOLD_LEGAL`) | Licencia no confirmada; hosts hardcodeados. |
| Métricas offline FIRESPARQL | Aplazado (`DOCUMENT_ONLY` / `HOLD_MISSING_CODE`) | Results≠repro; runner ausente. |
| Install/env CoT-SPARQL | Aplazado (`HOLD_HARDWARE` + `HOLD_LEGAL`) | 34B; embeddings ausentes. |

## Criterios (regla lexicográfica)

Orden obligatorio de decisión (sin suma de puntos):

1. Legalidad del uso propuesto.  
2. Evidencia nueva sobre reproducibilidad nativa.  
3. Protocolo/componente suficientemente definido (si no → definir protocolo).  
4. Viabilidad técnica con recursos conocidos.  
5. Valor metodológico distinto a lo ya comprobado.  
6. Coste/tiempo/riesgo proporcionales.  
7. No sustituir silenciosamente el método publicado.

## Consecuencias

- El Prompt 9 es **solo documental** respecto al protocolo API/SIB.  
- Un smoke API controlado queda como candidato **posterior**, sujeto a GO/NO-GO del protocolo.  
- Métodos con alto valor científico pero bloqueo legal/hardware/código permanecen en el portafolio sin forzarse a ejecución local.  
- Tracks incompatibles (end-to-end, oracle entities, agentic, domain-specific, CoT+grounding) no se compararán en una sola tabla de rendimiento.

## Limitaciones

- El gate no mide calidad intrínseca de los papers.  
- La factibilidad laptop ≠ invalidez científica.  
- `LICENSE_NOT_CONFIRMED` no implica “método inválido”, pero bloquea modificación, adapters y redistribución.  
- PE3 permanece `not_started`.

## Evidencia

- Matrices WAVE_A/B/C; smokes 5A/5B; audits por método; `LICENSE_MATRIX.csv`; `METHOD_REGISTRY.yaml`; `MACHINE_PROFILE.md`.  
- Artefactos de esta decisión: ver `audit/NATIVE_AUDIT_*`, `audit/SCIENTIFIC_BASELINE_PORTFOLIO.csv`, `audit/REPRODUCIBILITY_BARRIER_MATRIX.csv`, `audit/NEXT_EXECUTION_DECISION.md`.

## Condición de revisión futura

Revisar esta decisión cuando ocurra al menos uno de:

- Cierre del protocolo API/SIB (Prompt 9) con GO hacia smoke API; o NO-GO documentado.  
- Aclaración de licencia de `mkgqagent`, `rdfconfig_llm` (generador), `cot_sparql` o `firesparql` (código).  
- Aparición de checkpoints SGPT o trainer/runner FIRESPARQL.  
- Disponibilidad de GPU externa suficiente para CoT 34B o FT FIRESPARQL.  
- Cierre explícito de PE2/PE3/PE4 o transición planificada a evaluación común (fase posterior).

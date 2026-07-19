# NEXT_PROMPT_GUIDANCE — Qué debe proponer ChatGPT a continuación

**Fecha:** 2026-07-19  
**Estado lab:** WAVE_A static audit **complete**; sin installs ni experimentos.

## Prompt recomendado (prioridad 1)

**Título sugerido:** Prompt 4B — Environment definition WAVE_A (sin install)

**Objetivo:** Materializar specs de entorno y comandos *futuros* verificables por método WAVE_A, cerrando gaps detectados en la auditoría estática:

- `sparql_llm`: pip/Poetry vs ausencia de `uv`; alternativa a Compose (`docker run` Qdrant); 1 worker (no 6); env names (sin `.env.example`); **excluir** Virtuoso/Text2SPARQL full del plan local.
- `mkgqagent`: LICENSE; endpoints hardcodeados; `requests` faltante; RAM e5-large con **un solo agente** (evitar doble carga al import); aclarar que pool shipped ≠ trazas offline del paper.
- `rdfconfig_llm`: completar deps (pandas/munkres/scipy/tqdm); Ruby/Bundler; política de **copia de trabajo** (no mutar `upstream/**/sparql.yaml`); elegir árbol rdf-config (vendored vs pin companion).

**Salidas esperadas:**

- `environments/sparql_llm/README.md` (+ opcional `requirements.lock` *documental*, no instalado)
- `environments/mkgqagent/README.md`
- `environments/rdfconfig_llm/README.md`
- Actualizar `WAVE_A_EXECUTION_READINESS.md` columna environment_definition
- Actualizar `PLAN_SYNC.md` + este archivo + `ARTIFACT_INDEX.md` + push

**Restricciones:** sin `pip/poetry/bundle/npm install`, sin Docker build/run, sin API calls, sin modificar `upstream/`.

## Alternativa (prioridad 2)

**Offline micro-smoke solo `sparql_llm`:** instalar deps core en venv del lab (fuera de upstream) y ejecutar tests de componentes/validación VoID local; etiquetar `smoke_only` si aplica; **no** reproducción. Solo si el investigador acepta install.

## No proponer aún

- Smoke API multi-método en un solo prompt.  
- Train / fine-tune / WAVE_B–C ejecución.  
- Adapters (`common_adapter_allowed` sigue false).  
- Integrar código `LICENSE_NOT_CONFIRMED`.

## Formato del prompt a Cursor

Incluir siempre: actualizar `PLAN_SYNC.md` + índice + push GitHub al cerrar.

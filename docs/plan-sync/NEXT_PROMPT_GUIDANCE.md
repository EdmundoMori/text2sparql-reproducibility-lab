# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 13A — SGPT Z2 CPU build + preflight **PASS**

## Prompt recomendado (único)

**Título:** Prompt 13B — Cierre documental del entorno SGPT Z2 y decisión de cola ZERO_COST (sin Z3; sin train).

**Método:** `sgpt`  
**Objetivo:** Congelar evidencia RUNTIME_VERIFIED del Z2, actualizar cola ZERO_COST, decidir explícitamente si el siguiente paso es (a) NLTK data autorizado, (b) otro método $0, o (c) diferir. **Sin** GPT-2, **sin** train, **sin** Table 4.

**Restricciones:** ZERO_COST; no instalar más sin nueva autorización; conservar `audit_only`.

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

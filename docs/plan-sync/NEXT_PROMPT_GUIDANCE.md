# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt **11C** — política coste cero; online sparql_llm `NO_GO_ECONOMIC_ZERO_COST_POLICY`

## Prompt recomendado (único)

**Título:** Prompt 12 — Definición documental de entorno SGPT (ZERO_COST; sin train; sin Table 4)

**Método:** `sgpt`  
**Clase:** `GO_NEXT_ZERO_COST`  
**Acción:** `SGPT_ENVIRONMENT_DEFINITION` (Z1)

**Objetivo:** Documentar entorno reproducible (deps/pins, datos, límites RAM/VRAM, harness, blocked checkpoints) hacia un futuro smoke reducido etiquetado. Sin entrenamiento. Sin afirmar Table 4.

**Restricciones:**
- `MAX_EXTERNAL_MONETARY_COST_USD = 0.00`  
- Sin OpenRouter / paid API / POST `/chat`  
- Sin train / inferencia / descarga no autorizada  
- Sin adapters; `native_audit_complete=false`; `common_adapter_allowed=false`  
- Conservar `reproduction_status=audit_only` para sgpt  

**Condición de éxito:** especificación de entorno + checklist hacia Z2 (data/metric preflight) + stop conditions.

## No proponer

- Prompt 12 chat (`LOCAL_CHAT_API_ONE_QUESTION`) — **CANCELLED**  
- rdfconfig legal como GO_NEXT (queda DOCUMENT_ONLY en cola ZERO_COST)  
- Modelos “free” OpenRouter o LLM local como nativo  

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 12 — entorno SGPT documental; gate **`CONDITIONAL_DEPENDENCY_RESOLUTION`**

## Prompt recomendado (único)

**Título:** Prompt 12B — Resolución documental de pins SGPT mediante metadata oficial y compatibilidad, ZERO_COST, sin instalación.

**Método:** `sgpt`  
**Objetivo:** Proponer pins candidatos (transformers, spaCy, numpy, tqdm, NLTK, etc.) usando **solo metadata pública oficial**, coherentes con Python 3.8 + torch 1.13.1 y con `IMPORT_COMPATIBILITY_REQUIREMENTS.csv`. Sin pip install, sin Docker build, sin descargas de modelos, sin train.

**Restricciones:**
- Coste externo $0.00  
- No inventar compatibilidad no verificada; etiquetar UNKNOWN/PROPOSED  
- No ejecutar Z2/Z3  
- Conservar `audit_only` / `native_audit_complete=false` / `common_adapter_allowed=false`

**Condición de éxito:** constraints documentales + justificación por símbolo + stop conditions; posible transición a READY_FOR_Z2_ENV_BUILD solo si digest+pins quedan verificables sin install (si no, seguir CONDITIONAL).

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

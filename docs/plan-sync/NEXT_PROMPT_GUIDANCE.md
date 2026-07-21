# NEXT_PROMPT_GUIDANCE

**Fecha:** 2026-07-21  
**Tras:** Prompt 12B — pins SGPT; gate **`READY_FOR_Z2_DOWNLOAD_AUTHORIZATION`**

## Prompt recomendado (único)

**Título:** Prompt 13A — Autorización y descarga controlada de imagen y paquetes SGPT Z2 + construcción del entorno CPU, ZERO_COST, sin GPT-2, sin modelos spaCy, sin train.

**Método:** `sgpt`  
**Objetivo:** Con autorización humana explícita: pull imagen `python@sha256:314bc2fb…`, instalar **solo** constraints Z2 (`torch==1.13.1+cpu`, `transformers==4.25.1`, numpy/tqdm/nltk/toolchain), freeze, import probe CPU, **sin** GPT-2, **sin** spaCy models, **sin** train/eval.

**Restricciones:**
- Coste externo $0.00 (solo artefactos públicos gratuitos)  
- No `utils.dptree` / no QALD9 BaseDataset / no Apex  
- Conservar `audit_only`; no Table 4  
- Reducir métricas Z2 a core si NLTK data no autorizada  

**Condición de éxito:** entorno Z2 construido + evidencia import/data/metric o fallo etiquetado; aún no Z3.

## Objetivo de fase

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

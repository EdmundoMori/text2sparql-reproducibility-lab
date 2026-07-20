# CLEANING_AND_REPAIR_AUDIT — firesparql

**Fecha:** 2026-07-20  
**Veredicto:** `CLEANING_SMOKE = blocked` (OpenAI). Cleaning es **requerido** en el pipeline reportado (existen `results/step2_clean_sparql/`).

---

## Implementación — `codes/sparql-cleaning-llm.py`

| Aspecto | Valor | Evidencia |
|---|---|---|
| Modelo | `gpt-4o` | `CODE_VERIFIED` |
| Auth | `OPENAI_API_KEY` | `CODE_VERIFIED` |
| I/O | carpeta txt step1 → carpeta step2 | CLI 2 args |
| Prompt | permite corregir spacing / repetición; pide solo SPARQL limpio | `CODE_VERIFIED` |

Clasificación lab: **`semantic_repair_possible`** — el prompt no se limita a whitespace; un LLM puede alterar tokens/estructura (`INFERENCE` de riesgo + texto del prompt `CODE_VERIFIED`).

Batch: `run_all_cleaning.sh` (Snellius).

---

## Evidencia de uso en resultados

`results/step2_clean_sparql/{vanilla,one_shot,ft,vanilla_rag,ft_rag}/…` con conteos ~513 por config alineados a step1 (`RESULT_FILE_VERIFIED`).  
Métricas BLEU/ROUGE se calculan sobre cleaned (`bleu_rouge.py` + CSVs en step2) (`CODE_VERIFIED` / `RESULT_FILE_VERIFIED`).

---

## Implicaciones

- Reproducción nativa del paper **depende** de API OpenAI (coste, no-determinismo, TOS).  
- Sin cleaning, BLEU/ROUGE/ejecución no son comparables a artefactos versionados.  
- Gate legal: keys + LICENSE código.

# Informe: Prompt 2 — verificar artículo, código y evidencia

**Fecha:** 2026-07-18  
**Resultado:** Completado  
**Clones:** 0  
**Ejecuciones:** 0  

## Artefactos

- `audit/PAPER_CODE_MAPPING.md`
- `audit/INITIAL_AUDIT_MATRIX.csv`
- `audit/INCLUSION_DECISIONS.md`
- `audit/RESOURCE_ESTIMATION.md`
- `METHOD_REGISTRY.yaml` (schema 0.2)

## Inclusión

| Decisión | Métodos |
|---|---|
| INCLUDE_PRIMARY | sparql_llm, mkgqagent, sgpt |
| INCLUDE_CONDITIONAL | cot_sparql, firesparql, rdfconfig_llm |
| HISTORICAL_ONLY | tebaqa |
| EXCLUDE / PENDING | ninguno |

## Incertidumbres clave marcadas UNKNOWN

- Licencias SPDX: mkgqagent, cot_sparql, firesparql, scott2121 generator  
- Celdas numéricas Table 4 de SGPT  
- Venue formal de SPARQL-LLM más allá de arXiv  
- Viabilidad exacta inferencia LLaMA-3-8B en 6 GB VRAM  

# Evaluación y métricas — CoT-SPARQL

**Fecha:** 2026-07-20  
**Etiquetas:** `PAPER_REPORTED` | `CODE_VERIFIED` | `NOT_FOUND` | `README_REPORTED`

---

## Implementación en repositorio

| Artefacto | Estado | Evidencia |
|---|---|---|
| Scripts `eval*.py` / métricas | **NOT_FOUND** | búsqueda estática árbol |
| Predicciones guardadas | **NOT_FOUND** | |
| Integración GERBIL / F1-QALD | **NOT_FOUND** | |
| BLEU / F1 query en código | **NOT_FOUND** (deps `rouge`/`nltk` en env no cableadas a eval) | `environment.yml` vs ausencia callers |
| Valid-query rate | parcial: HTTP 200 en `validation.py` (no agregación benchmark) | `CODE_VERIFIED` |

**Conclusión:** las métricas del paper son **`PAPER_REPORTED` only**; no hay harness reproducible en el clon (`CODE_VERIFIED` / `NOT_FOUND`).

---

## Métricas reportadas en paper (no ejecutadas aquí)

Fuente: `audit/PAPER_CODE_MAPPING.md` § cot_sparql + DOI 10.3233/SSW240028 (`PAPER_REPORTED`):

| Métrica | Rol paper | En código |
|---|---|---|
| BLEU | calidad string query | `NOT_FOUND` |
| F1 (query) | overlap tokens/estructura reportada | `NOT_FOUND` |
| F1-QALD / GERBIL | QA end-to-end | `NOT_FOUND` |
| % queries válidas | validez | solo check HTTP puntual |

Resultados citados en mapping (abstract / tablas): p.ej. mejoras F1 **+4.4%** QALD-10 y **+3.0%** QALD-9 vs SOTA; F1-QALD **63.87** pilot QALD-10; F1 query ej. **89.36** VQuAnDa / **70.45** QALD-9 (`PAPER_REPORTED`).

---

## Implicación lab

Cualquier cifra de métricas en artefactos lab debe etiquetarse **`PAPER_REPORTED`**, nunca `CODE_VERIFIED` / `DATA_VERIFIED` de esta pasada. Reproducción nativa de tablas = **not_ready**.

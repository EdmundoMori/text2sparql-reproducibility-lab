# GENERALITY_AND_KG_USAGE_AUDIT — firesparql

**Fecha:** 2026-07-20  
**Clasificación:** `domain_specific_reimplementation_required`

---

## Acoplamiento ORKG / SciQA

| Señal | Evidencia |
|---|---|
| Prompts hardcoded “Open Research Knowledge Graph (ORKG)” | `CODE_VERIFIED` generate_* |
| Propiedades RAG de ORKG (`orkg-property.json`) | `DATA_VERIFIED` / `CODE_VERIFIED` |
| Paths SciQA en todos los entrypoints principales | `CODE_VERIFIED` |
| Ejecución results contra ORKG (nombre dir) | `RESULT_FILE_VERIFIED` |

---

## DBLP

Datos y transform FT presentes (`DATA_VERIFIED`), instruction distinta (“dblp KG”), pero **pipeline/results/README table** centrados en SciQA/ORKG (`README_REPORTED` + ausencia results DBLP → `INFERENCE`).

---

## Portabilidad a otro KG (p.ej. modelos de IA)

Requeriría como mínimo: reescribir prompts, reindexar propiedades/ontologia, regenerar most_similar, re-FT o re-prompt, runner SPARQL del KG objetivo, y probablemente cleaning prompt. **No** hay capa ontology-agnostic (OWL/RDFS/SHACL) (`NOT_FOUND`).

EL/RL clásicos: **no** (`CODE_VERIFIED` ausencia).  
KG access at inference: vía prompts/RAG properties + ejecución offline post-hoc; no linker runtime.

---

## Adapters comunes lab

`COMMON_EVALUATION_ADAPTATION = legally_blocked` mientras `LICENSE_NOT_CONFIRMED` y pesos/adapters sin gate.

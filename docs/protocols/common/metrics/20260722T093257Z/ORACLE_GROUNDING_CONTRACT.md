# ORACLE_GROUNDING_CONTRACT

**Status:** `ORACLE_CONTRACT_DEFINED` · `ORACLE_MANIFEST_MATERIALIZATION_PENDING`

## Roles
SUBJECT_CONSTANT_IRI · OBJECT_CONSTANT_IRI · PREDICATE_IRI · TYPE_CLASS_IRI · PROPERTY_PATH_IRI · GRAPH_IRI · FUNCTION_IRI · DATATYPE_IRI · STANDARD_VOCABULARY_IRI · UNKNOWN_IRI_ROLE

## Reglas
- Manifest generado solo por evaluador.
- Gold SPARQL completa **nunca** al método; respuestas gold **nunca**.
- Cada variante declara exactamente qué roles consume.
- `sgpt_qk` ≠ `sgpt_q`; IA_ORACLE_GROUNDING fuera de ranking IA_Q_ONLY.
- Uso parcial del manifest se registra; no agregar campos oracle post-resultados.

Schema: `configs/common/ORACLE_GROUNDING_MANIFEST_SCHEMA.json`.

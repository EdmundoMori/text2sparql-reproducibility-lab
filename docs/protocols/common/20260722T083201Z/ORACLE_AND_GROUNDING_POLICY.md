# ORACLE_AND_GROUNDING_POLICY

**RUN_ID:** `20260722T083201Z` · ORACLE_CONTRACT_PENDING (Prompt 18 / T3)

## Tipos

GOLD_ENTITY_ORACLE · GOLD_RELATION_ORACLE · GOLD_SCHEMA_ORACLE · FIXED_EXTERNAL_ENTITY_LINKER · FIXED_EXTERNAL_RELATION_LINKER · METHOD_INTERNAL_LINKING · NOT_OBSERVABLE

## Reglas

- cualquier gold input → IA_ORACLE_GROUNDING;
- outputs linker externo → IA_FIXED_EXTERNAL_GROUNDING;
- linker interno = parte del método;
- linking F1 solo si outputs y gold observables;
- no inferir linking scores desde query final sin protocolo aprobado;
- no mezclar sgpt_q y sgpt_qk;
- no presentar oracle-grounding como end-to-end.

Detalle: ORACLE_CONTRACT_PENDING.

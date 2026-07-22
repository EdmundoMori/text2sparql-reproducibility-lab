# COMMON_INPUT_CONTRACT

**RUN_ID:** `20260722T083201Z` · ADAPTER_CONTRACT_PENDING (detalle por método en T4)

## Campos mínimos

protocol_version · dataset_id · dataset_version · split · item_id · language · question · query_form (si oficial) · graph_id · graph_version · information_access_track · schema_bundle_ref (nullable) · oracle_grounding_ref (nullable) · external_grounding_ref (nullable) · allowed_information_manifest · gold_query_ref · gold_answer_ref · exclusion_status

## Regla

El adapter solo puede acceder a la información declarada por el track. Acceso adicional invalida la comparabilidad.

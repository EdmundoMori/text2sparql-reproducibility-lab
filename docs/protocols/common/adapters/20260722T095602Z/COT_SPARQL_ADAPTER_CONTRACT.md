# COT_SPARQL_ADAPTER_CONTRACT

**Pin:** `063edd9868425e54010a0cb49ce585ed2186be4d` · IA_FIXED_EXTERNAL_GROUNDING

Input: question + retrieval manifest + external entity/relation grounding + model + prompt → final SPARQL.

## cot_native_external_services
Spotlight/Entity-Fishing/Falcon/REBEL; capturar+hash; freeze versions; sin comparabilidad si no congelables.

## cot_common_frozen_grounding
Futuro controlled variant; mismo manifest para todos; no = reproducción nativa; nuevo variant_id.

Retrieval: parquet/pkl train-only. HTTP validation = method-internal; HTTP200 ≠ answer correctness.

**CONTRACT_BLOCKED_LEGAL · CONTRACT_BLOCKED_RUNTIME · CONTRACT_BLOCKED_MISSING_ARTIFACT**

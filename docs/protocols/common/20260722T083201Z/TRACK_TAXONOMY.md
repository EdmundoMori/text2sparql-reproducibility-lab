# TRACK_TAXONOMY — Modelo ortogonal

**RUN_ID:** `20260722T083201Z` · Prompt 16 · PROTOCOL_DEFINED

## Eje A — INFORMATION ACCESS

| ID | Entrada permitida | Prohibido |
|---|---|---|
| IA_Q_ONLY | pregunta; idioma; id benchmark; endpoint/snapshot común; metadata pública | gold entities/relations/SPARQL; linkers externos; ejemplos test |
| IA_SCHEMA_COMMON | todo IA_Q_ONLY + bundle schema/VoID/ontología común versionado | bundles privados distintos por método sin variante |
| IA_ORACLE_GROUNDING | pregunta + entidades/relaciones gold versionadas | presentarse como end-to-end |
| IA_FIXED_EXTERNAL_GROUNDING | pregunta + outputs linker externo común congelado | tratar como question-only |
| IA_DOMAIN_NATIVE | datasets/KGs del dominio nativo | mezcla directa con QALD/LC-QuAD |
| IA_HISTORICAL | referencia histórica | ranking activo |

## Eje B — EXECUTION STYLE (tags)

ES_SCHEMA_RAG_VALIDATION · ES_AGENTIC_MULTI_CALL · ES_SUPERVISED_GENERATOR · ES_DETERMINISTIC_SCHEMA_CONSTRUCTION · ES_COT_RETRIEVAL · ES_DOMAIN_FINETUNED_RAG · ES_TEMPLATE_HISTORICAL

## Eje C — ADAPTATION REGIME

AR_ZERO_SHOT · AR_FEW_SHOT_TRAIN_ONLY · AR_SUPERVISED_TRAIN_SPLIT · AR_DOMAIN_RETRAINED · AR_NATIVE_RELEASED_ASSET · AR_ORACLE_INPUT

## Eje D — MODEL CONTROL

MC_NATIVE_BACKBONE y MC_CONTROLLED_BACKBONE se reportan por separado. No atribuir diferencia al método si cambió método y backbone a la vez.

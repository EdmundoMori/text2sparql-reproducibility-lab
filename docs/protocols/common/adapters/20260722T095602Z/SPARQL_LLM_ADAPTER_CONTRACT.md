# SPARQL_LLM_ADAPTER_CONTRACT

**Pin:** `3748730e3bd2df2595280b918269fdaadb9fc0c3` · MIT

## sparql_llm_schema_common_native
- Surface: POST /chat
- Input: question, model, schema/index prebuilt, `enable_sparql_execution=false`
- Track: IA_SCHEMA_COMMON
- Schema: common bundle fijado
- Documentar mismatch naming `validate_output` vs `enable_output_validation` (no afirmar control HTTP incorrecto)
- Output: una `final_sparql` explícita
- Internal SPARQL: disabled (generate-only)
- LLM fijado sin fallback; index hash fijado; no auto-init/download en benchmark
- Online: BLOCKED_POLICY bajo ZERO_COST
- Legal: MIT · Implementation: pendiente · G6I pending

## sparql_llm_schema_common_internal_feedback
- `enable_sparql_execution=true` · METHOD_INTERNAL_ENDPOINT_FEEDBACK
- Comparison group separado; no habilitado mientras G4 no satisfecho; no mezclar con generate-only

# MODEL_AND_LLM_CONTROL_POLICY

**RUN_ID:** `20260722T083201Z`

## Registrar en cada run futuro

provider · model_id · revision · quantization · context size · temperature · seed · max output tokens · stop sequences · tools · retry · fallback · system prompt hash · user template hash · few-shot example IDs · API date/version · local model artifact hashes

## Reglas

- no cambiar método y LLM simultáneamente en comparación causal;
- native vs controlled backbone separados;
- no fallback silencioso;
- no mutable `latest`;
- registrar coste incluso si 0;
- API de pago bloqueada bajo ZERO_COST;
- sin seed estable → NONDETERMINISTIC_UNCONTROLLED_PROVIDER.

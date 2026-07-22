# SGPT_ADAPTER_CONTRACTS

**Pin:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b`

## Preparation
Features sintácticas fijadas; versiones registradas. sgpt_q: sin gold. sgpt_qk: solo roles oracle autorizados; no answers/SPARQL gold como input. Derivaciones gold actuales → incompatibilidad explícita.

## Training
Fuera de test; train/dev; checkpoint+params+logs hashed; no on-demand train en inferencia.

## Inference
Un input; checkpoint RO; sin KG/endpoint; sin linking interno; output SPARQL string.

## sgpt_q — IA_Q_ONLY
oracle_grounding_ref=null

## sgpt_qk — IA_ORACLE_GROUNDING
Solo entidades/roles autorizados; coverage/consumption; no comparar vs Q_ONLY.

Blockers: payload, preprocessing conformance, checkpoint común, training protocol, G4/G5 runtime.

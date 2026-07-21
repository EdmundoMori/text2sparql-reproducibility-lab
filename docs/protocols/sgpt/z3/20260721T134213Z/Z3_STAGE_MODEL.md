# Z3_STAGE_MODEL

**RUN_ID:** `20260721T134213Z`  
**Etiqueta:** `PROPOSED_PROTOCOL`

## Z3-P0 — PROTOCOL_DEFINITION
- Prompt **14A** (este documento)
- Documental; sin descarga; sin train
- Estado: **en curso / cierre 14A**

## Z3-P1 — ARTIFACT_ACQUISITION
- Nueva autorización humana (formulario artefactos)
- GPT-2 exacto + tensorboardX
- Caché aislada; **sin** model load; **sin** train

## Z3-P2 — MODEL_AND_ENTRYPOINT_PREFLIGHT
- Red bloqueada
- Import `scripts.model`; import `train` sin `main`
- Load tokenizer/config/model desde path local
- Tokens especiales + resize
- Batch canario; P2A load-only; P2B forward no-grad **solo** si autorizado
- Sin backward/optimizer/checkpoint

## Z3-P3 — ONE_OPTIMIZER_STEP_TRAINING
- Autorización **independiente**
- Un paso esperado; entrypoint upstream; subset canario
- Eval/checkpoints inherentes; sin calidad; sin Table 4

## Z3-P4 — EVIDENCE_CLOSURE
- Inventario, checksums, clasificación, re-gate Fase 1

## Regla de autorización
Ninguna autorización de una etapa se reutiliza automáticamente en otra.  
Auth 13A (`AUTHORIZED_AND_CONSUMED_13A`) **no** cubre P1–P3.

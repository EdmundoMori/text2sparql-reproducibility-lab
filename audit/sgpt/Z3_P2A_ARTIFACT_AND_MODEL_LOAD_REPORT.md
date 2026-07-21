# Z3_P2A_ARTIFACT_AND_MODEL_LOAD_REPORT — Prompt 14B

**Fecha:** 2026-07-21  
**Execution RUN_ID:** `20260721T135432Z`  
**Protocol RUN_ID:** `20260721T134213Z`  
**Clasificación:** **`Z3_P2A_MODEL_LOAD_PREFLIGHT_PASS`**  
**Coste:** **0.00**  
**Aprobador:** EDMUNDO MORI ORRILLO (`HUMAN_DECISION_VERIFIED`)

## Autorización

`AUTHORIZED_AND_CONSUMED_14B_P1_P2A` — P2B **no**; train **no**; auth 13A **no** reutilizada.

## P1 — Artefactos

| Item | Resultado |
|---|---|
| GPT-2 revision | `607a30d783dfa663caf39e06633721c8d4cfcd7e` |
| Files | 5/5 REQUIRED; sizes+SHA OK; LFS OID pytorch_model.bin match |
| Forbidden formats | no descargados |
| tensorboardX | 2.5.1 |
| protobuf | 3.20.1 |
| Z2 pins | torch 1.13.1+cpu / transformers 4.25.1 **preserved** |
| Z3 image | `text2sparql-lab/sgpt-z3-py38:20260721T135432Z` (`sha256:3363d73b…`) |

## P2A — Model-load preflight

| Check | Resultado |
|---|---|
| import scripts.model | PASS |
| import train (no main) | PASS |
| tokenizer/config/model local | PASS |
| loading unexpected/mismatched | 0 / 0 |
| missing custom layers | 268 expected (encoder/decoder/pose/dep + buffers) |
| special tokens + resize | vocab 50263 |
| n_params | 223797504 |
| dtype | float32 |
| RSS after load | ~1774 MiB (<5 GiB) |
| Dataset canary + collate | PASS (train n=1) |
| expected optimizer steps | **1** |
| forward / train | **NOT_EXECUTED** |
| network during offline | blocked (`--network none` + NetworkGuard) |

## No afirmado

Table 4; PE3; training; forward; native reproduction.

## Estados

`audit_only`; `native_audit_complete=false`; `common_adapter_allowed=false`; checkpoint absent.

## Siguiente

Firma de `HUMAN_Z3_ONE_STEP_TRAINING_APPROVAL.md` → Prompt 14C (one-step training) **solo** tras autorización.

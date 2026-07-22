# ENVIRONMENT_GATE — SGPT

**Actualizado:** Prompt **14D** (cierre Z3 + re-gate)

## Gate Z2 (cerrado)

`Z2_ENV_READY_PREFLIGHT_PASS` · Auth 13A consumida

## Gate Z3 (cerrado smoke)

| Campo | Valor |
|---|---|
| P2A | `Z3_P2A_MODEL_LOAD_PREFLIGHT_PASS` |
| P2B | `Z3_P2B_NOGRAD_FORWARD_PASS` |
| One-step raw att.2 | `Z3_OTHER_FAILED` |
| One-step operativo | `Z3_ONE_STEP_REDUCED_TRAINING_PASS` + qualifier indirecto |
| **Gate Z3** | **`SGPT_NATIVE_AUDIT_CLOSED_SMOKE_ONLY`** |
| reproduction_status | `smoke_only` |
| native_audit_complete | `true` (smoke_only; full repro not achieved) |
| common_adapter_allowed | `false` |
| Table 4 / PE3 | **no** / `not_started` |
| Coste | **0.00** |

Detalle: `environments/sgpt/Z3_CLOSURE_GATE.md`

## Siguiente

**Prompt 15** — gate final Fase 1 (Q11), ZERO_COST, sin adapters. **No** nuevo train SGPT.

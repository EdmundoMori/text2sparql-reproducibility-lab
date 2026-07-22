# environments/sgpt — Entorno SGPT (ZERO_COST)

**Upstream pin:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` · MIT  
**Política:** `MAX_EXTERNAL_MONETARY_COST_USD = 0.00`

## Estado

| Capa | Estado |
|---|---|
| Z1 | `COMPLETE_DOCUMENTED` |
| Z2 | `COMPLETE_Z2_CORE_PREFLIGHT` |
| Z3 | **`SGPT_NATIVE_AUDIT_CLOSED_SMOKE_ONLY`** |
| `reproduction_status` | **`smoke_only`** (`reduced_training_smoke_only`) |
| `native_audit_complete` | `true` (full reproduction **not** achieved) |
| `common_adapter_allowed` | `false` |

Cierre: `audit/sgpt/Z3_CLOSURE_REPORT.md` · Gate: `Z3_CLOSURE_GATE.md`

## Pesos

Checkpoints/tokenizer/model bins solo en `workdir/` (gitignore). No publicar en Git.

## Siguiente

Prompt **15** — gate final Fase 1 (comparativo), ZERO_COST, sin adapters. Sin nuevo train sin auth.

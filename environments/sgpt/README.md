# environments/sgpt — Entorno SGPT (ZERO_COST)

**method_id:** `sgpt`  
**Upstream pin:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b`  
**Licencia:** MIT — `LEGAL_VERIFIED`  
**Política:** `MAX_EXTERNAL_MONETARY_COST_USD = 0.00`

## Estado (Prompt 13B)

| Campo | Valor |
|---|---|
| Z1 | `COMPLETE_DOCUMENTED` |
| Z2 | `COMPLETE_Z2_CORE_PREFLIGHT` |
| Gate | `Z2_ENV_READY_PREFLIGHT_PASS` |
| Auth 13A | `AUTHORIZED_AND_CONSUMED_13A` |
| Freeze SHA-256 | `916d4b76a980ed1b558eb3bb26122f5e6dca9e02ffaeb5ee8e553f7cd66e71a5` |
| `reproduction_status` | `audit_only` |

Build runtime (13A): `builds/20260721T114919Z/` — imagen Docker **fuera de Git**.

## Artefactos clave

| Path | Rol |
|---|---|
| `ENVIRONMENT_GATE.md` | Gate actual |
| `builds/20260721T114919Z/Z2_RUN_MANIFEST.yaml` | Manifiesto cerrado |
| `builds/20260721T114919Z/z2-resolved-freeze.txt` | Freeze congelado |
| `../audit/sgpt/Z2_EVIDENCE_MATRIX.csv` | Matriz evidencia |
| `../audit/NEXT_POST_Z2_ZERO_COST_DECISION.md` | Decisión post-Z2 |

## Siguiente

**Prompt 14A** — protocolo Z3 reduced training **documental** (sin GPT-2, sin train).

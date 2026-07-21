# ENVIRONMENT_GATE — SGPT

**Actualizado:** Prompt **13B** (cierre Z1/Z2)

| Campo | Valor |
|---|---|
| **Gate** | **`Z2_ENV_READY_PREFLIGHT_PASS`** |
| Z1 | `COMPLETE_DOCUMENTED` |
| Z2 | `COMPLETE_Z2_CORE_PREFLIGHT` |
| RUN_ID | `20260721T114919Z` |
| Autorización 13A | `AUTHORIZED_AND_CONSUMED_13A` (no reutilizable) |
| Imagen | `text2sparql-lab/sgpt-z2-py38:20260721T114919Z` (fuera de Git) |
| torch | `1.13.1+cpu` `PACKAGE_RUNTIME_VERIFIED` |
| transformers | `4.25.1` `PACKAGE_RUNTIME_VERIFIED` |
| Freeze SHA-256 | `916d4b76a980ed1b558eb3bb26122f5e6dca9e02ffaeb5ee8e553f7cd66e71a5` |
| Preflight | `Z2_ENV_IMPORT_DATA_METRIC_PASS` (core only) |
| GPT-2 / spaCy / NLTK data | **no** descargados |
| Coste | **0.00** |
| Table 4 | **no** |
| `reproduction_status` | `audit_only` |

## Prompt 13A/13B closure

- 13A: build + preflight runtime.  
- 13B: congelación freeze, matriz de evidencia, re-gate post-Z2.  
- Rebuild: **requiere nueva autorización**.

## Siguiente prompt (único)

**Prompt 14A — Definición documental del protocolo SGPT Z3 reduced training smoke, ZERO_COST, sin descarga de GPT-2 y sin train.**

→ `audit/NEXT_POST_Z2_ZERO_COST_DECISION.md`

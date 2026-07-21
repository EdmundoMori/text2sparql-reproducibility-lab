# environments/sgpt — Definición documental de entorno (Prompt 12)

**method_id:** `sgpt`  
**Upstream pin:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b`  
**Licencia:** MIT (`LICENSE.md`) — `LEGAL_VERIFIED`  
**Política:** `MAX_EXTERNAL_MONETARY_COST_USD = 0.00`  
**Prompt 12:** solo documental — **sin** install, download, train, inferencia ni Docker build.

## Artefactos

| Archivo | Rol |
|---|---|
| `ENVIRONMENT_SPEC.yaml` | Spec principal |
| `DEPENDENCY_MANIFEST.yaml` | Dependencias |
| `IMPORT_COMPATIBILITY_REQUIREMENTS.csv` | Símbolos a conservar |
| `RUNTIME_PROFILES.md` | Perfiles A/B/C |
| `DEPENDENCY_RESOLUTION_PLAN.md` | Cómo fijar pins en el futuro |
| `CONTAINER_STRATEGY.md` | Docker futuro |
| `Dockerfile.native-py38.template` | TEMPLATE_ONLY / DO_NOT_BUILD |
| `DATA_AND_ARTIFACT_CONTRACT.md` | Datos y split drift |
| `MODEL_AND_CHECKPOINT_BOUNDARY.md` | GPT-2 vs checkpoint SGPT |
| `METRIC_PREFLIGHT_BOUNDARY.md` | Métricas léxicas / anomalías |
| `RESOURCE_LIMITS.md` | RAM/VRAM |
| `Z2_DATA_METRIC_PREFLIGHT_SPEC.md` | Futuro Z2 |
| `FUTURE_COMMANDS.md` | Comandos no ejecutados |
| `ENVIRONMENT_GATE.md` | Gate documental |

## Gate actual

Ver `ENVIRONMENT_GATE.md` → **`CONDITIONAL_DEPENDENCY_RESOLUTION`**.

## Siguiente paso

**Prompt 12B** — resolución documental de pins (metadata oficial), sin instalación.

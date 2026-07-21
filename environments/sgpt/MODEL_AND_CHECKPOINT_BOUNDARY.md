# MODEL_AND_CHECKPOINT_BOUNDARY — SGPT

| Artefacto | Estado | Notas |
|---|---|---|
| GPT-2 base público (`gpt2`) | **not_downloaded** | Requerido para crear modelo desde pretrained; **no** es checkpoint SGPT |
| Checkpoint SGPT entrenado | **NOT_FOUND** | Ausente en repo |
| `outputs/` / `runs/` | **NOT_FOUND** | Ausentes localmente |
| Futuro checkpoint reducido lab | no creado | Etiqueta `REDUCED_TRAINING_SMOKE`; **no** nativo Table 4 |
| Checkpoints paper | no evidencias locales | PAPER_REPORTED ≠ disponible |

**Prompt 12:** no descargar GPT-2; no buscar pesos externos; no sugerir que GPT-2 base sustituye un checkpoint SGPT.


---

## Prompt 14A — Z3 protocol definition (añadido)

- RUN_ID: `20260721T134213Z`
- Gate Z3: `READY_FOR_Z3_ARTIFACT_PREFLIGHT_AUTHORIZATION`
- Variante: lcquad2 QUESTION_ONLY CPU canary 1/1/1; expected optimizer steps = 1 (validar pre-run)
- GPT-2: `openai-community/gpt2` @ `607a30d7…` — **NOT_DOWNLOADED**
- tensorboardX==2.5.1 — **NOT_DOWNLOADED**
- Auths: dos formularios UNSIGNED en `docs/protocols/sgpt/z3/20260721T134213Z/`
- Informe: `audit/sgpt/Z3_REDUCED_TRAINING_PROTOCOL_REPORT.md`
- Gate Z2 permanece cerrado: `Z2_ENV_READY_PREFLIGHT_PASS`
- Conservado: `audit_only`; PE3 `not_started`; sin train

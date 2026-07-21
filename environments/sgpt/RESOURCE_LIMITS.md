# RESOURCE_LIMITS — SGPT

**Host (MACHINE_VERIFIED / re-check Prompt 12):**

| Recurso | Valor |
|---|---|
| RAM WSL | ~7.4 GiB |
| RAM host Windows | ~16 GiB |
| VRAM | ~6 GiB (RTX 4050) |
| Paper | 2×12 GB |
| CPU | 8C / 16T |
| Disco `/` | ~921G libres |
| nvcc | ausente |
| Docker | disponible |
| Conda | ausente |

## Z2 (propuesto)

- CPU only; sin GPU  
- memory limit propuesta: **4g** (contenedor)  
- **2** CPUs  
- sin model download  
- timeout propuesto: **600s**  
- no workers múltiples  
- red bloqueada  

## Z3 (aún no aprobado)

- batch/subset **no** fijados  
- OOM → stop  
- no multi-GPU; no Apex; no distributed launch en smoke reducido  
- requiere Z2 pass + autorización descarga GPT-2


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

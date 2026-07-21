# Z3_REDUCED_TRAINING_PROTOCOL_REPORT — Prompt 14A

**Fecha:** 2026-07-21  
**RUN_ID:** `20260721T134213Z`  
**Acción:** PZ1 `GO_NEXT_ZERO_COST`  
**Gate:** `READY_FOR_Z3_ARTIFACT_PREFLIGHT_AUTHORIZATION`  
**Coste monetario externo:** **0.00**  
**Descargas binarias / install / model load / forward / train:** **0**

Protocolo: `docs/protocols/sgpt/z3/20260721T134213Z/`

---

## 1. Objetivo

Definir un protocolo conservador para un futuro smoke de entrenamiento reducido SGPT Z3, sin ejecutar ni descargar artefactos de modelo.

## 2. Alcance

Solo documentación + GET metadata pública (HF/PyPI). Sin Docker/pip/train/infer.

## 3. Estado Z1/Z2

Z1 `COMPLETE_DOCUMENTED`; Z2 `COMPLETE_Z2_CORE_PREFLIGHT`; auth 13A `AUTHORIZED_AND_CONSUMED_13A`.

## 4. Política ZERO_COST

`MAX_EXTERNAL_MONETARY_COST_USD = 0.00`. Auth 13A no reutilizable.

## 5. Entry point

`upstream/sgpt/train.py` — ver `NATIVE_ENTRYPOINT_CONSTRAINTS.md`.

## 6. Bugs y restricciones

`--epochs=-1` corrompe params; `--device` sobrescrito; `--dataroot` ignorado en `_loaddata`; `dep_mapping` hard-coded; `train_batch_size=2` en main vs recálculo en `train()`; `eval_only` incompleto.

## 7. Etapas Z3

P0 (este prompt) → P1 artifacts → P2 preflight → P3 one-step → P4 closure. Auth no transferible entre etapas.

## 8. Variante

`lcquad2` + **QUESTION_ONLY**; knowledge/masked/fp16/distributed = false; CPU; `REDUCED_SMOKE_NOT_PAPER_REPRODUCTION`.

## 9. Dataset canario

1/1/1; uids train=`8714`, val=`3988`, test=`6077`; no representativo; no para métricas.

## 10. Parámetros

`Z3_PARAMS_CANDIDATE.json`; LR `6.25e-5`; seed 42; batch 1; `--epochs 1` obligatorio.

## 11. Step budget

Fórmula: `(len(dl)//grad_accum)*epochs`; con canario **esperado documentado = 1**; validación pre-run obligatoria.

## 12. GPT-2

`openai-community/gpt2` @ `607a30d783dfa663caf39e06633721c8d4cfcd7e`; REQUIRED: config, `pytorch_model.bin` (~548 MB, LFS sha `7c5d3f4b…`), vocab, merges, tokenizer_config. **NOT_DOWNLOADED**.

## 13. SummaryWriter

`tensorboardX==2.5.1` (MIT; numpy+protobuf≤3.20.1). **NOT_DOWNLOADED**.

## 14. Entorno futuro

Derivar de imagen Z2; si ausente → nueva auth de rebuild; instalar solo TBX.

## 15. Model preflight

P2A load-only; P2B forward no-grad opcional — **no** autorizados en 14A.

## 16. Training contract

P3 one-step; resultado máximo `Z3_ONE_STEP_REDUCED_TRAINING_PASS` ≠ Table 4.

## 17. Recursos

P2: 2 CPU / 5 GiB / 900 s; P3: 2 CPU / 6 GiB / 3600 s / output 6 GiB (`PROPOSED_RESOURCE_BOUND`).

## 18–19. Side effects / outputs

Todo en workdir; no versionar pesos/checkpoints.

## 20–21. Evidencia / claim boundary

Máximo futuro: `reduced_training_smoke_only`. Conservar `audit_only`.

## 22. Riesgos

`Z3_RISK_REGISTER.csv` (R01–R19).

## 23. Autorizaciones

Dos formularios **UNSIGNED**: artefactos+preflight; one-step training.

## 24. Gate

**`READY_FOR_Z3_ARTIFACT_PREFLIGHT_AUTHORIZATION`**

## 25. Siguiente paso

Investigador firma `HUMAN_Z3_ARTIFACT_AND_MODEL_PREFLIGHT_APPROVAL.md`.  
Luego: **Prompt 14B — Descarga controlada de artefactos GPT-2 y preflight offline de carga SGPT Z3, ZERO_COST, sin train.**

## 26. PE1–PE4

PE1 substantially_answered; PE2 partial_evidence; PE3 **not_started**; PE4 partial_evidence (protocolo Z3 documentado).

## 27. Fase 1

Abierta.

## 28. Objetivo de largo plazo

reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

## 29. Conclusión conservadora

Protocolo Z3 listo para **autorización humana de artefactos**. Sin descarga, sin load, sin train en 14A.

# Decisión 005 — Cierre smoke reduced training SGPT Z3

**ID:** `005_sgpt_z3_reduced_training_smoke_closure`  
**Fecha:** 2026-07-22  
**Prompt:** 14D  
**Coste:** USD 0.00

## 1. Contexto

Laboratorio text2sparql-reproducibility-lab; método `sgpt`; pin `1f6964d1…`; política ZERO_COST; Fase 1 abierta.

## 2. Evidencia Z1

Entorno/pins documentados; ancla temporal 2022-12.

## 3. Evidencia Z2

Preflight core PASS; freeze SHA conocido; auth 13A consumida.

## 4. Evidencia P2A

Model load offline PASS; GPT-2 revision verificada; imagen Z3 fijada.

## 5. Evidencia P2B

Un forward no-grad PASS; loss técnica; sin train.

## 6. Attempt 1

Raw `Z3_OTHER_FAILED` por conteo de `scheduler.step` (init+train). Optimizer/backward direct=1. Sin checkpoint. Auth consumida.

## 7. Attempt 2

Raw `Z3_OTHER_FAILED` (`optimizer_step=0`). Nativo: un batch, checkpoint-1, evals, save. Auth consumida.

## 8. Reconciliación del harness

Hook base `Optimizer.step` no capturó `transformers.AdamW`. Qualifier: `PASS_WITH_INDIRECT_OPTIMIZER_STEP_VERIFICATION`.

## 9. Estado de reproducción

`smoke_only` / `reduced_training_smoke_only`. No `partially_reproduced`.

## 10. Estado de auditoría nativa

`native_audit_complete=true`  
`outcome=completed_smoke_only_full_reproduction_not_achieved`  
`common_adapter_allowed=false`

## 11. Barreras restantes

Ckpt paper; VRAM; splits; métricas; full train/Table 4 no ZERO_COST-razonable.

## 12. Claim boundary

`reduced_training_smoke_only` — smoke de ruta de entrenamiento, no reproducción del artículo.

## 13. Relación con PE1–PE4

PE1 sustancial; PE2 evidencia parcial ampliada; PE3 no iniciado; PE4 barreras + limitación de instrumentación.

## 14. Consecuencias para evaluación común

Adapters **no** activados. Evaluación común solo tras gate global Fase 1 (Prompt 15).

## 15. Condiciones para reabrir SGPT

Nueva autorización con evidencia científica incremental; no re-train solo por contador.

## 16. Decisión

Cerrar Z3 SGPT como **`SGPT_NATIVE_AUDIT_CLOSED_SMOKE_ONLY`**. Seleccionar **Q11** como única `GO_NEXT_ZERO_COST`. No ejecutar Prompt 15 aquí.

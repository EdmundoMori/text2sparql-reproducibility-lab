# SGPT recovery assessment

**phase1:** smoke_only · MIT · GPT-2 base · paper checkpoints absent · Z3 smoke done · full training not done.

## SGPT_ZERO_COST_FULL_TRAINING_FEASIBILITY (documentary)

- Dataset: QALD-compatible train already in lab workdir (QALD acquired).
- Architecture: GPT-2 — fits local RTX 4050 ~6GB with small physical batch + grad accumulation.
- RESOURCE_EQUIVALENT_ADAPTATION allowed only if same dataset/samples/epochs/effective batch/optimizer/LR/arch/seeds; only physical_batch + grad_accum may change.
- Does **not** auto-claim statistical equivalence.

## Variants

| Variant | Status |
|---|---|
| SGPT_NATIVE_FAITHFUL_TRAINING | candidate ZERO_COST on local GPU if RESOURCE_EQUIVALENT_ADAPTATION documented |
| SGPT_PAPER_CHECKPOINT_FAITHFUL | blocked B_MODEL until public paper ckpt |

## Recoverability

- native: **R2/R5** training feasibility conditional
- common_benchmark: **R1/R2** after training or smoke-eval path under tracks
- Blockers: B_MODEL (paper ckpt), B_HARDWARE (full fidelity), B_GRAPH(runtime), B_EVALUATION(impl pending)

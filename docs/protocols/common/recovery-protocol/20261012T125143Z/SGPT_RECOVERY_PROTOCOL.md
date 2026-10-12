# SGPT recovery protocol

## Paths

- `SGPT_PAPER_CHECKPOINT_PATH` — blocked until authoritative checkpoint.
- `SGPT_ZERO_COST_RETRAIN_PATH` — future `SGPT_ZERO_COST_FULL_TRAINING_PREFLIGHT`.

## RESOURCE_EQUIVALENT_ADAPTATION

Required constant: architecture, base model revision, dataset, split, sample count, epochs, optimizer, LR, effective batch, seed, scheduler, max seq lengths, evaluation procedure.

Allowed: physical_batch_size, gradient_accumulation_steps iff effective batch constant. Any other difference → distinct adaptation flag.

Future feasibility: dry-run, one-batch memory, epoch-time, disk, ckpt size, walltime scenarios. **No training now.** Catalog `R25-SGPT-01`.

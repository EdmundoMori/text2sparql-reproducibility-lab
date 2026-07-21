# Z3_FUTURE_COMMAND_SPEC

**RUN_ID:** `20260721T134213Z`  
**Marca:** `DO_NOT_RUN_IN_PROMPT_14A` · `NOT_EXECUTED`

```bash
# DO_NOT_RUN_IN_PROMPT_14A
python train.py \
  --params_file <LAB_Z3_PARAMS_PATH> \
  --dataset lcquad2 \
  --epochs 1 \
  --eval_dataset test \
  --exp_name sgpt-z3-canary-20260721T134213Z
```

## No incluir
`--knowledge`, `--masked`, `--eval_only`, distributed launch, Apex, fp16, CUDA.

## Condiciones futuras
- Copia descartable del código; `data/lcquad2` = subset canario
- GPT-2 path local fijado; red bloqueada; HOME/caches aislados
- Outputs solo en workdir; upstream original **read-only**

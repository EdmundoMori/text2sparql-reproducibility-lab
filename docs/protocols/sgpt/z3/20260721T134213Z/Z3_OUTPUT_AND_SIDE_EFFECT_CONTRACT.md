# Z3_OUTPUT_AND_SIDE_EFFECT_CONTRACT

**RUN_ID:** `20260721T134213Z`

## Inventario esperado (código)
`runs/<exp_name>/<dataset>/`; TensorBoard; `checkpoint-<global_step>`; model/tokenizer; `training_args.bin`; `params.json`; `eval_results.txt`; final save+reload; HF/Python caches; Docker layers.

## Regla lab
Todo en **workdir** o cache local **ignorada por Git**.

## Versionar solo
manifiestos, hashes, logs texto, métricas técnicas, inventario, tamaños, clasificación.

## No versionar
pesos, checkpoints, tokenizer, caches, imagen Docker, `training_args.bin`, binarios.

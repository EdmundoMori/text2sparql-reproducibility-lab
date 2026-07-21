# NATIVE_ENTRYPOINT_CONSTRAINTS — SGPT train.py

**Upstream pin:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b`  
**Archivo:** `upstream/sgpt/train.py` (y datasets)  
**Etiqueta:** `CODE_VERIFIED`  
**Prompt:** 14A (`20260721T134213Z`) — **NOT_EXECUTED**

| Punto | Ubicación | Clasificación | Nota |
|---|---|---|---|
| SummaryWriter torch / fallback tensorboardX | train.py:29-31 | REQUIRED_NATIVE_PATH | Import a nivel módulo |
| import scripts.model (GPT2LMHeadModel, run_batch_generation) | train.py:18 | REQUIRED_NATIVE_PATH | Carga modelo custom |
| AutoTokenizer.from_pretrained | train.py:279,309,349 | REQUIRED_NATIVE_PATH | Path local futuro obligatorio |
| AutoConfig.from_pretrained | train.py:305 | REQUIRED_NATIVE_PATH | |
| GPT2LMHeadModel.from_pretrained | train.py:311,348 | REQUIRED_NATIVE_PATH | Custom class |
| resize_token_embeddings | train.py:312 | REQUIRED_NATIVE_PATH | Tras special tokens |
| Selección CPU/GPU real | train.py:288-295 | REQUIRED_NATIVE_PATH | Ignora en la práctica `--device` CLI |
| `--device` sobrescrito | train.py:244 vs 289-295 | KNOWN_BUG / FUTURE_HARNESS_CONTROL | `args.device` se reasigna por `cuda.is_available()` |
| `--epochs=-1` y `params["num_train_epochs"]=fromcommand.epochs` | train.py:222,267 | KNOWN_BUG | Siempre escribe epochs en params; si -1 corrompe |
| Corrección parcial `if epochs!=-1` | train.py:275-276 | KNOWN_BUG | Obligatorio pasar `--epochs 1` en Z3 |
| Ausencia de max_steps | train.py (sin flag) | NOT_RELEVANT_CANARY | Control vía epochs×batches |
| batch en `train()` | train.py:47-53 | REQUIRED_NATIVE_PATH | `per_gpu_train_batch_size * max(1,n_gpu)` |
| Hardcode `args.train_batch_size=2` en main | train.py:298 | KNOWN_BUG | Solo afecta dataloader/t_total pre-`train()`; `train()` recalcula |
| gradient_accumulation_steps | params + train.py:98-109 | REQUIRED_NATIVE_PATH | |
| Evaluación por época | train.py:124 | SIDE_EFFECT | Eval val inherente |
| Checkpoint por época/global_step | train.py:137-153 | SIDE_EFFECT | Escrita bajo runs/ |
| Guardado final + recarga | train.py:332-350 | SIDE_EFFECT | |
| Evaluación final | train.py:352-356 | SIDE_EFFECT | `--eval_dataset` |
| eval_only incompleto | train.py:302-303 | KNOWN_BUG | Rama `pass` sin cargar modelo |
| Rutas relativas de datos | dataset_lcquad2.py:87 | REQUIRED_NATIVE_PATH | `join("data", dataset, split+".json")` |
| `--dataroot` no usado en `_loaddata` | dataset_lcquad2.py:21,86-87 | KNOWN_BUG | Hard-coded `data/<dataset>/` |
| `dep_mapping.json` hard-coded | dataset_lcquad2.py:31 | REQUIRED_NATIVE_PATH | `data/lcquad2/dep_mapping.json` |
| Escrituras bajo runs/ | train.py:44-46 | SIDE_EFFECT / STOP_CONDITION | Solo workdir permitido en lab |

**No se proponen modificaciones upstream.** Controles futuros vía harness/copia descartable + subset en `data/lcquad2`.

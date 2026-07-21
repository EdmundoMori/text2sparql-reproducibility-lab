# Z3_RESOURCE_BUDGET

**RUN_ID:** `20260721T134213Z` · todos los valores: `PROPOSED_RESOURCE_BOUND`

## Baseline host
RAM WSL ~7.4 GiB; CPU 8C/16T; VRAM 6 GiB; Z2 CPU torch; paper 2×12 GB GPU.

## Por etapa
| Etapa | CPU | Memoria | Timeout | Disco/otros |
|---|---|---|---|---|
| P1 acquisition | n/a | verificar free space | n/a | margen artefactos (~0.55 GiB pesos + tokenizer + cache) |
| P2 model load | 2 | 5 GiB limit | 900 s | no GPU; no forward salvo auth |
| P3 one-step | 2 | 6 GiB max | 3600 s | output budget 6 GiB; free-RAM/disk gates |

## Stop conditions
RAM insuficiente; swap thrashing; OOM; output > presupuesto; timeout; imagen Docker ausente; intento GPU; cambio pins; artifacts incompletos.

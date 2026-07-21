# AUTHORIZATION_CONSUMPTION_RECORD — Prompt 13A / cierre 13B

| Campo | Valor |
|---|---|
| **authorization** | `HUMAN_DECISION_VERIFIED` |
| **approver** | EDMUNDO MORI ORRILLO |
| **decision_date** | 2026-07-21 |
| **run_id** | `20260721T114919Z` |
| **source** | `environments/sgpt/builds/20260721T114919Z/Z2_DOWNLOAD_BUILD_AUTHORIZATION.md` |
| **status** | **`AUTHORIZED_AND_CONSUMED_13A`** |
| **monetary_cost_usd** | **0.00** |

## Alcance consumido

- Imagen oficial `python:3.8.20-slim-bookworm` (digest amd64 esperado `sha256:314bc2fb…`).
- Paquetes Z2 CPU de `constraints.z2-cpu.direct.candidate.txt` + transitivas necesarias.
- Build Docker CPU aislado + probes offline autorizados (python/pip/import/data/métricas sintéticas).

## No reutilizable para

- Rebuild de la misma o nueva imagen sin **nueva** autorización humana explícita.
- Descargas futuras (cualquier artefacto).
- Recursos / corpus **NLTK**.
- **GPT-2** (tokenizer o pesos).
- Modelos **spaCy** (`en_core_web_sm` / `en_core_web_lg`).
- **Z3** (protocolo, train o smoke de entrenamiento).
- Inferencia, `train.py`, `eval.py`, `utils/dptree.py`, Table 4.

## Condición de reapertura

Nueva autorización humana explícita (aprobador, fecha, alcance, coste máximo, abort conditions).

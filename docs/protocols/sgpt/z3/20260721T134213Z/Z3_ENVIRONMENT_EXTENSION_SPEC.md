# Z3_ENVIRONMENT_EXTENSION_SPEC

**RUN_ID:** `20260721T134213Z` · `PROPOSED_PROTOCOL` · **NOT_EXECUTED**

## Base Z2 (cerrada)
| Campo | Valor |
|---|---|
| Tag | `text2sparql-lab/sgpt-z2-py38:20260721T114919Z` |
| ID | `sha256:75ab83f202a5c7d5cdfa60c1d2ff596fab3ec0e529252572d051e66c7c5f3c57` |
| Freeze SHA-256 | `916d4b76a980ed1b558eb3bb26122f5e6dca9e02ffaeb5ee8e553f7cd66e71a5` |
| Auth 13A | `AUTHORIZED_AND_CONSUMED_13A` — **no** reutilizable para rebuild |

## Reglas futuras
1. Verificar que la imagen local **aún existe**.
2. Si no existe → `STOP_REBUILD_REQUIRES_NEW_AUTHORIZATION`.
3. Imagen Z3 **derivada y separada** (nuevo tag).
4. Instalar **únicamente** `tensorboardX==2.5.1` (+ transitivas aprobadas: numpy ya presente; protobuf pin ≤3.20.1).
5. GPT-2 montado **read-only**; no en Git.
6. No NLTK data; no spaCy; no GPU/CUDA en primer protocolo.
7. No modificar pins Z2 directos.
8. `pip check` + freeze en etapa autorizada.

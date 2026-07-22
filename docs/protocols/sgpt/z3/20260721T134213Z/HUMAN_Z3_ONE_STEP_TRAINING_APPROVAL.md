# HUMAN_Z3_ONE_STEP_TRAINING_APPROVAL

**Estado:** **SIGNED_AND_CONSUMED**  
**RUN_ID protocolo:** `20260721T134213Z`  
**Coste máximo:** USD **0.00**

## Alcance aprobado
- Un único run canario LC-QuAD2 question-only  
- Subset fijado (uids en `Z3_CANARY_SELECTION.json`)  
- Un paso de optimización **esperado** (validar fórmula pre-run)  
- Límites: CPU 2; mem ≤6 GiB; timeout ≤3600 s; output ≤6 GiB  
- Outputs solo workdir  

## Ejecución

| Attempt | RUN_ID | Resultado | Auth |
|---|---|---|---|
| 1 | `20260721T183611Z` | `Z3_OTHER_FAILED` | consumida |
| 2 (reauth humana) | `20260722T072146Z` | `Z3_ONE_STEP_REDUCED_TRAINING_PASS` | consumida |

## No autorizado
Table 4; afirmación PE3; reutilización de esta auth; train multi-epoch; GPU salvo nueva auth.

## Consumo
Autorizaciones 14C attempt-1 y attempt-2 **consumidas**. No hay segundo intento automático.

**Aprobador:** EDMUNDO MORI ORRILLO  
**Fecha:** 2026-07-21 (auth) / 2026-07-22 (ejecución PASS)  
**Firma:** HUMAN_DECISION_VERIFIED (mensaje Cursor Prompt 14C + reauth post-attempt-1)

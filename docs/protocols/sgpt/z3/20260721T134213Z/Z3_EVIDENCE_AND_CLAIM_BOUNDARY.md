# Z3_EVIDENCE_AND_CLAIM_BOUNDARY

**RUN_ID:** `20260721T134213Z`  
**Estado post-14D:** cerrado smoke

## Permitido afirmar (tras cierre)

- entorno Z3 controlado; GPT-2 fijado; model load; forward no-grad; reduced training path canario;
- un paso de optimización con verificación **indirecta** de alta confianza;
- checkpoint canario en workdir; coste externo 0;
- `reproduction_status=smoke_only` / `reduced_training_smoke_only`;
- `native_audit_complete=true` con outcome smoke_only (full repro not achieved).

## Prohibido afirmar

reproducción nativa completa; `partially_reproduced`; Table 4; convergencia; calidad; Answer F1;
comparabilidad con métricas del artículo; PE3 completado; `OPTIMIZER_STEP_DIRECT_COUNTER_VERIFIED` / `EXACT_OPTIMIZER_HOOK_PASS` en attempt 2;
equivalencia a 40/70 épocas o 2×12 GB; checkpoint del paper.

## Etiqueta máxima

`reduced_training_smoke_only`

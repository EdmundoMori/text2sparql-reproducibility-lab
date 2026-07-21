# HUMAN_Z3_ARTIFACT_AND_MODEL_PREFLIGHT_APPROVAL

**Estado:** **UNSIGNED** — Cursor no firma.  
**RUN_ID protocolo:** `20260721T134213Z`  
**Coste máximo autorizado propuesto:** USD **0.00**

## Alcance propuesto (solo tras firma humana)
1. Descarga exacta GPT-2 revision `607a30d783dfa663caf39e06633721c8d4cfcd7e` (archivos REQUIRED del manifest).
2. Descarga/instalación `tensorboardX==2.5.1` (+ protobuf pin compatible) en imagen Z3 derivada.
3. Extensión de entorno Z3 (sin rebuild Z2 vía auth 13A).
4. Model-load preflight **P2A** (sin forward por defecto).
5. Forward no-grad **P2B** solo si se marca explícitamente abajo.

## No autorizado por este formulario
Entrenamiento; Table 4; NLTK data; spaCy; CUDA; modificar upstream; versionar pesos en Git.

## Casillas (humano)
- [ ] Apruebo descarga GPT-2 + tensorboardX bajo ZERO_COST  
- [ ] Apruebo extensión entorno Z3  
- [ ] Apruebo P2A model-load preflight  
- [ ] Apruebo P2B forward no-grad (opcional; vacío = no)  
- [ ] Confirmo auth 13A no se reutiliza  

**Aprobador:** _________________  
**Fecha:** _________________  
**Firma:** _________________

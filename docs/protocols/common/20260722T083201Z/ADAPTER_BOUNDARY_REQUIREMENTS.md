# ADAPTER_BOUNDARY_REQUIREMENTS

**RUN_ID:** `20260722T083201Z` · sin código · common_adapter_allowed=false

## Un futuro adapter

- vive fuera de upstream;
- no modifica upstream;
- recibe CommonInput;
- produce CommonOutput;
- preserva query final explícita;
- registra versión y hash;
- no añade información fuera del track;
- no corrige query usando gold;
- no fallback silencioso;
- no oculta fallos;
- no almacena secretos;
- no descarga dinámicamente durante benchmark;
- no cambia modelo sin nueva variante;
- registra todas las llamadas externas.

Future adapter gate: PENDING_PHASE2_PROTOCOL_AND_LEGAL_GATE.

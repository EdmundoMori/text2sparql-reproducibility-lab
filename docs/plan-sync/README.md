# Plan sync (Cursor ↔ ChatGPT)

Este directorio soporta el bucle de optimización del plan de prompts:

1. El investigador ejecuta un prompt en Cursor.  
2. Cursor documenta hallazgos en `PLAN_SYNC.md` (raíz) y docs específicos.  
3. Se hace push a GitHub.  
4. ChatGPT lee el repo y adapta el siguiente prompt.

**Entrada para ChatGPT:** [`../../PLAN_SYNC.md`](../../PLAN_SYNC.md)

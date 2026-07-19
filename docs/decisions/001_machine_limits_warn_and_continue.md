# Decisión 001 — Limitaciones de máquina: advertir, mitigar y continuar

**Fecha:** 2026-07-18  
**Estado:** Aceptada  
**Ámbito:** Operación del agente y afinado de pedidos experimentales

## Contexto

El host (Windows + WSL2, RAM WSL ≈7.4 GiB, RTX 4050 ≈6 GB VRAM, sin Compose/Conda/uv/`nvcc`) puede ejecutar el laboratorio, pero no todos los protocolos nativos “tal cual” el paper.

## Decisión

1. Integrar las limitaciones en `PROJECT_CONTEXT.md` §7 y `MACHINE_PROFILE.md`.  
2. Ante pedidos incompatibles o inconvenientes, el agente debe: **advertencia inmediata → solución concreta → continuar** con la ruta más segura.  
3. Las limitaciones afinan pedidos; no cancelan el proyecto ni omiten la fase solicitada.  
4. Las degradaciones que afecten reproducibilidad se documentan (estado `partially_reproduced`, `blocked`, `requires_external_gpu`, etc.).

## Consecuencias

- Preferencia por auditoría → smoke → API / subconjuntos antes de entrenamientos masivos.  
- El usuario puede pedir rutas ambiciosas; recibirá aviso y una alternativa ejecutable en local cuando exista.

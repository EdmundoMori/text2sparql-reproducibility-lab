# Decisión 002 — Versionar `upstream/` en GitHub

**Fecha:** 2026-07-19  
**Estado:** Activa (a petición del investigador)

## Contexto

El primer push omitió `upstream/` (~1.2 GiB de clones de terceros) para evitar un repo pesado y duplicar historial ajeno. El planificador (ChatGPT) necesita leer el código clonado en el mismo repo.

## Decisión

1. **Vendorar** los árboles de trabajo de `upstream/<method_id>/` en el repo del lab.  
2. Renombrar cada `upstream/*/.git` → `upstream/*/.git_local/` (ignorado por git) para poder añadir el código como archivos normales, conservando metadatos git locales.  
3. Seguir pinneando commits en `REPOSITORIES.lock.yaml`.  
4. Seguir sin modificar el código de método con fines de adaptación (adapters fuera).

## Trade-offs

| Pros | Contras |
|---|---|
| ChatGPT ve el código real | Repo ~1+ GiB; clones más lentos |
| Un solo sitio de verdad para el bucle | Archivos grandes (~80–88 MiB) sin LFS |
| Pins + árbol visibles juntos | Licencias de terceros viajan en el mirror |

## Alternativa descartada (por ahora)

Submódulos git: peor UX para lectura directa en la UI de GitHub/ChatGPT.

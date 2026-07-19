# EXECUTION_WORKSPACE_POLICY

**Fecha:** 2026-07-19  
**Prompt:** 4B (solo documental; **ninguna copia creada aquí**)

## Reglas para prompts futuros de ejecución

1. **Nunca** ejecutar procesos con side effects directamente sobre `upstream/`.  
2. Usar un **workspace local descartable** fuera de `upstream/` cuando el método escriba archivos (p. ej. `workdir/runs/<method_id>/<timestamp>/`).  
3. **No versionar** en git: secretos, caches, modelos, índices vectoriales, dumps, ni copias completas de código de terceros.  
4. **rdfconfig_llm:** `sparql.yaml` (y configs mutables) solo en la copia de ejecución descartable — nunca en `upstream/rdfconfig_llm/rdf-config/`.  
5. Toda copia futura debe registrar en un manifiesto local (no necesariamente git):
   - `source_path`
   - `source_commit` (pin)
   - checksum o file manifest
   - fecha
   - motivo  
6. **`LICENSE_NOT_CONFIRMED`:** inspección y posible ejecución aislada para investigación interna OK; **prohibido** adapters, integración al núcleo del lab, o redistribución del código.  
7. Este prompt **no** crea ninguna copia de ejecución.

## Layout sugerido (futuro, no creado ahora)

```text
workdir/                          # gitignored recomendado
  runs/<method_id>/<iso8601>/
    MANIFEST.yaml
    # copia mínima o symlink controlado según método
```

Añadir `workdir/` a `.gitignore` en el prompt que cree la primera copia, si aún no está.

# SMOKE_QUESTION — Prompt 11

**RUN_ID:** `20260721T100618Z`  
**Acción:** `LOCAL_CHAT_API_ONE_QUESTION`  
**Estado:** congelada para Prompt 12 — **no modificar** sin nuevo gate.

---

## Texto exacto

```text
How can I retrieve active site annotations in UniProt?
```

| Campo | Valor |
|---|---|
| Idioma | inglés |
| Rol | única pregunta del smoke L0 |
| Gold SPARQL | **ninguna** |
| Métrica de corrección | **ninguna** (smoke de ejecutabilidad, no PE3) |

---

## Justificación

1. La clase `http://purl.uniprot.org/core/Active_Site_Annotation` está en `LAB_MINIMAL_INDEX` (12 docs; `DATA_VERIFIED` / `INDEX_VERIFIED` en Prompt 10/10B).  
2. Compatible con el endpoint lógico UniProt del Settings mínimo.  
3. No requiere `enable_sparql_execution=true`.  
4. Permite observar retrieval → generación → validación VoID bajo `max_try_fix_sparql=0`.

La presencia de la clase en el índice es **contexto de diseño**, no gold answer ni criterio de éxito semántico.

---

## Éxito del smoke futuro (recordatorio)

Éxito funcional ≠ consulta correcta. Ver criterios en protocolo API/SIB (server_start, llm_call, retrieval, response, etc.).

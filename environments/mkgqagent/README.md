# Environment spec — mkgqagent

**Source commit:** `ba0f2f78611a7ccacc8c985a97f6008ef7ee6a6a`  
**Legal:** `LICENSE_NOT_CONFIRMED` (sin LICENSE en árbol)  
**Python:** 3.10 (Dockerfile) — host 3.10.12 OK  
**Estado:** documentado, no instalado.

## Conclusiones separadas

| Dimensión | Valor |
|---|---|
| `offline_smoke` | **NOT_READY** (FAISS+e5 implican download/modelo; no offline puro) |
| `api_smoke` | **CONDITIONAL** (key, hosts, RAM, un solo agente) |
| `native_reproduction` | **NOT_READY_OR_WEAK** (sin script offline; pool≠trazas paper; solo EN; hosts hardcode) |

## Hechos documentados (static audit)

- Requirements **sin pins estrictos** (`UNPINNED` / `LOWER_BOUND`).  
- `requests` **usado en código**, **ausente** en `requirements.txt` → `MISSING_UPSTREAM`.  
- `text2sparql-client` externo (pipx), no empaquetado.  
- LLM: `gpt-4o-2024-05-13`; embeddings: `intfloat/multilingual-e5-large` CPU.  
- FAISS prebuilt en `data/experience-pool/`.  
- `allow_dangerous_deserialization=True` al cargar FAISS.  
- Servicios: OpenAI, Falcon2, `141.57.8.18` SPARQL/EL, LangChain Hub.  
- Divergencias: planner JSON `plan` vs schema `steps`; `last_task` dict.  
- Datasets/prompts **EN** solo.  
- Pool shipped = ICL Q/SPARQL, no trazas offline del paper.  
- `main.py` instancia **ambos** agentes al import → riesgo doble e5.

## Estrategia futura de smoke (sin implementar aquí)

- Evitar cargar dos agentes a la vez.  
- **No** crear wrappers/adapters/scripts; **no** modificar `main.py`.  
- **No** ejecutar hosts externos en 4B.  
- Pendiente (futuro): ¿existe forma de instanciar un solo agente **sin** modificar código? Si no, documentar bloqueo o degradación (proceso/documentación), no parchear upstream.

## LICENSE_NOT_CONFIRMED

Inspección y posible ejecución aislada interna ≠ autorización de reutilización, adapters o redistribución.

## Artefactos

Ver `dependency_manifest.yaml`, `environment_variables.md`, `future_commands.md`.

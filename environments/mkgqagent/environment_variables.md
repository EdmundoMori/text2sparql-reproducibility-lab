# Variables de entorno — mkgqagent

Valores reales: **nunca** en git.

| Nombre | Obligatorio para api_smoke | Notas |
|---|---|---|
| `OPENAI_API_KEY` | sí | README_REPORTED; ChatOpenAI |
| `CORPORATE_SERVICE_BASE_URL` | conditional (dataset corporate) | Default hardcode `http://141.57.8.18:9199` en código |

Endpoints hardcodeados (no env): Falcon2 URL; SPARQL `141.57.8.18:40201/...`; LangChain Hub; HuggingFace model download.

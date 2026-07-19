# Variables de entorno — rdfconfig_llm

Fuente: `.env_sample` (placeholders; **no** copiar valores reales a git).

| Nombre | Uso |
|---|---|
| `OPENAI_API_KEY` | OpenAI client |
| `OPENAI_API_KEY2`, … | Rotación en `leave-one-set-out.py` (FT) |
| `PATH_RDF_CONFIG` | Path al dir rdf-config (debe apuntar a **copia** de ejecución, no upstream mutable) |
| `PATH_DIR` | Root del proyecto generator en workspace descartable |
| `PATH_PROMPTS` | default documental `data/prompt/prompts.json` |
| `PATH_VARIABLES` | default documental `data/prompt/variables.json` |
| `ENDPOINT_BGEE` | endpoint SPARQL |
| `ENDPOINT_UNIPROT` | endpoint SPARQL |
| `ENDPOINT_RHEA` | endpoint SPARQL |
| `ENDPOINT_UNIPROT_AND_BGEE` | endpoint SPARQL |

# Desviaciones — Prompt 10B

- FastEmbed 0.8.0 mean-pooling warning vs older CLS behaviour (documented; model id exact).
- HF hub offline in image ENV forced GCS fallback URL from FastEmbed provenance (same model id).
- Preflight requires CWD with `src/sparql_llm/agent/webapp` (upstream tree mount); package code from site-packages install.
- Prefix SPARQL fetch at import failed closed under `--network none` (expected; auto_init false; collection already populated).
- Cache and Qdrant remain gitignored under workdir/.

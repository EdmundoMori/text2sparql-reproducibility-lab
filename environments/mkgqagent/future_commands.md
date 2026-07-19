# Comandos futuros — mkgqagent (NO ejecutar en 4B)

## offline_smoke

**NOT_READY** — no hay camino offline documentado sin descarga de e5/FAISS load.

## api_smoke (CONDITIONAL — prompt posterior dedicado)

```bash
# Solo tras GO explícito: key, legal acceptance, RAM check
python3 -m venv environments/mkgqagent/.venv
source environments/mkgqagent/.venv/bin/activate
pip install -r upstream/mkgqagent/requirements.txt
pip install requests   # MISSING_UPSTREAM — documentar
# NO modificar main.py
# Problema abierto: uvicorn main:app carga ambos agentes
# Decisión pendiente antes de ejecutar: ¿single-agent sin patch?
# Si no hay forma sin modificar código → NO-GO o documentar OOM risk y abortar
cd upstream/mkgqagent   # solo como cwd de lectura; preferir copy policy si hay writes
# uvicorn main:app --host 127.0.0.1 --port 8000
# GET /api?question=...&dataset=https://text2sparql.aksw.org/2025/dbpedia/
```

**Prohibido en smoke:** adapters, copiar código al núcleo lab, declarar `reproduced`.

## native_reproduction

**NOT_READY_OR_WEAK** — no comandos hasta reconstrucción offline/pool/paper protocol.

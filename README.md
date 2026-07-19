# text2sparql-reproducibility-lab

Laboratorio local de investigación en **Text-to-SPARQL** / KGQA orientado a auditoría, reproducibilidad nativa y, posteriormente, evaluación común de métodos publicados.

## Documentos rectores

| Documento | Rol |
|---|---|
| [`PLAN_SYNC.md`](PLAN_SYNC.md) | **Entrada para ChatGPT:** estado post-prompt + bucle de optimización del plan |
| [`docs/plan-sync/`](docs/plan-sync/) | Índice de artefactos y guía del siguiente prompt |
| [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) | Estado del proyecto, métodos candidatos, métricas y reglas |
| [`RESEARCH_PROTOCOL.md`](RESEARCH_PROTOCOL.md) | Protocolo experimental y estados de reproducción |
| [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md) | Hardware, software y clases de reproducibilidad local |
| [`METHOD_REGISTRY.yaml`](METHOD_REGISTRY.yaml) | Registro de métodos y su estado |
| [`REPOSITORIES.lock.yaml`](REPOSITORIES.lock.yaml) | Pins de commits upstream |
| [`EXPERIMENT_REGISTRY.jsonl`](EXPERIMENT_REGISTRY.jsonl) | Log append-only de experimentos |

## Estructura

```text
text2sparql-reproducibility-lab/
├── upstream/              # Clones intactos: upstream/<method_id>
├── adapters/              # Adaptadores externos (fuera de upstream)
├── audit/                 # Fichas de auditoría por método
├── configs/               # Configuraciones del laboratorio
├── datasets/
│   ├── native/            # Datos de los papers (por método)
│   └── common/            # Benchmarks comunes (QALD-9 Plus, LC-QuAD 2.0, …)
├── environments/          # Specs de entornos (conda/uv/poetry/docker)
├── evaluation/            # Código de métricas y evaluación común
├── experiments/
│   ├── native/            # Definiciones de reproducción nativa
│   └── common/            # Definiciones de evaluación común
├── graph_snapshots/       # Snapshots/dumps de grafos cuando aplique
├── licenses/              # Copias o notas de licencias
├── logs/                  # Logs de comandos y ejecuciones
├── papers/                # Referencias / PDFs si se archivan localmente
├── prompts/               # Prompts del laboratorio (no de test-set leakage)
├── results/
│   ├── native/            # Resultados de reproducción nativa
│   └── common/            # Resultados del protocolo común
├── scripts/               # Utilidades de alto nivel
├── tests/                 # Tests del laboratorio (no de los papers)
├── PLAN_SYNC.md           # Estado para ChatGPT (bucle de prompts)
└── docs/
    ├── plan-sync/         # Índice + guía del siguiente prompt
    ├── methods/           # Documentación por método
    ├── decisions/         # Decisiones metodológicas
    └── reports/           # Informes de fase
```

**GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab — ChatGPT debe empezar por `PLAN_SYNC.md`. Los árboles `upstream/` están versionados (vendorizados); los metadatos git de cada clone viven localmente en `.git_local/` (ignorados). Pins: `REPOSITORIES.lock.yaml`.


## Reglas rápidas

- No modificar código en `upstream/`.
- No declarar reproducción sin ejecución documentada.
- Distinguir métricas **originales** vs **comunes**.
- No usar el test set para elegir prompts o hiperparámetros.
- No almacenar secretos: usar `.env` local (ignorado por git). Ver `.env.example`.
- **Limitaciones de máquina** (`MACHINE_PROFILE.md`, `PROJECT_CONTEXT.md` §7): si un pedido es inconveniente con RAM/GPU/Docker/herramientas locales, el agente debe **advertir → proponer solución → continuar** (no abortar la fase).

## Comandos de alto nivel

Requiere GNU Make. No instala dependencias globales por defecto.

```bash
make help
make status
make tree
make profile
```

## Fase activa

**Fase 1 — Auditoría y reproducibilidad nativa.**  
Workspace creado. Sin clones. Sin ejecución de métodos. Sin dependencias globales instaladas por este laboratorio.

## Licencia del laboratorio

Pendiente de decisión explícita. Los métodos upstream conservan sus propias licencias (ver `licenses/` y fichas de auditoría).

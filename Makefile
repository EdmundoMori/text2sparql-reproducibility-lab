# Makefile — comandos de alto nivel del laboratorio.
# No instala dependencias globales. No clona ni ejecuta métodos por defecto.

ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
PYTHON ?= python3

.PHONY: help status tree profile check-layout registries clean-pycache

help: ## Mostrar comandos disponibles
	@echo "text2sparql-reproducibility-lab — comandos de alto nivel"
	@echo
	@grep -E '^[a-zA-Z0-9_-]+:.*?## ' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  %-16s %s\n", $$1, $$2}'
	@echo
	@echo "Reglas: no modificar upstream/; no declarar reproducción sin ejecución."

status: ## Resumen del estado del workspace
	@echo "ROOT=$(ROOT)"
	@echo "Fecha: $$(date -Iseconds)"
	@echo "Fase: ver PROJECT_CONTEXT.md"
	@echo
	@echo "Métodos en METHOD_REGISTRY.yaml:"
	@$(PYTHON) -c "import pathlib; p=pathlib.Path('METHOD_REGISTRY.yaml'); print(p.read_text(encoding='utf-8').count('method_id:'), 'entradas method_id')"
	@echo "Clones en upstream/: $$(find upstream -mindepth 1 -maxdepth 1 ! -name '.gitkeep' | wc -l)"
	@echo "Locks en REPOSITORIES.lock.yaml: $$(grep -c 'commit_sha:' REPOSITORIES.lock.yaml || true) (0 esperado si repositories: [])"
	@echo "Experimentos registrados: $$(grep -cve '^[[:space:]]*$$' EXPERIMENT_REGISTRY.jsonl || true)"

tree: ## Mostrar estructura de directorios
	@find . -path './.git' -prune -o -print | sed -e 's|[^/]*/| |g' | head -n 200
	@echo
	@echo "(usa: find . -type d | sort  para listado completo)"

profile: ## Re-detectar perfil de máquina (best-effort)
	@echo "=== OS ==="
	@uname -a
	@echo "WSL_DISTRO_NAME=$${WSL_DISTRO_NAME:-}"
	@echo "=== CPU ==="
	@lscpu 2>/dev/null | egrep 'Model name|Architecture|CPU\(s\)|Thread|Core|Socket' || true
	@echo "=== RAM ==="
	@free -h || true
	@echo "=== GPU ==="
	@nvidia-smi 2>&1 || echo "nvidia-smi failed (sandbox or driver)"
	@echo "=== Docker ==="
	@docker --version 2>&1 || true
	@docker compose version 2>&1 || echo "docker compose: unavailable"
	@echo "=== Toolchain ==="
	@git --version 2>&1 || true
	@$(PYTHON) --version 2>&1 || true
	@java -version 2>&1 || true
	@node --version 2>&1 || true
	@poetry --version 2>&1 || true
	@conda --version 2>&1 || echo "conda=NOT_FOUND"
	@uv --version 2>&1 || echo "uv=NOT_FOUND"
	@echo "=== Disk ==="
	@df -h "$(ROOT)" || df -h /
	@echo
	@echo "Perfil documentado en MACHINE_PROFILE.md (no se sobrescribe automáticamente)."

check-layout: ## Verificar directorios esperados
	@missing=0; \
	for d in upstream adapters audit configs datasets/native datasets/common \
		environments evaluation experiments/native experiments/common \
		graph_snapshots licenses logs papers prompts \
		results/native results/common scripts tests \
		docs/methods docs/decisions docs/reports; do \
		if [ ! -d "$$d" ]; then echo "MISSING: $$d"; missing=1; fi; \
	done; \
	for f in README.md MACHINE_PROFILE.md METHOD_REGISTRY.yaml REPOSITORIES.lock.yaml \
		EXPERIMENT_REGISTRY.jsonl .env.example .gitignore Makefile \
		PROJECT_CONTEXT.md RESEARCH_PROTOCOL.md; do \
		if [ ! -f "$$f" ]; then echo "MISSING: $$f"; missing=1; fi; \
	done; \
	if [ "$$missing" -eq 0 ]; then echo "OK: layout completo"; else echo "FAIL: faltan elementos"; exit 1; fi

registries: ## Mostrar rutas de registros
	@echo "METHOD_REGISTRY.yaml"
	@echo "REPOSITORIES.lock.yaml"
	@echo "EXPERIMENT_REGISTRY.jsonl"
	@echo "Esquema de experimento (referencia): docs/reports/experiment_registry_schema.md"

clean-pycache: ## Eliminar __pycache__ del lab (no toca upstream de forma especial; aún vacío)
	@find "$(ROOT)" -type d -name '__pycache__' -prune -exec rm -rf {} + 2>/dev/null || true
	@echo "pycache limpiado (si existía)"

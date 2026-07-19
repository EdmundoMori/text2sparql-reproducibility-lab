# Comandos futuros — rdfconfig_llm (NO ejecutar en 4B)

## Prerrequisito host

```bash
# Fuera de 4B y solo con aprobación explícita:
# instalar Ruby + Bundler (apt/snap) — NO hecho aquí
ruby --version
bundle --version
```

## Companion CLI smoke (MIT, independiente)

```bash
# Tras Ruby/Bundler presentes
cd workdir/runs/rdfconfig_companion/<ts>/   # copia o checkout controlado — política workspace
bundle install
bundle exec rdf-config --config config/bgee --sparql
```

## Generator smoke (CONDITIONAL)

```bash
# 1) Crear workspace descartable con copia del generator + rdf-config incluido
# 2) Registrar MANIFEST (source commit, checksums)
# 3) venv + pip install -r requirements.txt
# 4) pip install pandas munkres scipy tqdm   # MISSING_UPSTREAM — sin inventar versiones exactas en docs
# 5) .env con PATH_RDF_CONFIG apuntando a la COPIA
# 6) Una pregunta vía generate_one_sparql / celda notebook
# NUNCA cwd=upstream/rdfconfig_llm para escritura
```

## native paper

Tras Zenodo download+verify (prompt futuro): alinear notebooks/CV con tablas paper.

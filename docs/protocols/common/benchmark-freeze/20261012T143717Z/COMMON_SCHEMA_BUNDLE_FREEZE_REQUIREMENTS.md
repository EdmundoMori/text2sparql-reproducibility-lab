# Common schema bundle freeze requirements

**RUN_ID:** `20261012T143717Z`
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION


Status: `PENDING_GRAPH_RUNTIME_AND_SCHEMA_CONSTRUCTION`.

Every `IA_SCHEMA_COMMON` execution in a direct group must receive one identical frozen bundle containing
`schema_bundle_id`, `graph_id`, `generator_version`, classes, properties, content hash and generation
procedure. No tailoring from QALD test questions is allowed. This is a runtime prerequisite, not a
design-freeze blocker. No schema was constructed in 25R4.

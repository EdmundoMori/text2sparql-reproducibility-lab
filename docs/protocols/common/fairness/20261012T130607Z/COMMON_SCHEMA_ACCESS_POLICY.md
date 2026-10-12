# Common schema access policy

**RUN_ID:** `20261012T130607Z`
**Protocol:** `1.0.0-25R3`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_EXECUTION


Every `IA_SCHEMA_COMMON` member receives one identical frozen bundle with `schema_bundle_id`, version,
content hash, generation process, graph target, classes, properties, and optional VoID/shapes. No richer
benchmark-supplied schema is permitted for one member of the same direct-comparison group. Endpoint-derived
extra schema is a declared `METHOD_INTERNAL_CAPABILITY`; Prompt 25R4 must decide whether it requires a
separate variant/group.

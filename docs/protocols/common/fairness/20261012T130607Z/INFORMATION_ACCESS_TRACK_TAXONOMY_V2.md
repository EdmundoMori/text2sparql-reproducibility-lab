# Information access track taxonomy V2

**RUN_ID:** `20261012T130607Z`
**Protocol:** `1.0.0-25R3`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_EXECUTION


| Track | Benchmark-supplied information | Boundary |
|---|---|---|
| IA_Q_ONLY | question, basic metadata, common endpoint reference | Native internal retrieval/linking allowed if non-gold, declared, reproducible and ZERO_COST |
| IA_SCHEMA_COMMON | IA_Q_ONLY plus identical frozen schema bundle | No richer method-specific benchmark bundle in the group |
| IA_ORACLE_GROUNDING | gold-derived entity/relation/property information for evaluated item | Must say oracle-assisted; never end-to-end |
| IA_FIXED_EXTERNAL_GROUNDING | same frozen external linker/grounder output supplied to every group member | Distinct from native internal linkers |
| IA_DOMAIN_NATIVE | different dataset/KG/domain | No QALD ranking |
| IA_HISTORICAL | historical context | No active ranking |

Taxonomy version: `2.0.0-25R3`.

Historical Prompt 19 adapter contracts and Prompt 25R2 recovery rows retain their original labels as evidence.
Where `PROMPT_25R3_RECONCILIATION` records a different `new_track`, V2 governs future fairness. F12 remains
blocked until any affected adapter contract/input mapping is explicitly reconciled; no silent reinterpretation
or implementation is authorized.

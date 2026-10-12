# Information boundary contract

**RUN_ID:** `20261012T130607Z`
**Protocol:** `1.0.0-25R3`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_EXECUTION


## BENCHMARK_SUPPLIED_INFORMATION

Only information crossing from harness/adapter to the method: question, language, benchmark item ID,
endpoint reference, schema bundle, oracle entities/relations, fixed external grounding, and demonstrations.
Every supplied field must appear in the frozen input manifest.

## METHOD_INTERNAL_INFORMATION_ACQUISITION

Retrievers, indexes, entity/relation linkers, endpoint feedback, internal search, agent tools and experience
pools invoked by the method itself. They require reproducibility and ZERO_COST evidence, but remain internal.

An internal linker does **not** create `IA_ORACLE_GROUNDING`. Oracle means gold-derived information for the
evaluated item crossed the benchmark boundary. Train-only demonstrations remain method-internal unless the
benchmark supplies them. A benchmark-supplied common frozen linker output is `IA_FIXED_EXTERNAL_GROUNDING`.

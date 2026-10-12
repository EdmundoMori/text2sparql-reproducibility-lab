# Benchmark freeze change control

**RUN_ID:** `20261012T143717Z`
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION


Changing dataset/test, graph target, track assignment, fairness taxonomy, primary metrics, failure
denominator, portfolio role, comparison group or ZERO_COST policy requires an explicit
`BENCHMARK_FREEZE_CHANGE_REQUEST` and a new freeze version.

Runtime hashes, adapter implementation hashes, model revision within an already frozen controlled slot,
resource profile and execution RUN_ID may change without a new design version only when they satisfy this
freeze. Any comparability change requires a new freeze version.

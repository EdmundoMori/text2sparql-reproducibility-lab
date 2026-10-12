# DBpedia deployment staged authorization map

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


| Stage | Scope | Prerequisite | Separate human gate | Output gate |
|---|---|---|---|---|
| D1 | Resource configuration and postcheck | Signed D1 form | Required | D1 runtime-resource PASS |
| D2 | Decompression + static RDF validation | D1 PASS | Required later | D2 artifact PASS |
| D3 | Runtime image acquisition by digest | D2 PASS + license resolved | Required later | D3 digest PASS |
| D4 | Virtuoso graph load | D3 PASS | Required later | D4 load PASS |
| D5 | Runtime technical graph validation/G4 | D4 PASS | Required later | G4 runtime PASS/FAIL |

Each stage has its own prerequisites, stop conditions, authorization and output. `D1_PASS_REQUIRED_BEFORE_D2_AUTHORIZATION`.
Nothing in D2–D5 was authorized or executed.

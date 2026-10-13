# Human D2 decompression and RDF-validation authorization

**RUN_ID:** `20261013T085129Z`
**Mode:** READ_ONLY_RUNTIME_VERIFICATION · ZERO_COST · NO_DEPLOYMENT
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


**Status:** `READY_UNSIGNED`

Proposed D2 scope only:

- [ ] verify the compressed canonical scope (114 files);
- [ ] verify existing checksums;
- [ ] decompress DBpedia 2016-10 into the approved Linux workdir;
- [ ] perform static file-level/RDF-syntax validation with pre-approved ZERO_COST tools;
- [ ] monitor disk usage and stop before the approved planning envelope is violated;
- [ ] record artifacts and hashes.

Disk prerequisite: Linux free space must remain above the conservative ~305 GiB envelope plus an explicit
operational margin. Stop on checksum mismatch, unexpected file count/size, disk pressure, malformed output,
ZERO_COST violation, freeze mismatch, or any need for an unauthorized stage.

Not authorized: Docker pull, container creation, Virtuoso, database load, SPARQL, gold, metrics, models,
training, adapters or benchmark.

Approver: ______ · Date: ______ · Decision: ______

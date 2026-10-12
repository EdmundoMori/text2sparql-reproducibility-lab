# PHASE2 DBpedia LOCAL_WSL_HOST_ADJUSTED selection and D1 preparation

**RUN_ID:** `20261012T150501Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_DEPLOYMENT · NO_RESOURCE_MODIFICATION
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


## 1. Executive summary

The human profile choice was consumed only for selection. A conditional 12/8 GiB D1 proposal is documented; nothing was configured.

## 2. Input freeze

COMMON_CORE_BENCHMARK_FREEZE_V1, version 1.0.0-25R4, SHA-256 `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c` remains unchanged and validator PASS.

## 3. Human selection

EDMUNDO MORI ORRILLO approved LOCAL_WSL_HOST_ADJUSTED on 2026-10-12.

## 4. Authorization boundary

PROFILE_SELECTION_ONLY; configuration and deployment remain unauthorized.

## 5. Current resources

WSL ~7.4 GiB RAM, 2 GiB swap, ~902 GiB Linux free, Docker client 29.1.3.

## 6. 15.19 GiB host verification

HUMAN_VERIFIED_WINDOWS_POWERSHELL; not inferred from WSL.

## 7. WSL memory headroom

12 GiB leaves 3.19 GiB; conditional and marginal.

## 8. Candidate allocations

8, 10, 11, 12, 13 and 14 GiB evaluated in the CSV; 14 GiB rejected.

## 9. Proposed allocation

12 GiB, MINIMUM_CAPACITY_CONDITIONAL_HIGH_RISK, not recommended capacity.

## 10. Swap

8 GiB proposed; no change; not equivalent to RAM.

## 11. Storage

~902 GiB free vs ~305 GiB envelope; 597 GiB headroom, 2.96×.

## 12. Docker

Client present; daemon inactive; Compose absent and not required merely for a single pinned container.

## 13. Runtime pin

Virtuoso 7.2.17 amd64 digest remains PINNED_METADATA_ONLY.

## 14. Runtime license

VERIFY_BEFORE_LOAD/NOASSERTION remains a material D3 blocker.

## 15. D1 scope

D1A–D1E only; D1_PASS_REQUIRED_BEFORE_D2_AUTHORIZATION.

## 16. Proposed .wslconfig

12GB memory / 8GB swap documentary template; not applied.

## 17. Rollback

Preserve/restore exact previous file state and remeasure after separately authorized restart.

## 18. Stop conditions

Host mismatch/starvation, restart/postcheck failure, disk, Docker, authorization, cost or freeze mismatch stop progression.

## 19. D1 authorization

READY_UNSIGNED; all five actions have separate checkboxes.

## 20. D2–D5 staging

Each later stage has a separate prerequisite, authorization, stop conditions and output gate.

## 21. DBpedia

114 compressed files remain compressed; NOT_DEPLOYED.

## 22. G4

NOT_SATISFIED.

## 23. G5

Implementation and conformance pending.

## 24. G6I

Implementation approval pending.

## 25. Adapters

common_adapter_allowed=false; no implementation.

## 26. Benchmark

NOT_CURRENTLY_ELIGIBLE; test remains SEALED.

## 27. Risks

Host headroom marginal, Windows C: low, daemon inactive, license unresolved, planning assumptions unmeasured.

## 28. Next action

Exactly one: `HUMAN_D1_RESOURCE_CONFIGURATION_AUTHORIZATION`; D1 execution prompt reserved, not authorized.

## 29. Claim boundaries

No claim of configured resources, deployed graph, executable method or benchmark result.

## 30. Conservative conclusion

The profile is selected and a gated proposal exists; the loop stops at the next human decision.

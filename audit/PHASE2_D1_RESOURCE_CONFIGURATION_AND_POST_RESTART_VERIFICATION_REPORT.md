# PHASE2 D1 resource configuration and post-restart verification report

**RUN_ID:** `20261013T085129Z`
**Mode:** READ_ONLY_RUNTIME_VERIFICATION · ZERO_COST · NO_DEPLOYMENT
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


## 1. Executive summary

D1P/D1H/D1R/D1V pass; overall D1 is PASS_RESOURCE_CONSTRAINED_PROFILE.

## 2. Input authorization

EDMUNDO MORI ORRILLO approved D1H/D1R/D1V on 2026-10-13; scope consumed only for D1.

## 3. D1 topology

Windows host controls WSL2; Ubuntu guest performs read-only verification.

## 4. D1P

PASS: split package prepared/published by Prompt25B-R1.

## 5. D1H

PASS from human-supplied Windows PowerShell evidence.

## 6. Windows config evidence

Backup/new hashes and final 10GB/2GB values recorded conservatively.

## 7. D1R

PASS from human restart report plus changed resource envelope in new guest.

## 8. D1V

PASS from independent read-only commands in the new Ubuntu session.

## 9. Memory

MemTotal 10182848 kB (~9.71 GiB), within 9.4–10.1 GiB.

## 10. Swap

SwapTotal 2097152 kB, /dev/sdc 2G, unused.

## 11. CPU

16 logical processors visible.

## 12. Linux filesystem

ext4 mounted; ~901.63 GiB raw available, above 305 GiB.

## 13. Docker

Client 29.1.3 present; daemon inactive, nonblocking for D1; no start/pull.

## 14. Resource capacity boundary

Full DBpedia/Virtuoso load feasibility remains unproven and high-risk.

## 15. DBpedia status

114 compressed files remain compressed; NOT_DEPLOYED.

## 16. G4

NOT_SATISFIED.

## 17. G5

Implementation and conformance pending.

## 18. G6I

Pending; G6D documented; adapters false.

## 19. Benchmark

NOT_CURRENTLY_ELIGIBLE; QALD test SEALED.

## 20. D1 final gate

D1_RESOURCE_CONFIGURATION_PASS_READY_FOR_D2_AUTHORIZATION

## 21. D2 authorization status

READY_UNSIGNED; D2 RESERVED_NOT_AUTHORIZED.

## 22. Next action

Exactly one: `HUMAN_D2_DECOMPRESSION_AND_RDF_VALIDATION_AUTHORIZATION`.

## 23. Claim boundary

D1 closes resource configuration only, not graph load/runtime feasibility.

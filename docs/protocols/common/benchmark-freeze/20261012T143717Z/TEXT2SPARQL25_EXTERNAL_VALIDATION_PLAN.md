# TEXT2SPARQL25 external-validation plan

**RUN_ID:** `20261012T143717Z`
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION


Status: `EXTERNAL_VALIDATION_PLAN_CONDITIONAL_LICENSE` — non-blocking for the QALD design freeze.

Verified metadata: first international challenge (2025), co-located with Text2KG at ESWC25, CEUR-WS
Vol-4094; DB25 and CK25; DB25 uses DBpedia **2015-10**; 200 DB25 pairs (100 English + 100 Spanish);
Precision/Recall/F1, NDCG for sorted results as reported in proceedings, plus query-complexity analysis;
leaderboard and endpoint response artifacts are public.
The official current AKSW examples repository is pinned for planning at
`c6666be31796d6b8555031198a6d54df166d4406` and lists DB25 questions/true results without payload download.

Conditional field: the current examples repository has Apache-2.0, but the official challenge page does not
separately state license scope for every dataset/graph payload. Graph-dump licensing and exact acquisition
scope must close before execution. Exact challenge-time repository revision and environment equivalence remain
unverified. No dataset was downloaded.

Future execution requires a separate acquisition manifest, graph ID, sealed/local split policy, evaluator
mapping, ZERO_COST/resource gates and authorization. QALD scores are never mixed with DB25 scores.

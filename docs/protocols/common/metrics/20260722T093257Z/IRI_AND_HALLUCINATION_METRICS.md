# IRI_AND_HALLUCINATION_METRICS

## A. query_grounding_constant_f1
Compara IRIs constantes predicted vs gold query. Diagnóstico. No demuestra linker outputs.

## B. hallucinated_iri_rate
IRI hallucinated iff: constant in predicted query ∧ not in standard vocab allowlist ∧ not in snapshot dictionary ∧ not in schema bundle ∧ not track-authorized.

Denominator: generated constant IRIs.

Deps: graph dictionary, schema manifest, vocab allowlist.

Status: `GRAPH_SNAPSHOT_PENDING` · `HALLUCINATED_IRI_RUNTIME_PENDING`.

Gold query alone ≠ universe of valid IRIs.

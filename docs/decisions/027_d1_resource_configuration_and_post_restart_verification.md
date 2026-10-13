# Decision 027 — D1 resource configuration and post-restart verification

Date: 2026-10-13 · RUN_ID: `20261013T085129Z`

The 10 GiB memory / 2 GiB swap constrained profile is effective. D1P, D1H, D1R and D1V pass under the
Windows-host/WSL2-Ubuntu topology. The local profile remains
`RESOURCE_CONSTRAINED_HIGH_RISK_FOR_FULL_GRAPH_LOAD`; D1 does not prove D4 feasibility or satisfy G4.

D2 authorization may be considered next, but D2 is not automatically authorized or executed.

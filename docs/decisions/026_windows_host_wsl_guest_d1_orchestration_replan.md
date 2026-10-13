# Decision 026 — Windows-host / WSL-guest D1 orchestration replan

Date: 2026-10-13 · RUN_ID: `20261013T080249Z`

Cursor's WSL dependency makes self-shutdown orchestration non-atomic. The interrupted authorized attempt
did apply 12/8, but is not D1 PASS. Old 12/8 is superseded; the new documentary subprofile is 10/2 to retain
5.19 GiB theoretical Windows headroom and avoid expanding host-side swap on a C: drive with ~7.4 GiB free.

D1 is split into D1P/D1H/D1R/D1V. Only D1P is performed here. ZERO_COST and the benchmark freeze remain
unchanged. If future D4 encounters local capacity failure, prefer an external ZERO_COST research server.

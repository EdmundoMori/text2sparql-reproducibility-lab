# Human authorization — deployment resource profile selection

**RUN_ID:** `20260722T162241Z`  
**Form status:** `READY_UNSIGNED`  
**Tag:** `RESOURCE_PROFILE_SELECTION_REQUIRED`

Select **exactly one**:

- [ ] `LOCAL_WSL_CURRENT` — RAM 7.35 GiB / swap 2.0 GiB — **NOT recommended** (HIGH OOM). Cost 0.00. No host change. Risk: load failure/host instability.
- [ ] `LOCAL_WSL_HOST_ADJUSTED` — raise WSL memory toward host ~15.19 GiB + swap — **conditional candidate**. Cost 0.00. Requires user `.wslconfig` + WSL restart (not applied by agents). Risk: residual OOM; host starvation.
- [ ] `WINDOWS_HOST_NATIVE_DOCKER` — Docker Desktop resource limits — conditional/untested. Cost 0.00. Path/interop complexity.
- [ ] `EXTERNAL_ZERO_COST_RESEARCH_SERVER` — preferred if available ZERO_COST specs — user must provide CPU/RAM/disk/access. Cost must remain 0.00.
- [ ] `REMOTE_IMMUTABLE_ENDPOINT` — only if immutable 2016-10-equivalent pin exists — **not primary substitute** for native without label.
- [ ] `REJECT_AND_DEFER_DEPLOYMENT` — keep compressed payload; defer native load.

## Empty fields

- approver:
- date:
- selected_profile:
- external_server_specs:
- decision:
- confirmation:

Does **not** authorize decompression, Docker pull, Virtuoso, or SPARQL.

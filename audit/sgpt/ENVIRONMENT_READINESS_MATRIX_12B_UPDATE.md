# ENVIRONMENT_READINESS_MATRIX — update 12B

| capability | new_status |
|---|---|
| transformers_pin | SELECTED_CANDIDATE_UNTESTED (4.25.1) |
| python_runtime | image digest verified (not pulled) |
| torch_runtime | Z2 CPU artifact identified (not downloaded) |
| gpt2_base | metadata only; DEFERRED_Z3 |
| import_preflight | awaiting Prompt 13A download auth |
| environment_gate | READY_FOR_Z2_DOWNLOAD_AUTHORIZATION |

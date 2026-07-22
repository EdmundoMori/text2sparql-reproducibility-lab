# D2 — Decompression and static RDF validation contract

**Status:** DOCUMENTED_NOT_EXECUTED · `NO_DECOMPRESSION`

Inputs: exactly 114 compressed files from handoff.  
Outputs: uncompressed files + SHA-256 + syntax validation logs.

Rules:

- never overwrite compressed
- sequential decompression
- abort if disk below envelope stop threshold
- SHA-256 uncompressed required
- syntax validation by serialization
- reject empty outputs
- no endpoint / SPARQL / QALD test

Requires future human execution authorization with decompression checkbox.

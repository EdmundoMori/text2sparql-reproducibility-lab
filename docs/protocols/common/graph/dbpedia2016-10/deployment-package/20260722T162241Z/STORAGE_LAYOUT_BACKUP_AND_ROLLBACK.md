# Storage layout, backup and rollback

Layout YAML: `configs/common/graph/dbpedia2016-10/deployment/DBPEDIA_2016_10_DEPLOYMENT_STORAGE_LAYOUT.yaml`

- `compressed/` **immutable** golden payload
- `uncompressed/` future D2 only
- `virtuoso/database|config|logs|checkpoints/`
- `rollback/` for DB copies
- Never version payloads in Git

Rollback: delete failed uncompressed/DB; restore from compressed; re-run authorized stage.

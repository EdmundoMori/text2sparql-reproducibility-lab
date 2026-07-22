# D3/D4 — Image acquisition and load contract

**Status:** DOCUMENTED_NOT_EXECUTED · `NO_DOCKER_PULL` · `NO_DEPLOYMENT`

## D3

- `docker pull` **by digest only** (`sha256:748863fd9026fac41667dac484e5044c6c34e95c75bce3bf26c9225fe7684eb6` for amd64)
- verify digest
- generate config from template + selected profile
- **no load**

## D4

- create container with bind mounts to layout
- bulk load 114 files in deterministic order
- checkpoint / error handling / restart
- transition toward read-only
- **no gold / no QALD test**

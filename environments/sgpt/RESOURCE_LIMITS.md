# RESOURCE_LIMITS — SGPT

**Host (MACHINE_VERIFIED / re-check Prompt 12):**

| Recurso | Valor |
|---|---|
| RAM WSL | ~7.4 GiB |
| RAM host Windows | ~16 GiB |
| VRAM | ~6 GiB (RTX 4050) |
| Paper | 2×12 GB |
| CPU | 8C / 16T |
| Disco `/` | ~921G libres |
| nvcc | ausente |
| Docker | disponible |
| Conda | ausente |

## Z2 (propuesto)

- CPU only; sin GPU  
- memory limit propuesta: **4g** (contenedor)  
- **2** CPUs  
- sin model download  
- timeout propuesto: **600s**  
- no workers múltiples  
- red bloqueada  

## Z3 (aún no aprobado)

- batch/subset **no** fijados  
- OOM → stop  
- no multi-GPU; no Apex; no distributed launch en smoke reducido  
- requiere Z2 pass + autorización descarga GPT-2  

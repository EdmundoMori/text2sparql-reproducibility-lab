# MACHINE_PROFILE

**Host lógico:** `LAPTOP-311333V7`  
**Fecha de detección:** 2026-07-18T10:46:14+02:00  
**Método de detección:** comandos locales (`uname`, `lscpu`, `free`, `nvidia-smi`, `docker`, `powershell.exe`, versiones de herramientas).  
**Nota:** la detección de GPU/Docker requiere acceso completo al host WSL; en sandbox restringido `nvidia-smi` puede fallar con “GPU access blocked”.

---

## 1. Sistema operativo y entorno

| Campo | Valor detectado |
|---|---|
| Host OS | Windows (hostname `LAPTOP-311333V7`) |
| Entorno de trabajo | **WSL2** |
| Distro WSL | Ubuntu 22.04.5 LTS (`Ubuntu-22.04`) |
| Kernel | `6.6.87.2-microsoft-standard-WSL2` |
| Arquitectura | `x86_64` |
| WSL Interop | Presente (`WSLInterop`, `WSL_INTEROP`) |

**Clasificación de plataforma:** Windows host + Linux guest (WSL2). El laboratorio opera dentro de WSL2/Ubuntu.

---

## 2. Hardware

| Recurso | Valor detectado | Notas |
|---|---|---|
| CPU | AMD Ryzen 7 7840HS w/ Radeon 780M Graphics | 8 cores / 16 threads |
| RAM visible en WSL | **7.4 GiB** total (`MemTotal` ≈ 7710908 kB) | Disponible ≈ 5.5 GiB en el momento de la medición |
| RAM del host Windows | **≈ 16 GiB** (`TotalPhysicalMemory` = 16309932032) | WSL no ve toda la RAM del host |
| GPU NVIDIA | GeForce RTX 4050 Laptop GPU | `nvidia-smi` OK fuera de sandbox |
| VRAM | **6141 MiB** (≈ 6 GiB) | Uso medido: 86 MiB |
| GPU AMD (host) | AMD Radeon 780M | Reportada por Windows; no usada como compute CUDA en WSL |
| CUDA (driver) | **13.0** (reportado por driver NVIDIA 581.86 / SMI 580.110) | Toolkit `nvcc` **no instalado** |
| Dispositivos `/dev/nvidia*` | **Ausentes** en el guest | Compute vía stack WSL (`/usr/lib/wsl/lib/nvidia-smi`) |
| Disco (`/`) | 1007G total, **901G libres** (6% usado) | Suficiente para clones, datasets y logs |

---

## 3. Software detectado

| Herramienta | Estado | Versión / detalle |
|---|---|---|
| Git | Presente | 2.34.1 |
| Python | Presente | 3.10.12 (`python3`; comando `python` ausente) |
| pip | Presente | 22.0.2 (Python 3.10) |
| Java | Presente | OpenJDK 21.0.11 (`java` + `javac`) |
| Node.js | Presente | v18.20.8 |
| npm | Presente | 10.8.2 |
| nvm | Presente | 0.39.7 |
| Conda | **Ausente** | — |
| uv | **Ausente** | — |
| Poetry | Presente | 2.3.1 |
| Ruby | **Ausente** | re-check 2026-07-19 (Prompt 4B): `ruby` not found |
| Bundler | **Ausente** | re-check 2026-07-19: `bundle` not found |
| Docker (CLI) | Presente | 29.1.3 |
| Docker (daemon) | Presente | Server 29.1.3, overlay2, cgroup v2 |
| Docker Compose | **Plugin ausente** | `docker compose` y `docker-compose` no disponibles |
| GNU Make | Presente | 4.3 |
| just | **Ausente** | Se usa `Makefile` |
| CUDA Toolkit (`nvcc`) | **Ausente** | Solo runtime/driver vía WSL |

**Dependencias globales:** no se ha instalado nada adicional en esta fase.

---

## 4. Clases de reproducibilidad en esta máquina

Definiciones operativas usadas por el laboratorio:

| Clase | Significado |
|---|---|
| `feasible_local_cpu` | Ejecutable en CPU local con recursos actuales (RAM/CPU/disco), sin GPU ni API de pago obligatoria |
| `feasible_local_gpu` | Ejecutable usando la GPU NVIDIA local (RTX 4050, ≈6 GB VRAM) |
| `feasible_using_api` | Ejecutable si se usan APIs externas (LLM/endpoints) con credenciales en `.env` |
| `requires_external_gpu` | Necesita GPU/VRAM o cluster fuera de esta máquina |
| `currently_unknown` | Aún no auditado; no se puede clasificar con evidencia |

### Clasificación actual del host (capacidad, no de métodos)

| Clase | ¿Aplicable al host? | Evidencia / límite |
|---|---|---|
| `feasible_local_cpu` | **Sí, con límites** | 16 hilos CPU; RAM WSL ≈ 7.4 GiB (estrecha para modelos grandes en memoria) |
| `feasible_local_gpu` | **Sí, con límites** | RTX 4050 ≈ 6 GB VRAM; apta para inferencia/ligero fine-tuning; insuficiente para muchos entrenamientos full-scale |
| `feasible_using_api` | **Sí** | Sin bloqueo de plataforma; requiere claves en `.env` (no versionadas) |
| `requires_external_gpu` | **Condicional** | Probable para entrenamientos grandes o VRAM >> 6 GB |
| `currently_unknown` | **Para cada método** | Ningún método ha sido auditado aún; la clase por `method_id` permanece `currently_unknown` |

### Asignación inicial por método candidato

Hasta completar la auditoría nativa, **todos** los `method_id` se marcan `currently_unknown` en `METHOD_REGISTRY.yaml`. No se infiere GPU/API/CPU solo por el nombre del repositorio.

---

## 5. Limitaciones detectadas

1. **RAM WSL limitada (≈7.4 GiB)** frente a ≈16 GiB del host: riesgo de OOM en pipelines Java/Python pesados o cargas RDF grandes.  
2. **VRAM ≈6 GB:** puede forzar cuantización, batches pequeños o APIs para LLMs grandes.  
3. **`nvcc` ausente:** no hay toolkit CUDA completo; PyTorch/TF con CUDA dependen de wheels/runtime, no de compilación local.  
4. **`/dev/nvidia*` ausente:** algunos contenedores o librerías que exigen device nodes clásicos pueden fallar; verificar caso a caso.  
5. **Docker Compose no instalado:** `docker compose` / `docker-compose` no disponibles; los stacks Compose requerirán instalar el plugin o invocar `docker` a bajo nivel.  
6. **Sin Conda ni uv:** entornos habrá que gestionarlos con venv/Poetry/Docker según el método.  
7. **Comando `python` ausente:** solo `python3` (relevante para scripts upstream que asuman `python`).  
8. **Ruby/Bundler ausentes:** bloquean smokes de `rdfconfig_llm` / companion hasta install explícito de runtime.  
9. **Sandbox de agentes:** detecciones GPU pueden fallar en entornos restringidos; usar perfil de esta fecha como referencia del host real.

**Re-detección Prompt 4B (2026-07-19):** RAM WSL 7.4 GiB / ~5.4 GiB available; `nvidia-smi` falló en entorno restringido (GPU access blocked); Poetry 2.3.1; Ruby/Bundler ABSENT; Compose ABSENT.

**Estas limitaciones no impiden el proyecto.** El comportamiento esperado del agente ante pedidos inconvenientes está definido en `PROJECT_CONTEXT.md` §7 (advertencia → solución → continuar).

---

## 6. Implicaciones para la Fase 1

- Priorizar auditorías y smoke tests ligeros antes de descargas masivas de modelos.  
- Documentar si un método exige GPU >6 GB o RAM >>8 GiB como `requires_external_gpu` o bloqueo por memoria.  
- Preferir contenedores solo tras confirmar compatibilidad Docker+GPU en WSL para ese método.  
- No clasificar un método como `feasible_*` sin evidencia de su auditoría.  
- Ante conflicto pedido↔hardware: avisar, proponer mitigación (§7.4 de `PROJECT_CONTEXT.md`) y continuar sin abortar la fase.

---

## 7. Protocolo de advertencia (referencia rápida)

Formato mínimo cuando un pedido sea inconveniente:

```text
ADVERTENCIA [recurso]: <por qué choca con este perfil>
SOLUCIÓN: <mitigación concreta>
CONTINÚO: <qué haré ahora con la ruta viable / degradada>
```

No bloquear al usuario; no ocultar el riesgo; registrar degradaciones que afecten a la etiqueta de reproducción.

---

## 8. Comandos de re-detección

```bash
make profile
# o:
uname -a
lscpu
free -h
nvidia-smi
docker info
docker compose version
git --version
python3 --version
java -version
node --version
conda --version; uv --version; poetry --version
df -h /
```


---

## Observation — Prompt 25A (20260722T162241Z)

Redeetected read-only for deployment package (no host changes):

| Campo | Valor |
|---|---|
| WSL RAM | 7.35 GiB |
| Host RAM | 15.19 GiB |
| Swap | 2.0 GiB |
| Disk free | 910.8 GiB (ext4) |
| Docker | 29.1.3 |
| Compose | ABSENT |
| `.wslconfig` | ABSENT |
| Feasibility tag | `LOCAL_WSL_CURRENT_PROFILE_CONDITIONAL_HIGH_RISK` |

Historical profile above preserved. No `.wslconfig` created/modified.

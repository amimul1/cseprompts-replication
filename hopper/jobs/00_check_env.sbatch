#!/bin/bash
# Checks GPU, driver, venv, torch<->CUDA and outbound internet from a compute node.
# Uses the smallest MIG slice so it starts quickly.   sbatch hopper/jobs/00_check_env.sbatch
#SBATCH --partition=gpuq
#SBATCH --qos=gpu
#SBATCH --job-name=cse-check
#SBATCH --output=/scratch/%u/cseprompts/logs/%x-%j.out
#SBATCH --error=/scratch/%u/cseprompts/logs/%x-%j.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --gres=gpu:1g.10gb:1
#SBATCH --mem=15gb
#SBATCH --time=0-00:20:00

set -uo pipefail
umask 0027
cd "${SLURM_SUBMIT_DIR:-$HOME/CSEPROMPTS}"
source hopper/env.sh

echo "== node: $(hostname)  job: ${SLURM_JOB_ID:-}  $(date)"
nvidia-smi
echo "== python / torch / vllm"
python - <<'EOF'
import sys, torch
print("python", sys.version.split()[0])
print("torch", torch.__version__, "cuda build", torch.version.cuda, "available", torch.cuda.is_available())
if torch.cuda.is_available():
    print("device", torch.cuda.get_device_name(0), "mem GB", round(torch.cuda.get_device_properties(0).total_memory / 1e9, 1))
import vllm; print("vllm", vllm.__version__)
EOF
echo "== outbound internet from compute node (decides where model downloads must run)"
if curl -sS -m 10 -o /dev/null -w "%{http_code}\n" https://huggingface.co; then
    echo "internet: YES"
else
    echo "internet: NO -> download models on the login node with hopper/download_model.sh"
fi
echo "== storage"
df -h "$HOME" "/scratch/$USER" 2>/dev/null

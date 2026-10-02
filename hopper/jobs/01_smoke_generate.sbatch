#!/bin/bash
# End-to-end smoke test: tiny model, first 5 prompts of each split.
#   sbatch hopper/jobs/01_smoke_generate.sbatch
#   sbatch --export=ALL,MODEL=Qwen/Qwen3-0.6B hopper/jobs/01_smoke_generate.sbatch
#SBATCH --partition=gpuq
#SBATCH --qos=gpu
#SBATCH --job-name=cse-smoke
#SBATCH --output=/scratch/%u/cseprompts/logs/%x-%j.out
#SBATCH --error=/scratch/%u/cseprompts/logs/%x-%j.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:2g.20gb:1
#SBATCH --mem=30gb
#SBATCH --time=0-01:00:00

set -euo pipefail
umask 0027
cd "${SLURM_SUBMIT_DIR:-$HOME/CSEPROMPTS}"
source hopper/env.sh

MODEL="${MODEL:-Qwen/Qwen2.5-Coder-0.5B-Instruct}"
OUT="$CSE_STORE/results/generations"

echo "== $(hostname) job ${SLURM_JOB_ID:-} model=$MODEL git=$(git rev-parse --short HEAD) $(date)"
nvidia-smi --query-gpu=name,memory.total --format=csv

python scripts/generate.py --model "$MODEL" --protocol greedy --limit 5 --gpu-mem 0.80 --out-dir "$OUT" --overwrite

echo "== sample output"
head -c 1500 "$OUT/${MODEL//\//__}/greedy__limit5/codingsites.jsonl"; echo

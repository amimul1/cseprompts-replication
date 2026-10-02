#!/bin/bash
# Generate outputs for one registered model and one decoding protocol.
#   sbatch --export=ALL,MODEL_KEY=llama31_8b_instruct,PROTOCOL=greedy  hopper/jobs/10_generate.sbatch
#   sbatch --export=ALL,MODEL_KEY=mistral_7b_instruct_v01,PROTOCOL=sampled hopper/jobs/10_generate.sbatch
# 7-8B models in bf16 fit a 40 GB MIG slice. For a full GPU, override on the command line:
#   sbatch --gres=gpu:A100.80gb:1 --export=ALL,MODEL_KEY=...,PROTOCOL=... hopper/jobs/10_generate.sbatch
#SBATCH --partition=gpuq
#SBATCH --qos=gpu
#SBATCH --job-name=cse-gen
#SBATCH --output=/scratch/%u/cseprompts/logs/%x-%j.out
#SBATCH --error=/scratch/%u/cseprompts/logs/%x-%j.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --gres=gpu:3g.40gb:1
#SBATCH --mem=60gb
#SBATCH --time=0-06:00:00

set -euo pipefail
umask 0027
cd "${SLURM_SUBMIT_DIR:-$HOME/CSEPROMPTS}"
source hopper/env.sh

: "${MODEL_KEY:?set MODEL_KEY, e.g. --export=ALL,MODEL_KEY=llama31_8b_instruct,PROTOCOL=greedy}"
: "${PROTOCOL:?set PROTOCOL (greedy or sampled)}"

echo "== $(hostname) job ${SLURM_JOB_ID:-} model_key=$MODEL_KEY protocol=$PROTOCOL git=$(git rev-parse --short HEAD) $(date)"
if [ -n "$(git status --porcelain)" ]; then echo "WARNING: repo has uncommitted changes (recorded as git_dirty)"; fi
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv

python scripts/generate.py --model-key "$MODEL_KEY" --protocol "$PROTOCOL"

echo "== outputs"
ls -la "$CSE_STORE/results/generations/$MODEL_KEY/$PROTOCOL/"

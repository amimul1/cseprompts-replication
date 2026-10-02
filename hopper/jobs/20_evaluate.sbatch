#!/bin/bash
# Evaluate one generation run. CPU only: runs model-written code under the harness sandbox,
# so never run it on the login node.
#   sbatch --export=ALL,MODEL_KEY=llama31_8b_instruct,PROTOCOL=greedy hopper/jobs/20_evaluate.sbatch
# Optional: TRACK=auto|manual (default auto; manual = your hand-cleaned files, pulled from git)
#           MODES=original (default: every test suite in the repo)
#   sbatch --export=ALL,MODEL_KEY=llama31_8b_instruct,PROTOCOL=greedy,TRACK=manual,MODES=original hopper/jobs/20_evaluate.sbatch
#SBATCH --partition=normal
#SBATCH --job-name=cse-eval
#SBATCH --output=/scratch/%u/cseprompts/logs/%x-%j.out
#SBATCH --error=/scratch/%u/cseprompts/logs/%x-%j.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32gb
#SBATCH --time=0-04:00:00

set -euo pipefail
umask 0027
cd "${SLURM_SUBMIT_DIR:-$HOME/CSEPROMPTS}"
source hopper/env.sh

: "${MODEL_KEY:?set MODEL_KEY}"
: "${PROTOCOL:?set PROTOCOL (greedy or sampled)}"
RUN="$CSE_STORE/results/generations/$MODEL_KEY/$PROTOCOL"
echo "== $(hostname) job ${SLURM_JOB_ID:-} run=$RUN git=$(git rev-parse --short HEAD) $(date)"

TRACK="${TRACK:-auto}"
MODES="${MODES:-}"   # empty = every test suite this repo has
echo "== track=$TRACK modes=${MODES:-all available}"
# shellcheck disable=SC2086  # MODES is a word list on purpose
python scripts/evaluate.py --run "$RUN" --track "$TRACK" ${MODES:+--modes $MODES} --workers "${SLURM_CPUS_PER_TASK:-16}" \
    --out "$CSE_STORE/results/evaluations"

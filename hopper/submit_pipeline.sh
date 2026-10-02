#!/bin/bash
# Queue generation (GPU) + evaluation (CPU) for one model and protocol. The evaluation starts
# automatically when the generation job finishes successfully (Slurm afterok dependency).
#   bash hopper/submit_pipeline.sh llama31_8b_instruct greedy
#   bash hopper/submit_pipeline.sh mistral_7b_instruct_v01 sampled
# Extra sbatch options for the generation job can follow, e.g. --gres=gpu:A100.80gb:1
set -euo pipefail
cd "$(dirname "$0")/.."
MODEL_KEY="${1:?usage: submit_pipeline.sh MODEL_KEY PROTOCOL [extra sbatch options for generation]}"
PROTOCOL="${2:?usage: submit_pipeline.sh MODEL_KEY PROTOCOL}"
shift 2
python3 -c "import json,sys; m=json.load(open('configs/models.json'))['models']; sys.exit(0 if '$MODEL_KEY' in m else 'unknown MODEL_KEY: $MODEL_KEY; known: ' + ', '.join(m))"
python3 -c "import json,sys; p=json.load(open('configs/protocols.json'))['protocols']; sys.exit(0 if '$PROTOCOL' in p else 'unknown PROTOCOL: $PROTOCOL; known: ' + ', '.join(p))"
if [ -n "$(git status --porcelain)" ]; then echo "WARNING: uncommitted changes in the repo (they will be recorded as git_dirty)"; fi
GEN=$(sbatch --parsable "$@" --export=ALL,MODEL_KEY="$MODEL_KEY",PROTOCOL="$PROTOCOL" hopper/jobs/10_generate.sbatch)
EVAL=$(sbatch --parsable --dependency=afterok:"$GEN" --export=ALL,MODEL_KEY="$MODEL_KEY",PROTOCOL="$PROTOCOL" \
       hopper/jobs/20_evaluate.sbatch)
echo "$(date +%F) generation job $GEN, evaluation job $EVAL (starts after $GEN succeeds): $MODEL_KEY / $PROTOCOL @ $(git rev-parse --short HEAD)"
echo "logs: /scratch/$USER/cseprompts/logs/cse-gen-$GEN.out and cse-eval-$EVAL.out"

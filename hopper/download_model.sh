#!/bin/bash
# Download a model's weights into $HF_HOME (on /scratch or /projects, never $HOME).
#   bash hopper/download_model.sh Qwen/Qwen2.5-Coder-0.5B-Instruct
# Gated models (Llama) need `hf auth login` first, with a token you create on huggingface.co.
# A download is network I/O, not computation, so it is OK on the login node if compute nodes
# have no internet (00_check_env.sbatch tells you which).
set -euo pipefail
cd "$(dirname "$0")/.."
source hopper/env.sh
MODEL="${1:?usage: download_model.sh <hf-model-id>}"
hf download "$MODEL" --exclude "*.pth" "original/*"
du -sh "$HF_HOME/hub/models--${MODEL//\//--}"

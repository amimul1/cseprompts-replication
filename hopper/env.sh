# Shared settings for every Hopper session and job:  source hopper/env.sh
#
# Storage (GMU ORC "Storage Space on the Cluster"):
#   $HOME        60 GB, backed up          -> code + Python venv
#   /scratch     no quota, 90-day purge    -> model weights, caches, logs, raw outputs
#   /projects    faculty-requested         -> set CSE_STORE to it once it exists
#
# Override any of these before sourcing, e.g.  export CSE_STORE=/projects/<prof>/cseprompts

# Compiler first, then Python.  `ml spider python/3.12.1-33` says it needs gnu12/12.3.0
# (the ORC docs use gnu10 for their older Python 3.9 module; same idea, newer compiler).
export CSE_COMPILER_MODULE="${CSE_COMPILER_MODULE:-gnu12/12.3.0}"
export CSE_PY_MODULE="${CSE_PY_MODULE:-python/3.12.1-33}"
module load "$CSE_COMPILER_MODULE" 2>/dev/null || true

export CSE_REPO="${CSE_REPO:-$HOME/CSEPROMPTS}"
export CSE_VENV="${CSE_VENV:-$HOME/envs/cseprompts}"
export CSE_STORE="${CSE_STORE:-/scratch/$USER/cseprompts}"

export HF_HOME="$CSE_STORE/hf_home"                 # model downloads (tens of GB each)
# The HF access token stays in your private, backed-up home folder, never on /scratch or in git.
export HF_TOKEN_PATH="$HOME/.cache/huggingface/token"
export UV_CACHE_DIR="$CSE_STORE/uv_cache"           # pip/uv wheel cache
export UV_LINK_MODE=copy                            # cache (/scratch) and venv ($HOME) are different filesystems
export UV_PYTHON_INSTALL_DIR="$HOME/.local/share/uv/python"
export VLLM_CACHE_ROOT="$CSE_STORE/vllm_cache"
# vLLM's engine runs in a child process. Forking it fails on Hopper ("Cannot re-initialize
# CUDA in forked subprocess", smoke job 1375234), so start it fresh with spawn.
export VLLM_WORKER_MULTIPROC_METHOD=spawn
export TMPDIR="${TMPDIR:-$CSE_STORE/tmp}"
export PATH="$HOME/.local/bin:$PATH"

mkdir -p "$HF_HOME" "$UV_CACHE_DIR" "$VLLM_CACHE_ROOT" "$TMPDIR" "$CSE_STORE/logs"

if [ -f "$CSE_VENV/bin/activate" ]; then
    # The venv's interpreter comes from this ORC module; load it so its shared libraries resolve.
    module load "$CSE_PY_MODULE" 2>/dev/null || true
    source "$CSE_VENV/bin/activate"
fi

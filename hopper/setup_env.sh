#!/bin/bash
# One-time environment setup on Hopper.  Run from the repo root:
#     bash hopper/setup_env.sh
#
# Follows the ORC "Managing Python Virtual Environments" recipe: load the compiler
# module, load an ORC Python module, build a venv in $HOME, pip-install into it.
# vLLM 0.30 needs Python >= 3.10, so we use ORC's python/3.12.1-33 (found with
# `ml spider python`).  Only if that module can't be loaded do we fall back to a
# user-space Python 3.12 from uv.
set -euo pipefail

cd "$(dirname "$0")/.."
export CSE_REPO="$PWD"
source hopper/env.sh          # loads gnu12/12.3.0, sets cache dirs on /scratch

PY_MODULE="$CSE_PY_MODULE"

if module load "$PY_MODULE" 2>/dev/null && python3 -c 'import sys; assert sys.version_info >= (3, 10)'; then
    echo ">> using ORC module $PY_MODULE: $(python3 --version)"
    python3 -m venv "$CSE_VENV"
    module unload "$PY_MODULE"      # as in the ORC PyTorch guide: the venv carries its own interpreter
else
    echo ">> $PY_MODULE not loadable; falling back to uv-managed Python 3.12"
    module load python 2>/dev/null || true
    command -v uv >/dev/null 2>&1 || python3 -m pip install --user --quiet uv
    uv python install 3.12
    uv venv --python 3.12 "$CSE_VENV"
fi

source "$CSE_VENV/bin/activate"
python -m pip install --upgrade --quiet pip

echo ">> installing GPU requirements (vLLM + torch; a few GB, takes several minutes)"
python -m pip install --cache-dir "$UV_CACHE_DIR/pip" -r requirements-gpu.txt

python - <<'EOF'
import sys, torch, vllm
print("python", sys.version.split()[0], "| torch", torch.__version__, "| cuda build", torch.version.cuda, "| vllm", vllm.__version__)
EOF
echo ">> done. Next: sbatch hopper/jobs/00_check_env.sbatch"

#!/usr/bin/env bash
set -e

CONDA_ENV=${1:-""}
if [ -n "$CONDA_ENV" ]; then
    # This is required to activate conda environment
    eval "$(conda shell.bash hook)"

    conda create -n $CONDA_ENV python=3.10.0 -y
    conda activate $CONDA_ENV

    conda install -c nvidia cuda-toolkit=12.9 -y
else
    echo "Skipping conda environment creation. Make sure you have the correct environment activated."
fi

# update pip to latest version for pyproject.toml setup.
pip install -U pip wheel

# install dev dependencies
pip install \
    "pytest" \
    "plotly==6.1.1" \
    "dash==3.0.4" \
    "jupyter"

# install
pip install -e .

conda activate $CONDA_ENV
#!/bin/bash

cd "$(dirname "$0")/.."
source venv/bin/activate
export PYTHONPATH=$(pwd)
python3 web/app.py

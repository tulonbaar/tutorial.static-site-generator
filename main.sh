#!/bin/bash

# Start a static site generator server
export PYTHONPATH=src
python3 src/main.py
cd public && python3 -m http.server 8888

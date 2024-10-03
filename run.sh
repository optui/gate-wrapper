#!/bin/bash

# Step 1: Activate the virtual environment
source venv/bin/activate

# Step 2: Export necessary environment variables
LD_LIBRARY_PATH=$(pwd)/venv/lib/python3.11/site-packages/opengate_core.libs:${LD_LIBRARY_PATH}
LD_PRELOAD=$(pwd)/venv/lib/python3.11/site-packages/opengate_core.libs/libG4processes-976c780f.so:$(pwd)/venv/lib/python3.11/site-packages/opengate_core.libs/libG4geometry-976dba65.so:${LD_PRELOAD}
export LD_LIBRARY_PATH
export LD_PRELOAD

# Step 3: Run the Python script
python3 main.py

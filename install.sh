#!/bin/bash
# Create virtual env, activate and Install alls modules python
#sudo apt install python3-ven

python3 -m venv .
source ./bin/activate

pip install mkdocs
pip install mkdocs-material
pip install notebook



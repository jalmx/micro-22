#!/bin/bash
# Create virtual env, activate and Install alls modules python
#sudo apt install python3-ven

python3 -m venv .
source ./bin/activate

pip install mkdocs
pip install mkdocs-material
pip install mkdocs-plugin-tags
pip install mkdocs-markmap
pip install mkdocs-pdf-export-plugin
pip install mkdocs-minify-plugin

pip install notebook
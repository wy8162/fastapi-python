#! /bin/bash
apt-get update
apt-get install -yq git curl jq python3 python3-pip
pip3 install poetry
git clone https://github.com/wy8162/study_gcp.git
cd study_gcp
poetry install
cd fastapi
poetry run python3 main.py
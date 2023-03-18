#! /bin/bash
apt-get update
apt-get install -yq git python3 python3-pip
pip3 install poetry
git clone https://github.com/wy8162/study_gcp.git
cd study_gcp

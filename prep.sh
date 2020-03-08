#!/usr/bin/env bash
#packages installation
sudo apt install python3 python3-pip python3-venv

path=$(dirname $(readlink -f $0))
echo ${path}

#env creation
python3 -m venv ${path}/env
source ${path}/env/bin/activate

#requirements installation
pip install -r ${path}/requirements.txt

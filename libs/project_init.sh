#!/usr/bin/env bash

pyenv install 3.6.7
pyenv local 3.6.7
pip install pipenv
pipenv install
pipenv run pip install pip==18.0
pipenv run python -m ipykernel install --user --name=ml_server_framework
#!/usr/bin/env bash
source config.sh

sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev

# Install pyenv and its dependencies
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
pyenv update

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv install 3.6.7
pyenv local 3.6.7
pip install pipenv
pipenv install
pipenv run pip install black
pipenv run pip install pip==18.0
pipenv run python -m ipykernel install --user --name=ml_server_framework
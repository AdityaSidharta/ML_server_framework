SHELL := /bin/bash

help:
	@echo "setup - setup pyenv and pipenv for the project"
	@echo "format - performing black formatting on the project"
	@echo "pylint - performing pylint to check the code quality"
	@echo "jupyter - open jupyter notebook on the project"
	@echo "docker-clean - prune all docker volumes, containers, and images"
	@echo "docker-compose - run and setup docker compose"

setup:
	bash libs/setup.sh
	pipenv shell

format:
	black src
	nbstripout */*

pylint:
	pylint src

jupyter:
	bash libs/run_jupyter.sh

docker-clean:
	bash libs/clean_docker.sh

docker-compose:
	bash libs/run_docker_compose.sh


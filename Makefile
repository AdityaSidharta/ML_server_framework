SHELL := /bin/bash

help:
	@echo "setup - setup pyenv and pipenv for the project"
	@echo "format - performing black formatting on the project"
	@echo "pylint - performing pylint to check the code quality"
	@echo "jupyter - open jupyter notebook on the project"
	@echo "docker-clean - prune all docker volumes, containers, and images"
	@echo "docker-postgres - run and setup postgress database"

setup:
	bash libs/setup.sh

format:
	black src

pylint:
	pylint src

jupyter:
	pipenv run jupyter notebook

docker-clean:
	bash docker/clean_docker.sh

docker-postgres:
	bash docker/docker-postgres/run_db.sh

docker-minio:
	bash docker/docker-minio/run_minio.sh

SHELL := /bin/bash

help:
	@echo "docker-clean - prune all docker volumes, containers, and images"
	@echo "docker-compose - run and setup docker compose"

docker-clean:
	bash libs/clean_docker.sh

docker-compose:
	bash libs/run_docker_compose.sh


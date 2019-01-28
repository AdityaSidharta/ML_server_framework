#!/usr/bin/env bash

source config.sh
docker build -t ml_server_deploy -f ./docker/docker-deploy/Dockerfile .
docker run -it -p ${FLASK_PORT}:1234 --network test_net ml_server_deploy
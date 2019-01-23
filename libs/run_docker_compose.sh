#!/usr/bin/env bash

rm -rf ./docker/docker-deploy/src
rm -f ./docker/docker-deploy/config.sh
cp -r src ./docker/docker-deploy/
cp config.sh ./docker/docker-deploy/
source config.sh
docker-compose up -d --build
#!/usr/bin/env bash

docker stop $(docker ps -a -q)
docker system prune
sudo rm -rf ./docker/docker-postgres/db/*

#!/usr/bin/env bash

set -e
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT

if [ $# != 1 ]
then
    echo "Number of arguments supplied is wrong"
    exit 1
fi

if [ $1 == 'deploy' ]
then
    bash libs/run_docker_deploy.sh
elif [ $1 == 'model' ]
then
    bash libs/run_docker_model.sh
elif [ $1 == 'filldata' ]
then
    bash libs/run_docker_filldata.sh
elif [ $1 == 'debug' ]
then
    tail -f /dev/null
else
    echo "The argument is not valid, only the following [deploy, model, filldata, debug] is accepted"
    exit 1
fi
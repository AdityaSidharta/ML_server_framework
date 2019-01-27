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
    bash libs/run_deploy.sh
elif [ $1 == 'model' ]
then
    bash libs/run_model.sh
elif [ $1 == 'fill_data' ]
then
    bash libs/run_fill_data.sh
else
    echo "The argument is not valid, only the following [deploy, model, fill_data] is accepted"
    exit 1
fi
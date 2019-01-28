FROM python:3.6.7

# Pull all the dependencies to 1 folder

FROM python:3.6.7-alpine

#WORKDIR /usr/src/app
#EXPOSE 1234
#COPY docker/docker-deploy/src /usr/src/app/src
#COPY docker/docker-deploy/config.sh ./
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#RUN /bin/bash -c "source ./config.sh; python ./src/flask/run_deploy.py"


WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 1234

ENTRYPOINT [ ./entrypoint.sh ]

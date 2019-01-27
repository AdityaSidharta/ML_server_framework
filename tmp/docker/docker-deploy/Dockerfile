FROM python:3.6.7

WORKDIR /usr/src/app
EXPOSE 1234
COPY ./src /usr/src/app/src
COPY config.sh ./
COPY ../../../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN /bin/bash -c "source ./config.sh; python ./src/flask/run_deploy.py"
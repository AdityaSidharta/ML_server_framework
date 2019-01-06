FROM python:3.6.7

WORKDIR /usr/src/app
COPY config.sh ./
COPY ./docker/docker-deploy/requirements.txt ./
COPY ./src /usr/src/app/src
EXPOSE 1234
RUN pip install --no-cache-dir -r requirements.txt
RUN /bin/bash -c "source config.sh"
RUN echo "$PWD"
RUN echo "$PYTHONPATH"
RUN echo "$MINIO_ACCESS_KEY"
CMD [ "python", "./src/flask/hello_world.py"]
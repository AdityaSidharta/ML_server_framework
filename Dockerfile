FROM python:3.6.7

WORKDIR /usr/src/app

COPY . /usr/src/app
EXPOSE 1234
RUN pip install -r requirements.txt
ENTRYPOINT ["./entrypoint.sh"]
CMD ["debug"]
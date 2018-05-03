#docker build -t chatroom:latest .
FROM python:3.6.5-alpine3.7
MAINTAINER Stark-X

WORKDIR /usr/src/app
COPY . .
RUN pip install pipenv && \
    ls && \
    pipenv install --system
CMD python server.py

# Filename: Dockerfile 
FROM python:3.8-slim

WORKDIR /usr/src/app
COPY * ./
RUN pip install pipenv
RUN pipenv install
ENTRYPOINT pipenv run python webhook.py
EXPOSE 80

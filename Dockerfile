# Filename: Dockerfile 
FROM python:3.8

WORKDIR /usr/src/app
COPY * ./
RUN pip install pipenv
RUN pipenv install
RUN pipenv graph
RUN pipenv run python webhook.py
EXPOSE 80

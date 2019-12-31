# Filename: Dockerfile 
FROM python:3.8

WORKDIR /usr/src/app
COPY * ./
RUN pip install pipenv
RUN pipenv install
RUN pipenv graph
ENTRYPOINT pipenv run python webhook.py
EXPOSE 80

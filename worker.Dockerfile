FROM python:3.10-slim

WORKDIR /worker
COPY . /worker

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile --verbose


FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile --verbose

#EXPOSE 8000


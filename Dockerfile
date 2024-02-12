FROM python:3.10-slim

WORKDIR /root

COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock

RUN	pip3 install pipenv && \
    apt-get update && apt-get install -y git && \
    pipenv install --system --deploy

COPY database ./database
COPY tests ./tests
COPY src ./src
COPY .env main.py ./


ARG FLAG
RUN echo ${FLAG}

EXPOSE 8000

#CMD ["python", "database/setup_database.py"]
#CMD ["python", "main.py", "-r"]
#CMD ["python", "main.py", "${FLAG}"]
#CMD ["python", "main.py", "-w"]

ENTRYPOINT ["sh", "-c", "python database/setup_database.py && python main.py -r"]
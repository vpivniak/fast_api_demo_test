# FastApi demo project

## Docker

Run application, worker and database using docker compose.

Run command below:

```sh
docker compose up -d
```

## App

Application is ready on route.

```
0.0.0.0:8001
```

```
0.0.0.0:8001/weather?date=2024-02-14
```

## Tests

Tests run outside the docker.

run commands below:

```sh
pip install pipenv
```
```sh
pipenv shell
```
```sh
pipenv install
```

```sh
source env.sh
```

```sh
pytest tests/
```

## Notes
#### Project only.
#### Suggested Improvements:
1. Split the worker functionality and the REST API endpoint application into two different projects (with monorepository)
2. Add more business logic for the temperature and cover them with tests
3. It is possible to add mysql tests with the test database for monitoring purposes
4. Implement running of tests inside of docker

## License
MIT
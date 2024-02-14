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
source env.sh
```

```sh
pytest tests/
```

## Notes
#### Project only.
#### Further improvements:
- '.env' file with 'secret keys' should be under gitignore. Added for test project only
- Split worker and application to the different projects with own dependencies.
- Add negative tests to check weather API.

## License

MIT
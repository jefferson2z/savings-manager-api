# Savings Manager API

The api for the Savings Manager app

## Install

```
$ pipenv install
```

## Run

```
$ uvicorn app.main:app --reload
```

## Generate Migration based on models

```
$ alembic revision --autogenerate -m 'descriptive message here'
```

## Run migrations to latest

```
$ alembic upgrade head
```

## Test

For testing run:

```
pytest
```

For coverage report run:

```
```

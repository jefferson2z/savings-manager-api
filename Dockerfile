FROM python:3.10-slim-buster as builder
RUN apt-get update \
  && apt-get -y install \
  libpq-dev \
  gcc

WORKDIR /usr/src/app
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt ./
RUN pip install  --no-cache -r requirements.txt


FROM python:3.10-slim-buster
RUN apt-get update \
  && apt-get -y install \
  libpq-dev

WORKDIR /usr/src/app

COPY --from=builder /venv /venv
COPY . .

ENV DATABASE_URI=sqlite:///./testing_database.db
ENV PATH="/venv/bin:$PATH"
CMD ["uvicorn", "app.main:app","--host", "0.0.0.0", "--reload"]

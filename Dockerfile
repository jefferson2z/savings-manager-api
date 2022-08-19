FROM python:3.10-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt

COPY . .

ENV DATABASE_URI=sqlite:///./testing_database.db

CMD ["uvicorn", "app.main:app","--host", "0.0.0.0", "--reload"]

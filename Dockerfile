FROM python:3.12-slim

RUN apt update && apt install -y build-essential libpq-dev

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

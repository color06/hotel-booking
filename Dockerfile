FROM python:3.12-slim


RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "poetry>=1.8"

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN poetry config virtualenvs.create false \
 && poetry install --no-root --only main --no-interaction --no-ansi


COPY . .


RUN poetry add --group prod "gunicorn>=21.2,<22" || true

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "4", \
     "--timeout", "120"]

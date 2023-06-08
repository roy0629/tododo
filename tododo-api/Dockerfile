FROM amd64/python:3.11.1-slim

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    apt-get clean

ENV TZ JST-9

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org/ | python -

COPY ./pyproject.toml /tododo-api/pyproject.toml
COPY ./app /tododo-api/app
WORKDIR /tododo-api
RUN poetry install --no-root --only main

WORKDIR /tododo-api/app

RUN useradd -M myuser
USER myuser

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]

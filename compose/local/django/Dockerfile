FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # curl to be able to install poetry
  && apt-get install -y curl \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN mkdir /etc/bash_completion.d
RUN /root/.poetry/bin/poetry completions bash > /etc/bash_completion.d/poetry.bash-completion

# Project Initialization
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN /root/.poetry/bin/poetry config virtualenvs.create false \
    && /root/.poetry/bin/poetry install --no-interaction --no-ansi --no-root

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/local/django/bashrc /root/.bashrc

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

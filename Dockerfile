FROM python:3.12.2-slim-bookworm

ARG UID=1000
ARG GID=1000
ARG DEBUG="false"
ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

WORKDIR /app

# install updates
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && apt-get install curl \
  && apt-get install gettext -y \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean
# install nodejs and npm
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - &&\
    apt-get install -y nodejs

RUN groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python \
  && mkdir -p /app/node_modules \
  && chown python:python -R /app \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

USER python

COPY --chown=python:python requirements*.txt ./
COPY --chown=python:python bin/ ./bin

RUN chmod 0755 bin/*

## Install python dependencies
RUN pip3 install --no-warn-script-location --no-cache-dir --user -r requirements.txt

COPY --chown=python:python . .

WORKDIR /app/src

ENTRYPOINT ["/app/bin/docker-entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "-c", "python:config.gunicorn", "config.wsgi"]
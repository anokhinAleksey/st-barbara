# St.Barbara Orthodox Cathedral website app

## Tech stack
### Back-end

- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://github.com/celery/celery)

### Front-end

- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)

### Packages and extensions**:

- *[gunicorn](https://gunicorn.org/)* for an app server in both development and production
- *[whitenoise](https://github.com/evansd/whitenoise)* for serving static files
- *[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)* for displaying info about a request

## Django apps

- `common` app to render a home, news and other "article"-like page
- `users` app for user-related actions
- `orthocalendar` app calculates core data about the liturgical year

## Running this app

You'll need to have [Docker installed](https://docs.docker.com/get-docker/).

#### Copy an example .env file because the real one is git ignored:

```sh
cp .env.example .env
```

#### Build everything:

```sh
docker compose -p st-barbara up -d --build
```

Now that everything is built and running we can treat it like any other Django app.

#### Setup the initial database:

```sh
docker exec -it st-barbara-web-1 bash
python3 manage.py migrate
```

#### Check it out in a browser:

Visit <http://localhost:8000> in your favorite browser.


#### Stopping everything:

```sh
# Stop the containers.
docker compose -p st-barbara stop
```

You can start things up again with `docker compose up` it should only take seconds.

#### Runiing conteiners:

```sh
docker compose -p st-barbara up -d
```

## Plans for future
- Add [allauth](https://docs.allauth.org/en/latest/index.html) app for user auth with email/social media
- Add processing of domain events with celery. Such as: send emails to subscribers on news posting
- Add telegram bot app for posting data to telegram channel (news, anounsments etc)
- Move menu to db to enable data-driven checks for displaing menu items based on current user group
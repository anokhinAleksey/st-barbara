#!/usr/bin/env bash

set -e

# Remove machine generates files
rm -rf ../static/*.* ../static/admin ../static/js ../static/css ../static/images ../static/fonts
# restore git files
touch ../static/.keep
#collect static files
python3 manage.py collectstatic --no-input

exec "$@"

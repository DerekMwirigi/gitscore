#!/bin/sh

# wait for PSQL server to start
sleep 10

su -m root -c "set -o errexit"
su -m root -c "set -o pipefail"
su -m root -c "set -o nounset"
su -m root -c "set -o xtrace"

su -m root -c "python manage.py makemigrations"
su -m root -c "python manage.py migrate"
su -m root -c "python manage.py init_superuser"
su -m root -c "python manage.py init_socialaccount_github_app"
su -m root -c "python manage.py collectstatic --noinput"
su -m root -c "python manage.py runserver 0.0.0.0:8000"
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate

if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
	python manage.py shell -c "import os; from django.contrib.auth import get_user_model; User=get_user_model(); username=os.environ['DJANGO_SUPERUSER_USERNAME']; password=os.environ['DJANGO_SUPERUSER_PASSWORD']; email=os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@kdrprint.com'); User.objects.filter(username=username).exists() or User.objects.create_superuser(username, email, password)"
fi

#!/bin/bash
set -e

if [ "$1" = 'back' ]; then
	# Apply database migrations
	echo "Apply database migrations"
	python manage.py migrate

	echo "from django.contrib.auth.models import User; users=User.objects; users.filter(username='admin').exists() or users.create_superuser('admin','admin@dev.com','abcd1234$')" | python manage.py shell

	# populate fixtures folder if exits
	if [ -d "fixtures" ]; then
	    python manage.py loaddata fixtures/* || : # silence errors
	fi

	# Start server
	echo "Starting server"
	python manage.py runserver 0.0.0.0:8000
fi

exec "$@"



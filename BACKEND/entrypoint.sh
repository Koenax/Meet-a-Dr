#!/bin/sh

if [ "$DATABASE" = "postgres" ];
then
  echo "Check if the database is running"

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done
  echo "PostgreSQL is up and running."
fi

python manage.py migrate

exec "$@"
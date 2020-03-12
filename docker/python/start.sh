#!/bin/sh

. venv/bin/activate

flask db init
flask db migrate
flask db upgrade

gunicorn -b 0.0.0.0:8080 flaskr:app --access-logfile - --error-logfile -

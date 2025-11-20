#!/bin/bash
echo "Running Django collectstatic..."
source /var/app/venv/*/bin/activate
python3 /var/app/current/manage.py collectstatic --noinput

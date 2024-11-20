#!/usr/bin/env bash

set -e  # Exit immediately if a command exits with a non-zero status

echo "Installing dependencies..."
pip install -r requirements.txt


echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Applying migrations..."
python manage.py migrate


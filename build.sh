#!/usr/bin/env bash
# exit on error
set -o errexit
/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
#pip install -r requirements.txt
pip install poetry==1.5.1

poetry install

python manage.py collectstatic --no-input
python manage.py migrate
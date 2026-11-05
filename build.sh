#!/usr/bin/env bash
# Render build step: install deps, collect static files, migrate, load demo data.
set -o errexit
pip install -r requirements.txt
cd my_tennis_club
python manage.py collectstatic --no-input
python manage.py migrate --no-input
# Free tier uses an ephemeral SQLite file, so seed demo members on every deploy (ignore if already present).
python manage.py loaddata sample_members || true

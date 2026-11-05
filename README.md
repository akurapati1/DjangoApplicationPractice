# DjangoApplicationPractice — My Tennis Club

A small **Django 5** application for managing a tennis club's members: list, search and view member details, with a customised admin. Built while working through core Django concepts — models & migrations, ORM, class-free views, template inheritance, URL routing, admin and testing.

## Features
- Home page with live member count
- Member directory with **search by name**
- Member detail page (404 for unknown ids)
- Django admin with list display, search and filters
- Template inheritance (`master.html`) and reverse URL resolution (`{% url %}`)
- Settings driven by environment variables; unit tests; sample fixture data

## Project layout
```
my_tennis_club/
  manage.py
  my_tennis_club/     project settings and root URLs
  members/            app: models, views, urls, admin, templates, migrations, fixtures, tests
```

## Getting started
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd my_tennis_club
python manage.py migrate
python manage.py loaddata sample_members      # optional demo data
python manage.py createsuperuser              # to use /admin/
python manage.py runserver
```
Open <http://127.0.0.1:8000/> (admin at `/admin/`).

## Tests
```bash
python manage.py test
```

## Configuration
| Variable | Default | Notes |
|---|---|---|
| `DJANGO_SECRET_KEY` | insecure dev key | **Set in production** |
| `DJANGO_DEBUG` | `true` | Set to `false` in production |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated |

## Data model
`Member(firstname, lastname, phone, joined_date)` — ordered by last then first name. Migration `0004` renames the original `members` model to `Member` and stores phone numbers as text (preserves existing rows).

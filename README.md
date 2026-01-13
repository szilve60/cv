# CV Webpage (Django)

This repository contains a Django-based CV website (app `resume`).

Quick start (local):

1. Create and activate virtualenv (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run migrations and start server:

```powershell
python manage.py migrate
python manage.py runserver
```

4. Admin: http://127.0.0.1:8000/admin/

Deploying to Railway:
- Create a GitHub repo from this project and push.
- On Railway, create a new project, choose GitHub and select the repo, set `DJANGO_SETTINGS_MODULE` if needed, and add environment variables like `SECRET_KEY` and `DEBUG=False`.

Notes:
- Database: default is SQLite (`db.sqlite3`). For production use, configure PostgreSQL on Railway and update `DATABASES` in `cvsite/settings.py`.

echo "Running database migrations..."
#!/usr/bin/env sh
# Entrypoint for Railway (ensure this file is executable on Unix hosts)
set -e
echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn cvsite.wsgi --bind 0.0.0.0:${PORT:-8000}

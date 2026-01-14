
import os
from pathlib import Path

try:
    import dj_database_url
except Exception:
    dj_database_url = None

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'replace-this-with-a-secure-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# ALLOWED_HOSTS: read from env or Railway fallback
raw_hosts = os.environ.get('DJANGO_ALLOWED_HOSTS', '')
if raw_hosts:
    ALLOWED_HOSTS = [h.strip() for h in raw_hosts.split(',') if h.strip()]
else:
    ALLOWED_HOSTS = []
    rail = (
        os.environ.get('RAILWAY_PUBLIC_DOMAIN')
        or os.environ.get('RAILWAY_PUBLIC_URL')
        or os.environ.get('RAILWAY_SERVICE_URL')
    )
    if rail:
        if '://' in rail:
            rail = rail.split('://', 1)[1]
        rail = rail.split('/', 1)[0]
        ALLOWED_HOSTS.append(rail)

# Force a default Railway host first (can be overridden via RAILWAY_FORCE_HOST env)
RAILWAY_FORCE_HOST = os.environ.get('RAILWAY_FORCE_HOST', 'web-production-6fc203.up.railway.app')
if RAILWAY_FORCE_HOST:
    if RAILWAY_FORCE_HOST in ALLOWED_HOSTS:
        ALLOWED_HOSTS.remove(RAILWAY_FORCE_HOST)
    ALLOWED_HOSTS.insert(0, RAILWAY_FORCE_HOST)

ALLOWED_HOSTS = [str(h) for h in ALLOWED_HOSTS]

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'resume',
]

# Middleware (WhiteNoise after SecurityMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cvsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'resume.context_processors.cv_lang',
            ],
        },
    },
]

WSGI_APPLICATION = 'cvsite.wsgi.application'

# Database: prefer DATABASE_URL (Postgres) when available
if os.environ.get('DATABASE_URL') and dj_database_url:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files / WhiteNoise
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# CSRF trusted origins for HTTPS (useful in Django 6+)
CSRF_TRUSTED_ORIGINS = []
for h in ALLOWED_HOSTS:
    if h and not h.startswith('127.') and not h.startswith('localhost') and ':' not in h:
        CSRF_TRUSTED_ORIGINS.append(f"https://{h}")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

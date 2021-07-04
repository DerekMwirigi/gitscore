from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# App Settings
APP_SETTINGS = {
    'BASE_URL': '',
    'PASSWORD_RESET_REQUEST_LIFETIME': timedelta(days=1)
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING["loggers"]["django.db.backends"] = {
            'level': 'DEBUG',
            'handlers': ['console'],
        }

# Rollbar
ROLLBAR = {
    'access_token': config('ROLLBAR_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
}
import rollbar
rollbar.init(**ROLLBAR)

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

OPTIONAL_APPS = [
    'django_extensions',
]

INSTALLED_APPS = PREQ_APPS + PROJECT_APPS + OPTIONAL_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

#Allow CORS requests from all domains (just for the scope of development):
CORS_ORIGIN_ALLOW_ALL = True

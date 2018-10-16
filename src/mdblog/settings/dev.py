from .base import *

INSTALLED_APPS += [
    'django.contrib.admin',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'mdblog.urls.dev'

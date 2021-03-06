"""
Django settings for mdblog project.

Generated by 'django-admin startproject' using Django 1.11.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
CONF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(CONF_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@tjg=-3tj_!9f())9*4h66)skz8mvibycs-!wrl(z9n#w7e@be'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'corsheaders',
    'oauth2_provider',
    # local app
    'blog',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mdblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(CONF_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mdblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# CORS Settings


#
PUBLIC_KEY = '''
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAp6Jugg2ywPquiUl7g30m
gOC2ZmqwHna8DLJgZ3acov8sjbbcT0PvsTPIb5v2KpNeMJ3H7kB7rycI2b93coUL
z6Jdwa7iJ0vC1x4ykF5AyYQwPnsersj1GeK5ZYB6YQewYqcOLhEIGCVT4A578IIw
UWUE6EpRxa15KmAXh4qdNwW3ygF77gMzLcyuudeLYTBBmgZ9Ug4/+e7NgN6MEm/P
KShu7/shJl/aEQhnN8rNqQ919ISFecH/MIp1gnRbkmmBWs8xpJxIwxZFzxKGMBRO
eWAL/5M0bTdaxDovQxcslQMipsmkm1u6f2G1Ahkj2abiR41+UEv+GUHYB2bwjJKP
pERTyULE1//q/HzzHfLeElctuYjSdkYSsTEOhiBQNaM0z6C3oKcNhBgQyYld3gO5
0RMPE64Gt0+Tr87JB5Qx2/oZFZsJ1Vb+SLeoJNsHIWx9oPXNJjm7nsKqGeTfk2rO
Fm2b5Px2QpZEqnWUBlVcKypVWh3t8SNkN4Tx6BGa6DGnG9lOdzdBKl3ucXUbp4TW
9+xAD1yDS6CDt/2067r+Y3fyRcb9TVf1ibm6ZS1meIQ7A1CjYKObLS8VCE6S/unY
RrwOS99ey/dyK4WYcrP3a32W0YpLJ5PaKey9MVBW/dgwbrfzDXf6RAuGC7Lr+P49
fnQwX/mVpUGQx/cycOWTmu0CAwEAAQ==
-----END PUBLIC KEY-----
'''


PRIVATE_KEY = '''
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
'''
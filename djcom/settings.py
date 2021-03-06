"""
Django settings for djcom project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join

#os.path.abspath(os.path.dirname(__file__).decode('utf-8'))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = [
    TEMPLATE_PATH,
]

#STATIC_PATH = os.path.join(BASE_DIR, 'static')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g33$wgm4d%pv*#qejak3dfb41a+d^7q^s3m%&g9es)*pukhxyg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',
    'utils',
    #'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'djcom.urls'

WSGI_APPLICATION = 'djcom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djcom',
        'USER': 'djcom',
        'PASSWORD': 'q1w2e3',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = ''
#MEDIA_URL = '/static/'

STATIC_URL = '/static/'
#STATICFILES_DIR = (
#    STATIC_PATH,
#)

#STATIC_ROOT = ''
#PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, u'static'),
)

SITE_NAME = 'Zaponki Kiev Ua'
META_KEYWORDS = 'Zaponki v Kieve'
META_DESCRIPTION = 'Kupit zaponki v Kieve'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    # 'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'utils.context_processor.djcom',
)
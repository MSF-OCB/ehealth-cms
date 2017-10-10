from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-z8j$zowgfj=9-%ei&jr*a*y8di8ixh8x$q7etc0)6cm21#2#n'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.postgresql',
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'wagtail', # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'wagtail',
            'PASSWORD': 'wagtail',
            'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '5432',
        }
    }

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')

try:
    from .local import *
except ImportError:
    pass


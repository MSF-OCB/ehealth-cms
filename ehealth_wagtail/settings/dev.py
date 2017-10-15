from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# TODO env
SECRET_KEY = '-z8j$zowgfj=9-%ei&,jr*a*y8di8ixh8x$q7etc0)6cm21#2#n'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# TODO too generic!!!
ALLOWED_HOSTS = ['*']

# TODO env variables!
GOOGLE_MAPS_V3_APIKEY = 'AIzaSyAzTKuGAzcoIwJ31pCktzJ2I8hcqwHOPJs'
GEO_WIDGET_DEFAULT_LOCATION = {'lat': 50.833349, 'lng': 4.364177}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = { 'default': dj_database_url.config(conn_max_age=500) }
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')

try:
    from .local import *
except ImportError:
    pass


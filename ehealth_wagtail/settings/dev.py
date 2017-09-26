from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-z8j$zowgfj=9-%ei&jr*a*y8di8ixh8x$q7etc0)6cm21#2#n'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

GOOGLE_MAPS_V3_APIKEY = 'AIzaSyAzTKuGAzcoIwJ31pCktzJ2I8hcqwHOPJs'
GEO_WIDGET_DEFAULT_LOCATION = {'lat': 50.833349, 'lng': 4.364177}

try:
    from .local import *
except ImportError:
    pass

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


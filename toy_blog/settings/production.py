import os
from .base import *
DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_db',                      # Or path to database file if using sqlite3.
        'USER': 'django_login',                      # Not used with sqlite3.
        'PASSWORD': os.environ["DATABASE_PASSWORD"],       # Not used with sqlite3.
        'HOST': 'LOCALHOST',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# UpdateCacheMiddleware *must* be the first middleware, and FetchFromCacheMiddleware
# *must* be the last
MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',)
                     + MIDDLEWARE_CLASSES
                     + ('django.middleware.cache.FetchFromCacheMiddleware',)

CACHE_MIDDLEWARE_ALIAS = 'memcached_middleware_alias'
CACHE_MIDDLEWARE_SECONDS = 10
CACHE_MIDDLEWARE_KEY_PREFIX = 'toy_blog'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['parlarjb.xen.prgmr.com']

STATIC_ROOT = '/usr/share/nginx/www/static/'

from .base import *
import django_heroku
DEBUG = False

ALLOWED_HOSTS = ['mysite.com', ]

# Activate Django-Heroku.
django_heroku.settings(locals())

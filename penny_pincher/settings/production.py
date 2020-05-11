import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['penny-pincher-ph.herokuapp.com']

# Activate Django-Heroku.
django_heroku.settings(locals())

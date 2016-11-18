# settings/local.py

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = "Localhost"
EMAIL_PORT = 3306

DATABASES = {
    "Default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "test",
        "USER": "root",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "",
    }
}

INSTALLED_APPS = ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES = ("debug_toolbar.middleware.DebugToolbarMiddleware", )
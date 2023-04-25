from .base import *
import os 



DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'glizzy',
        'PASSWORD': 'onefullsend'
    }
}
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '192.168.1.*'
]
ADMINS = [
    ("Dylan Garrett", "dreadnexus@protonmail.ch")
]
TIME_ZONE = os.environ.get("SERVER_TIME_ZONE")
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

from .base import *
import os 
import secrets



DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432
    }
}
ALLOWED_HOSTS = ["*"]
ADMINS = [
    ("Dylan Garrett", "dreadnexus@protonmail.ch")
]
#TIME_ZONE = os.environ.get("SERVER_TIME_ZONE")
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#SECRET_KEY = secrets.token_urlsafe()

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
#CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

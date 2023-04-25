from .base import *
import os 
import secrets



DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DATABASE_NAME"),
        'USER': os.environ.get("DATABASE_USER"),
        'PASSWORD': os.environ.get("DATABASE_PASSWORD")
    }
}
ALLOWED_HOSTS = ["*"]
ADMINS = [
    ("Dylan Garrett", "dreadnexus@protonmail.ch")
]
TIME_ZONE = os.environ.get("SERVER_TIME_ZONE")
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SECRET_KEY = secrets.token_urlsafe()

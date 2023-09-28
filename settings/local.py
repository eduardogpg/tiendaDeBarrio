import os
from .base import *
import pymysql
from dotenv import load_dotenv


load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

pymysql.version_info = (1, 4, 6, 'final', 0)

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NAME_DATABASE'),
        'USER': os.getenv('USER_DATABASE'),
        'PASSWORD': os.getenv('PASSWORD_DATABASE'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
from .base import *  # NOQA
# Debug
DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library',
        'USER': 'root',
        'PASSWORD': 'hjh1999823',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}





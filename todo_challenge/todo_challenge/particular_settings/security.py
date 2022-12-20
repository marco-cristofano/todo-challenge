import os
from cbs import BaseSettings


class SecuritySettings(BaseSettings):
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

    DEBUG = os.environ.get('DJANGO_MODE_DEBUG', 0)

    ALLOWED_HOSTS = ['*']

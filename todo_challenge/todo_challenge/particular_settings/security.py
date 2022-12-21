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

    DEBUG = bool(int(os.environ.get('DJANGO_MODE_DEBUG', 0)))

    SECRET_KEY = bool(os.environ['DJANGO_SECRET_KEY'])

    ALLOWED_HOSTS = ['*']

    CORS_ORIGIN_ALLOW_ALL = True

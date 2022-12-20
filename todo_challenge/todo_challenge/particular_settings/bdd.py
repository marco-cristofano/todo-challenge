import os
from cbs import BaseSettings


class BDDSettings(BaseSettings):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('POSTGRES_NAME', 'root'),
            'USER': os.environ.get('POSTGRES_USER', 'root'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'root'),
            'HOST': os.environ.get('POSTGRES_HOST', 'db'),
            'PORT': os.environ.get('POSTGRES_PORT', '5432')
        }
    }
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

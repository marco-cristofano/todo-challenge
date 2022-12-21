import os
from cbs import BaseSettings


class LoggingSettings(BaseSettings):

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(asctime)s %(name)s.%(funcName)s:%(lineno)s- %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
                'propagate': True,
            },
        }
    }

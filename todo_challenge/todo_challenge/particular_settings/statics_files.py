import os
from pathlib import Path
from cbs import BaseSettings

BASE_DIR = Path(__file__).parent.parent.parent


class StaticFilesSettings(BaseSettings):
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

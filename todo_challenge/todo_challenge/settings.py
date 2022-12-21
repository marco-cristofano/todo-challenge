from pathlib import Path

from todo_challenge.particular_settings.bdd import BDDSettings
from todo_challenge.particular_settings.rest import RestSettings
from todo_challenge.particular_settings.time_internalization import (
    TimeAndInternalizationSettings
)
from todo_challenge.particular_settings.security import SecuritySettings
from todo_challenge.particular_settings.statics_files import (
    StaticFilesSettings
)
from todo_challenge.particular_settings.templates import TemplatesSettings


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(
        BDDSettings,
        RestSettings,
        TimeAndInternalizationSettings,
        SecuritySettings,
        StaticFilesSettings,
        TemplatesSettings):

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'to_do.apps.ToDoConfig',
        'user.apps.UserConfig',
        'django_filters',
        'oauth2_provider',
        'corsheaders',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'corsheaders.middleware.CorsMiddleware',
    ]

    ROOT_URLCONF = 'todo_challenge.urls'

    WSGI_APPLICATION = 'todo_challenge.wsgi.application'



__getattr__, __dir__ = Settings.use()

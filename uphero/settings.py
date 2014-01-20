"""
Django settings for uphero project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j@5rjeqoj7q3=xbb0ba_w2kso9z^et9eal*3jz+bz^^3kxbe!v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'tinymce',
    'ckeditor',
    'ktv',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'uphero.urls'

WSGI_APPLICATION = 'uphero.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = '/home/zhou3594/workbench/uphero/static'
STATIC_URL = '/static/'

TINYMCE_DEFAULT_CONFIG = {
    'plugins':  "table, spellchecker, paste, searchreplace", 
    'theme':  "advanced", 
    'cleanup_on_startup':  True, 
    'custom_undo_redo_levels':  10, 
}
CKEDITOR_UPLOAD_PATH = "/home/zhou3594/workbench/media/uploads/"
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Full',
#         'language': 'en',
#         'height': 300,
#         'width': 800,
#     },
# }
CKEDITOR_CONFIGS = {
    'default': {
        'extraPlugins': 'youtube',
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink', 'Anchor',
              '-', 'Format',
              '-', 'SpellChecker', 'Scayt',
              '-', 'Maximize',
            ],
            [      'HorizontalRule',
              '-', 'Table',
              '-', 'BulletedList', 'NumberedList',
              '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
              '-', 'SpecialChar',
              '-', 'Source', 'youtube',
              '-', 'About',
            ]
        ],
        'width': 840,
        'height': 300,
        'toolbarCanCollapse': False,
    }
}

"""Settings that need to be set in order to run the tests."""
import os


DEBUG = True
FILER_DEBUG = True

SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

USE_I18N = True

# Settings needed to test a multilingual blog
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('de', 'Deutsch'),
]
ROOT_URLCONF = 'multilingual_events.tests.test_app.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../../static/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../../media/')

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'test_static'),
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': [os.path.join(os.path.dirname(__file__), '../templates')],
    'OPTIONS': {
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.i18n',
            'django.core.context_processors.request',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
        )
    }
}]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_nose',
    'cms',
    'sekizai',
    'menus',
    'filer',
    'easy_thumbnails',
    'mptt',
    'document_library',
    'hvad',
    'treebeard',
]

INTERNAL_APPS = [
    'multilingual_events.tests.test_app',
    'multilingual_events',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

SECRET_KEY = 'foobar'

CMS_SOFTROOT = True
CMS_PERMISSION = False
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_FRONTEND_LANGUAGES = ('en', 'de', )
CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
)

# versions might be a bit old, but for tests it will probably do
JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'  # NOQA
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'  # NOQA

SECRET_KEY = 'foobar'

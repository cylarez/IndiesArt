# Django settings for indiesart project.

import os.path
import sys

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

try:
    from settings_local import *
except ImportError:
    import sys
    sys.stderr.write('Unable to read settings_local.py\n')


TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Montreal'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = settings_local.MAIN_DIR + 'assets/'
MEDIA_ROOT = MAIN_DIR +'assets/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://files.indiesart.com/assets/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qv8-aux43t+_@6ij!@dox$pgthr*=ax70mc2di4p(7p&mru=6r'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'indiesart.urls'

TEMPLATE_DIRS = (
    MAIN_DIR +'templates/'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'main',
    'blog',
    'account',
    'mobile',
)

FACEBOOK_API_KEY = ''
FACEBOOK_SECRET_KEY = ''
FACEBOOK_INFINITE_KEY = ''

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'indiesart.contact@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = '838dg34_$'
EMAIL_PORT = 587
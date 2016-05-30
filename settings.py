# -*- coding: utf-8 -*-

import os.path
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'sqlite3.db', # Or path to database file if using sqlite3.
#         # The following settings are not used with sqlite3:
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#         'PORT': '', # Set to empty string for default.
#     }
# }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

# This is required if you want multilingual site or newsletter
gettext = lambda s: s
LANGUAGES = (
    ('fr', gettext(u'Français')),
    ('en', gettext(u'English')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.abspath(PROJECT_PATH+'/public/media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.abspath(PROJECT_PATH+'/public/static/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.abspath(PROJECT_PATH+'/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'coop_cms.utils.RequestMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(PROJECT_PATH + '/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    'django.core.context_processors.request',
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "balafon.Search.context_processors.quick_search_form",
    "balafon.Crm.context_processors.crm",
)

AUTHENTICATION_BACKENDS = (
    'coop_cms.perms_backends.ArticlePermissionBackend',
    'coop_cms.apps.email_auth.auth_backends.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',  # Django's default auth backend
)

# Serve provate pfiles
SERVE_FILE_BACKEND = 'filetransfers.backends.url.serve_file'


# CMS Settings

# Custom article class
COOP_CMS_ARTICLE_CLASS = 'basic_cms.models.Article'

# Custom modules loaded for populating the coop bar (editor menu)
COOP_BAR_MODULES = ('coop_cms.coop_bar_cfg', 'balafon.Emailing.coop_bar_cfg',)

# The models to propose as links
DJALOHA_LINK_MODELS = ('basic_cms.Article',)

# default logo size
COOP_CMS_ARTICLE_LOGO_SIZE = "128x128"

# Newsletter templates
COOP_CMS_NEWSLETTER_TEMPLATES = (
    ('coop_cms/newsletter.html', 'Basic'),
)

# Article templates
COOP_CMS_ARTICLE_TEMPLATES = (
    ('coop_cms/article.html', 'Basic'),
)

# Email used for sending an email
COOP_CMS_FROM_EMAIL = u'"Your Name" <your.name@your.domain.com>'

# Send an email to these addresses when testing a newsletter
COOP_CMS_TEST_EMAILS = (
    '"Your Name" <your.name@your.domain.com>',
)

# A prefix
COOP_CMS_SITE_PREFIX = 'http://your.domain.com'

# Reply to header when sending a newsletter
COOP_CMS_REPLY_TO = 'your.name@your.domain.com'


# CRM Settings

# Definition of the search forms than can be used
SEARCH_FORM_LIST = 'balafon.config.SEARCH_FORMS'

# Default country
BALAFON_DEFAULT_COUNTRY = 'France'

# The name of your company, assoociation ...
BALAFON_MY_COMPANY = u"My Company"

# True if Balafon is used standalone, False if you want to use it alongside a web site
BALAFON_AS_HOMEPAGE = True

# An email address to send you notifications
BALAFON_NOTIFICATION_EMAIL = 'your.name@your.domain.com'

# True if you can create "single contacts", contacts which are not linked to an entity
BALAFON_ALLOW_SINGLE_CONTACT = True

# If you don't allow single contact, the id of the entity type corresponding to individuals
#BALAFON_INDIVIDUAL_ENTITY_ID = 3

# True if you want to hide the entity type
BALAFON_NO_ENTITY_TYPE = False

# If your newsletter is developped with an external tool. Urls to download it
BALAFON_NEWSLETTER_SOURCES = (
)

# Add a search for group zones
#BALAFON_ZONE_GROUP_SEARCH = True

# If True show extra fields for billing address
BALAFON_SHOW_BILLING_ADDRESS = False

# PDF templates than can be proposed to export serach results to pdf file
# Make possible for example to print labels with addresses for a mailing
BALAFON_PDF_TEMPLATES = (
    ('pdf/labels_24.html', gettext(u'etiquettes 24')),
    ('pdf/labels_21.html', gettext(u'etiquettes 21')),
    ('pdf/labels_16.html', gettext(u'etiquettes 16')),
)

# Tune the pdf generation
BALAFON_PDF_OPTIONS = {
    'pdf/labels_24.html': {
        'margin-top': 0, 'margin-bottom': 0, 'margin-right': 0, 'margin-left': 0,
    },
    'pdf/labels_21.html': {
        'margin-top': 0, 'margin-bottom': 0, 'margin-right': 0, 'margin-left': 0,
    },
    'pdf/labels_16.html': {
        'margin-top': 0, 'margin-bottom': 0, 'margin-right': 0, 'margin-left': 0,
    },
    'pdf/address_strip.html': {
        'margin-top': 0, 'margin-bottom': 0, 'margin-right': 0, 'margin-left': 0,
    },
}

# Add extra fields to the pdf form
BALAFON_PDF_FORM_EXTRA_FIELDS = (
    # ('start_at', 'Etiquettes blanches', '0'),
)

# def start_at_label_context_patch(template, context):
#     contacts = context['contacts']
#     try:
#         start_at = int(context['start_at'])
#     except ValueError:
#         start_at = 0
#     context['contacts'] = [None]*start_at + list(contacts)
#     return context

# Functions than can be called before the generation of a pdf file
BALAFON_PDF_FORM_CONTEXT_HOOKS = {
    # 'pdf/labels_24.html': start_at_label_context_patch,
    # 'pdf/labels_21.html': start_at_label_context_patch,
    # 'pdf/labels_16.html': start_at_label_context_patch,
}

# True if you want to give a default subscription
# for example for subscribing to the newsletter with just an email addresss
#BALAFON_SUBSCRIPTION_DEFAULT_VALUE = True

# if BALAFON_SUBSCRIPTION_DEFAULT_VALUE is set, the id of the default subscription
#BALAFON_DEFAULT_SUBSCRIPTION_TYPE = 2

# True : Unnaccent postgresql addon is installed on the db
BALAFON_UNACCENT_FILTER_SUPPORT = True

# Tools to have common names for cities
BALAFON_CITY_FORMATTERS = (
   # ('replace', u' ', u'-'),
   # ('capitalize_words', u'-'),
   # ('replace', u'St-', u'Saint-'),
   # ('replace', u'Ste-', u'Sainte-'),
)

# Allow 'Mrs and Mr' gender : have one contact for a couple
BALAFON_ALLOW_COUPLE_GENDER = True

# List of email addresses that can be used for sending an emailing
BALAFON_EMAILING_SENDER_CHOICES = (
    ('your.name@your.domain.com ','your.name@your.domain.com'),
)

LOGIN_REDIRECT_URL = "/"

INSTALLED_APPS = (
    #contribs
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # Balafon
    'balafon',
    'balafon.Crm',
    'balafon.Search',
    'balafon.Emailing',
    #'balafon.Profile',
    'balafon.Users',

    #externals
    'djaloha',
    'colorbox',
    'coop_cms.apps.email_auth',
    'coop_cms',
    'coop_bar',
    'wkhtmltopdf',
    'captcha',
    'rest_framework',

    'basic_cms',

    #3rd parties
    'django_extensions',
    'floppyforms',
    'sorl.thumbnail',

    'django.contrib.admin',
    'django.contrib.admindocs',


    'eleve',
    
)

if not 'makemigrations' in sys.argv:
    INSTALLED_APPS = ('modeltranslation', ) + INSTALLED_APPS


if len(sys.argv) > 1 and 'test' == sys.argv[1]:
    INSTALLED_APPS += ('coop_cms.apps.test_app',)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'balafon_crm': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'coop_cms': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'colorbox': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
        },        
    }
}


import warnings
warnings.filterwarnings('ignore', r"django.contrib.localflavor is deprecated")
warnings.filterwarnings('ignore', "django.conf.urls.defaults is deprecated; use django.conf.urls instead")


# Create a local_settings_prod.py for your production settings : Put it under source control
# The local_settings.py should not be under source control and may vary between development machines

try:
    from local_settings import *
except ImportError:
    from local_settings_prod import *



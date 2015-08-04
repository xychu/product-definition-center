#
# Copyright (c) 2015 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#
"""
Django settings for pdc project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3hm)=^*sowhxr%m)%_u3mk+!ncy=c)147xbevej%l_lcdogu#+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

ITEMS_PER_PAGE = 50

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'pdc.apps.auth',
    'pdc.apps.common',
    'pdc.apps.compose',
    'pdc.apps.package',
    'pdc.apps.release',
    'pdc.apps.repository',
    'pdc.apps.contact',
    'pdc.apps.component',
    'pdc.apps.changeset',
    'pdc.apps.utils',
    'pdc.apps.bindings',
    'pdc.apps.usage',

    'mptt',
)

AUTH_USER_MODEL = 'kerb_auth.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'pdc.apps.auth.authentication.TokenAuthenticationWithChangeSet',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ],

    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'pdc.apps.common.renderers.ReadOnlyBrowsableAPIRenderer',
    ),

    'EXCEPTION_HANDLER': 'pdc.apps.common.handlers.exception_handler',

    'DEFAULT_PAGINATION_CLASS': 'pdc.apps.common.pagination.AutoDetectedPageNumberPagination',
}

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'pdc.apps.auth.middleware.KerberosUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'kobo.django.menu.middleware.MenuMiddleware',
    'pdc.apps.usage.middleware.UsageMiddleware',
    'pdc.apps.changeset.middleware.ChangesetMiddleware',
    'pdc.apps.utils.middleware.MessagingMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'pdc.apps.auth.backends.KerberosUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# LOGIN_URL = '/auth/krb5login'
# LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'pdc.urls'

import kobo
ROOT_MENUCONF = "pdc.menu"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "pdc/templates"),
            os.path.join(os.path.dirname(kobo.__file__), "hub", "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'kobo.django.menu.context_processors.menu_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'pdc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = '/usr/share/pdc/static'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "pdc/static"),
    "/usr/share/patternfly1/resources",
)


REST_API_URL = 'rest_api/'
REST_API_VERSION = 'v1'
REST_API_PAGE_SIZE = 20
REST_API_PAGE_SIZE_QUERY_PARAM = 'page_size'
REST_API_MAX_PAGE_SIZE = 100

API_HELP_TEMPLATE = "api/help.html"

DIST_GIT_WEB_ROOT_URL = "http://pkgs.example.com/cgit/"
DIST_GIT_RPM_PATH = 'rpms/'
DIST_GIT_REPO_FORMAT = DIST_GIT_WEB_ROOT_URL + DIST_GIT_RPM_PATH + "%s"
DIST_GIT_BRANCH_FORMAT = "?h=%s"

# ldap settings
LDAP_URI = "ldap://ldap.example.com:389"
LDAP_USERS_DN = "ou=users,dc=example,dc=com"
LDAP_GROUPS_DN = "ou=groups,dc=example,dc=com"
LDAP_CACHE_HOURS = 24

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = '^/%s.*$' % REST_API_URL

# mock kerberos login for debugging
DEBUG_USER = None

BROWSABLE_DOCUMENT_MACROS = {
    # need to be rewrite with the real host name when deploy.
    'HOST_NAME': 'http://localhost:8000',
    # make consistent with rest api root.
    'API_PATH': '%s%s' % (REST_API_URL, REST_API_VERSION),
}

EMPTY_PATCH_ERROR_RESPONSE = {
    'detail': 'Partial update with no changes does not make much sense.',
    'hint': ' '.join(['Please make sure the URL includes the trailing slash.',
                      'Some software may automatically redirect you the the',
                      'correct URL but not forward the request body.'])
}

# Messaging Bus Config
MESSAGE_BUS = {
    # MLP: Messaging Library Package
    #      e.g. `fedmsg` for fedmsg or `kombu` for AMQP and other transports that `kombu` supports.
    #           `qpid` for qpid AMQP supports.
    'MLP': '',

    # # `fedmsg` config example:
    # # fedmsg's config is managed by `fedmsg` package, so normally here just need to set the
    # # 'MLP' to 'fedmsg'
    # 'MLP': 'fedmsg',
    #
    # # `kombu` config example:
    # 'MLP': 'kombu',
    # 'URL': 'amqp://guest:guest@example.com:5672//',
    # 'EXCHANGE': {
    #     'name': 'pdc',
    #     'type': 'topic',
    #     'durable': False
    # },
    # 'OPTIONS': {
    #     # Set these two items to config `kombu` to use ssl.
    #     'login_method': 'EXTERNAL',
    #     'ssl': {
    #         'ca_certs': '',
    #         'keyfile': '',
    #         'certfile': '',
    #         'cert_reqs': ssl.CERT_REQUIRED,
    #     }
    # }
    #
    # # `qpid` config items:
    # 'MLP': 'qpid',
    # 'ENDPOINTS': ['amqps://example1.com:5671',
    #               'amqps://example2.com:5671',
    #               'amqps://example3.com:5671',
    #               ],
    # 'QUEUE': 'pdc',
    # 'SOCKET_TIMEOUT': 1,  # seconds, socket open timeout,
    # 'CONN_TIMEOUT': 5,    # seconds, whole connection timeout,
    # 'SEND_TIMEOUT': 1,    # seconds, msg send timeout,
    # 'CERT_FILE': '',
    # 'KEY_FILE': '',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(process)d [%(filename)s -- %(module)s.%(funcName)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    'handlers': {
        'stderr': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stderr
        },
        'stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stdout
        },
        'watchedfile': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'verbose',
            'filename': '/var/log/pdc/server.log',
            'delay': True,
        },
        # Send a warning email if we want it.
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'include_html': True,
        # }
    },
    'loggers': {
        'pdc': {
            'handlers': ['stderr'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['stderr'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

# Attempts to import server specific settings.
# Note that all server specific settings should go to 'settings_local.py'
try:
    from settings_local import *  # noqa
except ImportError:
    pass

if 'pdc.apps.bindings' in INSTALLED_APPS:
    WITH_BINDINGS = True
else:
    WITH_BINDINGS = False

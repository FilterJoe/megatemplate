import os
import uuid

# uuid is a unique identifier for each system. Uncomment the print statement just once when first
# setting up on your system to obtain the UUID unique to your system. Then replace 52238221199
# below with your number to get this settings file working as intended. The purpose? So that
# settings specific to dotcloud (or to your local dev environment) are triggered when appropriate.

on_dotcloud=True
system_id = uuid.getnode()
print system_id
if system_id == 52236371583:
    on_dotcloud=False # note that dotcloud's number for me has been 60355917464507 so far
print "on_dotcloud status: ", on_dotcloud

if on_dotcloud:
    import json
    with open('/home/dotcloud/environment.json') as f:
        env = json.load(f)
    settings_dir = os.path.dirname(__file__)
    PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

DEBUG = not on_dotcloud
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if not on_dotcloud:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'djangostack',
            'HOST': '/opt/bitnami/postgresql',
            'PORT': '5432',
            'USER': 'bitnami',
            'PASSWORD': '143001a0cd'
        }
    }

if on_dotcloud:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'happydb',
            'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
            'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
            'HOST': env['DOTCLOUD_DB_SQL_HOST'],
            'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
        }
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"

MEDIA_ROOT = ''
if on_dotcloud:
    MEDIA_ROOT = '/home/dotcloud/data/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"

MEDIA_URL = ''
if on_dotcloud:
    MEDIA_URL = '/media/' # dotcloud

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

STATIC_ROOT = ''
if on_dotcloud:
    STATIC_ROOT = '/home/dotcloud/volatile/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files

if not on_dotcloud:
    STATICFILES_DIRS = ('/home/bitnami/PycharmProjects/megatemplate/static',
    )
if on_dotcloud:
    STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't0#u-$+bqz5esc3hl!8d*kt&amp;1==x(6ic1hs3ne9th8^u8$h+di'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', # must load after sessions middleware and any encoding of response content
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# reorder (or add/remove) panels if I want with this:
#DEBUG_TOOLBAR_PANELS = (
#    'debug_toolbar.panels.version.VersionDebugPanel',
#    'debug_toolbar.panels.timer.TimerDebugPanel',
#    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#    'debug_toolbar.panels.headers.HeaderDebugPanel',
#    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#    'debug_toolbar.panels.template.TemplateDebugPanel',
#    'debug_toolbar.panels.sql.SQLDebugPanel',
#    'debug_toolbar.panels.signals.SignalDebugPanel',
#    'debug_toolbar.panels.logger.LoggingPanel',
#    )

#def custom_show_toolbar(request):
#    return True # Always show toolbar, for example purposes only.

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    #    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    #    'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
    #    'HIDE_DJANGO_SQL': False,
    #    'TAG': 'div',
    #    'ENABLE_STACKTRACES' : True,
}
INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'megatemplate.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'megatemplate.wsgi.application'


if not on_dotcloud:
    TEMPLATE_DIRS = ('/home/bitnami/PycharmProjects/megatemplate/templates',
        )
if on_dotcloud:
    TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates/'),
        )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'debug_toolbar', # for configuration options: http://pypi.python.org/pypi/django-debug-toolbar
    'south',
    'app1',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

if not on_dotcloud:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

if on_dotcloud: # dotcloud's logging code from tutorial:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
            },
        'handlers': {
            'null': {
                'level':'DEBUG',
                'class':'django.utils.log.NullHandler',
                },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'log_file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'verbose',
                'filename': '/var/log/supervisor/blogapp.log',
                'maxBytes': 1024*1024*25, # 25 MB
                'backupCount': 5,
                },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'log_file', 'mail_admins'],
                'level': 'INFO',
                'propagate': True,
                },
            'django.request': {
                'handlers': ['console', 'log_file', 'mail_admins'],
                'level': 'ERROR',
                'propagate': False,
                },
            'django.db.backends': {
                'handlers': ['console', 'log_file', 'mail_admins'],
                'level': 'INFO',
                'propagate': False,
                },
            # Catch All Logger -- Captures any other logging
            '': {
                'handlers': ['console', 'log_file', 'mail_admins'],
                'level': 'INFO',
                'propagate': True,
                }
        }
    }

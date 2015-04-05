#-*- coding: UTF-8 -*-

"""
Django settings for eda_tools project.

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
SECRET_KEY = '0)rapr7p%wo-f%u#ya0xdmo5mjda=%37n#^a^wvbv@zo4u^n3o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*',]

STATIC_ROOT = 'E:/mycode/django/eda_tools/eda_tools/static/'    #add by weining for static 
STATIC_URL = 'http://127.0.0.1:8000/static/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'gunicorn',         #add by weining for gunicorn
    'kb',                #-- for this app
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
  #  'django.middleware.csrf.CsrfViewMiddleware',                       #by weining 
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eda_tools.urls'

WSGI_APPLICATION = 'eda_tools.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web_db',
        'USER': 'root',
        'PASSWORD': 'certify',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = None     #--

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#STATIC_URL = 'E:/mycode/django/eda_tools/eda_tools/static/'
MEDIA_ROOT = 'E:/mycode/django/app_date/eda_tools_upfile'

TEMPLATE_DIRS = ('E:/mycode/django/eda_tools/eda_tools/Templates',)   #add by weining


# add by weining
LOGGING = {
           'version':1,
           'disable_existing_loggers':False,
           'formatters':{                   #
                         'simple':{
                                   'format':'[%(asctime)s]   functionnamD:[%(funcName)s]  messagD:[%(message)s]'
                                   },
                         },
           'handlers':{
                       'file':{
                               'level':'DEBUG',
                               'class':'logging.FileHandler',
                               'filename':'E:/mycode/django/app_date/eda_tools_log/debug.log',
                               'formatter':'simple'                    
                               },
                       'dbfile':{
                                 'level':'DEBUG',
                                 'class':'logging.FileHandler',
                                 'filename':'E:/mycode/django/app_date/eda_tools_log/db_debug.log',
                                 'formatter':'simple'
                                 },
                       'runfile':{
                                  'level':'DEBUG',
                                  'class':'logging.FileHandler',
                                  'filename':'E:/mycode/django/app_date/eda_tools_log/run.log',
                                  'formatter':'simple'
                                  },
                       'use_log_file':{            #用来记录用户使用行为
                                       'level':'DEBUG',
                                       'class':'logging.FileHandler',
                                       'filename':'E:/mycode/django/app_date/eda_tools_log/use_log.log',
                                       'formatter':'simple'
                                       },
                       'search_file':{               #用来记录用户搜索关键字
                                       'level':'DEBUG',
                                       'class':'logging.FileHandler',
                                       'filename':'E:/mycode/django/app_date/eda_tools_log/search.log',
                                       'formatter':'simple'
                                       },
                       },
           'loggers':{
                      'django.request':{
                                        'handlers':['file'],
                                        'level':'DEBUG',
                                        'propagate':True,
                                        },
                      'django.db.backends':{
                                            'handlers':['dbfile'],
                                            'level':'DEBUG',
                                            'propagate':True,                                            
                                            },
                      'my_log':{
                                'handlers':['runfile',],
                                'level':'DEBUG',
                                'propagate':True,
                                
                                },
                      'use_log':{
                                 'handlers':['use_log_file'],
                                 'level':'DEBUG',
                                 'propagate':True,
                                 },
                      'search_log':{
                                 'handlers':['search_file'],
                                 'level':'DEBUG',
                                 'propagate':True,
                                 },
                      },
           }




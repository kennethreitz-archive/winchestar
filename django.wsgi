import os
import sys

sys.path.append('/var/www/winchestar')

os.environ['PYTHON_EGG_CACHE'] = '/var/www/winchestar/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
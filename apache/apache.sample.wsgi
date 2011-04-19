import os
import sys

sys.path.append('/Users/cylarez/Sites/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'indiesart.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
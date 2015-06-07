from __future__ import unicode_literals

import os
import sys

from django.core.wsgi import get_wsgi_application

path = '/var/www' 
if path not in sys.path: 
    sys.path.insert(0, '/var/www/testsite') 
    sys.path.append('/var/www/testsite/blog/') 

os.environ['PYTHON_EGG_CACHE'] = '/tmp'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_PARENT = PROJECT_ROOT.rsplit("/", 1)[0]
sys.path.extend([PROJECT_ROOT, PROJECT_PARENT])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()

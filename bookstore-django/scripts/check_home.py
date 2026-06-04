import os
import sys
# Ensure project root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
import django
django.setup()
from django.test import Client
c = Client()
# Use a valid Host header to avoid DisallowedHost during tests
resp = c.get('/', HTTP_HOST='localhost:3000')
print('STATUS', resp.status_code)
print('LENGTH', len(resp.content))
print('TEMPLATE', resp.templates[0].name if resp.templates else 'none')

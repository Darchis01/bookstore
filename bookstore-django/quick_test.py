import os
import sys
sys.path.insert(0, r'c:\Users\HP\Documents\csc ass\bookstore-django')
os.chdir(r'c:\Users\HP\Documents\csc ass\bookstore-django')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.config.settings')

import django
django.setup()

from django.test import Client
client = Client()

response = client.get('/signup/')
print(f"Signup: {response.status_code}")
if response.status_code == 200:
    print("Form renders OK" if 'form' in response.content.decode() else "No form found")

response = client.get('/login/')
print(f"Login: {response.status_code}")
if response.status_code == 200:
    print("Form renders OK" if 'form' in response.content.decode() else "No form found")

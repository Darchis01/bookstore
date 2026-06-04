import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.config.settings')
django.setup()

import requests
from django.test import Client

client = Client()

print("=== Testing /signup/ ===")
try:
    response = client.get('/signup/')
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Content: {response.content.decode()[:500]}")
    else:
        print("Signup page loaded successfully")
except Exception as e:
    print(f"Error: {e}")

print("\n=== Testing /login/ ===")
try:
    response = client.get('/login/')
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Content: {response.content.decode()[:500]}")
    else:
        print("Login page loaded successfully")
except Exception as e:
    print(f"Error: {e}")

print("\n=== Testing /books/ ===")
try:
    response = client.get('/books/')
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Content: {response.content.decode()[:500]}")
    else:
        print("Books page loaded successfully")
except Exception as e:
    print(f"Error: {e}")

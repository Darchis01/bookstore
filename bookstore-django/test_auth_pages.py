#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.config.settings')
django.setup()

from django.test import Client

client = Client()

# Test signup page
response = client.get('/signup/')
print(f"Signup page status: {response.status_code}")
if response.status_code == 200:
    content = response.content.decode()
    if 'auth-form' in content and 'auth-panel' in content:
        print("✓ Signup page renders with proper CSS classes")
    if 'SignUpForm' in str(response.context) or 'form' in str(response.context):
        print("✓ Form context available")
else:
    print(f"Error: {response.content.decode()[:500]}")

print()

# Test login page
response = client.get('/login/')
print(f"Login page status: {response.status_code}")
if response.status_code == 200:
    content = response.content.decode()
    if 'auth-form' in content and 'auth-panel' in content:
        print("✓ Login page renders with proper CSS classes")
    if 'LoginForm' in str(response.context) or 'form' in str(response.context):
        print("✓ Form context available")
else:
    print(f"Error: {response.content.decode()[:500]}")

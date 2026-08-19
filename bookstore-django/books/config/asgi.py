import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Add the bookstore-django folder to sys.path so 'books' is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.config.settings')

application = get_wsgi_application()
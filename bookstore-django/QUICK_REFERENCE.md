# Django Bookstore - Quick Commands

## Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Deactivate:**
```bash
deactivate
```

## Installation & Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations (creates database)
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Load sample book data
python manage.py shell < load_books.py
```

## Running the Server

```bash
# Default port (3000)
python manage.py runserver 3000

# Custom port
python manage.py runserver 3001

# Make accessible from other machines
python manage.py runserver 0.0.0.0:3000
```

## Database Management

```bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Access database shell
python manage.py dbshell

# Django shell (Python REPL with Django models)
python manage.py shell
```

## Django Admin & Shortcuts

```bash
# Access admin interface
# Browser: http://localhost:3000/admin/

# Change password
python manage.py changepassword <username>

# Delete all data and start fresh
python manage.py migrate zero books
python manage.py migrate
```

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/customers/signup/` | Create new account |
| POST | `/api/customers/login/` | Login to account |
| GET | `/api/customers/profile/` | Get user profile |
| GET | `/api/books/` | List all books |
| GET | `/api/books/{id}/` | Get book details |
| GET | `/api/books/by_price/` | Filter by price range |
| POST | `/api/sales/` | Create new order |
| GET | `/api/sales/my_orders/` | Get user orders |
| GET | `/api/sales/order_summary/` | Get order stats |

## Useful Python Shell Commands

```python
# Start shell
python manage.py shell

# Import models
from books.models import Book
from customers.models import Customer
from sales.models import Sale
from django.contrib.auth.models import User

# Create objects
book = Book.objects.create(title="New Book", author="Author Name", price=19.99)

# Query objects
books = Book.objects.all()
book = Book.objects.get(book_id=1)

# Update objects
book.price = 15.99
book.save()

# Delete objects
book.delete()

# Count objects
count = Book.objects.count()

# Filter objects
books = Book.objects.filter(author="Harper Lee")

# Order objects
books = Book.objects.all().order_by('-price')

# Exit shell
exit()
```

## Development Server URLs

| URL | Purpose |
|-----|---------|
| http://localhost:3000/ | Home |
| http://localhost:3000/admin/ | Admin panel |
| http://localhost:3000/api/ | API root |
| http://localhost:3000/api/books/ | Books list |
| http://localhost:3000/api/customers/ | Customers list |
| http://localhost:3000/api/sales/ | Sales list |

## Testing with curl

```bash
# Create account
curl -X POST http://localhost:3000/api/customers/signup/ \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","email":"user@test.com","password":"pass123","name":"User One"}'

# Login
curl -X POST http://localhost:3000/api/customers/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@test.com","password":"pass123"}'

# List books
curl http://localhost:3000/api/books/

# Filter by author
curl "http://localhost:3000/api/books/?author=Harper%20Lee"

# Create order
curl -X POST http://localhost:3000/api/sales/ \
  -H "Content-Type: application/json" \
  -d '{"book":1,"quantity":2}'
```

## Installing Additional Packages

```bash
# Install new package
pip install package-name

# Save to requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

## Deployment (Production)

```bash
# Collect static files
python manage.py collectstatic

# Run with Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:3000

# Create .env with production settings
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com
```

## Troubleshooting

```bash
# Check Python version
python --version

# Check Django installation
python -c "import django; print(django.get_version())"

# Run tests
python manage.py test

# Check for issues
python manage.py check

# View migrations status
python manage.py showmigrations
```

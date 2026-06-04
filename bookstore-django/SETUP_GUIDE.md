# 🚀 Django Bookstore Setup Guide

A comprehensive step-by-step guide to set up and run the Django bookstore application.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [Running the Application](#running-the-application)
4. [Understanding the Project Structure](#understanding-the-project-structure)
5. [Common Tasks](#common-tasks)
6. [API Testing Guide](#api-testing-guide)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** - [Download](https://www.python.org/downloads/)
  - Verify: `python --version`
- **pip** (Python package manager) - Usually comes with Python
  - Verify: `pip --version`
- **Virtual environment support** - Usually built-in
  - Verify: `python -m venv --help`
- **Text editor or IDE** (VS Code, PyCharm, etc.) - Optional but recommended

---

## Initial Setup

### Step 1: Create Virtual Environment

A virtual environment isolates your project dependencies from your system Python.

**Windows (Command Prompt):**
```bash
cd bookstore-django
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
cd bookstore-django
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
cd bookstore-django
python -m venv venv
source venv/bin/activate
```

✅ You'll see `(venv)` at the start of your terminal prompt when activated.

### Step 2: Install Dependencies

With virtual environment activated:

```bash
pip install -r requirements.txt
```

This installs:
- Django 4.2.11
- Django REST Framework
- CORS headers support
- Database drivers
- And other required packages

⏱️ **This usually takes 2-5 minutes** depending on your internet speed.

### Step 3: Create Environment Configuration

Create a `.env` file from the template:

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

This file contains sensitive configuration. Default values work for local development.

### Step 4: Run Database Migrations

Django uses migrations to manage database schema changes:

```bash
python manage.py migrate
```

This creates your SQLite database (`db.sqlite3`) and initializes all tables.

✅ **Output:** You should see "OK" messages for each migration.

### Step 5: Create Admin Account

Create a superuser for the Django admin panel:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- Username: (e.g., `admin`)
- Email: (e.g., `admin@example.com`)
- Password: (must be at least 8 characters)
- Password confirmation

**Remember these credentials!** You'll use them to log into the admin panel.

### Step 6: Load Initial Book Data (Optional)

For testing, seed some initial book data:

```bash
python manage.py shell < load_books.py
```

---

## Running the Application

### Start the Development Server

```bash
python manage.py runserver 3000
```

✅ **Expected output:**
```
Starting development server at http://127.0.0.1:3000/
Quit the server with CONTROL-C.
```

Now you can access:
- **Main API**: http://localhost:3000/api/
- **Admin Panel**: http://localhost:3000/admin/
- **Books**: http://localhost:3000/api/books/

### Stop the Server

Press `Ctrl+C` in your terminal.

### Deactivate Virtual Environment

When done working:
```bash
deactivate
```

---

## Understanding the Project Structure

```
bookstore-django/
│
├── config/                   # Project settings & routing
│   ├── settings.py          # Main Django configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI application
│   └── __init__.py
│
├── books/                    # Books app
│   ├── models.py            # Book database model
│   ├── serializers.py       # Book data serializer
│   ├── views.py             # Book API endpoints
│   ├── urls.py              # Book URL routing
│   ├── admin.py             # Admin configuration
│   └── __init__.py
│
├── customers/               # Customers app
│   ├── models.py            # Customer database model
│   ├── serializers.py       # Customer & Auth serializers
│   ├── views.py             # Customer API & Auth endpoints
│   ├── urls.py              # Customer URL routing
│   ├── admin.py             # Admin configuration
│   └── __init__.py
│
├── sales/                   # Sales/Orders app
│   ├── models.py            # Sale database model
│   ├── serializers.py       # Sale data serializer
│   ├── views.py             # Sale API endpoints
│   ├── urls.py              # Sale URL routing
│   ├── admin.py             # Admin configuration
│   └── __init__.py
│
├── db.sqlite3               # SQLite database (created after migrate)
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create from .env.example)
├── README.md                # Main documentation
└── SETUP_GUIDE.md           # This file
```

### Key Components Explained

| Component | Purpose |
|-----------|---------|
| **models.py** | Defines database tables and relationships |
| **serializers.py** | Converts models to/from JSON for API |
| **views.py** | API logic - handles requests and responses |
| **urls.py** | Maps URLs to view functions |
| **admin.py** | Configures Django admin interface |

---

## Common Tasks

### Create a New Customer (Sign Up)

Using **curl**:
```bash
curl -X POST http://localhost:3000/api/customers/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepass123",
    "name": "John Doe",
    "phone": "555-0101"
  }'
```

Using **Python requests**:
```python
import requests

response = requests.post(
    'http://localhost:3000/api/customers/signup/',
    json={
        'username': 'johndoe',
        'email': 'john@example.com',
        'password': 'securepass123',
        'name': 'John Doe',
        'phone': '555-0101'
    }
)
print(response.json())
```

### Login a Customer

```bash
curl -X POST http://localhost:3000/api/customers/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepass123"
  }'
```

### List All Books

```bash
curl http://localhost:3000/api/books/
```

### Create an Order

```bash
curl -X POST http://localhost:3000/api/sales/ \
  -H "Content-Type: application/json" \
  -d '{
    "book": 1,
    "quantity": 2
  }'
```

### View Django Admin

1. Navigate to: http://localhost:3000/admin/
2. Login with your superuser credentials
3. Manage Books, Customers, and Sales

### Make Migrations After Model Changes

If you modify any model:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Access Django Shell

Interact with your database programmatically:

```bash
python manage.py shell
```

Example commands:
```python
from books.models import Book
from customers.models import Customer
from sales.models import Sale

# Get all books
books = Book.objects.all()
print(f"Total books: {books.count()}")

# Get a specific book
book = Book.objects.get(book_id=1)
print(book)

# Create a new book
new_book = Book.objects.create(
    title="New Book",
    author="New Author",
    price=19.99
)

# Exit shell
exit()
```

---

## API Testing Guide

### Using Postman

1. **Download Postman** from https://www.postman.com/downloads/
2. **Import endpoints** - Create requests for each endpoint
3. **Test each route** - Set method, URL, headers, and body

### Example Postman Flow

**1. Sign Up**
- **Method**: POST
- **URL**: http://localhost:3000/api/customers/signup/
- **Body** (JSON):
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "name": "Test User",
    "phone": "555-1234"
}
```

**2. Login**
- **Method**: POST
- **URL**: http://localhost:3000/api/customers/login/
- **Body** (JSON):
```json
{
    "email": "test@example.com",
    "password": "testpass123"
}
```

**3. List Books**
- **Method**: GET
- **URL**: http://localhost:3000/api/books/

**4. Create Order**
- **Method**: POST
- **URL**: http://localhost:3000/api/sales/
- **Body** (JSON):
```json
{
    "book": 1,
    "quantity": 2
}
```

### Using curl Commands

```bash
# Sign up
curl -X POST http://localhost:3000/api/customers/signup/ \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","email":"user1@test.com","password":"pass123","name":"User One"}'

# Get books
curl http://localhost:3000/api/books/

# Get books filtered by author
curl "http://localhost:3000/api/books/?author=Harper%20Lee"

# Get books by price range
curl "http://localhost:3000/api/books/by_price/?min_price=10&max_price=15"
```

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'django'"

**Solution**: Activate your virtual environment and install requirements:
```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Problem: "Port 3000 is already in use"

**Solution**: Use a different port:
```bash
python manage.py runserver 3001
```

Or find and kill the process using port 3000.

### Problem: Database locked error

**Solution**: Delete `db.sqlite3` and run migrations again:
```bash
rm db.sqlite3  # macOS/Linux
del db.sqlite3  # Windows
python manage.py migrate
```

### Problem: "No such table: books_book"

**Solution**: You haven't run migrations:
```bash
python manage.py migrate
```

### Problem: "SyntaxError" in models or views

**Solution**: Check your Python syntax:
```bash
python -m py_compile books/models.py  # or any .py file
```

### Problem: "Connection refused" when accessing API

**Ensure:**
1. Server is running: `python manage.py runserver`
2. Using correct URL: http://localhost:3000/api/...
3. No firewall blocking port 3000

### Problem: Forgot admin password

**Solution**: Create a new superuser:
```bash
python manage.py createsuperuser
```

### Problem: Changes to models aren't showing

**Solution**: Make and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Next Steps

After setup:

1. **Explore the Admin Panel**: http://localhost:3000/admin/
2. **Try the API**: http://localhost:3000/api/
3. **Read Django Documentation**: https://docs.djangoproject.com/
4. **Connect Frontend**: Integrate with React, Vue, or Angular
5. **Deploy**: Use Heroku, AWS, or DigitalOcean

---

## Useful Commands Reference

```bash
# Activate virtual environment
venv\Scripts\activate                    # Windows
source venv/bin/activate                # macOS/Linux

# Install/Update packages
pip install -r requirements.txt
pip install package-name
pip freeze > requirements.txt

# Database management
python manage.py migrate
python manage.py makemigrations
python manage.py migrate --fake-initial

# Server management
python manage.py runserver
python manage.py runserver 0.0.0.0:3000
python manage.py runserver 3001

# Admin management
python manage.py createsuperuser
python manage.py changepassword username

# Database interaction
python manage.py shell
python manage.py dbshell

# Collect static files (production)
python manage.py collectstatic

# Deactivate virtual environment
deactivate
```

---

**Need Help?** Check the main README.md or Django documentation at https://docs.djangoproject.com/

**Happy developing! 🎉**

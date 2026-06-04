# 📚 BookStore Web Application - Django

A full-stack bookstore web application built with Django REST Framework, featuring user authentication, book management, and order processing.

## ✨ Features

- **User Authentication**: Sign up and login with secure password handling
- **Book Catalog**: Browse and manage books with filtering and search
- **Order Management**: Create orders, view purchase history, and get order summaries
- **RESTful API**: Complete API endpoints for all operations
- **Admin Panel**: Django admin interface for managing books, customers, and sales
- **Database**: SQLite for development, PostgreSQL for production
- **CORS Support**: Ready for frontend integration

## 🛠️ Tech Stack

- **Backend**: Django 4.2.11
- **API**: Django REST Framework 3.14.0
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Authentication**: Django built-in authentication
- **Other**: CORS headers, Python Decouple for env management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip and virtualenv

### Installation

1. **Navigate to the project directory:**
```bash
cd bookstore-django
```

2. **Create and activate a virtual environment:**

**Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create a .env file from the example:**
```bash
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux
```

5. **Run migrations:**
```bash
python manage.py migrate
```

6. **Create a superuser (admin account):**
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

7. **Load sample data (optional):**
```bash
python manage.py shell < load_books.py
```

8. **Run the development server:**
```bash
python manage.py runserver 3000
```

The server will start at `http://localhost:3000`

## 📖 API Documentation

### Base URL
```
http://localhost:3000/api/
```

### Home Page
```
http://localhost:3000/
```

### Authentication Endpoints

#### Sign Up
```
POST /customers/signup/
Content-Type: application/json

{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "name": "John Doe",
    "phone": "555-0101"
}

Response: 201 Created
{
    "message": "Account created successfully",
    "customer": { ... }
}
```

#### Login
```
POST /customers/login/
Content-Type: application/json

{
    "email": "john@example.com",
    "password": "securepassword123"
}

Response: 200 OK
{
    "message": "Login successful",
    "customer": { ... },
    "user_id": 1
}
```

#### Get Profile
```
GET /customers/profile/
Authorization: Bearer <token> or Session authentication

Response: 200 OK
{
    "customer_id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "555-0101",
    ...
}
```

### Books Endpoints

#### List All Books
```
GET /books/
Optional filters:
  - ?author=Harper%20Lee
  - ?price=12.99
  - ?search=mockingbird
  - ?ordering=price or -price

Response: 200 OK
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "book_id": 1,
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "price": "12.99",
            ...
        }
    ]
}
```

#### Get Book by ID
```
GET /books/{id}/

Response: 200 OK
{
    "book_id": 1,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "price": "12.99",
    ...
}
```

#### Books by Price Range
```
GET /books/by_price/?min_price=10&max_price=15

Response: 200 OK
[...]
```

### Sales/Orders Endpoints

#### Create Order (Authenticated)
```
POST /sales/
Content-Type: application/json
Authorization: Required

{
    "book": 1,
    "quantity": 2
}

Response: 201 Created
{
    "sale_id": 1001,
    "customer": 1,
    "book": 1,
    "date": "2026-05-31",
    "quantity": 2,
    "total_price": "25.98",
    ...
}
```

#### Get My Orders (Authenticated)
```
GET /sales/my_orders/
Authorization: Required

Response: 200 OK
[...]
```

#### Get Order Summary (Authenticated)
```
GET /sales/order_summary/
Authorization: Required

Response: 200 OK
{
    "total_orders": 5,
    "total_spent": "125.50",
    "total_books_purchased": 12
}
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# For PostgreSQL (uncomment and configure):
# DB_NAME=bookstore
# DB_USER=postgres
# DB_PASSWORD=your_password
# DB_HOST=localhost
# DB_PORT=5432
```

### Using PostgreSQL (Production)

1. **Install PostgreSQL driver:**
```bash
pip install psycopg2-binary
```

2. **Update `config/settings.py`:**
Uncomment the PostgreSQL database configuration and update your `.env` file.

3. **Run migrations:**
```bash
python manage.py migrate
```

## 📊 Admin Interface

Access the Django admin panel at `http://localhost:3000/admin/`

Use your superuser credentials to:
- Manage books
- View customers
- Track sales/orders
- Manage users

## 🗄️ Database Schema

### Books Table
- book_id (Primary Key)
- title (VARCHAR 255)
- author (VARCHAR 255)
- price (DECIMAL 10,2)
- created_at (DateTime)
- updated_at (DateTime)

### Customers Table
- customer_id (Primary Key)
- user_id (Foreign Key to User)
- name (VARCHAR 255)
- email (VARCHAR 255, Unique)
- phone (VARCHAR 15)
- created_at (DateTime)
- updated_at (DateTime)

### Sales Table
- sale_id (Primary Key)
- customer_id (Foreign Key)
- book_id (Foreign Key)
- date (Date)
- quantity (Integer)
- total_price (DECIMAL 10,2)
- created_at (DateTime)
- updated_at (DateTime)

## 📁 Project Structure

```
bookstore-django/
├── config/
│   ├── settings.py       # Django settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI configuration
│   └── __init__.py
├── books/
│   ├── models.py         # Book model
│   ├── serializers.py    # Book serializer
│   ├── views.py          # Book viewset
│   ├── urls.py           # Book URLs
│   └── admin.py          # Django admin config
├── customers/
│   ├── models.py         # Customer model
│   ├── serializers.py    # Customer & auth serializers
│   ├── views.py          # Customer viewset
│   ├── urls.py           # Customer URLs
│   └── admin.py          # Django admin config
├── sales/
│   ├── models.py         # Sale model
│   ├── serializers.py    # Sale serializer
│   ├── views.py          # Sale viewset
│   ├── urls.py           # Sale URLs
│   └── admin.py          # Django admin config
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 🔐 Security

- Passwords are hashed using Django's built-in password hashing
- CSRF protection enabled by default
- SQL injection prevention through ORM
- CORS configured for trusted origins
- Update `SECRET_KEY` in production

## 🚀 Deployment

### Using Gunicorn

1. **Install Gunicorn:**
```bash
pip install gunicorn
```

2. **Run with Gunicorn:**
```bash
gunicorn config.wsgi:application --bind 0.0.0.0:3000
```

### Using Docker (Optional)

Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:3000"]
```

Build and run:
```bash
docker build -t bookstore-django .
docker run -p 3000:3000 bookstore-django
```

## 🐛 Troubleshooting

### ModuleNotFoundError
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

### Database errors
- Run `python manage.py migrate`
- Delete `db.sqlite3` and retry migrations if corrupted

### Port 3000 already in use
```bash
python manage.py runserver 3001
```

## 📝 Sample Workflow

1. **Sign up** at `/api/customers/signup/`
2. **Login** at `/api/customers/login/`
3. **Browse books** at `/api/books/`
4. **Create order** at `/api/sales/` with book ID and quantity
5. **View orders** at `/api/sales/my_orders/`
6. **Get summary** at `/api/sales/order_summary/`

## 📧 Support

For issues or questions, check the Django documentation:
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

**Happy coding! 🎉**

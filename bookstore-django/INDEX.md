# 📚 Django Bookstore Documentation Index

Welcome to the Django Bookstore Application! This index helps you navigate the documentation.

## 📖 Quick Navigation

### Getting Started
1. **[README.md](README.md)** ⭐ START HERE
   - Overview of the project
   - Features list
   - Quick start (5 minutes)
   - API documentation with examples
   - Deployment guide

2. **[SETUP_GUIDE.md](SETUP_GUIDE.md)** 🚀 Step-by-Step Setup
   - Prerequisites checklist
   - Detailed installation steps
   - Running the application
   - Project structure explanation
   - Common tasks
   - API testing guide
   - Troubleshooting

3. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** ⚡ Handy Cheatsheet
   - Virtual environment commands
   - Installation & setup one-liners
   - Database management commands
   - API endpoints table
   - Django shell examples
   - curl examples
   - Deployment commands

4. **[DJANGO_VS_NEXTJS.md](DJANGO_VS_NEXTJS.md)** 🔄 Migration Guide
   - Architecture comparison
   - What changed from Next.js
   - Key advantages of Django
   - Code examples comparison
   - Integration with frontend

## 🗂️ Project Files

### Configuration Files
| File | Purpose |
|------|---------|
| `manage.py` | Django management script (migrations, server, etc.) |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment variables template |
| `.gitignore` | Git ignore rules |
| `setup.bat` | Windows automated setup script |
| `setup.sh` | Linux/macOS automated setup script |
| `load_books.py` | Script to load sample book data |

### Core Application Files

#### `config/` - Project Settings
- `settings.py` - Django configuration
- `urls.py` - Main URL routing
- `wsgi.py` - WSGI application
- `asgi.py` - ASGI application

#### `books/` - Books Application
- `models.py` - Book database model
- `serializers.py` - Book API serializer
- `views.py` - Book API endpoints
- `urls.py` - Book URL routing
- `admin.py` - Django admin config

#### `customers/` - Customers & Authentication
- `models.py` - Customer database model
- `serializers.py` - Customer/Auth serializers
- `views.py` - Customer API & Auth endpoints
- `urls.py` - Customer URL routing
- `admin.py` - Django admin config

#### `sales/` - Sales/Orders
- `models.py` - Sale database model
- `serializers.py` - Sale API serializer
- `views.py` - Sale API endpoints
- `urls.py` - Sale URL routing
- `admin.py` - Django admin config

## 🚀 Quick Start (Fastest Path)

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it (Windows)
venv\Scripts\activate
# Or macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

**Then visit:**
- 🌐 API: http://localhost:3000/api/
- 🔐 Admin: http://localhost:3000/admin/
- 📚 Books: http://localhost:3000/api/books/

## 📡 API Overview

### Authentication
- `POST /api/customers/signup/` - Create account
- `POST /api/customers/login/` - Login
- `GET /api/customers/profile/` - Get profile

### Books
- `GET /api/books/` - List books
- `GET /api/books/{id}/` - Get single book
- `GET /api/books/by_price/` - Filter by price

### Orders
- `POST /api/sales/` - Create order
- `GET /api/sales/my_orders/` - Get user orders
- `GET /api/sales/order_summary/` - Get order stats

## 🔧 Common Tasks

### Create sample data
```bash
python manage.py shell < load_books.py
```

### Access Django admin
Visit http://localhost:3000/admin/ with your superuser credentials

### Make code changes to models
```bash
python manage.py makemigrations
python manage.py migrate
```

### Test an endpoint with curl
```bash
curl http://localhost:3000/api/books/
```

### Reset database
```bash
rm db.sqlite3  # or del db.sqlite3 on Windows
python manage.py migrate
```

## 💡 Learning Path

1. **Understand the structure** → [DJANGO_VS_NEXTJS.md](DJANGO_VS_NEXTJS.md)
2. **Set up locally** → [SETUP_GUIDE.md](SETUP_GUIDE.md)
3. **Learn the APIs** → [README.md](README.md) - API Documentation section
4. **Reference commands** → [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

## 📚 Key Concepts

### Models (Database)
- **Book**: Books in the catalog
- **Customer**: Registered users (linked to Django's User model)
- **Sale**: Purchase transactions

### Serializers
Convert between Python objects and JSON for API responses

### ViewSets
Provide standard API operations (list, create, retrieve, update, delete)

### URLs
Map HTTP requests to view functions

### Admin
Built-in interface to manage all data at http://localhost:3000/admin/

## 🌐 Connecting Frontend

The Django API is ready for any frontend framework:

```javascript
// React, Vue, Angular, etc.
fetch('http://localhost:3000/api/books/')
  .then(r => r.json())
  .then(data => console.log(data))
```

## 🐛 Need Help?

| Problem | Solution |
|---------|----------|
| Can't run manage.py | Activate virtual environment: `venv\Scripts\activate` |
| Import errors | Install dependencies: `pip install -r requirements.txt` |
| Database errors | Run migrations: `python manage.py migrate` |
| Port 3000 in use | Use different port: `python manage.py runserver 3001` |
| Forgot admin password | Create new: `python manage.py createsuperuser` |

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed troubleshooting.

## 🔗 Useful Links

- [Django Official Docs](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python.org](https://www.python.org/)
- [Postman](https://www.postman.com/) - API testing tool

## 📝 File Reading Order

**For newcomers:**
1. `README.md` - Get the big picture
2. `SETUP_GUIDE.md` - Follow steps 1-6
3. Try the API endpoints
4. Check `QUICK_REFERENCE.md` for commands

**For developers:**
1. `DJANGO_VS_NEXTJS.md` - Understand the migration
2. Study `books/models.py` - Understand the schema
3. Check `config/settings.py` - Understand configuration
4. Try `python manage.py shell` - Explore the models

**For deployment:**
1. `README.md` - Deployment section
2. `QUICK_REFERENCE.md` - Production commands
3. Set up `.env` with production values

---

**Ready to get started?** Begin with [README.md](README.md) or [SETUP_GUIDE.md](SETUP_GUIDE.md)! 🎉

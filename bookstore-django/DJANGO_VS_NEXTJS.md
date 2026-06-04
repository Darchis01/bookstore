# Next.js vs Django - Migration Summary

This document outlines the migration from Next.js to Django for the Bookstore application.

## Architecture Comparison

| Aspect | Next.js | Django |
|--------|---------|--------|
| **Type** | JavaScript/React Full-Stack | Python Backend Framework |
| **Frontend** | Built-in (React) | Separate (API only) |
| **Backend** | API Routes | REST Framework |
| **ORM** | Prisma | Django ORM |
| **Database** | SQLite/PostgreSQL | SQLite/PostgreSQL |
| **Authentication** | Custom JWT/Session | Built-in Auth System |
| **Admin Panel** | Custom required | Built-in Django Admin |
| **API Style** | RESTful (Next.js routes) | RESTful (DRF) |

## What Changed

### 1. **Project Structure**

**Before (Next.js):**
```
bookstore-webapp/
├── app/
│   ├── api/
│   │   ├── auth/
│   │   ├── books/
│   │   └── sales/
│   ├── books/
│   ├── components/
│   └── pages/
├── prisma/
└── package.json
```

**After (Django):**
```
bookstore-django/
├── books/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── customers/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── sales/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

### 2. **Language & Runtime**

- **Next.js**: Node.js (JavaScript/TypeScript)
- **Django**: Python 3.8+

### 3. **Database ORM**

**Next.js (Prisma):**
```typescript
// prisma/schema.prisma
model Book {
  id    Int     @id @default(autoincrement())
  title String
  author String
  price Decimal
}

// In code
const book = await prisma.book.findUnique({ where: { id: 1 } });
```

**Django:**
```python
# books/models.py
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# In code
book = Book.objects.get(book_id=1)
```

### 4. **API Endpoints**

**Next.js:**
```typescript
// app/api/books/route.ts
export async function GET() {
  const books = await prisma.book.findMany();
  return Response.json(books);
}
```

**Django:**
```python
# books/views.py
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Automatically creates:
# GET    /api/books/
# POST   /api/books/
# GET    /api/books/{id}/
# PUT    /api/books/{id}/
# DELETE /api/books/{id}/
```

### 5. **Authentication**

**Next.js:**
- Custom implementation with bcryptjs
- Session or JWT tokens

**Django:**
- Built-in User model
- Session-based authentication
- Easy to extend with tokens

**Next.js Example:**
```typescript
// app/api/auth/signup/route.ts
const hashedPassword = await bcrypt.hash(password, 10);
```

**Django Example:**
```python
# customers/views.py
user = User.objects.create_user(
    username=username,
    email=email,
    password=password
)
```

### 6. **Admin Interface**

**Next.js:**
- Need to build custom admin dashboard
- Manual CRUD operations

**Django:**
- Built-in admin panel at `/admin/`
- Automatic CRUD for all models
- User/permission management

Access Django admin:
```
http://localhost:3000/admin/
```

### 7. **Dependencies**

**Next.js (package.json):**
```json
{
  "dependencies": {
    "next": "^16.2.6",
    "react": "^18.2.0",
    "@prisma/client": "^5.0.0",
    "bcryptjs": "^2.4.3"
  }
}
```

**Django (requirements.txt):**
```
Django==4.2.11
djangorestframework==3.14.0
django-cors-headers==4.3.1
python-decouple==3.8
psycopg2-binary==2.9.9
```

## Key Advantages of Django

### ✅ For You (as a Django user):

1. **Familiar Framework** - You're comfortable with Django patterns
2. **Built-in Admin** - Manage data without building interfaces
3. **Batteries Included** - Authentication, permissions, serialization
4. **Python Ecosystem** - Vast library support
5. **Better Scaling** - Django is production-proven at scale
6. **Less Code** - DRF handles a lot automatically

### ✅ For the Project:

1. **Separation of Concerns** - Backend and frontend are separate
2. **Flexibility** - Easy to switch frontend (React, Vue, Angular)
3. **Security** - CSRF protection, SQL injection prevention built-in
4. **Testing** - Django test framework is excellent
5. **Deployment** - Easy deployment to any Python-capable server

## Migration Mapping

### Database Schema

| Concept | Next.js (Prisma) | Django |
|---------|------------------|--------|
| Model | `model` | `class Model` |
| Field | Field type | `models.FieldType` |
| Relation | `@relation` | `ForeignKey` |
| Unique | `@unique` | `unique=True` |
| Primary Key | `@id` | `primary_key=True` |
| Default | `@default` | `default=value` |

### API Response

**Next.js:**
```json
{
  "status": "success",
  "data": [...]
}
```

**Django:**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [...]
}
```

## Running Both (Comparison)

### Starting Next.js
```bash
npm run dev
# http://localhost:3000
```

### Starting Django
```bash
python manage.py runserver 3000
# http://localhost:3000
```

## Frontend Integration

### With React/Next.js Frontend

```javascript
// Still works! Call Django API instead
const response = await fetch('http://localhost:3000/api/books/');
const books = await response.json();
```

### With Vue/Angular Frontend

Django API is framework-agnostic:
```javascript
// In any framework
fetch('http://localhost:3000/api/books/')
  .then(r => r.json())
  .then(data => console.log(data))
```

## Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django for Beginners](https://djangoforbeginners.com/)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)

## Common Django Patterns You'll Use

### 1. Models (Database)
```python
class Book(models.Model):
    title = models.CharField(max_length=255)
```

### 2. Serializers (API Data)
```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

### 3. Views (API Logic)
```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

### 4. URLs (Routing)
```python
router.register(r'books', BookViewSet)
urlpatterns = [path('api/', include(router.urls))]
```

## Quick Comparison: Same Task

### Task: Get all books by an author

**Next.js:**
```typescript
const books = await prisma.book.findMany({
  where: { author: "Harper Lee" }
});
```

**Django:**
```python
books = Book.objects.filter(author="Harper Lee")
```

**API Call (Same for both):**
```bash
curl "http://backend/api/books/?author=Harper%20Lee"
```

---

**Everything is ready!** See `README.md` for setup instructions and `SETUP_GUIDE.md` for detailed walkthrough.

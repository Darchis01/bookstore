from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<html><head><title>Bookstore Django</title></head>"
        "<body style='font-family:Arial, sans-serif; margin:40px;'>"
        "<h1>Bookstore Django</h1>"
        "<p>Welcome! Your Django bookstore is running successfully.</p>"
        "<ul>"
        "<li><a href='/api/'>API Root</a></li>"
        "<li><a href='/api/books/'>Books</a></li>"
        "<li><a href='/api/customers/signup/'>Customer Sign Up</a></li>"
        "<li><a href='/api/sales/'>Sales</a></li>"
        "<li><a href='/admin/'>Admin</a></li>"
        "</ul>"
        "</body></html>"
    )

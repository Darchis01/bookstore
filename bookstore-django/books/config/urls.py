from books.config import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('frontend.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/customers/', include('books.customers.urls')),
    path('api/sales/', include('books.sales.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

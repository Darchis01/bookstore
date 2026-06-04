from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books_list, name='books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('flutterwave/init/', views.flutterwave_init, name='flutterwave_init'),
    path('flutterwave/verify/', views.flutterwave_verify, name='flutterwave_verify'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]

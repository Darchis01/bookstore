import json
import urllib.request
import urllib.error
import uuid

from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from books.models import Book, Category
from books.customers.models import Customer, Wishlist
from books.sales.models import Payment, Sale
from .forms import SignUpForm, LoginForm, PurchaseForm


def home(request):
    featured_books = Book.objects.order_by('-created_at')[:6]
    return render(request, 'frontend/home.html', {
        'featured_books': featured_books,
    })


def books_list(request):
    books = Book.objects.all()
    categories = Category.objects.all().order_by('name')
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        books = books.filter(category_id=category_id)
    
    # Search by title or author
    search_query = request.GET.get('search', '')
    if search_query:
        books = books.filter(
            models.Q(title__icontains=search_query) |
            models.Q(author__icontains=search_query) |
            models.Q(description__icontains=search_query)
        )
    
    books = books.order_by('title')

    wishlist_book_ids = set()
    if request.user.is_authenticated:
        wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
        wishlist_book_ids = set(wishlist.books.values_list('book_id', flat=True))
    
    return render(request, 'frontend/books.html', {
        'books': books,
        'categories': categories,
        'selected_category': category_id,
        'search_query': search_query,
        'wishlist_book_ids': wishlist_book_ids,
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    form = PurchaseForm(request.POST or None)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'Please log in to purchase books.')
            return redirect('{}?next={}'.format(reverse('login'), request.path))

        if form.is_valid():
            try:
                customer = Customer.objects.get(user=request.user)
            except Customer.DoesNotExist:
                messages.error(request, 'Please complete your customer profile before purchasing.')
                return redirect('profile')

            quantity = form.cleaned_data['quantity']
            Sale.objects.create(customer=customer, book=book, quantity=quantity)
            messages.success(request, f'Your purchase of {book.title} was successful.')
            return redirect('profile')

    return render(request, 'frontend/book_detail.html', {
        'book': book,
        'form': form,
        'flutterwave_public_key': settings.FLUTTERWAVE_PUBLIC_KEY,
    })


@login_required(login_url='login')
def flutterwave_init(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request method.')

    try:
        payload = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON payload.')

    book_id = payload.get('book_id')
    quantity = payload.get('quantity', 1)
    payment_method = payload.get('payment_method', 'card')

    if not book_id:
        return HttpResponseBadRequest('Book ID is required.')

    book = get_object_or_404(Book, book_id=book_id)

    try:
        quantity = int(quantity)
        if quantity < 1:
            quantity = 1
    except (TypeError, ValueError):
        quantity = 1

    customer, _ = Customer.objects.get_or_create(
        user=request.user,
        defaults={
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email or '',
            'phone': '',
        }
    )

    amount = book.price * quantity
    payment = Payment.objects.create(
        customer=customer,
        amount=amount,
        currency=settings.FLUTTERWAVE_CURRENCY,
        payment_method=payment_method,
    )
    tx_ref = f'sciobe_{payment.payment_id}_{book.book_id}_{quantity}_{uuid.uuid4().hex[:8]}'
    payment.flutterwave_ref = tx_ref
    payment.save(update_fields=['flutterwave_ref'])

    return JsonResponse({
        'public_key': settings.FLUTTERWAVE_PUBLIC_KEY,
        'tx_ref': tx_ref,
        'amount': str(amount),
        'currency': settings.FLUTTERWAVE_CURRENCY,
        'customer_email': request.user.email,
        'customer_phone': customer.phone,
        'customer_name': customer.name,
        'payment_id': payment.payment_id,
        'book_id': book.book_id,
        'quantity': quantity,
    })


@login_required(login_url='login')
def flutterwave_verify(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request method.')

    try:
        payload = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON payload.')

    tx_ref = payload.get('tx_ref')
    transaction_id = payload.get('transaction_id')

    if not tx_ref or not transaction_id:
        return HttpResponseBadRequest('tx_ref and transaction_id are required.')

    verify_url = f'https://api.flutterwave.com/v3/transactions/{transaction_id}/verify'
    request_obj = urllib.request.Request(
        verify_url,
        headers={
            'Authorization': f'Bearer {settings.FLUTTERWAVE_SECRET_KEY}',
            'Content-Type': 'application/json',
        },
        method='GET'
    )

    try:
        response = urllib.request.urlopen(request_obj)
        response_data = json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as exc:
        return JsonResponse({'error': f'Flutterwave verification failed: {exc.read().decode("utf-8")}'}, status=400)
    except urllib.error.URLError as exc:
        return JsonResponse({'error': f'Unable to reach Flutterwave: {exc.reason}'}, status=502)

    if response_data.get('status') != 'success':
        return JsonResponse({'error': 'Flutterwave verification did not return success.'}, status=400)

    data = response_data.get('data', {})
    if data.get('status') != 'successful':
        return JsonResponse({'error': 'Payment was not successful.'}, status=400)

    payment = Payment.objects.filter(flutterwave_ref=tx_ref).first()
    if not payment:
        return JsonResponse({'error': 'Payment record not found.'}, status=404)

    if payment.status != 'completed':
        parts = tx_ref.split('_')
        try:
            book_id = int(parts[2])
            quantity = int(parts[3])
        except (IndexError, TypeError, ValueError):
            return JsonResponse({'error': 'Unable to parse transaction reference.'}, status=400)

        book = get_object_or_404(Book, book_id=book_id)
        sale = Sale.objects.create(customer=payment.customer, book=book, quantity=quantity)
        payment.sale = sale
        payment.flutterwave_txn_id = str(data.get('id'))
        payment.status = 'completed'
        payment.amount = Decimal(str(data.get('amount', payment.amount)))
        payment.currency = data.get('currency', payment.currency)
        payment.completed_at = timezone.now()
        payment.save()
    else:
        sale = payment.sale

    return JsonResponse({
        'success': True,
        'message': 'Payment completed successfully.',
        'sale_id': sale.sale_id if sale else None,
    })


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('books')

    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        full_name = form.cleaned_data['full_name']
        phone = form.cleaned_data['phone']
        password = form.cleaned_data['password1']

        first_name, *last_name = full_name.split(' ', 1)
        last_name = last_name[0] if last_name else ''

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        customer = Customer.objects.create(
            user=user,
            name=full_name,
            email=email,
            phone=phone,
        )

        login(request, user)
        registration_time = timezone.localtime(customer.created_at).strftime('%B %d, %Y at %I:%M %p')
        messages.success(request, f'Account created successfully on {registration_time}. Welcome to Sciobe!')
        return redirect('books')

    return render(request, 'frontend/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('books')

    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.filter(email=email).first()

        if user is not None:
            authenticated_user = authenticate(username=user.username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'Login successful. Welcome back!')
                next_url = request.GET.get('next') or reverse('books')
                return redirect(next_url)

        messages.error(request, 'Invalid email or password.')

    return render(request, 'frontend/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required(login_url='login')
def profile(request):
    customer, created = Customer.objects.get_or_create(
        user=request.user,
        defaults={
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email or '',
            'phone': '',
        }
    )

    if created:
        messages.info(request, 'A customer profile was created for your account.')

    sales = Sale.objects.filter(customer=customer).order_by('-date')
    purchased_books = []
    for sale in sales:
        if sale.book not in purchased_books:
            purchased_books.append(sale.book)

    total_spent = sum((sale.total_price for sale in sales), Decimal('0.00'))
    
    # Get or create wishlist for the user
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    return render(request, 'frontend/profile.html', {
        'customer': customer,
        'sales': sales,
        'purchased_books': purchased_books,
        'total_spent': total_spent,
        'member_since': customer.created_at,
        'wishlist': wishlist,
    })

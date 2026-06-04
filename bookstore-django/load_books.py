from books.models import Book

books_data = [
    {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'price': 12.99
    },
    {
        'title': '1984',
        'author': 'George Orwell',
        'price': 13.99
    },
    {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'price': 11.99
    },
    {
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'price': 10.99
    },
    {
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'price': 14.99
    },
]

for book_data in books_data:
    book = Book.objects.create(**book_data)
    print(f"Created: {book.title}")

print(f"\nTotal books created: {Book.objects.count()}")

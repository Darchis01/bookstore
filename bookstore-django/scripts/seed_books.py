"""
Seed script to populate categories and books in the database.
Usage: python manage.py shell < scripts/seed_books.py
or: cd bookstore-django && python manage.py shell
     >>> exec(open('scripts/seed_books.py').read())
"""
import os
import sys
import django

# Ensure project root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from books.models import Category, Book

# Clear existing data (optional)
print("Seeding categories and books...")

# Define categories
categories_data = [
    {
        'name': 'Fiction',
        'description': 'Novels, stories, and imaginative narratives'
    },
    {
        'name': 'Science & Technology',
        'description': 'Books on science, technology, and innovation'
    },
    {
        'name': 'Self-Help & Personal Development',
        'description': 'Growth, mindfulness, and personal improvement'
    },
    {
        'name': 'Business & Finance',
        'description': 'Entrepreneurship, investing, and business strategy'
    },
    {
        'name': 'History & Biography',
        'description': 'Historical events, biographies, and memoirs'
    },
    {
        'name': 'Education & Learning',
        'description': 'Academic texts and learning resources'
    }
]

# Create categories
categories = {}
for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={'description': cat_data['description']}
    )
    categories[cat_data['name']] = category
    print(f"{'✓ Created' if created else '✓ Found'} category: {category.name}")

# Define books by category
books_data = {
    'Fiction': [
        {
            'title': 'The Midnight Library',
            'author': 'Matt Haig',
            'description': 'Discover the power of second chances. A life-changing novel about exploring the roads not taken and learning to love the life you\'re living. Perfect for anyone seeking inspiration and hope.',
            'price': 4500
        },
        {
            'title': 'Remarkably Bright',
            'author': 'Katherine Center',
            'description': 'Get lost in a heartwarming story about love, family, and finding your way. Readers rave about feeling uplifted and inspired for weeks after finishing this gem.',
            'price': 4200
        }
    ],
    'Science & Technology': [
        {
            'title': 'Thinking, Fast and Slow',
            'author': 'Daniel Kahneman',
            'description': 'Transform how you make decisions. Understand the hidden forces that shape your thinking and learn to avoid costly mental mistakes. A Nobel Prize winner\'s groundbreaking insights.',
            'price': 5500
        },
        {
            'title': 'The Innovators',
            'author': 'Walter Isaacson',
            'description': 'Uncover the stories behind every technological breakthrough. Inspiring narratives of genius, creativity, and determination that changed the world—and will change how you see innovation.',
            'price': 5000
        }
    ],
    'Self-Help & Personal Development': [
        {
            'title': 'Atomic Habits',
            'author': 'James Clear',
            'description': 'Build life-changing habits in just 1% a day. Discover the proven system that millions have used to transform their lives. Simple, practical, and incredibly effective.',
            'price': 4800
        },
        {
            'title': 'The 7 Habits of Highly Effective People',
            'author': 'Stephen Covey',
            'description': 'Master the principles that lead to personal and professional excellence. Transform your mindset and achieve your biggest goals. A timeless classic that works.',
            'price': 5200
        }
    ],
    'Business & Finance': [
        {
            'title': 'Zero to One',
            'author': 'Peter Thiel',
            'description': 'Learn how to build a billion-dollar company from scratch. Peter Thiel\'s revolutionary thinking on startups and the future. Essential reading for every entrepreneur.',
            'price': 5500
        },
        {
            'title': 'The Lean Startup',
            'author': 'Eric Ries',
            'description': 'Build your business faster with proven strategies. Eliminate waste, test quickly, and grow sustainably. The playbook that transformed startup culture.',
            'price': 5000
        }
    ],
    'History & Biography': [
        {
            'title': 'Steve Jobs',
            'author': 'Walter Isaacson',
            'description': 'Enter the mind of a visionary. The definitive biography of Steve Jobs, revealing how perfectionism and creativity revolutionized multiple industries.',
            'price': 5500
        },
        {
            'title': 'Becoming',
            'author': 'Michelle Obama',
            'description': 'Be inspired by an extraordinary life story. Michelle Obama\'s intimate memoir shares lessons on resilience, courage, and finding your authentic path.',
            'price': 6000
        }
    ],
    'Education & Learning': [
        {
            'title': 'Learning How to Learn',
            'author': 'Barbara Oakley',
            'description': 'Master any skill faster and retain it longer. Proven brain science techniques to unlock your learning potential. Transform how you study and grow.',
            'price': 4500
        },
        {
            'title': 'Make It Stick',
            'author': 'Peter Brown, Henry Roediger III, Mark Daniel McDaniel',
            'description': 'Stop wasting time on ineffective study methods. Learn the science-backed techniques to absorb and remember information like never before.',
            'price': 5000
        }
    ]
}

# Create books
for category_name, books_list in books_data.items():
    category = categories[category_name]
    for book_data in books_list:
        book, created = Book.objects.get_or_create(
            title=book_data['title'],
            author=book_data['author'],
            defaults={
                'description': book_data['description'],
                'price': book_data['price'],
                'category': category
            }
        )
        print(f"  {'✓ Created' if created else '✓ Found'} book: {book.title}")

print(f"\n✓ Seeding complete!")
print(f"Total categories: {Category.objects.count()}")
print(f"Total books: {Book.objects.count()}")

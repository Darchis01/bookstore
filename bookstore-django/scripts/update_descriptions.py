"""
Update book descriptions with more sales-focused copy.
Usage: python manage.py shell < scripts/update_descriptions.py
"""
import os
import sys
import django

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from books.models import Book

# Define updated descriptions
book_updates = {
    'The Midnight Library': 'Discover the power of second chances. A life-changing novel about exploring the roads not taken and learning to love the life you\'re living. Perfect for anyone seeking inspiration and hope.',
    'Remarkably Bright': 'Get lost in a heartwarming story about love, family, and finding your way. Readers rave about feeling uplifted and inspired for weeks after finishing this gem.',
    'Thinking, Fast and Slow': 'Transform how you make decisions. Understand the hidden forces that shape your thinking and learn to avoid costly mental mistakes. A Nobel Prize winner\'s groundbreaking insights.',
    'The Innovators': 'Uncover the stories behind every technological breakthrough. Inspiring narratives of genius, creativity, and determination that changed the world—and will change how you see innovation.',
    'Atomic Habits': 'Build life-changing habits in just 1% a day. Discover the proven system that millions have used to transform their lives. Simple, practical, and incredibly effective.',
    'The 7 Habits of Highly Effective People': 'Master the principles that lead to personal and professional excellence. Transform your mindset and achieve your biggest goals. A timeless classic that works.',
    'Zero to One': 'Learn how to build a billion-dollar company from scratch. Peter Thiel\'s revolutionary thinking on startups and the future. Essential reading for every entrepreneur.',
    'The Lean Startup': 'Build your business faster with proven strategies. Eliminate waste, test quickly, and grow sustainably. The playbook that transformed startup culture.',
    'Steve Jobs': 'Enter the mind of a visionary. The definitive biography of Steve Jobs, revealing how perfectionism and creativity revolutionized multiple industries.',
    'Becoming': 'Be inspired by an extraordinary life story. Michelle Obama\'s intimate memoir shares lessons on resilience, courage, and finding your authentic path.',
    'Learning How to Learn': 'Master any skill faster and retain it longer. Proven brain science techniques to unlock your learning potential. Transform how you study and grow.',
    'Make It Stick': 'Stop wasting time on ineffective study methods. Learn the science-backed techniques to absorb and remember information like never before.',
}

# Update books
updated_count = 0
for title, new_description in book_updates.items():
    try:
        book = Book.objects.get(title=title)
        book.description = new_description
        book.save()
        print(f"✓ Updated: {title}")
        updated_count += 1
    except Book.DoesNotExist:
        print(f"✗ Not found: {title}")

print(f"\n✓ Successfully updated {updated_count} book descriptions")

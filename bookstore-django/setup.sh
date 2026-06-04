#!/bin/bash

echo "========================================"
echo " Django Bookstore Setup Script"
echo "========================================"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
echo "Virtual environment created!"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed!"
echo ""

# Run migrations
echo "Running database migrations..."
python manage.py migrate
echo "Migrations completed!"
echo ""

# Create superuser
echo ""
echo "Creating superuser account (Django admin)..."
echo "Please enter admin credentials:"
python manage.py createsuperuser
echo ""

# Optional: Load sample data
echo ""
read -p "Do you want to load sample book data? (y/n): " load_data
if [ "$load_data" = "y" ] || [ "$load_data" = "Y" ]; then
    python manage.py shell < load_books.py
    echo "Sample data loaded!"
else
    echo "Skipped loading sample data."
fi
echo ""

echo "========================================"
echo " Setup Complete!"
echo "========================================"
echo ""
echo "To start the server, run:"
echo "  python manage.py runserver"
echo ""
echo "Then visit:"
echo "  http://localhost:3000/api/"
echo "  http://localhost:3000/admin/"
echo ""

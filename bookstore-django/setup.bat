@echo off
echo ========================================
echo  Django Bookstore Setup Script
echo ========================================
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
echo Virtual environment created!
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt
echo Dependencies installed!
echo.

REM Run migrations
echo Running database migrations...
python manage.py migrate
echo Migrations completed!
echo.

REM Create superuser
echo.
echo Creating superuser account (Django admin)...
echo Please enter admin credentials:
python manage.py createsuperuser
echo.

REM Optional: Load sample data
echo.
set /p load_data="Do you want to load sample book data? (y/n): "
if /i "%load_data%"=="y" (
    python manage.py shell < load_books.py
    echo Sample data loaded!
) else (
    echo Skipped loading sample data.
)
echo.

echo ========================================
echo  Setup Complete!
echo ========================================
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then visit:
echo   http://localhost:3000/api/
echo   http://localhost:3000/admin/
echo.
pause

from pathlib import Path

files = [
    'README.md',
    'SETUP_GUIDE.md',
    'QUICK_REFERENCE.md',
    'INDEX.md',
    'setup.bat',
    'setup.sh',
    'DJANGO_VS_NEXTJS.md',
]

for filename in files:
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    new_text = text.replace('http://localhost:8000', 'http://localhost:3000')
    new_text = new_text.replace('127.0.0.1:8000', '127.0.0.1:3000')
    new_text = new_text.replace('Port 8000', 'Port 3000')
    new_text = new_text.replace('port 8000', 'port 3000')
    path.write_text(new_text, encoding='utf-8')

print('Updated docs')

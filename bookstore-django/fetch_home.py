import requests

try:
    r = requests.get('http://127.0.0.1:8000/')
    print('STATUS', r.status_code)
    text = r.text
    print(text[:3000])
except Exception as e:
    print('ERROR', e)

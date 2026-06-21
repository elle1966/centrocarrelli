import os
import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\transpallet.html'
try:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Look for grid items
    items = re.findall(r'<a[^>]*class=[\"\']flotta-item[\"\'][^>]*>.*?</a>', html, re.DOTALL)
    print(f'Found {len(items)} transpallet items in flotta-grid:')
    for item in items:
        clean_item = re.sub(r'\s+', ' ', item)
        print('  -', clean_item[:160] + '...')
except Exception as e:
    print('Error:', e)

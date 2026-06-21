import re
import os

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
try:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Search for all links with javascript:void(0)
    links = re.findall(r'<a[^>]*href=[\"\']javascript:void\(0\)[\"\'][^>]*>.*?</a>', html, re.DOTALL)
    print(f'Found {len(links)} links with javascript:void(0):')
    for idx, l in enumerate(links):
        clean_link = re.sub(r'\s+', ' ', l)
        print(f'  {idx+1}: {clean_link[:160]}...')
except Exception as e:
    print('Error:', e)

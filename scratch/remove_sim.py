from bs4 import BeautifulSoup
import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Remove simulator elements
for el_id in ['wp-simulator-btn', 'wp-simulator-sidebar', 'wp-toast-notification']:
    el = soup.find(id=el_id)
    if el:
        el.decompose()
        print(f'Rimosso: #{el_id}')

# Remove simulator scripts
for s in soup.find_all('script'):
    text = s.string or ''
    if 'toggleWpSimulator' in text or 'switchWpTab' in text:
        s.decompose()
        print('Rimosso: script simulatore')

# Remove simulator styles
for s in soup.find_all('style'):
    text = s.string or ''
    if 'wp-simulator' in text or 'simulator' in text.lower():
        s.decompose()
        print('Rimosso: style simulatore')

with open(path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Fatto! Simulatore rimosso da homepage.html')

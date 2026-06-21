import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove "Soluzione Consigliata" badges
html = re.sub(r'<span[^>]*class="[^"]*badge[^"]*"[^>]*>Soluzione Consigliata</span>', '', html, flags=re.IGNORECASE)
html = re.sub(r'<div[^>]*class="[^"]*badge[^"]*"[^>]*>Soluzione Consigliata</div>', '', html, flags=re.IGNORECASE)

# Remove "Noleggio da XX€/giorno" text
html = re.sub(r'Noleggio da \d+€/giorno', '', html)

# Also check in the JS PRODUCTS array for rental/badge properties
html = re.sub(r"rental:\s*'[^']*'", "rental: ''", html)
html = re.sub(r"badge:\s*'[^']*'", "badge: ''", html)
html = re.sub(r'rental:\s*"[^"]*"', 'rental: ""', html)
html = re.sub(r'badge:\s*"[^"]*"', 'badge: ""', html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Fatto!')
print('Soluzione Consigliata rimasti:', html.count('Soluzione Consigliata'))
print('Noleggio da rimasti:', html.count('Noleggio da'))

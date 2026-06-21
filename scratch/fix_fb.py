import re
path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all facebook references
for m in re.finditer(r'href="[^"]*facebook[^"]*"', html, re.IGNORECASE):
    print(m.group())

# Replace any facebook URL with the correct one
html = re.sub(r'href="https?://[^"]*facebook\.com[^"]*"', 'href="https://www.facebook.com/CentroCarrelli.net/"', html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\nFatto! Link Facebook aggiornati.")

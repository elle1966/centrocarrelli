import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all centrocarrelli.net links with relative paths
html = html.replace('href="https://www.centrocarrelli.net/', 'href="/')
html = html.replace("href='https://www.centrocarrelli.net/", "href='/")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

count = html.count('centrocarrelli.net')
print(f'Riferimenti centrocarrelli.net rimasti: {count}')

from bs4 import BeautifulSoup

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
with open(path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Extract header
header = soup.find('header')
if header:
    with open(r'C:\Users\elly\.antigravity\centrocarrelli\header_snippet.html', 'w', encoding='utf-8') as f:
        f.write(str(header))
    print(f'Header estratto: {len(str(header))} bytes')

# Extract footer
footer = soup.find('footer')
if footer:
    with open(r'C:\Users\elly\.antigravity\centrocarrelli\footer_snippet.html', 'w', encoding='utf-8') as f:
        f.write(str(footer))
    print(f'Footer estratto: {len(str(footer))} bytes')

# Extract the CSS link and fonts needed
print('\n--- CSS da includere nelle pagine interne ---')
print('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&family=IBM+Plex+Mono:wght@400;500&display=swap">')
print('<link rel="stylesheet" href="/style.css">')
print('<script src="https://unpkg.com/lucide@0.460.0"></script>')

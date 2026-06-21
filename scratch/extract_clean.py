from bs4 import BeautifulSoup
import re, os, json

# Read the deploy index.html
with open(r'C:\Users\elly\.antigravity\centrocarrelli\deploy\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
body = soup.body

# Remove simulator elements
for el_id in ['wp-simulator-btn', 'wp-simulator-sidebar', 'wp-toast-notification']:
    el = body.find(id=el_id)
    if el:
        el.decompose()

# Remove style tags
for s in body.find_all('style'):
    s.decompose()

# Remove scripts
for s in body.find_all('script'):
    src = s.get('src', '')
    if 'app.js' in src:
        s.decompose()
    elif s.text and ('toggleWpSimulator' in s.text or 'switchWpTab' in s.text):
        s.decompose()

# Replace base64 images with /assets/ paths based on alt text
for img in body.find_all('img'):
    src = img.get('src', '')
    if src.startswith('data:image'):
        alt = img.get('alt', '')
        if 'Centro Carrelli' in alt and '30' in alt:
            img['src'] = '/assets/logo_centrocarrelli.png'
        elif 'carrello elevatore' in alt.lower() or 'forklift' in alt.lower() or 'magazzino tecnologico' in alt.lower():
            img['src'] = '/assets/hero_forklift.png'
        elif 'ECH 12 C' in alt:
            img['src'] = '/assets/ech12c_still.jpg'
        elif 'ECH 15 C' in alt:
            img['src'] = '/assets/ech15c_still.jpg'
        elif 'EXH 14 C' in alt:
            img['src'] = '/assets/exh14c_transpallet.png'
        elif 'ECU 16' in alt:
            img['src'] = '/assets/ecu16_usato.jpg'
        elif 'assistenza' in alt.lower() or 'furgone' in alt.lower() or 'van' in alt.lower() or 'Centro Carrelli' in alt:
            img['src'] = '/assets/service_van.png'
        elif 'portata' in alt.lower() or 'residua' in alt.lower():
            img['src'] = '/assets/article_portata_residua.jpg'
        elif 'batterie' in alt.lower() or 'litio' in alt.lower():
            img['src'] = '/assets/article_batterie.jpg'
        elif 'usati' in alt.lower() or 'ricondizionat' in alt.lower():
            img['src'] = '/assets/article_usati.jpg'
        else:
            print(f'  UNMAPPED image with alt: {alt[:100]}')

# Re-extract body after modifications
html_body = ''.join(str(child) for child in body.children).strip()

# Clean up comments
html_body = re.sub(r'<!--\s*(WordPress|Oxygen|Simulator|Toast|Controller|Notification).*?-->', '', html_body, flags=re.IGNORECASE)

# Clean up multiple newlines
html_body = re.sub(r'\n\s*\n', '\n', html_body)
html_body = html_body.strip()

# Save clean body
output_path = r'C:\Users\elly\.antigravity\centrocarrelli\clean_body.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_body)

print(f'Done! clean_body.html created at {output_path}')
print(f'Remaining data:image count: {html_body.count("data:image")}')
print(f'File size: {len(html_body)} bytes')

# Now update the JS too
with open(r'C:\Users\elly\.antigravity\centrocarrelli\app.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace assets/ with /assets/ in JS
js_content = js_content.replace("'assets/", "'/assets/")
js_content = js_content.replace('"assets/', '"/assets/')

# Save clean JS
js_output = r'C:\Users\elly\.antigravity\centrocarrelli\clean_script.js'
with open(js_output, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f'Done! clean_script.js created at {js_output}')
print(f'Remaining assets/ (without /) in JS: {js_content.count("assets/") - js_content.count("/assets/")}')

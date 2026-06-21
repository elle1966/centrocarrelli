import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace ALL remaining base64 img src with /assets/ paths based on alt text
# Pattern: src="data:image/png;base64,..." or src="data:image/jpeg;base64,..."

def replace_base64_img(match):
    full = match.group(0)
    alt_match = re.search(r'alt="([^"]*)"', full)
    alt = alt_match.group(1) if alt_match else ''
    
    # Determine replacement path
    path = None
    if '30' in alt and 'Centro Carrelli' in alt:
        path = '/assets/logo_centrocarrelli.png'
    elif 'magazzino' in alt.lower() or 'carrello elevatore' in alt.lower():
        path = '/assets/hero_forklift.png'
    elif 'ECH 12' in alt:
        path = '/assets/ech12c_still.jpg'
    elif 'ECH 15' in alt:
        path = '/assets/ech15c_still.jpg'
    elif 'EXH 14' in alt:
        path = '/assets/exh14c_transpallet.png'
    elif 'ECU 16' in alt:
        path = '/assets/ecu16_usato.jpg'
    elif 'assistenza' in alt.lower() or 'furgone' in alt.lower() or 'sede' in alt.lower():
        path = '/assets/service_van.png'
    elif 'portata' in alt.lower() or 'residua' in alt.lower():
        path = '/assets/article_portata_residua.jpg'
    elif 'batterie' in alt.lower() or 'litio' in alt.lower():
        path = '/assets/article_batterie.jpg'
    elif 'usati' in alt.lower() or 'ricondizionat' in alt.lower():
        path = '/assets/article_usati.jpg'
    
    if path:
        return re.sub(r'src="data:image[^"]*"', f'src="{path}"', full)
    else:
        print(f'UNMAPPED: {alt[:80]}')
        return full

# Match <img ... src="data:image..." ... />
html = re.sub(r'<img[^>]*src="data:image[^"]*"[^>]*/>', replace_base64_img, html, flags=re.DOTALL)
html = re.sub(r'<img[^>]*src="data:image[^"]*"[^>]*>', replace_base64_img, html, flags=re.DOTALL)

# Also fix the 3 products that had assets/ without leading /
html = html.replace("'assets/hero_forklift.png'", "'/assets/hero_forklift.png'")
html = html.replace("'assets/", "'/assets/")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

remaining = html.count('data:image')
print(f'Fatto! Remaining data:image: {remaining}')
size_mb = len(html) / 1024 / 1024
print(f'File size: {size_mb:.1f} MB')

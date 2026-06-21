import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
try:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Print the exact matches of promo-card-btn links
    matches = re.findall(r'<a[^>]*class=[\"\']promo-card-btn[\"\'][^>]*>.*?</a>', html, re.DOTALL)
    for m in matches:
        clean_m = m.encode('ascii', 'replace').decode('ascii')
        print('Button matches in HTML:')
        print(repr(clean_m))
except Exception as e:
    print('Error:', e)

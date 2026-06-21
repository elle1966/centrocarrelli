from bs4 import BeautifulSoup
import re

with open(r'C:\Users\elly\.antigravity\centrocarrelli\clean_body.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find and remove inline scripts that contain PRODUCTS array (will use separate JS file)
removed = 0
for script in soup.find_all('script'):
    if script.string and 'PRODUCTS' in script.string:
        script.decompose()
        removed += 1
        print('Removed inline script containing PRODUCTS array')
    elif script.string and ('initNavigation' in script.string or 'initForkliftFinder' in script.string):
        script.decompose()
        removed += 1
        print('Removed inline script containing app logic')

print(f'Total scripts removed: {removed}')

# Re-extract
html_body = ''.join(str(child) for child in soup.body.children).strip() if soup.body else ''.join(str(child) for child in soup.children).strip()

# Clean up multiple newlines
html_body = re.sub(r'\n\s*\n', '\n', html_body)
html_body = html_body.strip()

with open(r'C:\Users\elly\.antigravity\centrocarrelli\clean_body.html', 'w', encoding='utf-8') as f:
    f.write(html_body)

print(f'Updated clean_body.html')
print(f'Remaining data:image count: {html_body.count("data:image")}')
print(f'File size: {len(html_body)} bytes')

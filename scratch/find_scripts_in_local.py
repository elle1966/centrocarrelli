with open(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
matches = re.findall(r'<script[^>]*>', html)
for m in matches:
    print(m)

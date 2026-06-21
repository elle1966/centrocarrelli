import re
path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()
for m in re.finditer(r'centrocarrelli\.net', html):
    start = max(0, m.start() - 80)
    end = min(len(html), m.end() + 20)
    print(html[start:end].strip())
    print('---')

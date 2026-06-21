path = r'c:\Users\elly\.antigravity\centrocarrelli\index.html'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

idx = content.find('class="nav-logo"')
if idx != -1:
    print(content[idx:idx+800])
else:
    print("nav-logo not found")

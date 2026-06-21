files = [
    r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html',
    r'C:\Users\elly\Local Sites\centrocarrelli\app\public\azienda.html',
    r'C:\Users\elly\Local Sites\centrocarrelli\app\public\wp-content\mu-plugins\cc-homepage.php',
]

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('href="index.html"', 'href="/"')
    html = html.replace("href='index.html'", "href='/'")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'{path.split(chr(92))[-1]}: index.html rimasti = {html.count("index.html")}')

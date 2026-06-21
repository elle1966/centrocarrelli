import re

files = [
    r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html',
    r'C:\Users\elly\Local Sites\centrocarrelli\app\public\azienda.html',
    r'C:\Users\elly\Local Sites\centrocarrelli\app\public\wp-content\mu-plugins\cc-homepage.php',
]

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove Home nav item in various formats
    html = re.sub(r'<li class="nav-item"><a href="/">Home</a></li>\s*', '', html)
    html = re.sub(r"<li class=\"nav-item\"><a href=\"/\">Home</a></li>\s*", '', html)
    # Also from JS string concatenation in mu-plugin
    html = re.sub(r"'<a href=\"/\" style=\"[^\"]*\">Home</a>' \+\s*", '', html)
    html = re.sub(r"'<li class=\"nav-item\"><a href=\"/\" style=\"[^\"]*\">Home</a></li>' \+\s*", '', html)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    count = html.count('>Home<')
    print(f'{path.split(chr(92))[-1]}: "Home" rimasti = {count}')

import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
try:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Look for header links
    nav_blocks = re.findall(r'<header[^>]*>.*?</header>', html, re.DOTALL)
    if nav_blocks:
        print('Header blocks found in homepage.html:')
        for nav_block in nav_blocks:
            links = re.findall(r'<a[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', nav_block, re.DOTALL)
            for l in links:
                print(f"  Header link -> text: {re.sub('<[^>]+>', '', l[1]).strip()}, href: {l[0]}")
    else:
        print('Header tag not found, searching for general links inside <nav>...')
        navs = re.findall(r'<nav[^>]*>.*?</nav>', html, re.DOTALL)
        for nav in navs:
            links = re.findall(r'<a[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', nav, re.DOTALL)
            for l in links:
                print(f"  Nav link -> text: {re.sub('<[^>]+>', '', l[1]).strip()}, href: {l[0]}")

    # Inspect footer links
    footers = re.findall(r'<footer[^>]*>.*?</footer>', html, re.DOTALL)
    if footers:
        print('Footer blocks found in homepage.html:')
        for footer in footers:
            links = re.findall(r'<a[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', footer, re.DOTALL)
            for l in links:
                print(f"  Footer link -> text: {re.sub('<[^>]+>', '', l[1]).strip()}, href: {l[0]}")
except Exception as e:
    print('Error:', e)

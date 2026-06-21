import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find PRODUCTS array
    match = re.search(r'const PRODUCTS\s*=\s*\[(.*?)\];', content, re.DOTALL)
    if match:
        products_block = match.group(1)
        names = re.findall(r'name:\s*[\'\"](.*?)[\'\"]', products_block)
        print('Products in homepage.html:')
        for name in names:
            print(f' - {name}')
    else:
        print('PRODUCTS array not found')
except Exception as e:
    print('Error:', e)

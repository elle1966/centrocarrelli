import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
try:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Find PRODUCTS block
    match = re.search(r'const PRODUCTS\s*=\s*\[(.*?)\];', html, re.DOTALL)
    if match:
        products_block = match.group(1)
        # Find objects inside array
        obj_matches = re.findall(r'\{(.*?)\}', products_block, re.DOTALL)
        print(f'Found {len(obj_matches)} products in PRODUCTS array:')
        for idx, obj in enumerate(obj_matches):
            name_match = re.search(r'name:\s*[\'\"]([^\'\"]+)[\"\']', obj)
            link_match = re.search(r'link:\s*[\'\"]([^\'\"]+)[\"\']', obj)
            name = name_match.group(1) if name_match else 'Unknown'
            link = link_match.group(1) if link_match else 'None'
            print(f'  Product {idx+1} -> Name: {name}, Link: {link}')
    else:
        print('PRODUCTS array not found in homepage.html')
except Exception as e:
    print('Error:', e)

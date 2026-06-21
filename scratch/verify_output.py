import os
import re

def verify():
    wp_path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public'
    
    print('=== VERIFYING transpallet.html ===')
    t_path = os.path.join(wp_path, 'transpallet.html')
    if os.path.exists(t_path):
        with open(t_path, 'r', encoding='utf-8') as f:
            t_html = f.read()
        
        # Look for grid items
        items = re.findall(r'<a[^>]*class=\"flotta-item\"[^>]*>.*?</a>', t_html, re.DOTALL)
        if not items:
            items = re.findall(r'<a[^>]*class=[\"\']flotta-item[\"\'][^>]*>.*?</a>', t_html, re.DOTALL)
            
        print(f'Found {len(items)} linked items in flotta-grid:')
        for item in items:
            clean_item = re.sub(r'\s+', ' ', item)
            print('  -', clean_item[:160] + '...')
    else:
        print('Error: transpallet.html not found at', t_path)

    print('\n=== VERIFYING carrelli-frontali.html ===')
    f_path = os.path.join(wp_path, 'carrelli-frontali.html')
    if os.path.exists(f_path):
        with open(f_path, 'r', encoding='utf-8') as f:
            f_html = f.read()
            
        # Find all flotta-items
        items = re.findall(r'<div[^>]*class=\"flotta-item\"[^>]*>.*?</div>', f_html, re.DOTALL)
        if not items:
            items = re.findall(r'<div[^>]*class=[\"\']flotta-item[\"\'][^>]*>.*?</div>', f_html, re.DOTALL)
            
        print(f'Found {len(items)} items in flotta-grid:')
        for item in items:
            clean_item = re.sub(r'\s+', ' ', item)
            print('  -', clean_item[:160] + '...')
            
        # Let's verify that the 3.5t is not in f_html
        if '3.5 t' in f_html:
            print('WARNING: 3.5 t is still in the file!')
        else:
            print('Success: 3.5 t forklift was successfully removed.')
    else:
        print('Error: carrelli-frontali.html not found at', f_path)

if __name__ == '__main__':
    verify()

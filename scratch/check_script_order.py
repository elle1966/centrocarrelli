import os
import re

wp_path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public'
files = ['homepage.html', 'transpallet.html', 'carrelli-frontali.html']
for fn in files:
    path = os.path.join(wp_path, fn)
    if os.path.exists(path):
        print(f'=== {fn} ===')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find index of Lucide script src tag
        src_idx = content.find('https://unpkg.com/lucide')
        # Find index of lucide.createIcons
        call_idx = content.find('lucide.createIcons')
        
        print(f'  Lucide src tag index: {src_idx}')
        print(f'  lucide.createIcons call index: {call_idx}')
        if src_idx < call_idx:
            print('  Status: Correct (Library loaded before call)')
        else:
            print('  Status: ERROR (Library loaded AFTER call)')

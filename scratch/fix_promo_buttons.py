import os

def fix_promo_buttons(filepath):
    if not os.path.exists(filepath):
        print(f'File not found: {filepath}')
        return
        
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        replacements = {
            'href="javascript:void(0)" onclick="openProductModal(\'ech12c\')">Info': 'href="/ech12c.html">Info',
            'href="javascript:void(0)" onclick="openProductModal(\'ech15c\')">Info': 'href="/ech15c.html">Info',
            'href="javascript:void(0)" onclick="openProductModal(\'exh14c\')">Info': 'href="/exh14c.html">Info',
            'href="javascript:void(0)" onclick="openProductModal(\'ecu16\')">Info': 'href="/ecu16.html">Info',
            # Just in case there are single quotes on attributes
            'href=\'javascript:void(0)\' onclick=\'openProductModal(\"ech12c\")\'>Info': 'href="/ech12c.html">Info',
            'href=\'javascript:void(0)\' onclick=\'openProductModal(\"ech15c\")\'>Info': 'href="/ech15c.html">Info',
            'href=\'javascript:void(0)\' onclick=\'openProductModal(\"exh14c\")\'>Info': 'href="/exh14c.html">Info',
            'href=\'javascript:void(0)\' onclick=\'openProductModal(\"ecu16\")\'>Info': 'href="/ecu16.html">Info'
        }
        
        modified = False
        for target, replacement in replacements.items():
            if target in content:
                content = content.replace(target, replacement)
                modified = True
                
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Successfully updated promo buttons in: {filepath}')
        else:
            print(f'No promo buttons found or already updated in: {filepath}')
    except Exception as e:
        print(f'Error processing {filepath}: {e}')

if __name__ == '__main__':
    # Local site homepage
    fix_promo_buttons(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html')
    
    # Workspace files
    fix_promo_buttons(r'clean_body.html')
    fix_promo_buttons(r'centro2026/index.html')

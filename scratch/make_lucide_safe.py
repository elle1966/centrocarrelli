import os

def make_lucide_safe(directory):
    for root, dirs, files in os.walk(directory):
        # Skip cache directories to avoid rewriting files inside cache
        if 'cache' in root.lower() or '.git' in root.lower() or 'node_modules' in root.lower():
            continue
        for f in files:
            if f.endswith(('.html', '.js')):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()
                    
                    target = 'lucide.createIcons()'
                    safe_replacement = 'if (typeof lucide !== \'undefined\') { lucide.createIcons(); }'
                    
                    if target in content:
                        # Replace only if it is not already wrapped
                        # Simple check: make sure we don't double replace
                        if 'typeof lucide' not in content:
                            new_content = content.replace(target, safe_replacement)
                            with open(path, 'w', encoding='utf-8') as file:
                                file.write(new_content)
                            print(f'Made lucide safe in: {path}')
                except Exception as e:
                    print(f'Error processing {path}: {e}')

if __name__ == '__main__':
    # Clean workspace
    print('Processing workspace...')
    make_lucide_safe('.')
    
    # Clean local site
    wp_path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public'
    if os.path.exists(wp_path):
        print(f'Processing local site at {wp_path}...')
        make_lucide_safe(wp_path)
    else:
        print('Local site path not found.')

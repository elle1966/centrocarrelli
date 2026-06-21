import re
import os

def find_logo_in_html(directory):
    for root, dirs, files in os.walk(directory):
        if any(skip in root for skip in ['.git', '.netlify', 'node_modules', '.agents']):
            continue
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Find the nav-logo block
                idx = content.find('class="nav-logo"')
                if idx != -1:
                    print(f"File: {path}")
                    # Print 300 chars after nav-logo
                    print(content[idx:idx+400])
                    print("-" * 50)

if __name__ == '__main__':
    find_logo_in_html(r'c:\Users\elly\.antigravity\centrocarrelli')

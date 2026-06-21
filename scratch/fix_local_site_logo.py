import os
import re

def update_html_php_files(directory):
    print("Updating logo height in HTML/PHP files...")
    logo_pattern = re.compile(r'(<img[^>]*logo_centrocarrelli[^>]*>)', re.IGNORECASE)
    
    for root, dirs, files in os.walk(directory):
        if any(skip in root for skip in ['.git', '.netlify', 'node_modules', '.agents']):
            continue
        for file in files:
            if file.endswith(('.html', '.php')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    matches = logo_pattern.findall(content)
                    if not matches:
                        continue
                    
                    new_content = content
                    for match in matches:
                        # Replace style height to 45px
                        new_match = match
                        if 'style=' in match:
                            new_match = re.sub(r'height:\s*\d+px', 'height: 45px', new_match)
                        else:
                            new_match = new_match.replace('<img', '<img style="height: 45px; width: auto;"')
                        
                        new_content = new_content.replace(match, new_match)
                    
                    if new_content != content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"  Updated: {file}")
                except Exception as e:
                    print(f"  Error updating {file}: {e}")

def update_css_file(css_path):
    print(f"Updating CSS file: {css_path}")
    try:
        with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
            css = f.read()
        
        css_rule = """
.nav-logo img {
    height: 45px !important;
    width: auto !important;
    display: block;
}
"""
        # Let's check if the rule is already there
        if '.nav-logo img' not in css:
            # Let's append it or insert it after .nav-logo
            idx = css.find('.nav-logo {')
            if idx != -1:
                # Find end of .nav-logo block
                end_idx = css.find('}', idx)
                if end_idx != -1:
                    css = css[:end_idx+1] + css_rule + css[end_idx+1:]
                    print("  Inserted .nav-logo img rule in CSS.")
            else:
                css += css_rule
                print("  Appended .nav-logo img rule to CSS.")
            
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css)
        else:
            # Let's update it if height is different
            css = re.sub(r'\.nav-logo img\s*\{[^}]*\}', css_rule.strip(), css)
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css)
            print("  Updated existing .nav-logo img rule in CSS.")
            
    except Exception as e:
        print(f"  Error updating CSS: {e}")

if __name__ == '__main__':
    public_dir = r'C:\Users\elly\Local Sites\centrocarrelli\app\public'
    update_html_php_files(public_dir)
    update_css_file(os.path.join(public_dir, 'style.css'))

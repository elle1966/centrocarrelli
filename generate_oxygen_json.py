import json
import re
import os
from bs4 import BeautifulSoup

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    html_path = os.path.join(current_dir, "centro2026", "index.html")
    css_path = os.path.join(current_dir, "style.css")
    js_path = os.path.join(current_dir, "app.js")
    output_path = os.path.join(current_dir, "oxygen_page_import.json")
    
    # Read files
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()
        
    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read()
        
    # Parse with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    body = soup.body
    
    # Remove WordPress simulator elements
    wp_elements = [
        body.find(id="wp-simulator-btn"),
        body.find(id="wp-simulator-sidebar"),
        body.find(id="wp-toast-notification")
    ]
    for el in wp_elements:
        if el:
            el.decompose()
            
    # Remove any <style> tags in the body (CSS should be in the CSS editor/file, not mixed in HTML)
    for s in body.find_all('style'):
        s.decompose()
            
    # Remove scripts related to simulator or app.js
    for s in body.find_all('script'):
        src = s.get('src', '')
        if 'app.js' in src:
            s.decompose()
        elif s.text and ('toggleWpSimulator' in s.text or 'switchWpTab' in s.text):
            s.decompose()
            
    # Get clean HTML string (only the inner contents of <body>)
    # We join the string representation of all children of the body
    html_body = "".join(str(child) for child in body.children).strip()
    
    # Remove leftover WordPress/Simulator comments and raw text blocks
    html_body = re.sub(r'<!--\s*(WordPress|Oxygen|Simulator|Toast|Controller|Notification).*?-->', '', html_body, flags=re.IGNORECASE)
    patterns_to_remove = [
        r'WordPress / Oxygen Simulator Styles',
        r'WordPress / Oxygen Simulator Panel',
        r'Notification Toast',
        r'WordPress Customizer JS Controller'
    ]
    for pattern in patterns_to_remove:
        html_body = re.sub(pattern, '', html_body, flags=re.IGNORECASE)
        
    # Apply WordPress Media URL replacements
    url_mapping = {
        "assets/": "/assets/"
    }
    
    for relative_path, wp_url in url_mapping.items():
        html_body = html_body.replace(relative_path, wp_url)
        js_content = js_content.replace(relative_path, wp_url)
        
    # Remove empty lines or multiple consecutive newlines
    html_body = re.sub(r'\n\s*\n', '\n', html_body)
    html_body = html_body.strip()
    
    # Oxygen JSON structure for importing a Code Block
    oxygen_json = [
        {
            "name": "ct_code_block",
            "options": {
                "original": {
                    "code-php": html_body,
                    "code-css": css_content,
                    "code-js": js_content
                }
            }
        }
    ]
    
    # Save as JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(oxygen_json, f, indent=2, ensure_ascii=False)
        
    # Save clean HTML body to a separate file
    html_output_path = os.path.join(current_dir, "clean_body.html")
    with open(html_output_path, "w", encoding="utf-8") as f:
        f.write(html_body)
        
    print(f"Oxygen Builder JSON successfully created at: {output_path}")
    print(f"Clean HTML body successfully created at: {html_output_path}")

if __name__ == "__main__":
    main()


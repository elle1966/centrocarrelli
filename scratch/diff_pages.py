import os
import difflib
import re

def clean_html(content):
    # Remove script tags
    content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    # Remove style tags
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    # Remove head/meta tags
    content = re.sub(r'<head.*?>.*?</head>', '', content, flags=re.DOTALL | re.IGNORECASE)
    # Normalise whitespace
    content = re.sub(r'\s+', ' ', content)
    # Re-align tags slightly for diffing
    content = content.replace('>', '>\n').replace('<', '\n<')
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    return lines

def main():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bozza_path = os.path.join(current_dir, "centrocarrelli_bozza_2026", "index.html")
    root_path = os.path.join(current_dir, "index.html")
    
    with open(bozza_path, "r", encoding="utf-8") as f:
        bozza_content = f.read()
        
    with open(root_path, "r", encoding="utf-8") as f:
        root_content = f.read()
        
    # Extract body content
    body_bozza = re.search(r"<body[^>]*>(.*?)</body>", bozza_content, re.DOTALL | re.IGNORECASE).group(1)
    body_root = re.search(r"<body[^>]*>(.*?)</body>", root_content, re.DOTALL | re.IGNORECASE).group(1)
    
    # Clean base64 in root
    base64_pattern = r'data:image/[^;]+;base64,[^"\']+'
    body_root = re.sub(base64_pattern, 'PLACEHOLDER_BASE64', body_root)
    
    lines_bozza = clean_html(body_bozza)
    lines_root = clean_html(body_root)
    
    diff = difflib.unified_diff(lines_bozza, lines_root, fromfile='Bozza', tofile='Root', n=3)
    
    diff_output = '\n'.join(diff)
    print(f"Diff length: {len(diff_output)}")
    
    with open(os.path.join(current_dir, "scratch", "body_diff.txt"), "w", encoding="utf-8") as f:
        f.write(diff_output)
        
    print("Diff saved to scratch/body_diff.txt")

if __name__ == "__main__":
    main()

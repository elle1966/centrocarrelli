import os
import re
from bs4 import BeautifulSoup
import difflib

def compare_bodies():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bozza_path = os.path.join(current_dir, "centrocarrelli_bozza_2026", "index.html")
    root_path = os.path.join(current_dir, "index.html")
    
    with open(bozza_path, "r", encoding="utf-8") as f:
        bozza_soup = BeautifulSoup(f.read(), "html.parser")
        
    with open(root_path, "r", encoding="utf-8") as f:
        root_soup = BeautifulSoup(f.read(), "html.parser")
        
    # Get body contents
    bozza_body = bozza_soup.body
    root_body = root_soup.body
    
    # Strip base64 from root body img src
    for img in root_body.find_all('img'):
        src = img.get('src', '')
        if src.startswith('data:image'):
            img['src'] = 'PLACEHOLDER_BASE64'
            
    # Also strip base64 from bozza body img src (just in case)
    for img in bozza_body.find_all('img'):
        src = img.get('src', '')
        if src.startswith('data:image'):
            img['src'] = 'PLACEHOLDER_BASE64'
            
    # Format and compare
    bozza_formatted = bozza_body.prettify()
    root_formatted = root_body.prettify()
    
    # Remove empty lines
    bozza_lines = [line.strip() for line in bozza_formatted.split('\n') if line.strip()]
    root_lines = [line.strip() for line in root_formatted.split('\n') if line.strip()]
    
    print(f"Bozza body lines: {len(bozza_lines)}")
    print(f"Root body lines: {len(root_lines)}")
    
    diff = list(difflib.unified_diff(bozza_lines, root_lines, fromfile='Bozza', tofile='Root', n=1))
    
    # Print the first 50 lines of diff
    print("\nFirst 50 lines of unified diff between Bozza and Root Body:")
    for line in diff[:100]:
        print(line)

if __name__ == "__main__":
    compare_bodies()

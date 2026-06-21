import os
from bs4 import BeautifulSoup

def compare_styles():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bozza_path = os.path.join(current_dir, "centrocarrelli_bozza_2026", "index.html")
    root_path = os.path.join(current_dir, "index.html")
    css_path = os.path.join(current_dir, "style.css")
    
    with open(bozza_path, "r", encoding="utf-8") as f:
        bozza_soup = BeautifulSoup(f.read(), "html.parser")
        
    with open(root_path, "r", encoding="utf-8") as f:
        root_soup = BeautifulSoup(f.read(), "html.parser")
        
    with open(css_path, "r", encoding="utf-8") as f:
        css_text = f.read()
        
    bozza_styles = bozza_soup.find_all('style')
    root_styles = root_soup.find_all('style')
    
    print(f"Global style.css length: {len(css_text)}")
    print(f"Bozza inline styles: {len(bozza_styles)}")
    for idx, s in enumerate(bozza_styles):
        print(f"  Bozza style {idx} length: {len(s.text)}")
        print(f"  Start: {s.text[:100].strip()}...")
        
    print(f"Root inline styles: {len(root_styles)}")
    for idx, s in enumerate(root_styles):
        print(f"  Root style {idx} length: {len(s.text)}")
        print(f"  Start: {s.text[:100].strip()}...")

if __name__ == "__main__":
    compare_styles()

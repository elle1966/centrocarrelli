import os
import re
from bs4 import BeautifulSoup

def analyze():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bozza_path = os.path.join(current_dir, "centrocarrelli_bozza_2026", "index.html")
    root_path = os.path.join(current_dir, "index.html")
    
    with open(bozza_path, "r", encoding="utf-8") as f:
        bozza_soup = BeautifulSoup(f.read(), "html.parser")
        
    with open(root_path, "r", encoding="utf-8") as f:
        root_soup = BeautifulSoup(f.read(), "html.parser")
        
    # Analyze sections
    bozza_sections = [s.get('id') or s.get('class') for s in bozza_soup.find_all(['section', 'header', 'footer'])]
    root_sections = [s.get('id') or s.get('class') for s in root_soup.find_all(['section', 'header', 'footer'])]
    
    print("Bozza major elements:", bozza_sections)
    print("Root major elements:", root_sections)
    
    # Check elements by ID
    bozza_ids = {el.get('id'): el for el in bozza_soup.find_all(id=True)}
    root_ids = {el.get('id'): el for el in root_soup.find_all(id=True)}
    
    print("\nIDs in Bozza but not in Root:")
    for id_ in bozza_ids:
        if id_ not in root_ids:
            print(f"  - #{id_} ({bozza_ids[id_].name})")
            
    print("\nIDs in Root but not in Bozza:")
    for id_ in root_ids:
        if id_ not in bozza_ids:
            print(f"  - #{id_} ({root_ids[id_].name})")
            
    # Check sections content differences
    print("\nComparing sections by ID:")
    for id_ in sorted(set(bozza_ids.keys()) & set(root_ids.keys())):
        bozza_text = ' '.join(bozza_ids[id_].stripped_strings)
        root_text = ' '.join(root_ids[id_].stripped_strings)
        
        # Clean base64 in root text comparison
        root_text = re.sub(r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+', '', root_text)
        
        if len(bozza_text) != len(root_text):
            print(f"  - #{id_} text length mismatch: Bozza={len(bozza_text)}, Root={len(root_text)}")
            if len(bozza_text) < 500:
                print(f"    Bozza: {bozza_text[:100]}...")
                print(f"    Root : {root_text[:100]}...")

if __name__ == "__main__":
    analyze()

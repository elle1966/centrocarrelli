import os
from bs4 import BeautifulSoup

def find_styles():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bozza_path = os.path.join(current_dir, "centrocarrelli_bozza_2026", "index.html")
    root_path = os.path.join(current_dir, "index.html")
    
    with open(bozza_path, "r", encoding="utf-8") as f:
        bozza_soup = BeautifulSoup(f.read(), "html.parser")
        
    with open(root_path, "r", encoding="utf-8") as f:
        root_soup = BeautifulSoup(f.read(), "html.parser")
        
    print("Bozza styles count:", len(bozza_soup.find_all('style')))
    for idx, s in enumerate(bozza_soup.find_all('style')):
        print(f"Bozza style {idx} length: {len(s.text)}")
        
    print("\nRoot styles count:", len(root_soup.find_all('style')))
    for idx, s in enumerate(root_soup.find_all('style')):
        print(f"Root style {idx} length: {len(s.text)}")
        
    print("\nBozza scripts count:", len(bozza_soup.find_all('script')))
    for idx, s in enumerate(bozza_soup.find_all('script')):
        src = s.get('src')
        if src:
            print(f"Bozza script {idx} (external src={src})")
        else:
            print(f"Bozza script {idx} (inline) length: {len(s.text)}")
            
    print("\nRoot scripts count:", len(root_soup.find_all('script')))
    for idx, s in enumerate(root_soup.find_all('script')):
        src = s.get('src')
        if src:
            print(f"Root script {idx} (external src={src})")
        else:
            print(f"Root script {idx} (inline) length: {len(s.text)}")

if __name__ == "__main__":
    find_styles()

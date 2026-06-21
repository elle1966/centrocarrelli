import os
from bs4 import BeautifulSoup

def inspect_script():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_path = os.path.join(current_dir, "index.html")
    
    with open(root_path, "r", encoding="utf-8") as f:
        root_soup = BeautifulSoup(f.read(), "html.parser")
        
    scripts = root_soup.find_all('script')
    large_script = scripts[1]
    
    print(f"Large script length: {len(large_script.text)}")
    print("Start of script:")
    print(large_script.text[:200])
    print("\nEnd of script:")
    print(large_script.text[-200:])

if __name__ == "__main__":
    inspect_script()

import os
import re
from bs4 import BeautifulSoup

def find_large_lines():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_path = os.path.join(current_dir, "index.html")
    
    with open(root_path, "r", encoding="utf-8") as f:
        root_soup = BeautifulSoup(f.read(), "html.parser")
        
    scripts = root_soup.find_all('script')
    large_script = scripts[1].text
    
    lines = large_script.split('\n')
    print(f"Total lines in script: {len(lines)}")
    
    for idx, line in enumerate(lines):
        if len(line) > 1000:
            print(f"Line {idx} length: {len(line)}")
            print(f"Line starts with: {line[:100]}...")
            print(f"Line ends with: {line[-100:]}...")

if __name__ == "__main__":
    find_large_lines()

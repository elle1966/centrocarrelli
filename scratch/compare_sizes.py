import os
import re

def compare_sizes():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bozza_path = os.path.join(current_dir, "centrocarrelli_bozza_2026", "index.html")
    root_path = os.path.join(current_dir, "index.html")
    
    with open(bozza_path, "r", encoding="utf-8") as f:
        bozza_content = f.read()
        
    with open(root_path, "r", encoding="utf-8") as f:
        root_content = f.read()
        
    # Strip base64
    root_clean = re.sub(r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+', '', root_content)
    
    print(f"Bozza content length: {len(bozza_content)}")
    print(f"Root content length (clean): {len(root_clean)}")
    
    # Are they exactly the same clean content?
    # Let's strip whitespace and compare
    bozza_ws = re.sub(r'\s+', '', bozza_content)
    root_ws = re.sub(r'\s+', '', root_clean)
    
    print(f"Bozza whitespace-stripped length: {len(bozza_ws)}")
    print(f"Root whitespace-stripped length: {len(root_ws)}")
    
    if bozza_ws == root_ws:
        print("They are EXACTLY the same except for base64 images and whitespace!")
    else:
        print("They are DIFFERENT!")
        # Let's find first difference
        min_len = min(len(bozza_ws), len(root_ws))
        for i in range(min_len):
            if bozza_ws[i] != root_ws[i]:
                print(f"First diff at char {i}:")
                print(f"Bozza: {bozza_ws[max(0, i-20):i+50]}")
                print(f"Root : {root_ws[max(0, i-20):i+50]}")
                break

if __name__ == "__main__":
    compare_sizes()

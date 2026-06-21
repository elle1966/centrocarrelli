import json
import os

def check_js_paths():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(current_dir, "oxygen_page_import.json")
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    js_code = data[0]['options']['original']['code-js']
    print("Is 'https://centrocarrelli.local/' in JS code?", 'https://centrocarrelli.local/' in js_code)
    
    # Print some product definitions in the JS
    lines = js_code.split('\n')
    for idx, line in enumerate(lines):
        if 'image:' in line:
            print(f"  Line {idx}: {line.strip()}")

if __name__ == "__main__":
    check_js_paths()

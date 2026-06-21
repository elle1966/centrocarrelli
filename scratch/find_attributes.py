import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\elly\.antigravity\centrocarrelli\scratch\extracted_docx_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Split by FILE:
files_data = re.split(r'=========================================\s*FILE:', text)
for fd in files_data:
    if not fd.strip():
        continue
    lines = fd.split('\n')
    filename = lines[0].strip()
    content = "\n".join(lines[1:])
    print(f"\n=========================================")
    print(f"FILE: {filename}")
    print(f"=========================================")
    
    # Let's check if the content contains mentions of products or specifications
    lines_content = content.split('\n')
    for line in lines_content:
        if any(keyword in line.lower() for keyword in ["portata", "altezza", "alimentazione", "tipo di", "baricentro", "specifiche", "caratteristiche", "finder", "filtro", "filtri"]):
            print(line.strip())

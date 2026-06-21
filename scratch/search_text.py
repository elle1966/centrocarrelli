with open(r'c:\Users\elly\.antigravity\centrocarrelli\scratch\extracted_docx_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Split by FILE:
files_data = re.split(r'=========================================\s*FILE:', text)
for fd in files_data:
    if not fd.strip():
        continue
    lines = fd.split('\n')
    filename = lines[0]
    content = "\n".join(lines[1:])
    print(f"File: {filename}")
    print(f"Content length: {len(content)}")
    print("Preview first 500 chars:")
    print(content[:500])
    print("-" * 50)

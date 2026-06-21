with open(r'c:\Users\elly\.antigravity\centrocarrelli\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.finditer(r'\bimg\b', content)
for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 200)
    print(f"Match for 'img' at position {m.start()}:")
    print(content[start:end])
    print("-" * 50)

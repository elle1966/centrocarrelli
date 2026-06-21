import re

with open(r'C:\Users\elly\.antigravity\centrocarrelli\clean_body.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find all data:image occurrences and surrounding context
for m in re.finditer(r'data:image', html):
    start = max(0, m.start() - 300)
    context = html[start:m.start()]
    # find the last alt= before this
    alt_match = re.findall(r'alt="([^"]*)"', context)
    if alt_match:
        print('ALT:', alt_match[-1][:120])
    else:
        # Look for class or other context
        cls_match = re.findall(r'class="([^"]*)"', context)
        if cls_match:
            print('CLASS:', cls_match[-1][:100])
        else:
            print('Context:', context[-120:])
    print()

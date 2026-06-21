with open(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove ALL remaining references
html = html.replace('initScrollAnimations', '// removed')

# Also check for any opacity:0 in style attributes on sections
import re
# Remove style="opacity: 0" from any section tags
html = re.sub(r'style="[^"]*opacity:\s*0[^"]*"', '', html)

with open(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Final check
print('opacity: 0 count:', html.count('opacity: 0'))
print('opacity:0 count:', html.count('opacity:0'))
print('initScrollAnimations count:', html.count('initScrollAnimations'))
print('reveal-section count:', html.count('reveal-section'))

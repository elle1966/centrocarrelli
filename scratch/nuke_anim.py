with open(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the entire initScrollAnimations function and its call
import re

# Remove the function definition
html = re.sub(
    r'function\s+initScrollAnimations\s*\(\)\s*\{.*?\n\}',
    '// scroll animations removed',
    html,
    flags=re.DOTALL
)

# Remove the call to it
html = html.replace('initScrollAnimations();', '// initScrollAnimations disabled')

# Also force all animate-on-scroll elements to be visible via inline style tag
html = html.replace('</head>', '''<style>
.animate-on-scroll, .reveal-section, section {
    opacity: 1 !important;
    transform: none !important;
}
</style>
</head>''')

with open(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Fatto! Animazioni scroll rimosse completamente.')
print('initScrollAnimations count:', html.count('initScrollAnimations'))

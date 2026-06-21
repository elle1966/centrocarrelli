import re

files = [
    r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html',
    r'C:\Users\elly\Local Sites\centrocarrelli\app\public\azienda.html',
]

new_footer_links = '''<ul class="footer-links">
<li><a href="/news/">News</a></li>
<li><a href="/newsletter/">Newsletter</a></li>
<li><a href="/privacy-policy/">Privacy</a></li>
<li><a href="/mappa-sito/">Mappa sito</a></li>
<li><a href="/cookie-policy/">Cookie</a></li>
<li><a href="/contatti/">Contatti</a></li>
<li><a href="/lavora-con-noi/">Lavora con noi</a></li>
</ul>'''

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(
        r'<ul class="footer-links">.*?</ul>',
        new_footer_links,
        html,
        flags=re.DOTALL
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{path.split(chr(92))[-1]}: footer aggiornato')

# Fix mu-plugin footer (JS version)
path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\wp-content\mu-plugins\cc-homepage.php'
with open(path, 'r', encoding='utf-8') as f:
    php = f.read()

old_footer_links = """'<a href="/privacy-policy/" style="color:rgba(255,255,255,0.6);">Privacy Policy</a>' +
            '<a href="/cookie-policy/" style="color:rgba(255,255,255,0.6);">Cookie Policy</a>' +
            '<a href="/contatti/" style="color:rgba(255,255,255,0.6);">Contatti</a>'"""

new_footer_links_js = """'<a href="/news/" style="color:rgba(255,255,255,0.6);">News</a>' +
            '<a href="/newsletter/" style="color:rgba(255,255,255,0.6);">Newsletter</a>' +
            '<a href="/privacy-policy/" style="color:rgba(255,255,255,0.6);">Privacy</a>' +
            '<a href="/mappa-sito/" style="color:rgba(255,255,255,0.6);">Mappa sito</a>' +
            '<a href="/cookie-policy/" style="color:rgba(255,255,255,0.6);">Cookie</a>' +
            '<a href="/contatti/" style="color:rgba(255,255,255,0.6);">Contatti</a>' +
            '<a href="/lavora-con-noi/" style="color:rgba(255,255,255,0.6);">Lavora con noi</a>'"""

php = php.replace(old_footer_links, new_footer_links_js)

with open(path, 'w', encoding='utf-8') as f:
    f.write(php)
print('cc-homepage.php: footer aggiornato')

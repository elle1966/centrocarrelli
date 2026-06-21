path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove any remaining "Soluzione Consigliata" text
html = html.replace('Soluzione Consigliata', '')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Soluzione Consigliata rimasti: {html.count("Soluzione Consigliata")}')
print(f'Noleggio da rimasti: {html.count("Noleggio da")}')

with open(r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html', 'r', encoding='utf-8') as f:
    html = f.read()
print('reveal-section count:', html.count('reveal-section'))
print('sec.style.opacity count:', html.count("sec.style.opacity"))
print('section-visible count:', html.count('section-visible'))

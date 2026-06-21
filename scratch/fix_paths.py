with open(r'C:\Users\elly\.antigravity\centrocarrelli\clean_body.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('src="assets/', 'src="/assets/')
html = html.replace("src='assets/", "src='/assets/")

with open(r'C:\Users\elly\.antigravity\centrocarrelli\clean_body.html', 'w', encoding='utf-8') as f:
    f.write(html)

remaining = html.count('assets/') - html.count('/assets/')
print(f'Fixed! Remaining non-prefixed assets/: {remaining}')
print(f'Total /assets/ references: {html.count("/assets/")}')

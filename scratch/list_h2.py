from bs4 import BeautifulSoup

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'
with open(path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

for i, h2 in enumerate(soup.find_all('h2'), 1):
    text = h2.get_text(strip=True)
    print(f'{i}. {text}')

import os
import re
from bs4 import BeautifulSoup

path = r'C:\Users\elly\.gemini\antigravity\brain\ef322864-b0b9-45c8-a2b6-ab68d82e01cc\.system_generated\steps\564\content.md'
if not os.path.exists(path):
    print('File not found')
    exit()

with open(path, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

posts = soup.find_all(class_='oxy-post')
print(f'Found {len(posts)} posts with class oxy-post')

products = []
for p in posts:
    link_tag = p.find('a', class_='oxy-post-title')
    if not link_tag:
        link_tag = p.find('a', class_='oxy-post-image')
    if not link_tag:
        continue
        
    link = link_tag.get('href')
    
    title_tag = p.find('a', class_='oxy-post-title')
    title = title_tag.text.strip() if title_tag else ''
    
    img_div = p.find('div', class_='oxy-post-image-fixed-ratio')
    img_style = img_div.get('style', '') if img_div else ''
    img_url = ''
    if img_style:
        url_match = re.search(r'url\((.*?)\)', img_style)
        if url_match:
            img_url = url_match.group(1).strip('\'"')
            
    if not img_url:
        img_tag = p.find('img')
        img_url = img_tag.get('src', '') if img_tag else ''

    text_content = p.text.strip()
    
    prod = {
        'title': title,
        'link': link,
        'image': img_url,
        'text': text_content
    }
    
    if link not in [x['link'] for x in products]:
        products.append(prod)

print(f'\nExtracted {len(products)} unique transpallet products:')
for idx, prod in enumerate(products):
    print(f'PRODUCT {idx+1}:')
    print('  Title:', prod['title'])
    print('  Link:', prod['link'])
    print('  Image:', prod['image'])
    clean_text = re.sub(r'\s+', ' ', prod['text'])
    print('  Text preview:', clean_text[:240])

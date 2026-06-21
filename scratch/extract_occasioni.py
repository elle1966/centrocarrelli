import re
import os

path = r'C:\Users\elly\.gemini\antigravity\brain\ef322864-b0b9-45c8-a2b6-ab68d82e01cc\.system_generated\steps\522\content.md'
if not os.path.exists(path):
    print('File not found')
    exit()

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for product/post entries
# Usually they are inside oxy-post classes, or look like titles with links
# Let's find all hrefs containing '/carrelli/' or look for headings
print('--- Page head first 1000 chars ---')
print(text[:1000])

print('\n--- Searching for titles & links ---')
# Let's search for links containing '/carrelli/' or product titles
links = re.findall(r'href=[\"\'](https://www.centrocarrelli.net/carrelli/[^\"\']+)[\"\']', text)
unique_links = list(set(links))
print(f'Found {len(unique_links)} unique product links:')
for idx, link in enumerate(unique_links[:15]):
    print(f'  {idx+1}: {link}')

# Let's look for markdown link syntax [Text](URL) or headers
print('\n--- Searching for markdown headings and links ---')
md_links = re.findall(r'\[([^\]]+)\]\((https://www.centrocarrelli.net/carrelli/[^\)]+)\)', text)
unique_md = {}
for name, url in md_links:
    unique_md[url] = name
print(f'Found {len(unique_md)} product markdown links:')
for url, name in unique_md.items():
    print(f'  - {name}: {url}')

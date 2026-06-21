import re
from bs4 import BeautifulSoup
import json

def extract_products(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('div', class_='oxy-post')
    
    products = []
    for post in posts:
        title_el = post.find('a', class_='oxy-post-title')
        if not title_el:
            continue
        name = title_el.text.strip()
        link = title_el.get('href', '')
        
        # Image
        img_container = post.find('div', class_='oxy-post-image-fixed-ratio')
        image = ""
        if img_container:
            style = img_container.get('style', '')
            img_match = re.search(r'url\((.*?)\)', style)
            if img_match:
                image = img_match.group(1).strip("'\"")
        
        if not image:
            img_el = post.find('img')
            if img_el:
                image = img_el.get('src', '')
                
        # Specs paragraph
        specs = {}
        p_el = post.find('p')
        if p_el:
            # Let's get the raw text with spaces instead of newlines
            text = p_el.get_text(' ').strip()
            # Replace multiple spaces/tabs/newlines with a single space
            text = re.sub(r'\s+', ' ', text)
            
            # Now let's extract matches using regex
            # e.g., "Marca: STILL Modello: R 60-25 Matricola: 51602312050 Anno fabbricazione: 2000 Alimentazione: Elettrico Portata: 2500 Sollevamento mm: 4200"
            for field in ["Marca", "Modello", "Matricola", "Anno fabbricazione", "Alimentazione", "Portata", "Sollevamento mm"]:
                pattern = rf'{field}:\s*(.*?)(?=\s*(?:Marca|Modello|Matricola|Anno fabbricazione|Alimentazione|Portata|Sollevamento mm):|$)'
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    specs[field.lower()] = match.group(1).strip()
        
        prod_id = specs.get('matricola', name)
        if not prod_id:
            continue
            
        # Check if already added
        if any(p['id'] == prod_id for p in products):
            continue
            
        products.append({
            'id': prod_id,
            'name': name,
            'link': link,
            'image': image,
            'specs': specs
        })
        
    return products

if __name__ == '__main__':
    prods = extract_products(r'C:\Users\elly\.gemini\antigravity\brain\ef322864-b0b9-45c8-a2b6-ab68d82e01cc\.system_generated\steps\181\content.md')
    print(f"Extracted {len(prods)} unique products:")
    print(json.dumps(prods, indent=2))

from bs4 import BeautifulSoup
import re

path = r'C:\Users\elly\Local Sites\centrocarrelli\app\public\homepage.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Map product IDs to their asset image paths
image_map = {
    "id: 'rx20'": "/assets/hero_forklift.png",
    "id: 'ech12'": "/assets/ech12c_still.jpg",
    "id: 'ech15'": "/assets/ech15c_still.jpg",
    "id: 'exh14'": "/assets/exh14c_transpallet.png",
    "id: 'ecu16'": "/assets/ecu16_usato.jpg",
    "id: 'rx60'": "/assets/hero_forklift.png",
    "id: 'exv14'": "/assets/exh14c_transpallet.png",
    "id: 'rx70'": "/assets/hero_forklift.png",
}

# Replace base64 image strings in the PRODUCTS JS array
# Pattern: image: 'data:image/...'  (single-quoted base64 string)
count = 0
for product_id, asset_path in image_map.items():
    # Find the product block and replace its base64 image
    idx = html.find(product_id)
    if idx == -1:
        print(f"Product {product_id} not found")
        continue
    
    # Find "image: '" after this product id
    img_start = html.find("image: '", idx)
    if img_start == -1 or img_start > idx + 500:
        print(f"image: field not found for {product_id}")
        continue
    
    img_start += len("image: '")
    img_end = html.find("'", img_start)
    
    old_value = html[img_start:img_end]
    if len(old_value) > 200:  # It's a base64 string
        html = html[:img_start] + asset_path + html[img_end:]
        count += 1
        print(f"Replaced base64 for {product_id} -> {asset_path}")
    else:
        print(f"Already short for {product_id}: {old_value[:80]}")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nFatto! {count} immagini base64 sostituite con percorsi /assets/")
print(f"Remaining data:image in file: {html.count('data:image')}")

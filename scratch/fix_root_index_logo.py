path = r'c:\Users\elly\.antigravity\centrocarrelli\index.html'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find the nav-logo block
idx = content.find('class="nav-logo"')
if idx != -1:
    img_start = content.find('<img', idx)
    if img_start != -1 and img_start < idx + 400:
        tag_end = content.find('>', img_start)
        img_tag = content[img_start:tag_end+1]
        print(f"Original tag: {img_tag[:120]}...{img_tag[-50:]}")
        
        # Replace height: 80px or height: 50px or style="..." with height: 45px
        import re
        new_img_tag = re.sub(r'style="height:\s*\d+px;\s*width:\s*auto;"', 'style="height: 45px; width: auto;"', img_tag)
        new_img_tag = re.sub(r"style='height:\s*\d+px;\s*width:\s*auto;'", 'style="height: 45px; width: auto;"', new_img_tag)
        # fallback if it's just height
        if 'height:' in new_img_tag and 'height: 45px' not in new_img_tag:
            new_img_tag = re.sub(r'height:\s*\d+px', 'height: 45px', new_img_tag)
        
        if new_img_tag != img_tag:
            content = content[:img_start] + new_img_tag + content[tag_end+1:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully updated inline style to height: 45px in root index.html")
        else:
            print("No changes made (already 45px or unmatched pattern)")
else:
    print("nav-logo not found in root index.html")

import os
import re
from bs4 import BeautifulSoup

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def compare_nodes(node_b, node_r, path="body"):
    is_str_b = hasattr(node_b, 'name') and node_b.name is None
    is_str_r = hasattr(node_r, 'name') and node_r.name is None
    
    if is_str_b and is_str_r:
        tb = clean_text(node_b)
        tr = clean_text(node_r)
        if tb != tr and (tb or tr):
            print(f"Text mismatch at {path}:")
            print(f"  Bozza: '{tb}'")
            print(f"  Root : '{tr}'")
        return
        
    if is_str_b != is_str_r:
        print(f"Node type mismatch at {path}: Bozza is string={is_str_b}, Root is string={is_str_r}")
        return
        
    if node_b.name != node_r.name:
        print(f"Tag mismatch at {path}: Bozza=<{node_b.name}>, Root=<{node_r.name}>")
        return
        
    # Compare attributes
    attrs_b = node_b.attrs
    attrs_r = node_r.attrs
    
    cb = ' '.join(attrs_b.get('class', []))
    cr = ' '.join(attrs_r.get('class', []))
    if cb != cr:
        print(f"Class mismatch at {path} ({node_b.name}):")
        print(f"  Bozza: '{cb}'")
        print(f"  Root : '{cr}'")
        
    for attr in ['id', 'href', 'src', 'alt', 'style']:
        vb = attrs_b.get(attr)
        vr = attrs_r.get(attr)
        if vb or vr:
            if attr == 'src' and (str(vb).startswith('data:') or str(vr).startswith('data:')):
                continue
            if vb != vr:
                print(f"Attr '{attr}' mismatch at {path} ({node_b.name}):")
                print(f"  Bozza: '{vb}'")
                print(f"  Root : '{vr}'")
                
    children_b = [c for c in node_b.children if not (hasattr(c, 'name') and c.name is None and not clean_text(c))]
    children_r = [c for c in node_r.children if not (hasattr(c, 'name') and c.name is None and not clean_text(c))]
    
    if len(children_b) == 1 and children_b[0].name is None and len(children_r) == 1 and children_r[0].name is None:
        compare_nodes(children_b[0], children_r[0], path)
        return
        
    min_len = min(len(children_b), len(children_r))
    for i in range(min_len):
        child_b = children_b[i]
        child_r = children_r[i]
        tag_b = child_b.name or "text"
        tag_r = child_r.name or "text"
        compare_nodes(child_b, child_r, f"{path} > {tag_b}[{i}]")
        
    if len(children_b) > len(children_r):
        print(f"Bozza has extra children at {path}: {[c.name or 'text' for c in children_b[min_len:]]}")
    elif len(children_r) > len(children_b):
        print(f"Root has extra children at {path}: {[c.name or 'text' for c in children_r[min_len:]]}")

def main():
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bozza_path = os.path.join(current_dir, "centro2026", "index.html")
    root_path = os.path.join(current_dir, "index.html")
    
    with open(bozza_path, "r", encoding="utf-8") as f:
        bozza_soup = BeautifulSoup(f.read(), "html.parser")
        
    with open(root_path, "r", encoding="utf-8") as f:
        root_soup = BeautifulSoup(f.read(), "html.parser")
        
    bozza_body = bozza_soup.body
    root_body = root_soup.body
    
    print("Starting node-by-node body comparison with centro2026...")
    compare_nodes(bozza_body, root_body)
    print("Comparison finished.")

if __name__ == "__main__":
    main()

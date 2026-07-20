from bs4 import BeautifulSoup
import json

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\css_props.json', 'r') as f:
    props = json.load(f)

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\Process.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("=== ALL IMAGES ===")
for img in soup.find_all('img'):
    src = img.get('src', '')
    img_classes = img.get('class', [])
    parent = img.parent
    pp = parent.parent if parent else None
    gp = pp.parent if pp else None
    
    for el in [gp, pp, parent]:
        if el:
            for c in (el.get('class') or []):
                if c in props and 'left' in props[c] and 'top' in props[c]:
                    pos = props[c]
                    print(f"SRC: {src}, classes: {img_classes}, container: {c}, pos: {pos}")
                    break

print("\n=== FEATURE TITLES ===")
for p in soup.find_all('p'):
    text = p.get_text().strip()
    if any(x in text for x in ['25+ Years', 'Everything Under', 'Permit', 'Free 3D', 'Speed to']):
        parent = p.parent
        pp = parent.parent if parent else None
        for el in [parent, pp]:
            if el:
                for c in (el.get('class') or []):
                    if c in props and 'left' in props[c]:
                        print(f"Title: '{text}' -> {c}: {props[c]}")
                        break

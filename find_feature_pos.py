from bs4 import BeautifulSoup
import json

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\css_props.json', 'r') as f:
    props = json.load(f)

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all text elements with titles and then find nearest image container
targets = ['25+ Years of Local Experience', 'Everything Under One Roof', 'Permit Experts', 'Free 3D Design Rendering', 'Speed to Completion']

for p in soup.find_all('p'):
    text = p.get_text().strip()
    if text in targets:
        # Get position from parent classes
        parent = p.parent
        pp = parent.parent if parent else None
        for el in [parent, pp]:
            if el:
                classes = el.get('class', [])
                for c in classes:
                    if c in props and 'left' in props[c]:
                        print(f"Title: '{text}' -> container class: {c}, pos: {props[c]}")
                        break

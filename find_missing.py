from bs4 import BeautifulSoup
import json

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\css_props.json', 'r') as f:
    props = json.load(f)

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Map: container class -> correct icon
# Positions (from top):
# 4822 -> Permit Experts icon (matches title at top:4850.5)
# 4961 -> Free 3D Design Rendering icon (matches title at top:4990.5)
# 5083 -> Speed to Completion icon (matches title at top:5112.5)
# Need to find 25+ Years and Everything Under One Roof icon containers

# First let's find their title positions
for p in soup.find_all('p'):
    text = p.get_text().strip()
    if '25+' in text or 'Everything Under' in text:
        parent = p.parent
        pp = parent.parent if parent else None
        for el in [parent, pp]:
            if el:
                for c in (el.get('class') or []):
                    if c in props:
                        print(f"Title: '{text}' class={c} pos={props[c]}")

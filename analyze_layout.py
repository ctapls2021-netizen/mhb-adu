import json
from bs4 import BeautifulSoup

# Load CSS properties
with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\css_props.json', 'r') as f:
    props = json.load(f)

# Load ADUTypes.astro
filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("--- TEXT BLOCKS ---")
for p in soup.find_all('p'):
    text = p.get_text().strip()
    if text in ["Attached ADU", "Detached ADU", "Garage Conversion", "Above-Garage ADU", "JADU", "Two-Story ADU"]:
        parent = p.parent
        classes = parent.get('class', []) + p.get('class', [])
        # Find position
        pos = None
        for c in classes:
            if c in props:
                pos = props[c]
                break
        print(f"Title: {text}, Classes: {classes}, Pos: {pos}")

print("\n--- IMAGE BLOCKS ---")
for img in soup.find_all('img'):
    src = img.get('src')
    parent = img.parent
    grandparent = parent.parent if parent else None
    
    classes = []
    if grandparent: classes += grandparent.get('class', [])
    if parent: classes += parent.get('class', [])
    classes += img.get('class', [])
    
    pos = None
    for c in classes:
        if c in props and 'left' in props[c] and 'top' in props[c]:
            pos = props[c]
            break
            
    print(f"Img Src: {src}, Classes: {classes}, Pos: {pos}")

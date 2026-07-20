from bs4 import BeautifulSoup
import json

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\css_props.json', 'r') as f:
    props = json.load(f)

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all images and their positions
for img in soup.find_all('img'):
    src = img.get('src', '')
    parent = img.parent
    pp = parent.parent if parent else None
    gp = pp.parent if pp else None
    
    for el in [gp, pp, parent]:
        if el:
            for c in (el.get('class') or []):
                if c in props and 'left' in props[c] and 'top' in props[c]:
                    pos = props[c]
                    top_str = pos['top'].replace('px','')
                    if '%' not in top_str:
                        try:
                            top = float(top_str)
                            if top >= 4800 and top <= 5400:
                                print(f"IMG src={src}")
                                print(f"  container_class={c}, pos={pos}")
                        except:
                            pass
                    break

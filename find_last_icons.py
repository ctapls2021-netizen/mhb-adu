from bs4 import BeautifulSoup
import json

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\css_props.json', 'r') as f:
    props = json.load(f)

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\Process.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all images in the range of the 25+ Years and Everything Under One Roof icons
# 25+ Years title at top:5252.5 → icon should be around top:5220-5260
# Everything Under One Roof title at top:5383.5 → icon should be around top:5350-5390
# Permit Experts title at top:4850.5 → icon at top:4822 → delta: ~28px above
# So:
# 25+ Years icon should be around top: 5252.5 - 28 ≈ 5224
# Everything Under One Roof icon should be around top: 5383.5 - 28 ≈ 5355

print("=== IMAGES in range 5200-5450 ===")
for img in soup.find_all('img'):
    src = img.get('src', '')
    img_classes = img.get('class', [])
    parent = img.parent
    pp = parent.parent if parent else None
    gp = pp.parent if pp else None
    
    for el in [gp, pp, parent]:
        if el:
            for c in (el.get('class') or []):
                if c in props and 'top' in props[c]:
                    top_str = props[c]['top'].replace('px','')
                    if '%' not in top_str:
                        try:
                            top = float(top_str)
                            if 5100 <= top <= 5500:
                                print(f"SRC: {src}, img_classes: {img_classes}, container: {c}, pos: {props[c]}")
                        except:
                            pass
                    break

import re
import json

with open('css_props.json', 'r') as f:
    props = json.load(f)

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\HeaderAndHero.astro', 'r', encoding='utf-8') as f:
    html = f.read()

classes = re.findall(r'class="([^"]+)"', html)
for clist in classes:
    for c in clist.split():
        if c in props:
            p = props[c]
            if 'width' in p and p['width'] == '1px':
                print('Found 1px element!', c, p)
            if 'border-left' in str(p) or 'border-right' in str(p):
                print('Found border element!', c, p)

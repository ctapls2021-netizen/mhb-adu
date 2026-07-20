import re
import json

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Naive CSS parser
rules = re.findall(r'(\.[^{]+)\{([^}]*)\}', css)
class_props = {}
for selector, body in rules:
    # Handle multiple selectors like .a, .b
    for sel in selector.split(','):
        sel = sel.strip()
        if sel.startswith('.'):
            cls = sel[1:].split(':')[0] # remove pseudo-classes
            props = {}
            for prop in body.split(';'):
                if ':' in prop:
                    k, v = prop.split(':', 1)
                    props[k.strip()] = v.strip()
            if cls not in class_props:
                class_props[cls] = {}
            class_props[cls].update(props)

with open('css_props.json', 'w') as f:
    json.dump(class_props, f)
print('Parsed CSS')

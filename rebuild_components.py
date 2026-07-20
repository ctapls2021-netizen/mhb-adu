import os
import json
from bs4 import BeautifulSoup
import re

base_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web'
clean_html_path = os.path.join(base_dir, 'clean_site', 'index.html')
astro_comps_dir = os.path.join(base_dir, 'astro_site', 'src', 'components')
css_props_path = os.path.join(base_dir, 'astro_site', 'css_props.json')

with open(clean_html_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(css_props_path, 'r') as f:
    props = json.load(f)

soup = BeautifulSoup(html, 'html.parser')
inner_wrapper = soup.find(id='container').find('div').find('div')

def get_top(element):
    classes = element.get('class', [])
    for c in classes:
        if c in props and 'top' in props[c]:
            val = props[c]['top'].replace('px', '')
            try:
                return float(val)
            except:
                pass
    # If not found, check children
    for child in element.find_all(True):
        child_classes = child.get('class', [])
        for c in child_classes:
            if c in props and 'top' in props[c]:
                val = props[c]['top'].replace('px', '')
                try:
                    return float(val)
                except:
                    pass
    return 0

elements = [c for c in inner_wrapper.children if c.name]
elements.sort(key=lambda x: get_top(x))

components = {
    'HeaderAndHero': [],
    'WhyChooseUs': [],
    'Financing': [],
    'ADUTypes': [],
    'Process': [],
    'TestimonialsAndFooter': []
}

for e in elements:
    top = get_top(e)
    if top < 1000:
        components['HeaderAndHero'].append(str(e))
    elif top < 1500:
        components['WhyChooseUs'].append(str(e))
    elif top < 2700:
        components['Financing'].append(str(e))
    elif top < 5200:
        components['ADUTypes'].append(str(e))
    elif top < 10000:
        components['Process'].append(str(e))
    else:
        components['TestimonialsAndFooter'].append(str(e))

for comp, html_blocks in components.items():
    content = "---\n---\n" + "".join(html_blocks) + "\n"
    with open(os.path.join(astro_comps_dir, f'{comp}.astro'), 'w', encoding='utf-8') as f:
        f.write(content)

print("Rebuilt components successfully with all children.")

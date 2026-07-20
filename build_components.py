import os
import re
import json
from bs4 import BeautifulSoup

base_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site'
components_dir = os.path.join(base_dir, 'src', 'components')
os.makedirs(components_dir, exist_ok=True)

with open(os.path.join(base_dir, 'css_props.json'), 'r', encoding='utf-8') as f:
    props = json.load(f)

html_file = os.path.join(base_dir, 'src', 'pages', 'index.astro')
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

parts = re.split(r'---', html)
frontmatter = parts[1] if len(parts) > 2 else ''
html_part = parts[2] if len(parts) > 2 else html

soup = BeautifulSoup(html_part, 'html.parser')
container = soup.find(id='container')
wrapper = container.find('div')
inner_wrapper = wrapper.find('div')

components = {
    'HeaderAndHero': {'max_top': 950, 'divs': []},
    'WhyChooseUs': {'max_top': 2350, 'divs': []},
    'Financing': {'max_top': 2800, 'divs': []},
    'ADUTypes': {'max_top': 4600, 'divs': []},
    'Process': {'max_top': 10000, 'divs': []},
    'TestimonialsAndFooter': {'max_top': 999999, 'divs': []}
}
comp_keys = list(components.keys())

for child in inner_wrapper.find_all('div', recursive=False):
    classes = child.get('class', [])
    top = 0
    for c in classes:
        if c in props and 'top' in props[c]:
            val = props[c]['top']
            val = val.replace('px', '').strip()
            try:
                top = float(val)
            except:
                pass
    
    # find component
    assigned = False
    for k in comp_keys:
        if top < components[k]['max_top']:
            components[k]['divs'].append(str(child))
            assigned = True
            break
    if not assigned:
        components['TestimonialsAndFooter']['divs'].append(str(child))

# Write components
for k in comp_keys:
    comp_html = '\n'.join(components[k]['divs'])
    # Since these are absolute, we don't strictly need a wrapper, but let's just output the divs
    content = f"---\n// {k} Component\n---\n\n" + comp_html
    with open(os.path.join(components_dir, f"{k}.astro"), 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.astro
imports = "\n".join([f"import {k} from '../components/{k}.astro';" for k in comp_keys])
renders = "\n".join([f"      <{k} />" for k in comp_keys])

new_frontmatter = f"---\nimport '../styles/global.css';\n{imports}\n---"

# We must keep the outer container and wrapper intact
# We will clear inner_wrapper and append the components tags
inner_wrapper.clear()
for k in comp_keys:
    inner_wrapper.append(BeautifulSoup(f"<{k} />", 'html.parser'))

# Reassemble
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_frontmatter + '\n' + str(soup))

print('Componentization completed successfully.')

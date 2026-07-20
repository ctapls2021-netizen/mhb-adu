import os
import json
import re
import math
from bs4 import BeautifulSoup

base_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site'
comps_dir = os.path.join(base_dir, 'src', 'components')

# Load CSS props
with open(os.path.join(base_dir, 'css_props.json'), 'r', encoding='utf-8') as f:
    props = json.load(f)

def get_coords(classes):
    top, left = 0, 0
    for c in classes:
        if c in props:
            if 'top' in props[c]:
                try: top = float(props[c]['top'].replace('px', ''))
                except: pass
            if 'left' in props[c]:
                try: left = float(props[c]['left'].replace('px', ''))
                except: pass
    return top, left

# Collect all images and texts
elements = []

for file in os.listdir(comps_dir):
    if not file.endswith('.astro'): continue
    with open(os.path.join(comps_dir, file), 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    for div in soup.find_all('div'):
        classes = div.get('class', [])
        top, left = get_coords(classes)
        
        # If it has an img
        img = div.find('img')
        if img and img.get('src', '').startswith('/index Adu_files/'):
            elements.append({
                'type': 'img',
                'file': file,
                'src': img['src'],
                'top': top,
                'left': left,
                'tag': str(img)
            })
            
        # If it has text
        text = div.get_text(separator=' ', strip=True)
        if text:
            # clean text
            text = re.sub(r'\s+', ' ', text)
            elements.append({
                'type': 'text',
                'file': file,
                'text': text,
                'top': top,
                'left': left
            })

with open('visual_elements.json', 'w') as f:
    json.dump(elements, f, indent=2)

print('Visual elements extracted.')

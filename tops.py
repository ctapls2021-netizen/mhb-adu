import codecs, sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
from bs4 import BeautifulSoup
import re

html_file = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\pages\index.astro'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

html_part = re.split(r'---', html)[2] if '---' in html else html
soup = BeautifulSoup(html_part, 'html.parser')

css_file = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

def get_top(classes):
    for cls in classes:
        m = re.search(r'\.' + cls + r'\s*\{[^}]*top:\s*(-?[0-9]+)px', css)
        if m:
            return int(m.group(1))
    return -1

container = soup.find(id='container')
wrapper = container.find('div').find('div')

elements = []
for idx, child in enumerate(wrapper.find_all('div', recursive=False)):
    # encode text to ascii ignoring unicode errors
    text = child.get_text(separator=' ', strip=True)[:30].replace('\n', ' ')
    text = text.encode('ascii', 'ignore').decode('ascii')
    classes = child.get('class', [])
    top = get_top(classes)
    elements.append({'idx': idx, 'top': top, 'text': text})

elements.sort(key=lambda x: x['top'])
for e in elements:
    if e['text'] or e['top'] > -1:
        print(f"[{e['idx']}] Top: {e['top']}px - {e['text']}")

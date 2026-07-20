import os
from bs4 import BeautifulSoup

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
for img in soup.find_all('img'):
    src = img.get('src')
    if src and any(x in src for x in ['Attached ADU', 'Garage Conversion', 'Detached ADU', 'Above-Garage ADU', 'JADU']):
        img['style'] = "object-fit: cover !important; width: 100% !important; height: 100% !important;"

content = "---\n---\n" + "".join([str(c) for c in soup.children])
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

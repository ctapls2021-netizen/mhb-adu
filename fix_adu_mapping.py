import os
from bs4 import BeautifulSoup

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Map of image class to correct image path
class_to_img = {
    'css-qw3zwa': '/images/Attached ADU.png',
    'css-z3as1s': '/images/Detached ADU.png',
    'css-y9pif0': '/images/Garage Conversion.png',
    'css-9edryz': '/images/Above-Garage ADU.png',
    'css-baon7m': '/images/JADU.png',
    'css-j8fkso': '/images/Two-Story ADU.png'
}

for img in soup.find_all('img'):
    classes = img.get('class', [])
    for c in classes:
        if c in class_to_img:
            img['src'] = class_to_img[c]
            break

content = "---\n---\n" + "".join([str(c) for c in soup.children])
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

from bs4 import BeautifulSoup

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Print each image with its src AND nearby text title
for img in soup.find_all('img'):
    src = img.get('src', '')
    style = img.get('style', '')
    classes = ' '.join(img.get('class', []))
    # Walk up to find a title nearby
    parent = img.parent
    grandparent = parent.parent if parent else None
    ggp = grandparent.parent if grandparent else None
    container_classes = []
    for el in [img, parent, grandparent, ggp]:
        if el:
            container_classes += el.get('class', [])
    
    print(f"SRC: {src}")
    print(f"  img classes: {classes}")
    print(f"  style: {style}")
    print()

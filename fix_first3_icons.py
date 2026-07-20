from bs4 import BeautifulSoup

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Mapping by image class:
# css-1tlhgb -> top:4822 -> Permit Experts (title at 4850.5)
# css-f0o2nb -> top:4961 -> Free 3D Design Rendering (title at 4990.5)
# css-u7gf77 -> top:5083 -> Speed to Completion (title at 5112.5)

class_to_icon = {
    'css-1tlhgb': '/images/Permit Experts.png',
    'css-f0o2nb': '/images/Free 3D Design Rendering.png',
    'css-u7gf77': '/images/Speed to Completion.png',
}

for img in soup.find_all('img'):
    classes = img.get('class', [])
    for c in classes:
        if c in class_to_icon:
            img['src'] = class_to_icon[c]
            img['style'] = "width: 100% !important; height: 100% !important; top: 0 !important; left: 0 !important; position: relative !important; object-fit: contain !important;"
            print(f"Fixed: {c} -> {class_to_icon[c]}")
            break

content = "---\n---\n" + "".join([str(c) for c in soup.children])
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

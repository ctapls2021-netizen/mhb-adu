from bs4 import BeautifulSoup

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# These image classes have bad positioning (top/left negative %)
# Force them to be visible with proper cover styling
bad_classes = ['css-qw3zwa', 'css-z3as1s', 'css-9edryz', 'css-y9pif0', 'css-baon7m', 'css-j8fkso']

cover_style = "object-fit: cover !important; width: 100% !important; height: 100% !important; position: relative !important; top: 0 !important; left: 0 !important; max-width: none !important;"

for img in soup.find_all('img'):
    classes = img.get('class', [])
    for c in classes:
        if c in bad_classes:
            img['style'] = cover_style
            break

content = "---\n---\n" + "".join([str(c) for c in soup.children])
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done - fixed image positioning styles")

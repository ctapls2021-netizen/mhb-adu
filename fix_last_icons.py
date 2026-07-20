from bs4 import BeautifulSoup

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\Process.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# css-eqt5tl → 25+ Years of Local Experience (top:5221 matches title at 5252)
# css-i12894 → Everything Under One Roof (top:5352 matches title at 5383)

for img in soup.find_all('img'):
    classes = img.get('class', [])
    if 'css-eqt5tl' in classes:
        img['src'] = '/images/25+ Years of Local Experience.png'
        print("Fixed: 25+ Years")
    elif 'css-i12894' in classes:
        img['src'] = '/images/Everything Under One Roof.png'
        print("Fixed: Everything Under One Roof")

content = "---\n---\n" + "".join([str(c) for c in soup.children])
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

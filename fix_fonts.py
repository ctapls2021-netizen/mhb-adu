import re

css_file = r"c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css"
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix font-family names
def fix_font(match):
    name = match.group(1)
    new_name = re.sub(r':(Regular|Bold|Italic|Medium|SemiBold|ExtraBold|Semi Bold|Medium Italic|Extra Bold Italic|Semi Bold Italic|Bold Italic)', '', name)
    return 'font-family: ' + new_name + match.group(2)

css_new = re.sub(r'font-family:\s*([^;]+)(;|\})', fix_font, css)
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_new)
print('Fonts fixed in CSS.')

html_file = r"c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\pages\index.astro"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

styles = re.findall(r'style="([^"]+)"', html)
orange_styles = [s for s in styles if 'orange' in s.lower() or 'rgb(255' in s or '#ff' in s.lower()]
print('Orange styles in HTML:', orange_styles)

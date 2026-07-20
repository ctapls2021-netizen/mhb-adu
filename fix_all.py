import re

html_file = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\index Adu.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract styles safely
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL | re.IGNORECASE)
css = '\n'.join(styles)

# Remove @font-face
css = re.sub(r'@font-face\s*\{[^}]+\}', '', css)

# Fix font-family names ONLY inside values.
def fix_font_value(match):
    name = match.group(1)
    new_name = re.sub(r':(Regular|Bold|Italic|Medium|SemiBold|ExtraBold|Semi Bold|Medium Italic|Extra Bold Italic|Semi Bold Italic|Bold Italic)', '', name)
    return 'font-family: ' + new_name + match.group(2)

css = re.sub(r'font-family:\s*([^;\}]+)(;|\})', fix_font_value, css)

css_file = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css'
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print('Restored global.css successfully without unescaping.')

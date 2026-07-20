import re

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\HeaderAndHero.astro', 'r', encoding='utf-8') as f:
    html = f.read()

m2 = re.search(r'<p[^>]*>.*?CA Lic\..*?</p>', html, re.DOTALL)
if m2:
    print('Found p tag classes:')
    tag = m2.group(0)
    m3 = re.search(r'class="([^"]+)"', tag)
    if m3:
        print(m3.group(1))

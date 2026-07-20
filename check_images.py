import os
import re

astro_site = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site'

# Check CSS
css_file = os.path.join(astro_site, 'src', 'styles', 'global.css')
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

urls = re.findall(r'url\(([^)]+)\)', css)
print('URLs in CSS:')
for u in set(urls):
    print(u)

# Check components
print('\nImgs in Components:')
comps_dir = os.path.join(astro_site, 'src', 'components')
for file in os.listdir(comps_dir):
    with open(os.path.join(comps_dir, file), 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', content)
    if imgs:
        print(f'{file}:', set(imgs))

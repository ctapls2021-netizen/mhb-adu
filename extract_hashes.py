import os
import re

comps_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components'
used_hashes = set()
for file in os.listdir(comps_dir):
    if not file.endswith('.astro'): continue
    with open(os.path.join(comps_dir, file), 'r', encoding='utf-8') as f:
        content = f.read()
    
    for m in re.finditer(r'<img[^>]+src=[\"\']/index Adu_files/([^\"\']+)[\"\']', content):
        used_hashes.add(m.group(1))

print('MAPPING = {')
for h in used_hashes:
    print(f'    "{h}": "",')
print('}')

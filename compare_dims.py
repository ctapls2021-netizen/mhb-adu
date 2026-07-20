import os
from PIL import Image

imgs_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\public\images'
figma_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\public\index Adu_files'

user_images = []
for file in os.listdir(imgs_dir):
    path = os.path.join(imgs_dir, file)
    if os.path.isfile(path) and not file.endswith('.svg'):
        try:
            with Image.open(path) as img:
                w, h = img.size
                user_images.append({'name': file, 'w': w, 'h': h, 'ratio': round(w/h, 2)})
        except:
            pass

print("USER IMAGES:")
user_images.sort(key=lambda x: x['w'] * x['h'], reverse=True)
for i in user_images:
    print(f"{i['name']} - {i['w']}x{i['h']} (ratio: {i['ratio']})")

print("\nFIGMA IMAGES (Used in components):")
used_hashes = set()
comps_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components'
import re
for file in os.listdir(comps_dir):
    if file.endswith('.astro'):
        with open(os.path.join(comps_dir, file), 'r', encoding='utf-8') as f:
            content = f.read()
        for m in re.finditer(r'src=[\"\']/index Adu_files/([^\"\']+)[\"\']', content):
            used_hashes.add(m.group(1))

figma_images = []
for file in used_hashes:
    path = os.path.join(figma_dir, file)
    if os.path.isfile(path) and not file.endswith('.svg'):
        try:
            with Image.open(path) as img:
                w, h = img.size
                figma_images.append({'name': file, 'w': w, 'h': h, 'ratio': round(w/h, 2)})
        except:
            pass

figma_images.sort(key=lambda x: x['w'] * x['h'], reverse=True)
for i in figma_images:
    print(f"{i['name']} - {i['w']}x{i['h']} (ratio: {i['ratio']})")

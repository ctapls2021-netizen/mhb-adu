import os
import re

comps_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components'
imgs_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\public\images'

img_files = os.listdir(imgs_dir)
names = []
for i in img_files:
    base = os.path.splitext(i)[0]
    base_clean = re.sub(r'\s*\(\d+\)', '', base)
    names.append({'file': i, 'search': base_clean, 'matched': False})

for file in os.listdir(comps_dir):
    if not file.endswith('.astro'): continue
    filepath = os.path.join(comps_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    img_tags = []
    # Find all img tags
    for m in re.finditer(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']([^>]*)>', content):
        img_tags.append({
            'src': m.group(1),
            'start': m.start(),
            'end': m.end(),
            'full': m.group(0),
            'replaced_with': None
        })

    # To handle multiple matches (like 3 cards), we consume the img_tags so they can't be matched twice
    for n in names:
        # relax search: allow spaces to be anything
        search = re.escape(n['search']).replace(r'\ ', r'\s*')
        # match ignoring case and newlines
        m = re.search(search, content, re.IGNORECASE | re.DOTALL)
        if m:
            text_pos = m.start()
            closest_img = None
            min_dist = float('inf')
            for img in img_tags:
                if img['replaced_with']: continue
                dist = abs(img['start'] - text_pos)
                if dist < min_dist:
                    min_dist = dist
                    closest_img = img
            if closest_img and min_dist < 2000:
                closest_img['replaced_with'] = '/images/' + n['file']
                n['matched'] = True
                print(f"Matched {n['file']} in {file} (dist: {min_dist})")

    # Reconstruct the file with replaced images
    offset = 0
    new_content = ""
    last_end = 0
    for img in img_tags:
        if img['replaced_with']:
            new_content += content[last_end:img['start']]
            new_tag = img['full'].replace(img['src'], img['replaced_with'])
            # remove srcset if exists to avoid showing old image
            new_tag = re.sub(r'srcset=[\"\'][^\"\']+[\"\']', '', new_tag)
            new_content += new_tag
            last_end = img['end']
    new_content += content[last_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('\nUNMATCHED:')
for n in names:
    if not n['matched']:
        print(n['file'])

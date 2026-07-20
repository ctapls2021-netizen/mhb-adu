import os, json, re, math

imgs_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\public\images'
img_files = os.listdir(imgs_dir)

names = []
for i in img_files:
    if i.endswith('.svg'):
        # For SVGs, search the name without extension
        search = os.path.splitext(i)[0]
    else:
        search = os.path.splitext(i)[0]
        search = re.sub(r'\s*\(\d+\)', '', search)
    names.append({'file': i, 'search': search})

with open('visual_elements.json', 'r') as f:
    elements = json.load(f)

texts = [e for e in elements if e['type'] == 'text']
imgs = [e for e in elements if e['type'] == 'img']

replacements = []

for n in names:
    search_re = re.escape(n['search']).replace(r'\ ', r'\s*')
    # find best text match
    best_text = None
    for t in texts:
        if re.search(search_re, t['text'], re.IGNORECASE):
            best_text = t
            break
            
    if best_text:
        # find closest img in the SAME FILE
        closest_img = None
        min_dist = float('inf')
        for i in imgs:
            if i['file'] == best_text['file']:
                dist = math.sqrt((i['top'] - best_text['top'])**2 + (i['left'] - best_text['left'])**2)
                if dist < min_dist:
                    min_dist = dist
                    closest_img = i
        
        if closest_img:
            replacements.append({
                'file': closest_img['file'],
                'target': closest_img['tag'],
                'replace_with': f"/images/{n['file']}"
            })
            print(f"Matched {n['file']} to {closest_img['src']} in {closest_img['file']} (dist: {min_dist:.2f})")
    else:
        print(f"Unmatched text: {n['file']}")

with open('replacements.json', 'w') as f:
    json.dump(replacements, f, indent=2)

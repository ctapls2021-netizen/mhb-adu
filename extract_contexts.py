import os, re, json
comps_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components'
tags = []
for file in os.listdir(comps_dir):
    if not file.endswith('.astro'): continue
    with open(os.path.join(comps_dir, file), 'r', encoding='utf-8') as f:
        content = f.read()
    
    for m in re.finditer(r'<img[^>]+src=[\"\']([^\"\']+)[\"\'][^>]*>', content):
        start = max(0, m.start() - 100)
        end = min(len(content), m.end() + 100)
        ctx = content[start:end]
        # clean ctx
        ctx_clean = re.sub(r'<[^>]+>', ' ', ctx)
        
        tags.append({
            'file': file,
            'src': m.group(1),
            'full': m.group(0),
            'context': ctx_clean.strip()
        })
with open('img_tags.json', 'w') as f:
    json.dump(tags, f, indent=2)

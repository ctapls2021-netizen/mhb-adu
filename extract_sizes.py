import os, re
comps_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components'
for file in os.listdir(comps_dir):
    if not file.endswith('.astro'): continue
    with open(os.path.join(comps_dir, file), 'r', encoding='utf-8') as f:
        content = f.read()
    
    for m in re.finditer(r'<img([^>]+)>', content):
        attrs = m.group(1)
        src = re.search(r'src=[\"\']([^\"\']+)[\"\']', attrs)
        sizes = re.search(r'sizes=[\"\']([^\"\']+)[\"\']', attrs)
        src_val = src.group(1) if src else 'None'
        size_val = sizes.group(1) if sizes else 'None'
        # only show original hashes
        if 'index Adu_files' in src_val:
            print(f'{file} | {src_val.split("/")[-1][:8]}... | sizes: {size_val}')

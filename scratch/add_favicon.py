import os
import shutil
import re

# 1. Copy the favicon
src_favicon = r'C:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\lp ADU MHB\favicon.png'
dst_favicon = 'public/favicon.png'
shutil.copyfile(src_favicon, dst_favicon)
print("Copied favicon")

# 2. Update index.astro
index_path = 'src/pages/index.astro'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if there is an existing favicon link
if '<link rel="icon"' in content:
    content = re.sub(r'<link[^>]*rel=[\"\']icon[\"\'][^>]*>', '<link rel="icon" type="image/png" href="/favicon.png" />', content)
    print("Replaced existing favicon link")
else:
    # Insert it right before <title> or inside <head>
    content = content.replace('<head>', '<head>\n<link rel="icon" type="image/png" href="/favicon.png" />')
    print("Inserted new favicon link")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

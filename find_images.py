import re
with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\WhyChooseUs.astro', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.findall(r'<img[^>]*src="([^"]+)"[^>]*class="([^"]+)"[^>]*>', html)
for src, cls in m:
    print('SRC:', src, 'CLASS:', cls)

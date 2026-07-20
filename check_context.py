import re

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\ADUTypes.astro', 'r', encoding='utf-8') as f:
    content = f.read()

imgs = re.finditer(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', content)
for m in imgs:
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print('IMG:', m.group(1))
    print('Context:', content[start:end])
    print('-'*50)

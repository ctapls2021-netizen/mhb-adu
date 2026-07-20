import re

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\HeaderAndHero.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the classes for the first text
m1 = re.search(r'<p[^>]*>.*?Los Angeles ADU Builders.*?You Can Actually Trust.*?</p>', html, re.DOTALL)
if m1:
    m = re.search(r'class="([^"]+)"', m1.group(0))
    if m:
        print('Text 1 classes:', m.group(1))

# Find the classes for the second text
m2 = re.search(r'<p[^>]*>.*?From expedited city permits.*?contractor headaches\..*?</p>', html, re.DOTALL)
if m2:
    m = re.search(r'class="([^"]+)"', m2.group(0))
    if m:
        print('Text 2 classes:', m.group(1))

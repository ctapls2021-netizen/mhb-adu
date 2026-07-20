import re

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\clean_site\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m1 = re.search(r'<p[^>]*>.*?Los Angeles ADU Builders.*?You Can Actually Trust.*?</p>', html, re.DOTALL)
if m1:
    m = re.search(r'class="([^"]+)"', m1.group(0))
    if m:
        print('Original Text 1 classes:', m.group(1))

m2 = re.search(r'<p[^>]*>.*?From expedited city permits.*?contractor headaches\..*?</p>', html, re.DOTALL)
if m2:
    m = re.search(r'class="([^"]+)"', m2.group(0))
    if m:
        print('Original Text 2 classes:', m.group(1))

m3 = re.search(r'<p[^>]*>.*?CA Lic\..*?</p>', html, re.DOTALL)
if m3:
    m = re.search(r'class="([^"]+)"', m3.group(0))
    if m:
        print('Original Top Bar classes:', m.group(1))

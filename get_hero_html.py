import re

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\HeaderAndHero.astro', 'r', encoding='utf-8') as f:
    html = f.read()

def print_clean(text):
    print(text.replace('\u200b', ''))

idx1 = html.find('Los Angeles ADU Builders')
if idx1 != -1:
    print_clean('Text 1 HTML: ' + html[max(0, idx1-200):idx1+200])

print('---')
idx2 = html.find('From expedited city permits')
if idx2 != -1:
    print_clean('Text 2 HTML: ' + html[max(0, idx2-200):idx2+200])

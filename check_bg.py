import re

with open(r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Search for background-image on ADU image classes
classes = ['css-qw3zwa', 'css-z3as1s', 'css-9edryz', 'css-y9pif0', 'css-baon7m', 'css-j8fkso',
           'css-o7b50b', 'css-isagh0', 'css-4jygia', 'css-5ns3tt', 'css-hoha6l', 'css-5nbm1l', 'css-isthp9']

for c in classes:
    m = re.search(r'\.' + c + r'\s*\{[^\}]+\}', css)
    if m:
        print(c, ':', m.group(0))

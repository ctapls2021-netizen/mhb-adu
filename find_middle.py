import re

html_file = r"c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\pages\index.astro"
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# search for all elements with absolute positioning that could be a line
css_file = r"c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css"
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# look for left: 960px or similar
for line in css.splitlines():
    if "left" in line and "px" in line and ("95" in line or "96" in line):
        print(line)


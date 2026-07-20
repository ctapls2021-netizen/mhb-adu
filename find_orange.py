import re

html_file = r"c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\pages\index.astro"
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# search for all divs and their classes
divs = re.findall(r'<div[^>]+class="([^"]+)"[^>]*>', html)

# We want to check the css of these classes to see if any has an orange background or border
css_file = r"c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css"
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

for cls_list in set(divs):
    for cls in cls_list.split():
        # find the css rule for this class
        match = re.search(r'\.' + cls + r'\s*\{([^}]+)\}', css)
        if match:
            rule = match.group(1).lower()
            if 'orange' in rule or 'rgba(255' in rule or 'rgb(255' in rule or 'border' in rule or 'background' in rule:
                if 'width: 1px' in rule or 'width: 2px' in rule or 'width:1px' in rule or 'left: 960px' in rule:
                    print(f"Suspect class: {cls}, Rule: {rule}")

# also check images
imgs = re.findall(r'<img[^>]+class="([^"]+)"[^>]*>', html)
for cls_list in set(imgs):
    for cls in cls_list.split():
        match = re.search(r'\.' + cls + r'\s*\{([^}]+)\}', css)
        if match:
            rule = match.group(1).lower()
            if 'width: 1px' in rule or 'width: 2px' in rule or 'width:1px' in rule:
                print(f"Suspect img class: {cls}, Rule: {rule}")

import re
import os

css_file = r"c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css"
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

css_clean = re.sub(r"@font-face\s*\{[^}]+\}", "", css)
with open(css_file, "w", encoding="utf-8") as f:
    f.write(css_clean)
print("Removed @font-face rules from CSS.")

html_file = r"c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\pages\index.astro"
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

if "scrnli" in html.lower():
    print("Found scrnli in HTML!")

# Let's search for an image that is near the middle.
# An orange line... wait!
# If the text is split across the orange line, the line is literally a gap.
# Are there any images with width=1 or width=2?
matches = re.findall(r'<img[^>]+src="([^"]+)"[^>]*>', html)
print(f"Total images: {len(matches)}")


import re

with open('src/components/HeaderAndHero.astro', 'r', encoding='utf-8') as f:
    html = f.read()
with open('src/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find all classes in html
classes = set()
for m in re.finditer(r'class="([^"]+)"', html):
    for c in m.group(1).split():
        classes.add(c)

print("Border/line CSS rules for classes in HeaderAndHero.astro:")
for c in sorted(classes):
    pattern = r'\.' + re.escape(c) + r'\b[^{}]*\{([^}]+)\}'
    for m in re.finditer(pattern, css):
        styles = m.group(1)
        if 'border' in styles:
            print(f"Class: .{c} | Style: {styles.strip()}")

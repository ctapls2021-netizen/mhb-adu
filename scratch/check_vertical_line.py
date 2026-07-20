import re

with open('src/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

matches = re.finditer(r'border-left[^;}]*', css)
print("All border-left matches in global.css:")
for m in matches:
    print(m.group(0))

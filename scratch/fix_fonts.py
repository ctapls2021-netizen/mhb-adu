with open('src/components/Process.astro', 'r', encoding='utf-8') as f:
    c = f.read()

import re

# Remove ALL remaining gradient overlays
c = re.sub(r'<div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 50%; z-index: 30; background: linear-gradient\(180deg, rgba\(0,0,0,0\) 0%, rgba\(0,0,0,0\.7\) 100%\);"></div>', '', c)

# Remove ALL remaining text overlays
c = re.sub(r'<div style="position: absolute; left: 30px; bottom: 30px; z-index: 30; display: flex; flex-direction: column;"><span style="color: #FFF; font-family: \'Playfair Display\', serif; font-size: 30px; font-weight: 400; line-height: 32px;">ADU</span><span style="color: #FFF; font-family: \'Inter\', sans-serif; font-size: [^"]+; text-transform: uppercase;">.*?</span></div>', '', c)

with open('src/components/Process.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('All HTML text overlays removed!')

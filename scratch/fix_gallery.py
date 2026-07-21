import os
import shutil
import re

# 1. Copy images
src_dir = r'C:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\lp ADU MHB\project'
dst_dir = 'public/images'

images = [
    'Inglewood.jpg', 'Reseda, CA.jpg', 'Sherman Oaks.jpg',
    'Studio City 1.jpg', 'Studio City.jpg', 'Woodland Hills, CA.jpg'
]

for img in images:
    s = os.path.join(src_dir, img)
    d = os.path.join(dst_dir, img)
    if os.path.exists(s):
        shutil.copyfile(s, d)
        print(f'Copied {img}')

# 2. Update Process.astro
process_path = 'src/components/Process.astro'
with open(process_path, 'r', encoding='utf-8') as f:
    content = f.read()

def overlay(city_name):
    # This uses a gradient from 0% opacity to 70% opacity over the bottom half, then absolute text
    # using Playfair 30px / 32px line-height, and Inter 20px / 20px line-height.
    return f'''<div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 50%; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); z-index: 10; pointer-events: none;"></div>
  <div style="position: absolute; left: 30px; bottom: 30px; z-index: 20; color: #FFF; pointer-events: none;">
    <p style="margin: 0; padding: 0; font-family: 'Playfair Display', serif; font-size: 30px; font-weight: 400; line-height: 32px; letter-spacing: 0px;">ADU</p>
    <p style="margin: 0; padding: 0; font-family: 'Inter', sans-serif; font-size: 20px; font-weight: 400; line-height: 20px; letter-spacing: 0px; text-transform: uppercase;">{city_name}</p>
  </div>'''

replacements = {
    'css-1z9nvy': ('Inglewood.jpg', 'INGLEWOOD'),
    'css-923teq': ('Studio City 1.jpg', 'STUDIO CITY'),
    'css-6sc260': ('Reseda, CA.jpg', 'RESEDA, CA'),
    'css-1z6gsa': ('Sherman Oaks.jpg', 'SHERMAN OAKS'),
    'css-a5wsjo': ('Woodland Hills, CA.jpg', 'WOODLAND HILLS, CA'),
    'css-tw5efc': ('Studio City.jpg', 'STUDIO CITY')
}

for cls, (img_name, city) in replacements.items():
    # Regex to find the div block
    pattern = rf'<div class="({cls}\s*css-roiesn|css-roiesn\s*{cls})"\s*>.*?<img[^>]*src="[^"]*{re.escape(img_name)}"[^>]*>.*?</div>'
    
    def replacer(match):
        m = match.group(0)
        # We need to make sure the div has position: relative and overflow: hidden
        # The original tag might just be <div class="...">
        # So we replace the class part and add style
        inner_img = re.search(r'<img[^>]*>', m).group(0)
        # return new wrapper
        return f'<div class="{cls} css-roiesn" style="position: relative; overflow: hidden;">{inner_img}{overlay(city)}</div>'
        
    content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open(process_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Process.astro')

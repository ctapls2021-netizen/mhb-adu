with open('src/components/Process.astro', 'r', encoding='utf-8') as f:
    c = f.read()

import re

# We want to remove the text overlays from ONLY these three images:
# Sherman Oaks.jpg
# Woodland Hills, CA.jpg
# Studio City.jpg (the second one)

images_to_strip = ['Sherman Oaks.jpg', 'Woodland Hills, CA.jpg', 'Studio City.jpg']

for img in images_to_strip:
    # Find the image tag
    idx = c.find(img)
    if idx == -1:
        continue
    
    # The overlay comes right after the img tag and its div
    # It looks like: .../></div><div style="position: absolute...
    # Find the start of the card block
    start_card = c.rfind('<div class="css-', 0, idx)
    end_card = c.find('</div></div>', idx) + 12
    
    card_block = c[start_card:end_card]
    
    # Remove gradient and text overlays from this block
    card_block_clean = re.sub(r'<div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 50%; z-index: 30; background: linear-gradient\(180deg, rgba\(0,0,0,0\) 0%, rgba\(0,0,0,0\.7\) 100%\);"></div>', '', card_block)
    card_block_clean = re.sub(r'<div style="position: absolute; left: 30px; bottom: 30px; z-index: 30; display: flex; flex-direction: column;"><span style="color: #FFF; font-family: \'Playfair Display\', serif; font-size: 30px; font-weight: 400; line-height: 32px;">ADU</span><span style="color: #FFF; font-family: \'Inter\', sans-serif; font-size: 20px; font-weight: 400; line-height: 32px; text-transform: uppercase;">.*?</span></div>', '', card_block_clean)
    
    # Replace in file content
    c = c.replace(card_block, card_block_clean)
    print(f'Stripped overlays from {img}')

with open('src/components/Process.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done!')

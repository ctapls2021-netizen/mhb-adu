with open('src/components/ADUTypes.astro', 'r', encoding='utf-8') as f:
    c = f.read()

imgs = ['Attached ADU.png', 'Detached ADU.png', 'Above-Garage ADU.png', 'Garage Conversion.png', 'JADU.png', 'Two-Story ADU.png']
count = 0
for img in imgs:
    old = f'src="/images/{img}" style="object-fit: cover'
    new = f'src="/images/{img}" style="object-fit: contain'
    if old in c:
        c = c.replace(old, new)
        count += 1
        print(f'Fixed: {img}')
    else:
        print(f'Not found (cover): {img}')

with open('src/components/ADUTypes.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print(f'Total fixed: {count}')

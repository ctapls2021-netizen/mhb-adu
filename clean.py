with open('src/components/HeaderAndHero.astro', 'r', encoding='utf-8') as f:
    content = f.read()

s = '<div class="css-a07or2 css-lla91'
i = content.find(s)
if i != -1:
    e = content.find('<script>', i)
    new_content = content[:i] + content[e:]
    with open('src/components/HeaderAndHero.astro', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Cleaned')
else:
    print('Not found')
